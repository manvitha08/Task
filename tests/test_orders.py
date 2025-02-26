import pytest
from httpx import AsyncClient
from main import app, get_db, Base, engine  # Import directly from main
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
import os

# Add the root directory to Python's module search path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Set up test database (in-memory SQLite)
@pytest.fixture(scope="function")
def db_session():
    """Fixture to provide a fresh test database session using in-memory SQLite."""
    engine_test = create_engine("sqlite:///:memory:", connect_args={"check_same_thread": False})
    Base.metadata.create_all(bind=engine_test)  # Create tables for testing
    session = sessionmaker(autocommit=False, autoflush=False, bind=engine_test)()

    yield session

    session.close()
    Base.metadata.drop_all(bind=engine_test)  # Cleanup after test

@pytest.fixture(scope="function")
def override_get_db(db_session):
    """Override FastAPI's database dependency with test session."""
    def _get_db_override():
        yield db_session

    app.dependency_overrides[get_db] = _get_db_override  # Override FastAPI's DB dependency

    yield

    app.dependency_overrides.clear()  # Reset overrides after test

@pytest.fixture(scope="function")
async def client(override_get_db):
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
    assert response.status_code in [200, 201]  # Allow 200 or 201
    assert response.json()["symbol"] == "AAPL"

@pytest.mark.asyncio
async def test_get_orders(client):
    """Test retrieving orders with GET /orders."""
    response = await client.get("/orders")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
