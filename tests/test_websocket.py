from starlette.testclient import TestClient
from trade_order_service.main import app

def test_websocket():
    client = TestClient(app)
    with client.websocket_connect("/ws") as websocket:
        websocket.send_text("subscribe")
        data = websocket.receive_text()
        assert data == "Message received: subscribe"
