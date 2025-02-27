# Trade-Order-Service
This project is a simple backend service built with FastAPI that accepts and retrieves trade orders. It uses SQLite for simplicity and supports real-time order status updates via WebSockets. The application is containerized with Docker, and a CI/CD pipeline is set up using GitHub Actions to automatically run tests, build a Docker image, and deploy to an AWS EC2 instance

# Features
**REST API Endpoints:**
POST /orders – Submit a trade order with details (symbol, price, quantity, order type).
  
GET /orders – Retrieve a list of submitted orders.

**WebSocket Endpoint:**
ws://<host>:8000/ws – Real-time updates for order status.

**Database:**
Uses SQLite for storage (can be switched to PostgreSQL in production).

**Containerization:**
Dockerfile provided for building the Docker image.

**CI/CD:**
  GitHub Actions workflow for testing, building, and deploying the application to AWS EC2.

**Deployment:**
  The application is deployed on an AWS EC2 instance using Docker and Docker Compose.

# Project Structure
```bash
trade-order-service/
├── trade_order_service/        # Application package
│   ├── __init__.py             # Empty file to mark as a package
│   ├── main.py                 # FastAPI application code
│   └── db.py                   # Database setup (SQLite)
├── tests/                      # Test cases
│   ├── __init__.py             # Empty file
│   ├── test_orders.py          # API tests for orders
│   └── test_websocket.py       # WebSocket tests
├── requirements.txt            # Python dependencies
├── Dockerfile                  # Instructions to build the Docker image
├── docker-compose.yml          # (Optional) Local multi-container setup
└── .github/
    └── workflows/
        └── deploy.yml          # GitHub Actions workflow for CI/CD
```
