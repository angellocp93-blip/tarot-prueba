import json
import os

with open("data/cards_78.json", "r", encoding="utf-8") as f:
    cards_list = json.load(f)

# 1. 12 TIRADAS DETALLADAS
spreads_data = [
    {
        "id": "carta-del-dia",
        "name": "Carta del Día / Consejo Instantáneo",
        "card_count": 1,
        "difficulty": "Principiante",
        "description": "La tirada fundamental para sintonizar con la energía del día, recibir una guía directa ante una duda rápida o meditar en un arquetipo.",
        "when_to_use": "Cada mañana al despertar, o en cualquier momento que necesites un consejo rápido y directo para actuar con sabiduría.",
        "positions": [
            {"pos": 1, "name": "Energía central y consejo", "desc": "¿Qué energía predomina en tu jornada y qué actitud consciente debes adoptar?"}
        ],
        "layout": "single"
    },
    {
        "id": "pasado-presente-futuro",
        "name": "Pasado, Presente y Futuro",
        "card_count": 3,
        "difficulty": "Principiante",
        "description": "La tirada clásica de tres cartas que revela la línea temporal de cualquier asunto: de dónde vienes, dónde estás y hacia dónde te diriges.",
        "when_to_use": "Para obtener una visión general rápida y clara sobre el desarrollo de cualquier situación personal, amorosa o laboral.",
        "positions": [
            {"pos": 1, "name": "Pasado / Raíz", "desc": "Causas, vivencias o influencias recientes que originaron la situación actual."},
            {"pos": 2, "name": "Presente / Momento actual", "desc": "La realidad inmediata: cómo estás viviendo y percibiendo la situación hoy."},
            {"pos": 3, "name": "Futuro / Tendencia probable", "desc": "Hacia dónde se encamina el asunto si mantienes la trayectoria actual."}
        ],
        "layout": "row-3"
    },
    {
        "id": "situacion-obstaculo-consejo",
        "name": "Situación, Obstáculo y Consejo",
        "card_count": 3,
        "difficulty": "Principiante",
        "description": "Una tirada resolutiva y práctica diseñada para desatascar problemas, entender el nudo del conflicto y recibir una acción concreta.",
        "when_to_use": "Cuando te sientes bloqueado en un proyecto, en una relación o ante un problema y necesitas saber exactamente qué hacer.",
        "positions": [
            {"pos": 1, "name": "La Situación", "desc": "La naturaleza real del asunto tal como se presenta ahora."},
            {"pos": 2, "name": "El Obstáculo / Desafío", "desc": "Qué te está frenando (puede ser un factor externo o un bloqueo interno propio)."},
            {"pos": 3, "name": "El Consejo / Acción", "desc": "La mejor estrategia o actitud para superar el obstáculo y avanzar."}
        ],
        "layout": "triangle-up"
    },
    {
        "id": "mente-cuerpo-espiritu",
        "name": "Mente, Cuerpo y Espíritu (Alineación Holística)",
        "card_count": 3,
        "difficulty": "Principiante",
        "description": "Tirada de autoconocimiento y salud integral para evaluar cómo están alineados tus pensamientos, tu energía física y tu conexión espiritual.",
        "when_to_use": "En momentos de chequeo personal, cambios de estación o cuando sientes cansancio y no sabes de dónde proviene el desajuste.",
        "positions": [
            {"pos": 1, "name": "Mente / Pensamientos", "desc": "Estado psicológico, preocupaciones, creencias predominantes y claridad mental."},
            {"pos": 2, "name": "Cuerpo / Vitalidad", "desc": "Salud física, hábitos, necesidades corporales y energía material disponible."},
            {"pos": 3, "name": "Espíritu / Alma", "desc": "Propósito interno, lección que tu ser superior busca integrar hoy."}
        ],
        "layout": "row-3"
    },
    {
        "id": "cruz-simple",
        "name": "La Cruz Simple (4 Factores Clave)",
        "card_count": 4,
        "difficulty": "Intermedio",
        "description": "Una poderosa estructura en cruz para analizar cualquier cuestión sopesando los puntos a favor, las fuerzas en contra, la tendencia y el consejo final.",
        "when_to_use": "Antes de tomar una decisión importante o firmar un acuerdo comercial, para medir ventajas y riesgos.",
        "positions": [
            {"pos": 1, "name": "A favor / Fuerzas aliadas", "desc": "Tus fortalezas, apoyos externos y lo que juega a tu favor."},
            {"pos": 2, "name": "En contra / Obstáculos", "desc": "Riesgos, debilidades o personas que se oponen a tus planes."},
            {"pos": 3, "name": "Resolución / Tendencia", "desc": "El desenlace más probable según la interacción de ambas fuerzas."},
            {"pos": 4, "name": "Consejo maestro", "desc": "La clave maestra que inclinará la balanza a tu favor."}
        ],
        "layout": "cross-4"
    },
    {
        "id": "dos-caminos",
        "name": "Los Dos Caminos (Tirada de Decisión)",
        "card_count": 5,
        "difficulty": "Intermedio",
        "description": "Especialmente diseñada para dilemas entre dos opciones (ej. Aceptar o rechazar una oferta; Elegir opción A o B).",
        "when_to_use": "Cuando dudas entre dos caminos incompatibles y deseas comparar qué ocurriría si eliges uno u otro.",
        "positions": [
            {"pos": 1, "name": "El dilema / Punto de partida", "desc": "El origen de la indecisión y lo que realmente está en juego."},
            {"pos": 2, "name": "Camino A: Consecuencias", "desc": "Qué experimentarás si eliges la primera opción."},
            {"pos": 3, "name": "Camino A: Desenlace", "desc": "El resultado final al que te conduce la opción A."},
            {"pos": 4, "name": "Camino B: Consecuencias", "desc": "Qué experimentarás si eliges la segunda opción."},
            {"pos": 5, "name": "Camino B: Desenlace", "desc": "El resultado final al que te conduce la opción B."}
        ],
        "layout": "v-shape"
    },
    {
        "id": "vinculo-pareja",
        "name": "Vínculo y Relación de Pareja",
        "card_count": 6,
        "difficulty": "Intermedio",
        "description": "Explora la dinámica afectiva entre dos personas: cómo ve cada uno la relación, qué sienten, qué los une y hacia dónde va el vínculo.",
        "when_to_use": "Para parejas que desean profundizar su complicidad, o durante crisis amorosas para entender el sentir de ambas partes sin juzgar.",
        "positions": [
            {"pos": 1, "name": "Tú / Tu sentir actual", "desc": "Tus emociones, expectativas y actitud consciente e inconsciente en la relación."},
            {"pos": 2, "name": "La otra persona / Su sentir", "desc": "Lo que la otra persona siente, piensa y espera del vínculo."},
            {"pos": 3, "name": "El lazo / Lo que los une", "desc": "El punto fuerte de la relación: afinidades, recuerdos o propósito común."},
            {"pos": 4, "name": "La fricción / Lo que los separa", "desc": "Diferencias, heridas no resueltas o interferencias externas."},
            {"pos": 5, "name": "Futuro cercano", "desc": "La evolución probable del vínculo en los próximos meses."},
            {"pos": 6, "name": "Consejo para el amor", "desc": "La actitud recomendada para sanar o fortalecer la relación."}
        ],
        "layout": "columns-2"
    },
    {
        "id": "herradura",
        "name": "Tirada de la Herradura (7 Cartas)",
        "card_count": 7,
        "difficulty": "Intermedio / Avanzado",
        "description": "Una de las tiradas más completas y tradicionales del tarot europeo. Dibuja un arco parabólico que ilumina todos los ángulos de un asunto.",
        "when_to_use": "Para consultas globales de gran calado donde se requiere una visión profunda y detallada de presente, influencias ocultas y futuro.",
        "positions": [
            {"pos": 1, "name": "El pasado lejano", "desc": "Eventos y decisiones pasadas que formaron el cimiento de la situación."},
            {"pos": 2, "name": "El presente inmediato", "desc": "Dónde te encuentras ahora mismo y qué factores demandan atención."},
            {"pos": 3, "name": "Fuerzas ocultas / Inconsciente", "desc": "Factores que no estás viendo o influencias que actúan bajo la superficie."},
            {"pos": 4, "name": "El obstáculo principal", "desc": "El desafío concreto que debes sortear para triunfar."},
            {"pos": 5, "name": "Entorno y personas cercanas", "desc": "La influencia de familiares, amigos o colegas en el asunto."},
            {"pos": 6, "name": "Acción recomendada", "desc": "El mejor paso táctico que debes dar."},
            {"pos": 7, "name": "Desenlace final", "desc": "El resultado final definitivo y la lección integrada."}
        ],
        "layout": "horseshoe"
    },
    {
        "id": "siete-chakras",
        "name": "Alineación de los 7 Chakras",
        "card_count": 7,
        "difficulty": "Avanzado",
        "description": "Tirada energética que lee el estado de cada uno de los centros bioenergéticos del cuerpo, desde la raíz hasta la coronilla.",
        "when_to_use": "Durante limpiezas energéticas, momentos de transformación interior o para detectar bloqueos somáticos o psíquicos.",
        "positions": [
            {"pos": 1, "name": "Muladhara (Raíz)", "desc": "Supervivencia, seguridad material, estabilidad terrenal y arraigo."},
            {"pos": 2, "name": "Svadhisthana (Sacro)", "desc": "Sexualidad, creatividad, placer, emociones y fluidez vital."},
            {"pos": 3, "name": "Manipura (Plexo Solar)", "desc": "Poder personal, autoestima, fuerza de voluntad y digestión emocional."},
            {"pos": 4, "name": "Anahata (Corazón)", "desc": "Amor incondicional, compasión, perdón y apertura afectiva."},
            {"pos": 5, "name": "Vishuddha (Garganta)", "desc": "Comunicación, autenticidad, expresión de la verdad y creatividad verbal."},
            {"pos": 6, "name": "Ajna (Tercer Ojo)", "desc": "Intuición, discernimiento lúcido, visión interior e imaginación."},
            {"pos": 7, "name": "Sahasrara (Corona)", "desc": "Conexión espiritual superior, fe, trascendencia y propósito divino."}
        ],
        "layout": "vertical-line"
    },
    {
        "id": "cruz-celta",
        "name": "La Cruz Celta Completa (10 Cartas)",
        "card_count": 10,
        "difficulty": "Avanzado / Maestro",
        "description": "La tirada reina del Tarot por excelencia. Creada por Arthur Edward Waite, analiza un tema en todas sus dimensiones psicológicas, temporales y espirituales.",
        "when_to_use": "Para las consultas más cruciales de la vida: encrucijadas vitales, grandes transformaciones o lecturas maestras anuales.",
        "positions": [
            {"pos": 1, "name": "El Centro / La Situación presente", "desc": "El núcleo del asunto y la energía que rodea al consultante."},
            {"pos": 2, "name": "El Cruce / El Desafío inmediato", "desc": "La fuerza que cruza al consultante (puede ayudar o trabar el camino)."},
            {"pos": 3, "name": "La Base / Raíz del pasado", "desc": "El fundamento histórico y la causa profunda que sostiene la situación."},
            {"pos": 4, "name": "El Pasado reciente", "desc": "Acontecimientos inmediatos que acaban de ocurrir y aún tienen eco."},
            {"pos": 5, "name": "La Corona / Mejor potencial", "desc": "Lo más elevado a lo que puedes aspirar conscientemente en esta situación."},
            {"pos": 6, "name": "El Futuro inmediato", "desc": "Lo que ocurrirá en las próximas semanas o meses a corto plazo."},
            {"pos": 7, "name": "Tú mismo / Actitud psicológica", "desc": "Cómo te estás posicionando internamente ante el problema."},
            {"pos": 8, "name": "El Entorno / Influencias externas", "desc": "Cómo ven la situación los demás y qué energía te llega de fuera."},
            {"pos": 9, "name": "Esperanzas y Temores", "desc": "Tus deseos más íntimos mezclados con tus miedos inconscientes."},
            {"pos": 10, "name": "El Resultado final / Culminación", "desc": "La resolución acumulativa de todas las fuerzas en juego."}
        ],
        "layout": "celtic-cross"
    },
    {
        "id": "rueda-zodiacal",
        "name": "Rueda Astrológica / Las 12 Casas",
        "card_count": 12,
        "difficulty": "Maestro",
        "description": "Una carta por cada una de las doce casas de la carta natal. Un mapa panorámico completo para ver cómo se proyecta el año en todas las áreas de la vida.",
        "when_to_use": "Lecturas de Año Nuevo, cumpleaños o balances vitales para conocer el clima de salud, dinero, amor, hogar y carrera.",
        "positions": [
            {"pos": 1, "name": "Casa I: La Personalidad y el Yo", "desc": "Vitalidad, autoimagen, nuevos comienzos e identidad."},
            {"pos": 2, "name": "Casa II: Dinero y Recursos", "desc": "Ingresos propios, finanzas, autoestima y bienes materiales."},
            {"pos": 3, "name": "Casa III: Comunicación y Entorno", "desc": "Estudios, traslados cortos, hermanos y expresión verbal."},
            {"pos": 4, "name": "Casa IV: Hogar y Raíces", "desc": "Familia, vivienda, intimidad y seguridad emocional."},
            {"pos": 5, "name": "Casa V: Creatividad y Romance", "desc": "Hijos, placeres, proyectos artísticos y romances lúdicos."},
            {"pos": 6, "name": "Casa VI: Salud y Trabajo diario", "desc": "Rutinas laborales, hábitos de salud y servicio a otros."},
            {"pos": 7, "name": "Casa VII: Pareja y Asociaciones", "desc": "Matrimonio, contratos formales, socios y vínculos de tú a tú."},
            {"pos": 8, "name": "Casa VIII: Transformación y Finanzas compartidas", "desc": "Crisis regeneradoras, sexualidad profunda, herencias e impuestos."},
            {"pos": 9, "name": "Casa IX: Viajes largos y Filosofía", "desc": "Estudios superiores, expansión espiritual y horizontes lejanos."},
            {"pos": 10, "name": "Casa X: Carrera y Éxito social", "desc": "Vocación, reputación profesional, metas públicas y logros."},
            {"pos": 11, "name": "Casa XI: Amistades y Sueños", "desc": "Grupos sociales, redes, proyectos comunitarios e ideales futuros."},
            {"pos": 12, "name": "Casa XII: Inconsciente y Trascendencia", "desc": "Retiro espiritual, karma, sueños y lecciones del alma oculta."}
        ],
        "layout": "circle-12"
    },
    {
        "id": "proposito-vida",
        "name": "Propósito y Misión de Vida",
        "card_count": 5,
        "difficulty": "Avanzado",
        "description": "Tirada para conectar con el llamado esencial de tu alma: tus talentos innatos, el bloqueo kármico a superar y cómo servir al mundo.",
        "when_to_use": "Durante crisis vocacionales, despertares espirituales o cuando te preguntas qué viniste a aprender y aportar en esta vida.",
        "positions": [
            {"pos": 1, "name": "El Don del Alma", "desc": "Tu talento innato, la virtud que trajiste contigo para brillar."},
            {"pos": 2, "name": "El Bloqueo Kármico", "desc": "La lección o herida que debes sanar para desplegar tu potencial."},
            {"pos": 3, "name": "El Camino de Aprendizaje", "desc": "La disciplina o experiencia que te ayuda a madurar hoy."},
            {"pos": 4, "name": "Tu Servicio al Mundo", "desc": "Cómo puedes aportar valor y mejorar la vida de los demás."},
            {"pos": 5, "name": "La Culminación Espiritual", "desc": "La victoria del alma cuando te alineas con tu auténtica verdad."}
        ],
        "layout": "star-5"
    }
]

