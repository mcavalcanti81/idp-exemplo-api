from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    assert client.get("/health").json() == {"status": "ok"}


def test_ping():
    assert client.get("/ping").json() == {"ping": "pong"}


def test_root_reports_environment(monkeypatch):
    monkeypatch.setenv("APP_ENV", "dev")
    body = client.get("/").json()
    assert body["service"] == "exemplo-api"
    assert body["environment"] == "dev"
