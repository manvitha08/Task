import websockets
import pytest

@pytest.mark.asyncio
async def test_websocket():
    """Test WebSocket connection and real-time updates."""
    uri = "ws://localhost:8000/ws"  # Ensure this matches your WebSocket endpoint in main.py
    async with websockets.connect(uri) as websocket:
        # Send a message to the WebSocket server
        await websocket.send("subscribe")
        
        # Receive the response from the WebSocket server
        response = await websocket.recv()
        
        # Assert that the response is what we expect
        assert response == "Message received: subscribe"