# 2. LIBRO DE COMBINACIONES
combinations_data = {
    "principles": {
        "elements": {
            "Fuego": {"suit": "Bastos", "quality": "Acción, pasión, entusiasmo", "allies": ["Aire"], "conflicts": ["Agua"]},
            "Agua": {"suit": "Copas", "quality": "Emoción, amor, intuición", "allies": ["Tierra"], "conflicts": ["Fuego"]},
            "Aire": {"suit": "Espadas", "quality": "Mente, verdad, discernimiento", "allies": ["Fuego"], "conflicts": ["Tierra"]},
            "Tierra": {"suit": "Oros", "quality": "Materia, dinero, solidez", "allies": ["Agua"], "conflicts": ["Aire"]}
        },
        "synthesis_rules": [
            "Arcano Mayor + Arcano Mayor: Anuncia un giro decisivo o lección kármica de gran escala.",
            "Arcano Mayor + Arcano Menor: El Arcano Mayor define el principio cósmico y el Menor la circunstancia práctica donde se manifiesta.",
            "Arcano Menor + Arcano Menor: Señala situaciones cotidianas, dinámicas humanas inmediatas y resoluciones a corto plazo.",
            "Dos cartas del mismo palo: Intensificación exponencial de esa energía (ej. dos Copas = gran desborde afectivo; dos Oros = consolidación financiera).",
            "Fuego + Agua (Bastos + Copas): Tensión de vapor; pasión efervescente que puede ser creativa o desgastante si no hay templanza.",
            "Aire + Fuego (Espadas + Bastos): Expansión veloz; las ideas del aire avivan las llamas de la acción. Éxito rápido.",
            "Tierra + Agua (Oros + Copas): Fecundidad pura; el agua nutre la tierra generando cosechas abundantes en amor y bienestar.",
            "Tierra + Aire (Oros + Espadas): Realismo analítico; planificación rigurosa que asegura la estabilidad pero puede carecer de calidez."
        ]
    },
    "iconic_pairs": [
        {
            "card_a": "el-loco", "card_b": "el-mago",
            "title": "El Salto Creador",
            "essence": "La chispa de la idea (Loco) encuentra instantáneamente las herramientas y la habilidad técnica para manifestarse (Mago).",
            "love": "Declaración audaz que inicia un romance apasionado y lleno de química mutua.",
            "work": "Lanzamiento impecable de un emprendimiento innovador; genialidad creadora puesta en acción.",
            "advice": "No te quedes solo en soñar; ponte a trabajar hoy mismo con tus herramientas disponibles."
        },
        {
            "card_a": "la-torre", "card_b": "la-estrella",
            "title": "De las Cenizas a la Gracia",
            "essence": "La caída súbita de una situación falsa (Torre) abre inmediatamente paso a una sanación milagrosa y esperanza renovada (Estrella).",
            "love": "Ruptura dolorosa de una farsa que te permite sanar el corazón y encontrar un amor verdadero y transparente.",
            "work": "Pérdida de un empleo insostenible que resulta ser la mejor bendición para encontrar tu verdadera vocación.",
            "advice": "No llores por las paredes derribadas; contempla el cielo estrellado que ahora tienes sobre ti."
        },
        {
            "card_a": "el-diablo", "card_b": "los-enamorados",
            "title": "La Tentación del Vínculo",
            "essence": "Pasión carnal irresistible mezclada con dinámicas de apego, celos o una elección moral decisiva entre el placer efímero y el amor verdadero.",
            "love": "Atracción magnética sexual muy intensa; peligro de manipulación o infidelidad si no hay madurez.",
            "work": "Oferta económica muy tentadora pero con cláusulas éticamente dudosas o leoninas.",
            "advice": "No vendas tu libertad por una noche de placer o una promesa dorada; elige desde tus valores del corazón."
        },
        {
            "card_a": "la-muerte", "card_b": "el-juicio",
            "title": "Resurrección y Nuevo Comienzo",
            "essence": "Cierre definitivo e irreversible del pasado (Muerte) seguido de una llamada divina a despertar y renacer a una nueva vida (Juicio).",
            "love": "Superación completa de un duelo amoroso; renacimiento del alma listo para un amor maduro.",
            "work": "Reinvención profesional radical; cambiar de carrera con éxito rotundo respondiendo a tu auténtica vocación.",
            "advice": "Deja morir lo viejo sin miedo; la trompeta de tu renacimiento ya está sonando."
        },
        {
            "card_a": "la-sacerdotisa", "card_b": "la-luna",
            "title": "El Océano del Subconsciente",
            "essence": "Intuición extrema, sueños clarividentes y misterios profundos que emergen a la superficie.",
            "love": "Conexión anímica telepática, pero cuidado con malentendidos alimentados por miedos imaginarios.",
            "work": "Investigación secreta brillante; descubrir lo que otros ocultan gracias a tu olfato.",
            "advice": "Confía en tus corazonadas pero no te dejes arrastrar por paranoias; enciende la luz de la verdad."
        },
        {
            "card_a": "el-sol", "card_b": "el-mundo",
            "title": "El Triunfo Absoluto",
            "essence": "La combinación más luminosa de todo el Tarot: éxito rotundo, alegría radiante, culminación perfecta y expansión total.",
            "love": "Amor pleno, matrimonio dichoso, viajes inolvidables juntos y celebración de la vida.",
            "work": "Consolidación de la cumbre profesional, reconocimiento internacional, premios y prosperidad.",
            "advice": "Celebra con humildad y gratitud; has alcanzado la maestría de este ciclo vital."
        },
        {
            "card_a": "la-emperatriz", "card_b": "el-emperador",
            "title": "La Alianza Sagrada",
            "essence": "La unión perfecta entre la creatividad fértil y nutricia (Emperatriz) y el orden, estructura y liderazgo pragmático (Emperador).",
            "love": "Pareja ideal y complementaria: amor, respeto, proyectos compartidos y estabilidad familiar sólida.",
            "work": "Creación y estructuración de una empresa próspera y duradera con cimientos inamovibles.",
            "advice": "Combina la ternura con la disciplina; nutre tus sueños y protégelos con reglas claras."
        },
        {
            "card_a": "el-ermitano", "card_b": "la-rueda-de-la-fortuna",
            "title": "El Ojo del Huracán",
            "essence": "En medio de los cambios drásticos e imprevistos del destino (Rueda), el sabio permanece inmóvil en su centro interior (Ermitaño).",
            "love": "Aceptar con madurez los cambios en la relación sin perder la propia paz personal.",
            "work": "Saber esperar el momento justo para actuar cuando los ciclos del mercado giren a tu favor.",
            "advice": "No intentes frenar la rueda del destino; quédate en tu centro y observa la lección con sabiduría."
        },
        {
            "card_a": "la-fuerza", "card_b": "el-carro",
            "title": "El Avance Imparable",
            "essence": "La fuerza de voluntad y determinación exterior (Carro) aliada con la paciencia y el autodominio interior (Fuerza). Victoria garantizada.",
            "love": "Superar juntos cualquier obstáculo familiar o externo gracias al amor firme y la lealtad.",
            "work": "Conquista de metas muy ambiciosas mediante liderazgo ético y constancia a prueba de balas.",
            "advice": "Avanza sin miedo; tienes tanto el coraje para actuar como la templanza para no equivocarte."
        },
        {
            "card_a": "la-justicia", "card_b": "el-juicio",
            "title": "La Sentencia Cósmica",
            "essence": "Alineación de la ley terrenal con la justicia divina. Cuentas claras, redención y veredicto favorable tras largas pruebas.",
            "love": "Resolución madura y justa de acuerdos prenupciales, divorcios o reconciliaciones transparentes.",
            "work": "Resolución definitiva y victoriosa de litigios, auditorías limpias y ascensos por méritos propios.",
            "advice": "Sé impecable con la verdad; el universo te recompensará con creces por tu integridad."
        }
    ]
}

