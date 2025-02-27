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
# Prerequisites
Python 3.10+

Docker (for containerization)

An AWS EC2 instance (Ubuntu recommended) with Docker installed

A GitHub repository with GitHub Actions enabled

# Setup
###1. Clone the Repository
```bash
git clone https://github.com/your-username/trade-order-service.git
cd trade-order-service
```
###2. Install Python Dependencies
```bash
pip install -r requirements.txt
```
3. Configure the Application
Review and update any settings in trade_order_service/main.py and trade_order_service/db.py as needed.

Running Locally
Start the Application
bash
Copy
Edit
uvicorn trade_order_service.main:app --reload
The app will be available at http://localhost:8000.

Run Tests
bash
Copy
Edit
pytest tests/
Containerization
Build the Docker Image
bash
Copy
Edit
docker build -t manvitha0802/trade-order-service:latest .
Run the Docker Container Locally
bash
Copy
Edit
docker run -p 8000:8000 manvitha0802/trade-order-service:latest
Deployment to AWS EC2
EC2 Setup
Launch an EC2 Instance:

Use an Ubuntu AMI.
Configure the security group to allow inbound SSH (port 22) and the application port (default 8000).
Install Docker on the EC2 Instance:

bash
Copy
Edit
sudo apt update
sudo apt install -y docker.io
sudo systemctl start docker
sudo systemctl enable docker
(Optional) Install Docker Compose:

Either install Docker Compose or use Docker Compose V2 commands (e.g., docker compose).
