from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Depends
from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS (Optional: Needed if frontend connects)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to restrict specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database Setup (Switch to PostgreSQL in Production)
DATABASE_URL = "sqlite:///./orders.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Order Model (SQLAlchemy)
class Order(Base):
    __tablename__ = "orders"
    
    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, index=True)
    price = Column(Float)
    quantity = Column(Integer)
    order_type = Column(String)

Base.metadata.create_all(bind=engine)

# Pydantic Model for Request Body
class OrderCreate(BaseModel):
    symbol: str
    price: float
    quantity: int
    order_type: str

# Dependency for DB Session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# WebSocket Management
class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

manager = ConnectionManager()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Message received: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)

# REST Endpoints
@app.post("/orders")
async def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    """Creates a new trade order and broadcasts it to WebSocket clients."""
    new_order = Order(**order.dict())
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    
    # Broadcast order update
    await manager.broadcast(f"New Order: {new_order.symbol} - {new_order.quantity} shares at {new_order.price}")

    return new_order

@app.get("/orders", response_model=List[OrderCreate])
def get_orders(db: Session = Depends(get_db)):
    """Returns all stored trade orders."""
    return db.query(Order).all()
