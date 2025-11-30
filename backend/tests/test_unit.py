import pytest
from pydantic import ValidationError
from app.schemas import MoodMapCreate, MoodCheckRequest

def test_mood_map_create_valid():
    """Prueba que el modelo acepta datos correctos."""
    valid_data = {
        "mood_name": "Tranquilo",
        "color_hex": "#FFFFFF",
        "music_url": "https://music.com",
        "description": "Test description"
    }
    mood = MoodMapCreate(**valid_data)
    assert mood.mood_name == "Tranquilo"
    assert mood.color_hex == "#FFFFFF"

def test_mood_map_create_missing_field():
    """Prueba que el modelo falla si falta un campo obligatorio."""
    invalid_data = {
        "mood_name": "Incompleto",
    }
    
    with pytest.raises(ValidationError):
        MoodMapCreate(**invalid_data)

def test_mood_check_request_whitespace():
    """Verifica si pudiéramos tener lógica de limpieza en el modelo."""
    request = MoodCheckRequest(mood_input="  Feliz  ")
    assert request.mood_input == "  Feliz  "