# 3. GUIA PRACTICA DE CARTAS INVERTIDAS
reversed_guide = {
    "methods": [
        {
            "name": "1. Energía Bloqueada o Retrasada",
            "desc": "El significado luminoso de la carta está presente pero encuentra un tapón temporal o retraso en manifestarse en la materia. Ej: As de Oros invertido indica que el dinero llegará pero con demora."
        },
        {
            "name": "2. Proceso de Interiorización Psicológica",
            "desc": "La energía de la carta no se expresa hacia afuera sino que se está viviendo de manera interna y profunda. Ej: El Loco invertido puede ser una revolución mental íntima que aún no se muestra socialmente."
        },
        {
            "name": "3. Polaridad Sombra (Exceso o Carencia)",
            "desc": "La carta advierte de un desequilibrio por pasarse de la raya o por quedarse corto en el arquetipo. Ej: El Emperador invertido puede ser tiranía (exceso de autoridad) o cobardía e indisciplina (carencia de autoridad)."
        },
        {
            "name": "4. Señal de Redirección o Alerta Cósmica",
            "desc": "Una señal del universo que te pide detenerte, observar el mapa y cambiar de ruta antes de tropezar con una piedra evitable."
        }
    ]
}

# 4. APP DE PRACTICA (PREGUNTAS DE QUIZ Y FLASHCARDS)
quiz_questions = [
    {
        "id": 1,
        "question": "¿Qué Arcano Mayor lleva el número 0 y representa el inicio del viaje del alma y el salto de fe?",
        "options": ["El Loco", "El Mago", "El Colgado", "La Rueda de la Fortuna"],
        "correct": 0,
        "explanation": "El Loco es el arcano 0, simboliza el punto cero, la inocencia y el coraje para lanzarse a lo desconocido."
    },
    {
        "id": 2,
        "question": "¿Qué elemento y palo del Tarot están asociados a la mente, la verdad, el discernimiento y los dilemas?",
        "options": ["Copas (Agua)", "Espadas (Aire)", "Bastos (Fuego)", "Oros (Tierra)"],
        "correct": 1,
        "explanation": "Las Espadas corresponden al elemento Aire, que rige el pensamiento racional, la palabra y la verdad."
    },
    {
        "id": 3,
        "question": "¿Qué representa la Lemniscata (símbolo de infinito) sobre la cabeza de El Mago y La Fuerza?",
        "options": ["Riqueza material infinita", "Conexión constante con la sabiduría cósmica y potencial ilimitado", "Tiempo perdido", "Inmortalidad del cuerpo físico"],
        "correct": 1,
        "explanation": "La Lemniscata simboliza la conexión directa de la mente con el infinito y el dominio armónico de la energía."
    },
    {
        "id": 4,
        "question": "¿Cuál es la carta que marca una ruptura súbita de ilusiones falsas mediante un rayo de verdad liberador?",
        "options": ["La Muerte", "El Diablo", "La Torre", "El Juicio"],
        "correct": 2,
        "explanation": "La Torre representa la demolición necesaria de lo falso para poder edificar sobre la verdad."
    },
    {
        "id": 5,
        "question": "En el Tarot Rider-Waite, ¿qué detalle clave tienen las cadenas del hombre y la mujer en El Diablo?",
        "options": ["Están con candado indestructible", "Están flojas alrededor del cuello, pudiendo quitárselas cuando despierten", "Están atadas a una gran roca", "No tienen cadenas"],
        "correct": 1,
        "explanation": "Las cadenas están flojas, revelando que los apegos y adicciones son trampas voluntarias del ego que podemos soltar."
    },
    {
        "id": 6,
        "question": "¿Qué Arcano Menor muestra a un hombre haciendo malabares con dos pentáculos rodeados por una cinta de infinito?",
        "options": ["Dos de Oros", "Dos de Bastos", "Dos de Copas", "Dos de Espadas"],
        "correct": 0,
        "explanation": "El Dos de Oros representa la flexibilidad, el equilibrio dinámico y la capacidad de adaptarse a múltiples tareas."
    },
    {
        "id": 7,
        "question": "¿Qué mensaje esencial transmite la carta de La Muerte (Arcano XIII)?",
        "options": ["Muerte física inminente", "Fin definitivo de un ciclo viejo para que nazca lo nuevo", "Una maldición", "Estancamiento eterno"],
        "correct": 1,
        "explanation": "La Muerte nunca significa muerte física en el tarot, sino profunda transformación y cierre de ciclo."
    },
    {
        "id": 8,
        "question": "¿Qué carta representa a una mujer con los ojos vendados rodeada de espadas clavadas en el fango pero con salida libre?",
        "options": ["Dos de Espadas", "Ocho de Espadas", "Nueve de Espadas", "La Sacerdotisa"],
        "correct": 1,
        "explanation": "El Ocho de Espadas es la prisión mental autoimpuesta: la cárcel está en tus pensamientos, la salida está libre."
    },
    {
        "id": 9,
        "question": "¿Cuál de las siguientes cartas es conocida tradicionalmente como 'la carta de los deseos cumplidos'?",
        "options": ["Nueve de Copas", "Nueve de Bastos", "Nueve de Oros", "Nueve de Espadas"],
        "correct": 0,
        "explanation": "El Nueve de Copas refleja profunda satisfacción emocional, deseos alcanzados y disfrute dichoso."
    },
    {
        "id": 10,
        "question": "¿Qué Arcano Mayor culmina con honores el viaje del Loco mostrando una danzante en una corona triunfal?",
        "options": ["El Sol", "El Juicio", "El Mundo", "La Rueda de la Fortuna"],
        "correct": 2,
        "explanation": "El Mundo (XXI) representa la culminación perfecta, integración de opuestos y el cierre victorioso del viaje."
    }
]

# Write everything to combined tarot_database.json and tarot_database.js
database = {
    "cards": cards_list,
    "spreads": spreads_data,
    "combinations": combinations_data,
    "reversed_guide": reversed_guide,
    "quiz": quiz_questions,
    "meta": {
        "version": "1.0.0",
        "total_cards": len(cards_list),
        "total_spreads": len(spreads_data),
        "created_for": "Plataforma Personal 78 Mapas Mentales del Tarot",
        "license": "Uso personal exclusivo"
    }
}

with open("data/tarot_database.json", "w", encoding="utf-8") as f:
    json.dump(database, f, ensure_ascii=False, indent=2)

with open("data/tarot_database.js", "w", encoding="utf-8") as f:
    f.write("const TAROT_DB = ")
    json.dump(database, f, ensure_ascii=False, indent=2)
    f.write(";\n\nif (typeof module !== 'undefined') { module.exports = TAROT_DB; }\n")

print("Complete database saved to data/tarot_database.json and data/tarot_database.js!")
print(f"Cards: {len(database['cards'])}, Spreads: {len(database['spreads'])}, Quiz: {len(database['quiz'])}")
