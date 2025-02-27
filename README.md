## Trade-Order-Service
This project is a simple backend service built with FastAPI that accepts and retrieves trade orders. It uses SQLite for simplicity and supports real-time order status updates via WebSockets. The application is containerized with Docker, and a CI/CD pipeline is set up using GitHub Actions to automatically run tests, build a Docker image, and deploy to an AWS EC2 instance

## Features
**REST API Endpoints:**

• POST /orders – Submit a trade order with details (symbol, price, quantity, order type).
  
• GET /orders – Retrieve a list of submitted orders.

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
  # API documentation
 [ API documentation](http://127.0.0.1:8000/docs#/default/get_orders_orders_get)

## Project Structure
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
## Prerequisites
• Python 3.10+

• Docker (for containerization)

• An AWS EC2 instance (Ubuntu recommended) with Docker installed

• A GitHub repository with GitHub Actions enabled

## Setup
### 1. Clone the Repository
```bash
git clone https://github.com/your-username/trade-order-service.git
cd trade-order-service
```
### 2. Install Python Dependencies
```bash
pip install -r requirements.txt
```
### 3. Configure the Application
Review and update any settings in ```bash trade_order_service/main.py ``` and ```bash trade_order_service/db.py ``` as needed.

## Running Locally
### Start the Application
```bash
uvicorn trade_order_service.main:app --reload
```
The app will be available at http://localhost:8000.

### Run Tests
```bash
pytest tests/
```
## Containerization
### Build the Docker Image
```bash
docker build -t manvitha0802/trade-order-service:latest .
```
### Run the Docker Container Locally
```bash
docker run -p 8000:8000 manvitha0802/trade-order-service:latest
```
## Deployment to AWS EC2
### EC2 Setup
#### 1. Launch an EC2 Instance:
Use an Ubuntu AMI.

Configure the security group to allow inbound SSH (port 22) and the application port (default 8000).
#### 2. Install Docker on the EC2 Instance:
```bash
sudo apt update
sudo apt install -y docker.io
sudo systemctl start docker
sudo systemctl enable docker
```
#### 3. (Optional) Install Docker Compose:

Either install Docker Compose or use Docker Compose V2 commands (e.g., ```bash docker compose ```).

## GitHub Actions CI/CD
The CI/CD pipeline is defined in ```bash .github/workflows/deploy.yml ```. It performs the following tasks:

• Runs tests on pull requests.

• Builds and pushes the Docker image to DockerHub.

• SSHes into your EC2 instance and deploys the latest Docker image using Docker Compose.

## Required GitHub Secrets
Configure these secrets in your repository (Settings → Secrets and variables → Actions):

• **DOCKERHUB_USERNAME** – Your DockerHub username.

• **DOCKERHUB_PASSWORD** – Your DockerHub password or personal access token (with Read & Write permissions).

• **EC2_HOST** – The public IP or hostname of your EC2 instance.

• **EC2_USER** – The SSH username (e.g., ubuntu).

• **EC2_SSH_KEY_B64** – The Base64-encoded content of your private SSH key (generated from your ```bash trade-order-key.pem ``` file).

## Troubleshooting
• **SSH Key Issues:**

Verify that the EC2_SSH_KEY_B64 secret is correctly set by checking the debug output in the workflow logs.

• **Docker Compose Command Not Found:**

Update the deploy script to use the correct command based on your EC2 instance setup.

• **CI/CD Pipeline Failures:**

Review the GitHub Actions logs for error messages and verify that all secrets are correctly configured.

## Contributing
Feel free to submit issues or pull requests with improvements.
