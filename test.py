import asyncio
import websockets

async def echo(websocket, path):
    name = await websocket.recv()
    print(f"< {name}")

    greeting = f"Hello {name}!"

    await websocket.send(greeting)
    print(f"> {greeting}")

asyncio.run(websockets.serve(echo, "localhost", 8765))
