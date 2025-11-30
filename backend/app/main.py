# backend/app/main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.orm.exc import NoResultFound
from typing import List

# Importar modelos y esquemas
from .models import Base, MoodMap as DBMoodMap 
from .schemas import MoodMapCreate, MoodMap as SchemaMoodMap, MoodCheckRequest, MoodCheckResponse 

# --- 1. CONFIGURACIÓN DE LA BASE DE DATOS ---

# La URL de conexión a SQLite. El archivo 'vibe_db.db' se crea en el directorio /app.
SQLALCHEMY_DATABASE_URL = "sqlite:///./vibe_db.db" 

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    # Necesario para SQLite en entornos de desarrollo asíncronos/multihilo
    connect_args={"check_same_thread": False} 
)

# Sesión local para interactuar con la DB
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crea las tablas definidas en models.py si no existen
Base.metadata.create_all(bind=engine)

# Función de dependencia: Obtiene una sesión de DB por cada solicitud
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI(title="VibeDeck API")

# --- 2. LÓGICA DE INSERCIÓN INICIAL (SEEDING) ---

def seed_initial_moods(db: Session):
    """Inserta datos iniciales si la DB está vacía para que la app sea funcional."""
    if db.query(DBMoodMap).count() == 0:
        initial_moods = [
            DBMoodMap(
                mood_name="Calmado", 
                color_hex="#4682B4", # Azul acero
                # URL 
                music_url="https://www.youtube.com/watch?v=hLQl3WQQoQ0&list=PLVGaMAFj8qy0I6lcbGhBAaNQXdcLH9sfQ", 
                description="Ideal para relajarse y meditar."
            ),
            DBMoodMap(
                mood_name="Enérgico", 
                color_hex="#FFD700", # Dorado
                # URL 
                music_url="https://www.youtube.com/watch?v=hLQl3WQQoQ0&list=PLVGaMAFj8qy0I6lcbGhBAaNQXdcLH9sfQ", 
                description="Para empezar el día con fuerza."
            )
        ]
        db.add_all(initial_moods)
        db.commit()

# Llama a la función de seeding al iniciar la aplicación
with SessionLocal() as db:
    seed_initial_moods(db)

# --- 3. ENDPOINTS DE LA API ---

@app.get("/api/moods/", response_model=List[SchemaMoodMap])
def read_moods(db: Session = Depends(get_db)):
    """Muestra todos los mapas de ánimo guardados."""
    return db.query(DBMoodMap).all()

@app.post("/api/moods/check", response_model=MoodCheckResponse)
def check_mood(request: MoodCheckRequest, db: Session = Depends(get_db)):
    """Busca el estado de ánimo (sensible a mayúsculas/minúsculas) y devuelve sus recursos."""
    mood_name = request.mood_input.strip()
    
    # Busca el ánimo usando la función ilike para hacer la búsqueda insensible a mayúsculas/minúsculas
    vibe = db.query(DBMoodMap).filter(
        DBMoodMap.mood_name.ilike(mood_name)
    ).first()
    
    if not vibe:
        raise HTTPException(
            status_code=404, 
            detail=f"No se encontró un VibeDeck para '{mood_name}'. Intenta con 'Calmado' o 'Enérgico'."
        )
    
    return MoodCheckResponse(
        mood_name=vibe.mood_name,
        color_hex=vibe.color_hex,
        music_url=vibe.music_url
    )

@app.post("/api/moods/", response_model=SchemaMoodMap, status_code=201)
def create_mood(mood: MoodMapCreate, db: Session = Depends(get_db)):
    """Permite crear un nuevo mapa de ánimo (solo para administración)."""
    db_mood = DBMoodMap(**mood.model_dump())
    
    db.add(db_mood)
    db.commit()
    db.refresh(db_mood)
    return db_mood
