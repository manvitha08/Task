import websockets
import pytest

@pytest.mark.asyncio
async def test_websocket():
    """Test WebSocket connection and real-time updates."""
    uri = "ws://localhost:8000/ws"
    async with websockets.connect(uri) as websocket:
        await websocket.send("subscribe")
        response = await websocket.recv()
        assert response == "Message received: subscribe"


