# backend/tests/test_main.py
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.main import app, get_db
from app.models import Base

SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(name="session")
def session_fixture():
    """Crea las tablas antes del test y las borra después."""
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)

@pytest.fixture(name="client")
def client_fixture(session):
    """Sobrescribe la dependencia get_db para usar la DB de prueba."""
    def override_get_db():
        try:
            yield session
        finally:
            session.close()

    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
    app.dependency_overrides.clear()

# --- CASOS DE PRUEBA ---

def test_create_mood(client):
    """Prueba la creación de un nuevo mood."""
    payload = {
        "mood_name": "Triste",
        "color_hex": "#000080",
        "music_url": "http://music.com/sad",
        "description": "Música para llorar"
    }
    response = client.post("/api/moods/", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["mood_name"] == "Triste"
    assert "id" in data

def test_read_moods(client):
    """Prueba que se pueden leer los moods (incluyendo el seeding si aplica o creados)."""
    client.post("/api/moods/", json={
        "mood_name": "TestMood",
        "color_hex": "#123456",
        "music_url": "url",
        "description": "desc"
    })

    response = client.get("/api/moods/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    assert data[0]["mood_name"] == "TestMood"

def test_check_mood_success(client):
    """Prueba buscar un mood existente."""
    client.post("/api/moods/", json={
        "mood_name": "Feliz",
        "color_hex": "#FFFF00",
        "music_url": "http://happy.com",
        "description": "Muy feliz"
    })

    # Buscarlo (probamos mayúsculas/minúsculas)
    payload = {"mood_input": "feLiZ"} 
    response = client.post("/api/moods/check", json=payload)
    
    assert response.status_code == 200
    data = response.json()
    assert data["mood_name"] == "Feliz"
    assert data["color_hex"] == "#FFFF00"

def test_check_mood_not_found(client):
    """Prueba buscar un mood que no existe."""
    payload = {"mood_input": "Enojado"} 
    response = client.post("/api/moods/check", json=payload)
    
    assert response.status_code == 404
    assert "No se encontró un VibeDeck" in response.json()["detail"]