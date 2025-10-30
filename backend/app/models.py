# backend/app/models.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Base de la que heredan todos los modelos de SQLAlchemy
Base = declarative_base()

class MoodMap(Base):
    """Define la tabla 'mood_maps' para almacenar la relación Ánimo -> Recursos."""
    
    __tablename__ = "mood_maps"

    id = Column(Integer, primary_key=True, index=True)
    # El nombre del ánimo, debe ser único para evitar duplicados
    mood_name = Column(String, unique=True, index=True) 
    # Código de color hexadecimal para el fondo del Frontend
    color_hex = Column(String)                          
    # URL de un iframe de YouTube/Spotify para la música
    music_url = Column(String)                          
    # Descripción corta del ambiente
    description = Column(String)