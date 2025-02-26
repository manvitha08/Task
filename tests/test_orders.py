import pytest
from httpx import AsyncClient
from main import app  # Import FastAPI app
from database import get_db, Base, engine
from sqlalchemy.orm import sessionmaker
import sys
import os

# Add the root directory to Python's module search path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from trade_order_service.main import app  # If your project is structured this way

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

# Change fixture decorator to pytest_asyncio.fixture
@pytest_asyncio.fixture(scope="function")
async def client():
    """Fixture to create a test client for API requests."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client
