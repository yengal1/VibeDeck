// frontend/script.js

// CLAVE: Usa el nombre del servicio Docker Compose del Backend.
const API_CHECK_URL = 'http://api:8000/api/moods/check'; 

const moodInput = document.getElementById('mood-input');
const resultBox = document.getElementById('result-box');
const vibeName = document.getElementById('vibe-name');
const vibeDesc = document.getElementById('vibe-desc');
const musicPlayer = document.getElementById('music-player');
const appContainer = document.getElementById('app-container');

async function checkVibe() {
    const mood = moodInput.value.trim();
    if (!mood) {
        alert("Por favor, ingresa un estado de ánimo.");
        return;
    }

    resultBox.classList.add('loading'); // Muestra estado de carga
    resultBox.classList.remove('hidden');

    try {
        const response = await fetch(API_CHECK_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            // Envía el ánimo ingresado al Backend
            body: JSON.stringify({ mood_input: mood })
        });

        if (!response.ok) {
            // Lanza un error si el estado de ánimo no fue encontrado (ej: 404)
            const errorData = await response.json();
            throw new Error(errorData.detail || 'Error en el servidor.');
        }

        const data = await response.json();
        
        // --- PROCESAMIENTO EXITOSO ---
        
        // 1. Actualiza los estilos y el DOM
        appContainer.style.backgroundColor = data.color_hex + '50'; // Color de fondo semitransparente
        vibeName.innerText = data.mood_name;
        vibeDesc.innerText = data.color_hex;
        
        // 2. Inserta el reproductor de música (iframe)
        const iframeHtml = `
            <iframe src="${data.music_url}" frameborder="0" allow="autoplay; encrypted-media; gyroscope" allowfullscreen></iframe>
        `;
        musicPlayer.innerHTML = iframeHtml;
        
        resultBox.classList.remove('loading');

    } catch (error) {
        // --- MANEJO DE ERRORES ---
        alert("Error VibeDeck: " + error.message);
        appContainer.style.backgroundColor = '#FFCCCC50'; // Fondo rojo de error
        musicPlayer.innerHTML = '<p class="error-message">Música no disponible. Intenta de nuevo.</p>';
        resultBox.classList.remove('loading');
        vibeName.innerText = 'Error';
        vibeDesc.innerText = '';
        console.error("Error al buscar Vibe:", error);
    }
}