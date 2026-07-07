from __future__ import annotations

import json
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse


class MockHandler(BaseHTTPRequestHandler):
    server_version = "ProjectAMock/1.0"

    def do_GET(self) -> None:
        parsed = urlparse(self.path)
        if parsed.path in ("/", ""):
            self._json(
                200,
                {
                    "code": 0,
                    "service": "project-a-mock",
                    "endpoints": [
                        "GET /jmeter-api/health",
                        "POST /jmeter-api/login",
                        "GET /jmeter-api/profile",
                    ],
                },
            )
            return

        if parsed.path == "/jmeter-api/health":
            self._json(200, {"code": 0, "status": "ok", "service": "project-a-mock"})
            return

        if parsed.path == "/jmeter-api/profile":
            auth = self.headers.get("Authorization", "")
            if auth != "Bearer jt_alice_demo_token":
                self._json(401, {"code": 40101, "message": "unauthorized"})
                return
            self._json(200, {"code": 0, "profile": {"username": "alice", "role": "tester"}})
            return

        self._json(404, {"code": 40401, "message": "not found"})

    def do_POST(self) -> None:
        parsed = urlparse(self.path)
        if parsed.path != "/jmeter-api/login":
            self._json(404, {"code": 40401, "message": "not found"})
            return

        payload = self._read_json()
        username = payload.get("username")
        password = payload.get("password")

        if username is None or password is None or username == "" or password == "":
            self._json(400, {"code": 40001, "message": "username and password are required"})
            return
        if username == "not_exist":
            self._json(200, {"code": 1001, "message": "user not found"})
            return
        if username == "alice" and password != "123456":
            self._json(200, {"code": 1002, "message": "wrong password"})
            return
        if username == "alice" and password == "123456":
            self._json(200, {"code": 0, "message": "success", "token": "jt_alice_demo_token"})
            return

        self._json(200, {"code": 1001, "message": "user not found"})

    def log_message(self, format: str, *args: object) -> None:
        return

    def _read_json(self) -> dict:
        length = int(self.headers.get("Content-Length", "0"))
        if length == 0:
            return {}
        raw = self.rfile.read(length).decode("utf-8")
        try:
            return json.loads(raw)
        except json.JSONDecodeError:
            return {}

    def _json(self, status: int, body: dict) -> None:
        data = json.dumps(body, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)


def start_mock_server(host: str, port: int) -> ThreadingHTTPServer:
    server = ThreadingHTTPServer((host, port), MockHandler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    return server


def run_mock_server_forever(host: str = "127.0.0.1", port: int = 3100) -> None:
    server = ThreadingHTTPServer((host, port), MockHandler)
    print(f"Mock API listening on http://{host}:{port}")
    print("Try: GET /jmeter-api/health")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping mock API server...")
    finally:
        server.shutdown()
        server.server_close()


if __name__ == "__main__":
    from config.settings import get_settings

    settings = get_settings()
    run_mock_server_forever(settings.mock_host, settings.mock_port)
