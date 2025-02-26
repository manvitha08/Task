import pytest
import asyncio
import websockets

@pytest.mark.asyncio
async def test_websocket():
    """Test WebSocket connection and real-time updates."""
    uri = "ws://localhost:8000/ws"
    async with websockets.connect(uri) as websocket:
        await websocket.send("subscribe")
        response = await websocket.recv()
        assert response == "Subscribed to updates"
