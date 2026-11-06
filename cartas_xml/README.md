# 📜 Archivos XML de Estudio Profundo del Tarot (78 Cartas)

Esta carpeta contiene la colección completa de los **78 archivos XML** del Tarot, uno para cada carta. Están diseñados para que puedas abrir cualquier archivo con un editor de texto (como Bloc de Notas, Notepad++, VS Code o Sublime Text), modificar o enriquecer sus textos fácilmente y tener tu contenido siempre organizado y bajo tu control.

---

## 📂 Organización de Carpetas

```text
cartas_xml/
├── arcanos_mayores/       -> 22 Arcanos Mayores (00_el_loco.xml al 21_el_mundo.xml)
├── bastos/                -> 14 Arcanos Menores de Fuego (As a Rey de Bastos)
├── copas/                 -> 14 Arcanos Menores de Agua (As a Rey de Copas)
├── espadas/               -> 14 Arcanos Menores de Aire (As a Rey de Espadas)
├── oros/                  -> 14 Arcanos Menores de Tierra (As a Rey de Oros)
└── README.md              -> Esta guía de referencia
```

---

## 🏷️ Estructura de Cada Archivo XML

Cada archivo `.xml` cuenta con las siguientes etiquetas limpias y fáciles de editar:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<arcano id="el-loco">
  <numero>0</numero>
  <nombre>El Loco</nombre>
  <tipo>Arcano Mayor</tipo>
  <palo>Ninguno</palo>
  <elemento>Aire</elemento>
  <astrologia>Urano</astrologia>

  <!-- 1. HISTORIA Y ORIGEN SIMBÓLICO -->
  <historia>
    Escribe aquí los orígenes históricos del arcano, su evolución desde el Tarot de Marsella y Visconti-Sforza hasta Rider-Waite-Smith...
  </historia>

  <!-- 2. SIGNIFICADO FUNDAMENTAL -->
  <significado_fundamental>
    Escribe aquí la esencia arquetípica, el mensaje central y psicológico de la carta...
  </significado_fundamental>

  <!-- 3. LA CARTA EN POSICIÓN NORMAL -->
  <posicion_normal>
    <resumen>Resumen general del arcano al derecho.</resumen>
    <amor>Mensaje e interpretación en vínculos, parejas y romance.</amor>
    <dinero_trabajo>Mensaje en profesión, proyectos, negocios y finanzas.</dinero_trabajo>
    <salud>Mensaje de vitalidad física, bienestar y energía corporal.</salud>
    <espiritualidad>Mensaje de evolución del alma, intuición y propósito sagrado.</espiritualidad>
  </posicion_normal>

  <!-- 4. LA CARTA EN POSICIÓN INVERTIDA -->
  <posicion_invertida>
    <resumen>Resumen general del bloqueo o exceso del arcano al invertirse.</resumen>
    <amor>Desafíos o advertencias en el plano afectivo.</amor>
    <dinero_trabajo>Desafíos, advertencias o lecciones en el trabajo o dinero.</dinero_trabajo>
    <salud>Aspectos del cuerpo o mente que requieren cuidado o atención.</salud>
    <espiritualidad>Bloqueos internos y cómo sanar o realinear la energía.</espiritualidad>
  </posicion_invertida>

  <!-- 5. LO QUE LO HACE ÚNICO FRENTE A SUS SIMILARES (Opción A: Texto directo) -->
  <lo_que_lo_hace_unico>
    Explicación comparativa clara de qué distingue a esta carta frente a otras cartas semejantes de la baraja...
  </lo_que_lo_hace_unico>

  <!-- O BIEN (Opción B: Lista de comparativas etiquetadas por carta) -->
  <!--
  <lo_que_lo_hace_unico>
    <resumen>Resumen general de su singularidad arquetípica.</resumen>
    <comparativas>
      <comparar carta="El Emperador">
        Explicación de la diferencia frente a El Emperador...
      </comparar>
      <comparar carta="El Mago">
        Explicación de la diferencia frente a El Mago...
      </comparar>
    </comparativas>
  </lo_que_lo_hace_unico>
  -->

  <!-- 6. CURIOSIDADES DEL ARCANO -->
  <curiosidades>
    <item>Primera curiosidad, mito o dato poco conocido.</item>
    <item>Segunda curiosidad o simbolismo oculto.</item>
    <item>Tercera curiosidad o anécdota histórica.</item>
  </curiosidades>

  <!-- 7. UNA HISTORIA INSPIRADA -->
  <historia_inspirada>
    <titulo>Título de la historia o parábola</titulo>
    <relato>
      Cuento narrativo o parábola viva que encarna la energía del arcano para transmitir su enseñanza de manera inolvidable...
    </relato>
  </historia_inspirada>

  <!-- 8. AUDIOLIBRO Y CAPÍTULOS INTERACTIVOS -->
  <audio>
    <archivo>assets/audio/el-loco.wav</archivo>
    <titulo>El Salto al Vacío Sagrado - Audio Guía</titulo>
    <!-- NOTA: La duración se calcula automáticamente desde el archivo de audio (.wav o .mp3) -->
    <capitulos>
      <capitulo tiempo="0:00">Introducción y Simbolismo del Precipicio</capitulo>
      <capitulo tiempo="2:45">Significado en Posición Normal</capitulo>
      <capitulo tiempo="5:30">Amor, Vocación y Espiritualidad</capitulo>
      <capitulo tiempo="8:15">Posición Invertida y Advertencias</capitulo>
      <capitulo tiempo="11:00">Diferencias con otros Arcanos</capitulo>
      <capitulo tiempo="13:20">Meditación Guiada del Salto Sagrado</capitulo>
    </capitulos>
  </audio>
</arcano>
```

---

## ⚡ ¿Cómo Sincronizar y Actualizar la Web?

### Opción 1: Todo en 1 Clic (Recomendado)
Haz doble clic en **`actualizar_todo.bat`** en la carpeta principal:
1. Sincroniza todos tus archivos XML modificados.
2. Calcula automáticamente las duraciones de los audios existentes.
3. Procesa los capítulos interactivos.
4. Te pregunta si deseas subir a GitHub de inmediato (`S/N`) y hace el `git push` automáticamente.

### Opción 2: Sincronización Local Rápida
Haz doble clic en **`sincronizar_textos.bat`** para ver tus cambios de inmediato en tu navegador local (`index.html`).

### Opción 3: Manual por Consola
```bash
python tools/sync_xml_to_db.py
git add .
git commit -m "Actualizar cartas XML y audiolibros"
git push origin main
```
