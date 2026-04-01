"""FastAPI entrypoint that mounts the existing Flask app and provides WebSocket updates."""
from fastapi import FastAPI, WebSocket
from starlette.middleware.wsgi import WSGIMiddleware

from app import app as flask_app
from ws_manager import manager

fastapi_app = FastAPI()


@fastapi_app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            await websocket.receive_text()  # keep alive / no-op
    except Exception:
        manager.disconnect(websocket)


# Mount existing Flask application for all HTTP routes
fastapi_app.mount("/", WSGIMiddleware(flask_app))

# uvicorn entrypoint
app = fastapi_app
