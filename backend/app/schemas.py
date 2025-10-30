# backend/app/schemas.py
from pydantic import BaseModel, Field
from typing import Optional, List

# Esquema para crear o actualizar un MoodMap (lo que el usuario/admin envía)
class MoodMapCreate(BaseModel):
    mood_name: str = Field(..., min_length=3, max_length=50)
    # Valida que el color HEX siga el patrón básico (#RGB o #RRGGBB)
    color_hex: str = Field(..., pattern="^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$") 
    music_url: str
    description: Optional[str] = None

# Esquema de respuesta completo (lo que la API devuelve al listar)
class MoodMap(MoodMapCreate):
    id: int

    # Configuración necesaria para mapear el objeto de SQLAlchemy a Pydantic
    class Config:
        from_attributes = True

# Esquema de Request para la función principal "Check"
class MoodCheckRequest(BaseModel):
    mood_input: str

# Esquema de Response para la función principal "Check" (datos que usa el JS)
class MoodCheckResponse(BaseModel):
    mood_name: str
    color_hex: str
    music_url: str