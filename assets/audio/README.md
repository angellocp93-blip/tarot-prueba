# 🎧 Directorio de Audiolibros y Audio Guías de Tarot

Esta carpeta está preparada para alojar los archivos de audio (audiolibros, meditaciones guiadas o lecciones en audio) de cada una de las 78 cartas del Tarot.

---

## 📁 Nomenclatura Exacta de Archivos

Para que la plataforma reproduzca automáticamente el audio correspondiente a cada carta sin necesidad de configurar nada, nombra cada archivo con el `id` de la carta seguido de la extensión `.mp3`:

### 👑 Arcanos Mayores (22 archivos)
- `el-loco.mp3` - 0. El Loco
- `el-mago.mp3` - I. El Mago
- `la-sacerdotisa.mp3` - II. La Sacerdotisa
- `la-emperatriz.mp3` - III. La Emperatriz
- `el-emperador.mp3` - IV. El Emperador
- `el-hierofante.mp3` - V. El Hierofante
- `los-enamorados.mp3` - VI. Los Enamorados
- `el-carro.mp3` - VII. El Carro
- `la-fuerza.mp3` - VIII. La Fuerza
- `el-ermitano.mp3` - IX. El Ermitaño
- `la-rueda-de-la-fortuna.mp3` - X. La Rueda de la Fortuna
- `la-justicia.mp3` - XI. La Justicia
- `el-colgado.mp3` - XII. El Colgado
- `la-muerte.mp3` - XIII. La Muerte
- `la-templanza.mp3` - XIV. La Templanza
- `el-diablo.mp3` - XV. El Diablo
- `la-torre.mp3` - XVI. La Torre
- `la-estrella.mp3` - XVII. La Estrella
- `la-luna.mp3` - XVIII. La Luna
- `el-sol.mp3` - XIX. El Sol
- `el-juicio.mp3` - XX. El Juicio
- `el-mundo.mp3` - XXI. El Mundo

---

### 🔥 Arcanos Menores - Bastos (14 archivos)
- `as-de-bastos.mp3`
- `dos-de-bastos.mp3`
- `tres-de-bastos.mp3`
- `cuatro-de-bastos.mp3`
- `cinco-de-bastos.mp3`
- `seis-de-bastos.mp3`
- `siete-de-bastos.mp3`
- `ocho-de-bastos.mp3`
- `nueve-de-bastos.mp3`
- `diez-de-bastos.mp3`
- `sota-de-bastos.mp3`
- `caballero-de-bastos.mp3`
- `reina-de-bastos.mp3`
- `rey-de-bastos.mp3`

---

### 💧 Arcanos Menores - Copas (14 archivos)
- `as-de-copas.mp3`
- `dos-de-copas.mp3`
- `tres-de-copas.mp3`
- `cuatro-de-copas.mp3`
- `cinco-de-copas.mp3`
- `seis-de-copas.mp3`
- `siete-de-copas.mp3`
- `ocho-de-copas.mp3`
- `nueve-de-copas.mp3`
- `diez-de-copas.mp3`
- `sota-de-copas.mp3`
- `caballero-de-copas.mp3`
- `reina-de-copas.mp3`
- `rey-de-copas.mp3`

---

### 💨 Arcanos Menores - Espadas (14 archivos)
- `as-de-espadas.mp3`
- `dos-de-espadas.mp3`
- `tres-de-espadas.mp3`
- `cuatro-de-espadas.mp3`
- `cinco-de-espadas.mp3`
- `seis-de-espadas.mp3`
- `siete-de-espadas.mp3`
- `ocho-de-espadas.mp3`
- `nueve-de-espadas.mp3`
- `diez-de-espadas.mp3`
- `sota-de-espadas.mp3`
- `caballero-de-espadas.mp3`
- `reina-de-espadas.mp3`
- `rey-de-espadas.mp3`

---

### 🪙 Arcanos Menores - Oros (14 archivos)
- `as-de-oros.mp3`
- `dos-de-oros.mp3`
- `tres-de-oros.mp3`
- `cuatro-de-oros.mp3`
- `cinco-de-oros.mp3`
- `seis-de-oros.mp3`
- `siete-de-oros.mp3`
- `ocho-de-oros.mp3`
- `nueve-de-oros.mp3`
- `diez-de-oros.mp3`
- `sota-de-oros.mp3`
- `caballero-de-oros.mp3`
- `reina-de-oros.mp3`
- `rey-de-oros.mp3`

---

## 🎚️ Recomendaciones Técnicas de Audio
- **Formato:** `.mp3` (o `.m4a` / `.aac`).
- **Bitrate recomendado:** 128 kbps o 192 kbps (ideal para voz hablada).
- **Peso por archivo:** Entre 2 MB y 6 MB (para 3 a 7 minutos de locución).
- **Canales:** Mono o Stereo, frecuencia de muestreo 44.1 kHz.

---

## 🚀 Cómo Subirlos a GitHub

### Opción A: Desde la Web de GitHub (Sin comandos)
1. Ve a tu repositorio en GitHub: `https://github.com/angellocp93-blip/tarot-prueba`
2. Navega a `assets` -> `audio`.
3. Haz clic en el botón **Add file** -> **Upload files**.
4. Arrastra tus archivos `.mp3` desde tu computadora.
5. Haz clic en **Commit changes**.
6. ¡Listo! La web en GitHub Pages reproducirá tus audios inmediatamente.

### Opción B: Desde tu Computadora con Git
1. Pega tus archivos `.mp3` dentro de esta carpeta (`TAROT/assets/audio/`).
2. Abre tu terminal en la carpeta del proyecto y ejecuta:
   ```bash
   git add assets/audio
   git commit -m "Agregar audiolibros de cartas"
   git push origin main
   ```
