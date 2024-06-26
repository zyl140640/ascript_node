import websocket


class WebSocketClient:
    def __init__(self):
        self.ws = websocket.WebSocket()

    def __enter__(self):
        return self

    def connect(self, url):
        try:
            self.ws.connect(url)
        except Exception as e:
            print(f"连接 {url} 失败。错误: {str(e)}")

    def send(self, message):
        try:
            self.ws.send(message)
        except Exception as e:
            print(f"发送消息失败。错误: {str(e)}")

    def receive(self):
        try:
            return self.ws.recv()
        except Exception as e:
            print(f"接收消息失败。错误: {str(e)}")

    def __exit__(self, type, value, traceback):
        self.ws.close()
