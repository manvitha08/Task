import pytest
from httpx import AsyncClient
from main import app  # Import FastAPI app
from database import get_db, Base, engine
from sqlalchemy.orm import sessionmaker

# Set up test database (in-memory SQLite)
TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="function")
def db_session():
    """Fixture to provide a fresh test database session."""
    Base.metadata.create_all(bind=engine)  # Create tables
    session = TestSessionLocal()
    yield session
    session.close()
    Base.metadata.drop_all(bind=engine)  # Clean up after tests

@pytest.fixture(scope="function")
async def client():
    """Fixture to create a test client for API requests."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client

@pytest.mark.asyncio
async def test_create_order(client):
    """Test creating an order with POST /orders."""
    response = await client.post("/orders", json={
        "symbol": "AAPL",
        "price": 150.5,
        "quantity": 10,
        "order_type": "buy"
    })
    assert response.status_code == 201
    assert response.json()["symbol"] == "AAPL"

@pytest.mark.asyncio
async def test_get_orders(client):
    """Test retrieving orders with GET /orders."""
    response = await client.get("/orders")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
