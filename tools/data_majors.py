# -*- coding: utf-8 -*-
"""
Datos maestros para los 22 Arcanos Mayores del Tarot (0 a 10)
"""

import os

def load_user_el_loco():
    curiosidades_path = os.path.join('Investigaci\u00f2n', 'Arcanos mayores', 'EL LOCO', 'Curiosidades.txt')
    historia_path = os.path.join('Investigaci\u00f2n', 'Arcanos mayores', 'EL LOCO', 'Historia.txt')
    
    curiosidades = []
    if os.path.exists(curiosidades_path):
        with open(curiosidades_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line.startswith('•') or line.startswith('-'):
                    curiosidades.append(line.lstrip('•- ').strip())
                elif line:
                    curiosidades.append(line)
    
    titulo_historia = "El Reino de las Paredes de Cristal"
    relato_historia = ""
    if os.path.exists(historia_path):
        with open(historia_path, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            lines = content.split('\n')
            first_line = lines[0].strip()
            if 'Una Historia Inspirada' in first_line:
                if ':' in first_line:
                    titulo_historia = first_line.split(':', 1)[1].strip()
                relato_historia = '\n'.join(lines[1:]).strip()
            else:
                relato_historia = content

    return curiosidades, titulo_historia, relato_historia

user_curiosidades, user_titulo, user_relato = load_user_el_loco()

MAJORS_DATA_1 = [
    # 0. EL LOCO
    {
        "id": "el-loco",
        "number": 0,
        "roman": "0",
        "name": "El Loco",
        "folder": "arcanos_mayores",
        "filename": "00_el_loco.xml",
        "element": "Aire",
        "astrology": "Urano",
        "historia": (
            "En las barajas renacentistas más antiguas, como el Tarot Visconti-Sforza del siglo XV, "
            "El Loco (Il Matto) era representado como un mendigo andrajoso o un vagabundo con plumas en el pelo, "
            "una figura marginal de la sociedad medieval. En el Tarot de Marsella evolucionó hacia el bufón sagrado, "
            "aquel que tiene permiso para decir las verdades más crudas ante el rey sin perder la cabeza. "
            "A principios del siglo XX, Arthur Edward Waite y Pamela Colman Smith revolucionaron su iconografía: "
            "dejó de ser un desterrado para transformarse en un joven solar, místico y radiante, que camina con paso ligero "
            "hacia el precipicio cargando solo un fardo diminuto y una rosa blanca, encarnando el salto de fe espiritual."
        ),
        "significado_fundamental": (
            "El Loco representa el potencial puro en estado virgen, la energía primigenia antes de cualquier limitación, "
            "definición o forma. Es el espíritu libre que confía ciegamente en el flujo universal. Simboliza el inicio sagrado "
            "de cualquier viaje vital, la inocencia que no teme equivocarse y el coraje espontáneo de quien sabe que para "
            "crear algo nuevo es imprescindible soltar todo equipaje del pasado."
        ),
        "posicion_normal": {
            "resumen": "Comienzo espontáneo, valentía inocente, libertad sin ataduras y fe ciega en el porvenir.",
            "amor": "Aparición de un nuevo romance inesperado e ilusionante. Relaciones libres de prejuicios, basadas en la diversión y la autenticidad sin ataduras rígidas ni miedos al pasado.",
            "dinero_trabajo": "Emprender una nueva vocación o proyecto innovador. Disposición a asumir riesgos calculados. Salir de la zona de confort profesional con optimismo y frescura creativa.",
            "salud": "Vitalidad desbordante, ligereza corporal y entusiasmo rejuvenecido. Es recomendable cuidar la distracción física para evitar torceduras o pequeños descuidos por imprudencia.",
            "espiritualidad": "Mente de principiante, conexión directa con la intuición y el alma. Se despierta la capacidad de maravillarse ante la existencia y soltar dogmas asfixiantes."
        },
        "posicion_invertida": {
            "resumen": "Imprudencia desmedida, caos, irresponsabilidad o, en el polo opuesto, parálisis por miedo al qué dirán.",
            "amor": "Inmadurez emocional, promesas vacías, miedo irracional al compromiso o huidas impulsivas cuando la relación exige madurez y responsabilidad afectiva.",
            "dinero_trabajo": "Riesgos ciegos e insensatos. Firmar acuerdos sin leer la letra pequeña, gastos descontrolados o proyectos utópicos que carecen de bases sólidas.",
            "salud": "Agotamiento físico por excesos o desórdenes de horario. Negligencia ante síntomas médicos y tendencia a conductas temerarias.",
            "espiritualidad": "Sensación de pérdida de rumbo existencial. Caer en la ingenuidad espiritual, seguir gurús sin discernimiento o desconectarse de la realidad cotidiana."
        },
        "lo_que_lo_hace_unico": (
            "Es el único arcano de toda la baraja que posee el número Cero (0). Al no tener una posición fija en la secuencia "
            "numérica, puede colocarse tanto al inicio absoluto como al final supremo de los Arcanos Mayores. "
            "A diferencia de El Mago (que necesita concentrar su voluntad con herramientas sobre la mesa) o El Juicio (que evalúa minuciosamente el pasado), "
            "El Loco camina sin ataduras ni posesiones, personificando el puente infinito entre la nada y el todo."
        ),
        "curiosidades": user_curiosidades if user_curiosidades else [
            "El Joker de la baraja común: El Loco sobrevivió a la evolución de las cartas de juego tradicionales transformándose en el Comodín (Joker). Al igual que en el Tarot, el Joker no tiene un valor fijo; puede ser cualquier carta, rompe las reglas del juego y aporta el elemento de la imprevisibilidad.",
            "El viaje del Loco: En el estudio del Tarot, se considera que los otros 21 Arcanos Mayores son personas, lecciones y obstáculos que El Loco se encuentra en su camino. El Tarot entero es la historia de cómo El Loco evoluciona hasta convertirse en El Mundo (XXI).",
            "La rosa blanca y el perrillo: La rosa blanca en su mano izquierda representa los deseos purificados y la inocencia prístina, mientras que el perro que salta a su lado simboliza el instinto animal integrado que advierte del abismo sin frenar su avance espiritual."
        ],
        "historia_inspirada": {
            "titulo": user_titulo if user_titulo else "El Reino de las Paredes de Cristal",
            "relato": user_relato if user_relato else (
                "En el Reino de la Constancia, todo estaba perfectamente medido. Las calles eran líneas rectas imperecederas, "
                "los ciudadanos despertaban a la misma hora y cada destino estaba escrito en pesados libros de mármol..."
            )
        },
        "audio": {
            "archivo": "assets/audio/el-loco.mp3",
            "titulo": "El Loco - El Salto al Vacío Sagrado",
            "duracion_estimada": "4:30 min"
        }
    },

    # 1. EL MAGO
    {
        "id": "el-mago",
        "number": 1,
        "roman": "I",
        "name": "El Mago",
        "folder": "arcanos_mayores",
        "filename": "01_el_mago.xml",
        "element": "Aire / Mercurio",
        "astrology": "Mercurio",
        "historia": (
            "En las barajas del siglo XV (Tarocchi di Mantegna y Visconti-Sforza), El Mago era 'Il Bagatto', un feriante o titiritero "
            "callejero que entretenía al público con trucos de prestidigitación. Con el ocultismo del siglo XVIII (Court de Gébelin y Éliphas Lévi), "
            "la figura se transformó en el Hermes Trismegisto del hermetismo. En la versión Rider-Waite-Smith, Pamela Colman Smith lo corona con "
            "el símbolo del infinito (lemniscata) y coloca sobre su mesa los cuatro símbolos de los palos (vara, copa, espada y pentáculo), "
            "haciéndolo el maestro de los cuatro elementos alquímicos y el puente consciente entre el cielo y la tierra."
        ),
        "significado_fundamental": (
            "El Mago es el arquetipo de la voluntad activa, la manifestación consciente y el poder creador. Si El Loco es la energía "
            "potencial no dirigida, El Mago es el rayo enfocado en un objetivo claro. Representa el axioma hermético 'Como es arriba, es abajo': "
            "su brazo derecho apunta al cosmos y el izquierdo a la tierra, canalizando la energía divina para materializar realidades concretas en el plano físico."
        ),
        "posicion_normal": {
            "resumen": "Poder de manifestación, maestría de recursos, elocuencia, claridad mental e iniciativa arrolladora.",
            "amor": "Atracción magnética, conquista comunicativa y chispa seductora. Se inicia una etapa donde ambas partes tienen el poder de moldear la relación hacia un nuevo nivel de entendimiento y pasión.",
            "dinero_trabajo": "Capacidad resolutiva para convertir ideas en negocios rentables. Momento óptimo para lanzar proyectos, liderar equipos o negociar contratos ventajosos con astucia e inteligencia.",
            "salud": "Fuerza vital enérgica, excelente coordinación y mente ágil. Recuperación rápida de molestias físicas gracias a una actitud proactiva y hábitos equilibrados.",
            "espiritualidad": "Consciencia de ser cocreador de la propia realidad. Conexión de la intención interna con la acción externa a través del alineamiento de pensamientos y palabras."
        },
        "posicion_invertida": {
            "resumen": "Manipulación, engaño, uso egoísta de talentos, dispersión o bloqueo de la propia capacidad creadora.",
            "amor": "Juegos psicológicos, falsas promesas o encanto superficial que oculta intenciones egocéntricas. Inseguridad encubierta con arrogancia.",
            "dinero_trabajo": "Proyectos que se quedan en palabras y nunca se ejecutan. Riesgo de estafas, charlatanería o venta de humo. Falta de ética en negociaciones.",
            "salud": "Agotamiento mental por sobrepensar. Dolores de cabeza, tensión nerviosa o mal uso de la energía física por dispersión constante.",
            "espiritualidad": "Ego espiritual desmedido. Creerse superior a los demás por conocimientos esotéricos o utilizar la energía para someter voluntades ajenas."
        },
        "lo_que_lo_hace_unico": (
            "Es el único arcano mayor que posee sobre su mesa de trabajo las cuatro herramientas sagradas del Tarot "
            "(la Vara del Fuego, la Copa del Agua, la Espada del Aire y el Oromiel de la Tierra) listas para ser usadas. "
            "A diferencia de La Sacerdotisa (que custodia el misterio en silencio e introspección), El Mago actúa en el mundo exterior, "
            "demostrando que todo lo que necesitamos para triunfar ya está a nuestro alcance."
        ),
        "curiosidades": [
            "La lemniscata infinita: La figura en ocho sobre su cabeza representa la eternidad del pensamiento y el flujo continuo de la consciencia divina.",
            "El cinturón de ouroboros: La serpiente que se muerde la cola en su cintura simboliza la autorrenovación infinita y la protección hermética de su energía vital.",
            "Las flores rojas y blancas: Las rosas rojas a sus pies encarnan el deseo y la pasión humana, mientras los lirios blancos representan el pensamiento puro y la sabiduría."
        ],
        "historia_inspirada": {
            "titulo": "El Aprendiz de las Cuatro Aguas",
            "relato": (
                "En el taller del Valle de Hermes, el maestro no enseñaba con palabras, sino señalando la mesa de piedra vacía. "
                "'El mundo no te dará nada que no te atrevas a nombrar', le dijo al joven artesano. El muchacho tomó una rama de roble "
                "y sintió el fuego de su vocación; tomó una vasija de barro y sintió el torrente de sus emociones; forjó una hoja de plata "
                "y afiló su razón; y recogió un puñado de tierra fértil para sembrar su sustento. Cuando alzó su diestra hacia la estrella del alba "
                "y posó la izquierda sobre la arcilla húmeda, la mesa se iluminó: había comprendido que los milagros no caen del cielo, "
                "sino que se tejen con las manos de quien sabe unir su voluntad al universo."
            )
        },
        "audio": {
            "archivo": "assets/audio/el-mago.mp3",
            "titulo": "El Mago - La Alquimia de la Voluntad",
            "duracion_estimada": "4:15 min"
        }
    },

    # 2. LA SACERDOTISA
    {
        "id": "la-sacerdotisa",
        "number": 2,
        "roman": "II",
        "name": "La Sacerdotisa",
        "folder": "arcanos_mayores",
        "filename": "02_la_sacerdotisa.xml",
        "element": "Agua / Luna",
        "astrology": "La Luna",
        "historia": (
            "Originalmente denominada 'La Papisa' (La Papessa) en las cortes italianas del siglo XV, la carta evocaba la legendaria figura "
            "medieval de la Papisa Juana, una mujer que según el mito popular gobernó la Iglesia vestida de varón. En el siglo XIX, Antoine Court "
            "de Gébelin la asoció con la diosa egipcia Isis, velada ante los no iniciados. Pamela Colman Smith la situó entre las dos columnas del Templo "
            "de Salomón —Boaz (oscura) y Jachin (clara)—, vistiendo un manto azul que fluye como agua viva y sosteniendo en su regazo el pergamino de la Tora, "
            "fijándola como la guardiana absoluta de los misterios esotéricos y la intuición inconsciente."
        ),
        "significado_fundamental": (
            "La Sacerdotisa es el arquetipo de la sabiduría interior, el silencio sagrado, la intuición clarividente y el conocimiento de los planos sutiles. "
            "Representa la noche fértil del alma, el útero psíquico donde germinan las verdades antes de salir a la luz. Enseña que no todas las respuestas "
            "se hallan en el análisis lógico externo; hay misterios que solo se revelan cuando se aquieta el ego y se escucha la voz interior."
        ),
        "posicion_normal": {
            "resumen": "Intuición profunda, serenidad, reserva sabia, secretos revelados y conexión con el subconsciente.",
            "amor": "Conexión de almas sutil y telepática. Intimidad espiritual basada en el entendimiento sin necesidad de muchas palabras. Posible atracción por alguien enigmático o necesidad de introspección antes de comprometerse.",
            "dinero_trabajo": "Actuar con prudencia y confidencialidad. Excelente momento para el estudio, la investigación profunda o la consultoría. Confía en tus corazonadas antes de firmar acuerdos.",
            "salud": "Equilibrio hormonal, ciclos biológicos y serenidad del sistema nervioso. Se recomienda prestar atención a los sueños y practicar meditación o técnicas de respiración consciente.",
            "espiritualidad": "Despertar del tercer ojo y dones intuitivos. Capacidad para leer entre líneas en el libro de la vida y acceder a la memoria de los registros del alma."
        },
        "posicion_invertida": {
            "resumen": "Secretismo tóxico, frialdad emocional, intuición bloqueada, chismes o desconexión del cuerpo.",
            "amor": "Desconfianza, barreras defensivas infranqueables o secretos no confesados que distancian a la pareja. Sentimiento de aislamiento e incomprensión.",
            "dinero_trabajo": "Información oculta deliberadamente, falta de transparencia en el entorno laboral o tomar decisiones basadas en ilusiones sin contrastar datos reales.",
            "salud": "Alteraciones en los ciclos del sueño, desequilibrios del sistema reproductor femenino o somatización de emociones reprimidas por guardar silencio durante demasiado tiempo.",
            "espiritualidad": "Superstición, miedo a los propios dones psíquicos o desconexión del plano espiritual debido a un escepticismo árido y defensivo."
        },
        "lo_que_lo_hace_unico": (
            "Es la única carta que custodia el umbral entre las dos columnas del templo primordial (la dualidad de la luz y la oscuridad, "
            "lo visible y lo invisible). A diferencia de El Hierofante (que enseña dogmas religiosos y doctrinas públicas para las masas), "
            "La Sacerdotisa guarda el secreto místico interior: no habla con discursos, sino a través de revelaciones oníricas y silencios sagrados."
        ),
        "curiosidades": [
            "El velo de granadas: El velo bordado con granadas a sus espaldas alude al mito de Perséfone en el Inframundo y a la fertilidad oculta del inconsciente.",
            "La luna creciente a sus pies: Simboliza su dominio absoluto sobre las mareas emocionales y la capacidad de iluminar la oscuridad psíquica.",
            "El rollo de la TORA: La palabra 'TORA' (parcialmente cubierta por su manto) contiene un juego de letras que forma anagramas sagrados: TARO (Tarot), ROTA (Rueda) y ORAT (Rezar)."
        ],
        "historia_inspirada": {
            "titulo": "La Guardiana del Velo Azul",
            "relato": (
                "En la biblioteca más antigua del desierto, los sabios discutían a gritos sobre el origen del universo. "
                "Solo una mujer permanecía sentada en el pórtico, mirando el pozo de agua profunda. Un joven se le acercó y le preguntó: "
                "—¿Por qué no participas en el debate? ¿Acaso no sabes la verdad? "
                "La mujer sonrió en silencio, tomó una hoja seca y la dejó caer sobre la superficie del agua. Las ondas se abrieron "
                "mostrando el reflejo exacto de las estrellas de medianoche. "
                "—Quien grita la verdad solo convence a su propio orgullo —susurró ella con voz de manantial—. Quien escucha en silencio, "
                "se convierte en el espejo del infinito."
            )
        },
        "audio": {
            "archivo": "assets/audio/la-sacerdotisa.mp3",
            "titulo": "La Sacerdotisa - Los Secretos del Agua Silenciosa",
            "duracion_estimada": "4:40 min"
        }
    },

    # 3. LA EMPERATRIZ
    {
        "id": "la-emperatriz",
        "number": 3,
        "roman": "III",
        "name": "La Emperatriz",
        "folder": "arcanos_mayores",
        "filename": "03_la_emperatriz.xml",
        "element": "Tierra / Venus",
        "astrology": "Venus",
        "historia": (
            "Históricamente vinculada a las emperatrices del Sacro Imperio Romano Germánico, en los tarots del Renacimiento se mostraba "
            "como una soberana temporal con escudo imperial de águila bicéfala. En la tradición esotérica moderna evolucionó hacia la Gran Madre, "
            "la diosa Gaia, Deméter y Afrodita. Pamela Colman Smith la retrata en un trigal dorado en plena cosecha, recostada entre cojines aterciopelados, "
            "con un vestido estampado de granadas (símbolo de fertilidad) y una corona de doce estrellas, personificando la abundancia sensorial y la fuerza nutricia de la naturaleza."
        ),
        "significado_fundamental": (
            "La Emperatriz es la encarnación suprema de la fertilidad, la creación artística, la belleza sensorial y la nutrición incondicional. "
            "Es la fuerza que hace brotar las flores, fecundar las ideas y alimentar a los seres vivos. Nos enseña a conectar con el placer de estar vivos, "
            "a amar nuestro cuerpo físico y a confiar en que el universo es inherentemente abundante para quienes cultivan con paciencia y amor."
        ),
        "posicion_normal": {
            "resumen": "Abundancia material, fertilidad creadora, amor maternal, sensualidad y florecimiento de proyectos.",
            "amor": "Romance colmado de pasión, dulzura, ternura y placer físico. Fecundidad, armonía doméstica, consolidación de la pareja y posible gestación o nacimiento.",
            "dinero_trabajo": "Crecimiento próspero en negocios y carreras profesionales. Proyectos creativos que maduran con éxito. Prosperidad económica y entorno laboral cálido y colaborativo.",
            "salud": "Vitalidad radiante, fertilidad biológica óptima, equilibrio hormonal y conexión plena con el bienestar físico y los cinco sentidos.",
            "espiritualidad": "Veneración de la naturaleza como templo sagrado. Consciencia de que el cuerpo es el vehículo divino del alma y de que la creación es un acto de amor cósmico."
        },
        "posicion_invertida": {
            "resumen": "Bloqueo creativo, codependencia asfixiante, descuido personal, esterilidad de ideas o vanidad superficial.",
            "amor": "Apego excesivo, manipulación maternal o abandono del autocuidado por complacer a otros. Discusiones domésticas o frialdad sensorial.",
            "dinero_trabajo": "Gastos suntuosos innecesarios, pereza laboral o proyectos que se quedan estancados por falta de disciplina o exceso de comodismo.",
            "salud": "Problemas ginecológicos, fatiga crónica, desórdenes alimenticios o descuido de la nutrición y el descanso corporal.",
            "espiritualidad": "Desconexión con la tierra y el propio cuerpo. Sentimiento de escasez y desconsuelo existencial por perder la fe en los ciclos naturales."
        },
        "lo_que_lo_hace_unico": (
            "Es la única soberana que gobierna desde un jardín vivo al aire libre y no encerrada en un palacio de piedra. "
            "A diferencia de La Sacerdotisa (que nutre el espíritu virgen e intangible), La Emperatriz materializa la carne, el trigo, el vino y los sentidos. "
            "Y a diferencia de El Emperador (que impone el orden mediante leyes y ejércitos), ella reina a través del florecimiento espontáneo y el cuidado maternal."
        ),
        "curiosidades": [
            "La corona de doce estrellas: Representa las doce constelaciones zodiacales y los doce meses del año, coronándola como reina del tiempo y de las estaciones terrestres.",
            "El símbolo de Venus en el cojín: El corazón con el glifo venusino confirma su correspondencia astrológica con el amor, el arte, la armonía y la belleza estética.",
            "El río y la cascada: El agua que riega el campo simboliza las emociones puras que fertilizan el intelecto y dan vida a la materia."
        ],
        "historia_inspirada": {
            "titulo": "La Canción del Trigal Dorado",
            "relato": (
                "Hubo un invierno tan largo que la gente de la comarca olvidó el color verde. Los hombres intentaban tallar espigas de piedra "
                "y las mujeres lloraban mirando la tierra helada. Entonces, llegó una mujer descalza cuyo manto arrastraba aroma a madreselva. "
                "No dio discursos ni promulgó edictos; simplemente se arrodilló, besó la tierra escarchada y cantó una antigua melodía de cuna. "
                "Bajo el calor de su voz, la nieve se derritió en riachuelos de cristal y los primeros brotes de trigo estallaron hacia el cielo. "
                "—Nada que sea forzado da fruto perdurable —dijo acariciando una espiga—. La vida solo florece cuando es amada con paciencia infinita."
            )
        },
        "audio": {
            "archivo": "assets/audio/la-emperatriz.mp3",
            "titulo": "La Emperatriz - El Huerto Sagrado de la Vida",
            "duracion_estimada": "4:20 min"
        }
    },

    # 4. EL EMPERADOR
    {
        "id": "el-emperador",
        "number": 4,
        "roman": "IV",
        "name": "El Emperador",
        "folder": "arcanos_mayores",
        "filename": "04_el_emperador.xml",
        "element": "Fuego / Aries",
        "astrology": "Aries",
        "historia": (
            "Heredero directo de los césares romanos y los reyes francos medievales, El Emperador representaba en el Tarot del Renacimiento "
            "la soberanía terrenal, la corona y la ley feudal. En el Tarot de Marsella viste armadura y porta el cetro imperial. Arthur Edward Waite "
            "y Pamela Colman Smith le confirieron una presencia pétrea y adusta: sentado en un trono macizo de granito rojo adornado con cuatro cabezas "
            "de carnero (símbolo de Aries), vestido con cota de malla y sosteniendo el cetro de la cruz ansada (Ankh egipcia) y el orbe del mundo, "
            "representando el poder de la estructura, la ley y la conquista civilizatoria."
        ),
        "significado_fundamental": (
            "El Emperador encarna el principio paterno, la autoridad legítima, la estructura sólida, la disciplina y el orden protector. "
            "Si La Emperatriz es la fuerza orgánica y fértil de la naturaleza, El Emperador es el arquitecto que canaliza esa fuerza mediante límites saludables, "
            "construyendo ciudades, leyes e imperios donde la vida puede desarrollarse con seguridad. Enseña a liderar la propia vida con firmeza moral y constancia."
        ),
        "posicion_normal": {
            "resumen": "Liderazgo firme, estabilidad económica, disciplina constructiva, protección y capacidad ejecutiva.",
            "amor": "Relación madura, comprometida y con bases sólidas a largo plazo. Sentimiento de protección, lealtad y proyectos familiares estables.",
            "dinero_trabajo": "Posición de mando, ascensos por mérito propio y consolidación de empresas o patrimonios. Dominio de la estrategia financiera y orden presupuestario impecable.",
            "salud": "Constitución física resistente, buena disciplina con el ejercicio y hábitos regulares. Fortaleza ósea y vigor muscular.",
            "espiritualidad": "Dominio del propio carácter y templanza ante las tentaciones. Comprender que la disciplina espiritual es el andamio necesario para edificar la iluminación interior."
        },
        "posicion_invertida": {
            "resumen": "Tiranía, terquedad rígida, autoritarismo, abuso de poder o, por el contrario, cobardía e inmadurez ejecutiva.",
            "amor": "Control posesivo, celos, frialdad emocional o imposición machista de reglas que asfixian la libertad de la pareja.",
            "dinero_trabajo": "Conflictos con jefes o figuras de autoridad. Bancarrota por mala gestión o rigidez mental que impide adaptarse a los cambios del mercado.",
            "salud": "Hipertensión, cefaleas intensas, contracturas crónicas en el cuello o accidentes por exceso de tensión y orgullo obstinado.",
            "espiritualidad": "Dogmatismo dogmático, rigidez moral hipócrita o incapacidad para aceptar que existen misterios que escapan a la razón y al control humano."
        },
        "lo_que_lo_hace_unico": (
            "Es el único soberano del mazo sentado sobre un trono de roca sólida tallada con cabezas de carnero, con una montaña árida a sus espaldas "
            "que demuestra que su poder se ha forjado en la adversidad más dura. A diferencia de El Rey de Oros (que busca ante todo el bienestar material y el lujo), "
            "El Emperador es un guerrero civilizador que antepone el deber, la justicia y la defensa de su territorio por encima de cualquier comodidad personal."
        ),
        "curiosidades": [
            "El cetro Ankh: En su mano derecha sostiene la cruz ansada egipcia, revelando que su autoridad sobre la materia está consagrada a la preservación de la vida inmortal.",
            "La armadura bajo la túnica roja: Demuestra que, aunque esté sentado en paz, el verdadero líder nunca baja la guardia y siempre está preparado para proteger a su pueblo.",
            "Las cuatro cabezas de carnero: Hacen referencia al signo de Aries, el primer signo del zodiaco, regido por Marte, principio del fuego creador y la iniciativa incansable."
        ],
        "historia_inspirada": {
            "titulo": "La Muralla de Piedra Viva",
            "relato": (
                "Cuando las hordas del caos amenazaron el valle fértil, todos buscaron al hombre de la montaña. Lo encontraron tallando "
                "bloques de granito con sus propias manos heridas. '¿Por qué no usas la magia para salvarnos?', le gritaron desesperados. "
                "El hombre no soltó el cincel. Miró a los aldeanos a los ojos y dijo con voz de trueno contenido: 'La magia sin cimientos es "
                "un sueño que el primer viento derriba. Si queréis un reino que dure mil años, dejad de pedir milagros y aprended a colocar "
                "la primera piedra con vuestra propia sangre'. Aquel día, los aldeanos aprendieron la disciplina; y el valle nunca fue conquistado."
            )
        },
        "audio": {
            "archivo": "assets/audio/el-emperador.mp3",
            "titulo": "El Emperador - El Trono de la Firmeza",
            "duracion_estimada": "4:25 min"
        }
    },

    # 5. EL HIEROFANTE
    {
        "id": "el-hierofante",
        "number": 5,
        "roman": "V",
        "name": "El Hierofante",
        "folder": "arcanos_mayores",
        "filename": "05_el_hierofante.xml",
        "element": "Tierra / Tauro",
        "astrology": "Tauro",
        "historia": (
            "Conocido originalmente como 'El Papa' en el Tarot de Marsella, representaba la máxima autoridad eclesiástica de la cristiandad medieval. "
            "Arthur Edward Waite cambió su nombre por 'El Hierofante' (el intérprete de los misterios sagrados en los ritos griegos de Eleusis), "
            "despojándolo del dogma católico exclusivo para elevarlo a custodio universal de la tradición iniciática. Aparece sentado entre dos pilares, "
            "portando la tiara papal de tres coronas y la cruz de tres brazos, bendiciendo a dos sacerdotes arrodillados sobre un tablero de llaves cruzadas."
        ),
        "significado_fundamental": (
            "El Hierofante es el puente entre lo divino y lo humano, el maestro espiritual, la sabiduría ancestral transmitida por linajes y el compromiso con valores éticos elevados. "
            "Representa la educación, las instituciones respetables, el consejo sabio de mentores y la necesidad de pertenecer a una comunidad con principios compartidos."
        ),
        "posicion_normal": {
            "resumen": "Sabiduría tradicional, consejo espiritual, matrimonio o alianza sagrada, aprendizaje con mentores y fidelidad a los propios principios.",
            "amor": "Compromiso formal, boda, unión basada en valores espirituales compartidos y respeto mutuo duradero.",
            "dinero_trabajo": "Éxito a través de métodos probados, formación académica, respaldo de instituciones serias y trabajo ético impecable.",
            "salud": "Recurrir a la medicina tradicional o a profesionales de comprobada experiencia. Bienestar a través de rutinas equilibradas.",
            "espiritualidad": "Estudio de textos sagrados, integración en una tradición o escuela filosófica y búsqueda de un maestro o guía espiritual verídico."
        },
        "posicion_invertida": {
            "resumen": "Dogmatismo asfixiante, hipocresía moral, fanatismo religioso, rebelión contra normas absurdas o malos consejos de falsos gurús.",
            "amor": "Presión familiar o social que ahoga la relación. Romper con tradiciones obsoletas o descubrir doble moral en la pareja.",
            "dinero_trabajo": "Burocracia paralizante, resistencia al cambio en la empresa o escándalos institucionales por falta de transparencia.",
            "salud": "Terapias dudosas recomendadas por charlatanes. Negarse a seguir tratamientos médicos contrastados por prejuicios ideológicos.",
            "espiritualidad": "Ruptura liberadora con dogmas religiosos impuestos. Búsqueda de un camino espiritual propio fuera de las iglesias convencionales."
        },
        "lo_que_lo_hace_unico": (
            "A sus pies descansan dos llaves de oro y plata cruzadas que abren los misterios del cielo y de la tierra, "
            "y dos acólitos visten túnicas con motivos florales (rosas rojas y lirios blancos), simbolizando la enseñanza directa de maestro a discípulo. "
            "A diferencia de La Sacerdotisa (que guarda el saber en secreto e intuición solitaria), El Hierofante exterioriza la sabiduría y la enseña públicamente a la comunidad."
        ),
        "curiosidades": [
            "Las tres coronas de la tiara: Simbolizan su autoridad sobre los tres mundos: el material, el astral y el espiritual.",
            "El gesto de bendición: Su mano derecha levanta dos dedos hacia arriba y dos hacia abajo, el signo esotérico de la bendición que conecta lo esotérico con lo exotérico.",
            "Las llaves de San Pedro: Una es de oro (sol/espíritu) y la otra de plata (luna/alma), recordando que solo la unión de ambas abre las puertas del conocimiento supremo."
        ],
        "historia_inspirada": {
            "titulo": "El Guardián de las Dos Llaves",
            "relato": (
                "Un joven monje pasó diez años memorizando cada salmo de la gran abadía. Orgulloso, acudió al viejo abad y le dijo: "
                "'He aprendido cada palabra de los códices sagrados; ya soy un maestro'. El anciano tomó dos llaves oxidadas y las arrojó al lodo del patio. "
                "'Tráemelas limpias', ordenó. El joven se arrodilló, se ensució las vestiduras y frotó las llaves contra su propio pecho hasta que brillaron. "
                "'Ahora mira tus manos', dijo el abad sonriendo: 'Están llenas de tierra. La doctrina que no se ensucia sirviendo al prójimo no es más "
                "que polvo de biblioteca. Solo quien baja al barro merece abrir las puertas del cielo'."
            )
        },
        "audio": {
            "archivo": "assets/audio/el-hierofante.mp3",
            "titulo": "El Hierofante - La Tradición de los Misterios",
            "duracion_estimada": "4:35 min"
        }
    },

    # 6. LOS ENAMORADOS
    {
        "id": "los-enamorados",
        "number": 6,
        "roman": "VI",
        "name": "Los Enamorados",
        "folder": "arcanos_mayores",
        "filename": "06_los_enamorados.xml",
        "element": "Aire / Géminis",
        "astrology": "Géminis",
        "historia": (
            "En las barajas medievales y de Marsella, la carta mostraba a un joven indeciso entre dos mujeres (que representaban el vicio y la virtud) "
            "mientras Cupido apuntaba su flecha desde el cielo. Arthur Edward Waite y Pamela Colman Smith transformaron radicalmente la escena "
            "en el Edén primordial: representan a Adán y Eva desnudos bajo las alas protectoras del arcángel Rafael (ángel de la sanación y el aire), "
            "con el Árbol de la Vida detrás del hombre y el Árbol del Conocimiento con la serpiente detrás de la mujer, elevando el significado de la elección moral "
            "a la integración sagrada de las polaridades masculina y femenina (Hieros Gamos)."
        ),
        "significado_fundamental": (
            "Los Enamorados representa el poder del amor auténtico, la alineación de valores, la atracción de almas afines y, crucialmente, "
            "la toma de una decisión trascendental basada en el corazón y no en el miedo. Simboliza la reconciliación de opuestos: la mente consciente (el hombre) "
            "mira a la mente inconsciente (la mujer), quien a su vez eleva su mirada hacia la supraconsciencia divina (el arcángel)."
        ),
        "posicion_normal": {
            "resumen": "Amor profundo, elecciones alineadas con el alma, reciprocidad emocional, armonía de valores y unión sagrada.",
            "amor": "Romance apasionado y maduro. Hallar a alguien con quien compartir valores de vida. Comunicación transparente, química magnética y decisiones de futuro en pareja.",
            "dinero_trabajo": "Sociedades laborales armoniosas y fructíferas. Elegir entre dos caminos profesionales guiándose por la verdadera vocación y la ética.",
            "salud": "Vitalidad en equilibrio. Conexión armónica entre cuerpo, mente y emociones. Buenos hábitos gracias al amor propio y el autocuidado.",
            "espiritualidad": "Integración del ánima y el ánimus (Jung). Matrimonio interior entre la razón y la intuición bajo la guía de la consciencia superior."
        },
        "posicion_invertida": {
            "resumen": "Dilemas desgarradores, desalineación de valores, infidelidad, elecciones cobardes o conflicto interno entre deber y deseo.",
            "amor": "Desconexión en la pareja, dudas sobre el futuro juntos, tentaciones que quiebran la confianza o permanecer en un vínculo por miedo a la soledad.",
            "dinero_trabajo": "Desacuerdos graves entre socios. Tomar una decisión financiera apresurada que traiciona los propios principios éticos.",
            "salud": "Conflictos emocionales somatizados en el sistema respiratorio o circulatorio. Fatiga provocada por la indecisión constante y la ansiedad.",
            "espiritualidad": "Fragmentación interna. Escuchar las voces del ego en lugar de la verdad del corazón; negar la sombra personal culpando a otros."
        },
        "lo_que_lo_hace_unico": (
            "Es la única carta donde la mirada traza un triángulo sagrado: el hombre mira a la mujer, la mujer mira al arcángel y el arcángel bendice a ambos. "
            "A diferencia del 2 de Copas (que representa el flechazo o la conexión personal entre dos personas), Los Enamorados es una iniciación mayor: "
            "exige elegir qué clase de ser humano quieres ser mediante la persona y los valores que decides abrazar."
        ),
        "curiosidades": [
            "El arcángel Rafael: Su nombre en hebreo significa 'Medicina de Dios', indicando que el amor genuino tiene el poder absoluto de sanar cualquier herida del alma.",
            "Las doce llamas del árbol del hombre: Representan los doce signos del zodiaco y las pasiones activas de la voluntad.",
            "La montaña violeta de fondo: Simboliza la cima de la consciencia espiritual a la que solo se puede ascender cuando los opuestos se reconcilian."
        ],
        "historia_inspirada": {
            "titulo": "La Encrucijada de los Dos Espejos",
            "relato": (
                "Al llegar a la cima del monte Horeb, una viajera encontró dos senderos custodiados por un ángel de fuego lila. "
                "A la izquierda, un camino pavimentado de oro prometía aplausos, comodidad y la aprobación de todos los reyes. "
                "A la derecha, un sendero estrecho de flores silvestres exigía desnudez de alma y verdad innegociable. "
                "—¿Cuál de los dos me llevará a la felicidad? —preguntó la viajera temblando. "
                "El ángel extendió sus alas y sonrió con compasión infinita: "
                "—Ningún camino hace feliz a quien elige con la cabeza llena de miedos ajenos. Elige aquello que, aun si perdieras todo lo material, "
                "haría que tu corazón cantara al anochecer. Lo que amas con verdad es tu único y verdadero destino."
            )
        },
        "audio": {
            "archivo": "assets/audio/los-enamorados.mp3",
            "titulo": "Los Enamorados - La Elección Sagrada del Corazón",
            "duracion_estimada": "4:45 min"
        }
    },

    # 7. EL CARRO
    {
        "id": "el-carro",
        "number": 7,
        "roman": "VII",
        "name": "El Carro",
        "folder": "arcanos_mayores",
        "filename": "07_el_carro.xml",
        "element": "Agua / Cáncer",
        "astrology": "Cáncer",
        "historia": (
            "Inspirado en los desfiles triunfales de los generales en la Roma imperial y en los 'Trionfi' de Petrarca que dieron origen al Tarot renacentista. "
            "En el Tarot de Marsella y Rider-Waite-Smith, el héroe coronado no lleva riendas en sus manos: conduce su carroza cúbica mediante la pura fuerza de su voluntad "
            "y su concentración mental. Va protegido por una armadura con lunas crecientes en los hombros y bajo un dosel de estrellas azules, mientras dos esfinges "
            "—una blanca y otra negra— tiran en direcciones opuestas, simbolizando el dominio consciente sobre las pasiones e instintos contradictorios de la psique humana."
        ),
        "significado_fundamental": (
            "El Carro representa la victoria sobre los obstáculos, la autodeterminación inquebrantable, el avance imparable y el triunfo de la mente disciplinada. "
            "Enseña que el éxito no depende de la ausencia de conflictos internos o externos, sino de la capacidad de mantener el rumbo firme integrando las fuerzas polares (luz y sombra) "
            "hacia un mismo propósito supremo."
        ),
        "posicion_normal": {
            "resumen": "Triunfo, avance acelerado, disciplina férrea, superación de pruebas, viajes exitosos y control emocional.",
            "amor": "Superar crisis de pareja con madurez y decisión. Conquistar metas conjuntas o tomar las riendas de la propia vida sentimental dejando atrás amores del pasado.",
            "dinero_trabajo": "Victoria en proyectos competitivos, liderazgo indiscutido, consecución de metas ambiciosas y excelente momento para expandir negocios al extranjero.",
            "salud": "Fuerza de voluntad admirable para superar adicciones o adoptar rutinas deportivas exigentes. Recuperación rápida de enfermedades.",
            "espiritualidad": "El alma doma el vehículo del cuerpo y de las emociones. Avance espiritual mediante la autodisciplina y el propósito inquebrantable."
        },
        "posicion_invertida": {
            "resumen": "Pérdida de control, agresión desmedida, choque contra la realidad, falta de dirección o parálisis por sabotaje interno.",
            "amor": "Luchas de poder en la pareja, autoritarismo destructivo o relación que se estrella por no saber frenar los impulsos de orgullo y rencor.",
            "dinero_trabajo": "Proyectos que descarrilan por exceso de arrogancia o falta de planificación. Pérdidas en viajes o disputas legales descontroladas.",
            "salud": "Agotamiento extremo por conducir la propia vida a velocidades insostenibles (burnout). Riesgo de accidentes de tráfico o contracturas musculares agudas.",
            "espiritualidad": "Ego fuera de control. Creer que la fuerza bruta puede sustituir a la gracia divina; desconexión entre lo que se predica y lo que se practica."
        },
        "lo_que_lo_hace_unico": (
            "Es el único vehículo triunfal conducido sin riendas físicas: las dos esfinges (una blanca y otra negra) descansan a sus pies y avanzan "
            "únicamente por la telepatía y el magnetismo del conductor. A diferencia de El Mago (que prepara el terreno con sus herramientas), "
            "El Carro ya está en marcha por el mundo conquistando la victoria en el plano tangible."
        ),
        "curiosidades": [
            "Las esfinges blanca y negra: Simbolizan las fuerzas opuestas de la misericordia y la severidad cabalística que intentan desviarse pero son domadas por la mente superior.",
            "Las lunas en las hombreras: Son las caras de Urim y Tumim del sumo sacerdote hebreo, que indicaban si las decisiones estaban bendecidas por la divinidad.",
            "El dosel estrellado: Indica que el guerrero está guiado por las influencias cósmicas celestiales y no solo por sus deseos terrenales."
        ],
        "historia_inspirada": {
            "titulo": "Las Dos Esfinges de la Puerta de Tebas",
            "relato": (
                "Antes de coronarse príncipe, el guerrero debía cruzar el Desfiladero de las Sombras conduciendo un carro de bronce tirado por dos leones alados. "
                "El león blanco quería volar hacia las nubes de la ilusión; el león negro quería descender a las cavernas del instinto salvaje. "
                "El guerrero soltó el látigo y las cadenas. Cerró los ojos, respiró hondo y visualizó el obelisco de la ciudad natal al final del cañón. "
                "Fijó su mente con tal pureza en el horizonte que los dos leones, sintiendo la vibración inquebrantable de su pecho, unieron sus lomos "
                "y corrieron al unísono como si fueran un solo relámpago. Al llegar a Tebas, la multitud vitoreó: no celebraban la velocidad del carro, "
                "sino al hombre que había vencido a su propia tempestad interior."
            )
        },
        "audio": {
            "archivo": "assets/audio/el-carro.mp3",
            "titulo": "El Carro - La Victoria de la Voluntad",
            "duracion_estimada": "4:30 min"
        }
    },

    # 8. LA FUERZA
    {
        "id": "la-fuerza",
        "number": 8,
        "roman": "VIII",
        "name": "La Fuerza",
        "folder": "arcanos_mayores",
        "filename": "08_la_fuerza.xml",
        "element": "Fuego / Leo",
        "astrology": "Leo",
        "historia": (
            "En el Tarot de Marsella, La Fuerza ocupaba el número XI y mostraba a una mujer sujetando las fauces abiertas de un león "
            "mientras llevaba un sombrero con forma de lemniscata. Waite y la Golden Dawn intercambiaron su posición con La Justicia (colocando La Fuerza en el VIII "
            "para alinearla con el signo astrológico de Leo). Pamela Colman Smith suavizó la lucha: la doncella viste de blanco virginal coronada de flores vivas "
            "y acaricia las fauces del león rojizo con infinita ternura, demostrando que la verdadera fuerza espiritual no reside en el músculo ni en la violencia, "
            "sino en la compasión, la paciencia y el amor incondicional que domestica la fiera de los instintos primarios."
        ),
        "significado_fundamental": (
            "La Fuerza es el dominio suave del corazón sobre el instinto animal, la valentía moral, la resiliencia compasiva y la paciencia que todo lo vence. "
            "Nos enseña que reprimir nuestras pasiones o atacar la agresividad con más violencia solo engendra monstruos mayores; la fiera interior se calma "
            "abrazándola con consciencia, entendimiento y ternura serena."
        ),
        "posicion_normal": {
            "resumen": "Coraje sereno, paciencia infinita, autodominio compasivo, sanación de heridas emocionales y victoria del amor sobre el miedo.",
            "amor": "Vínculo apasionado pero lleno de respeto, paciencia y ternura. Capacidad para resolver desavenencias con empatía y comprensión profunda.",
            "dinero_trabajo": "Superar situaciones de alta presión o conflictos laborales mediante la diplomacia firme, la constancia y el carisma magnético sin recurrir a la agresividad.",
            "salud": "Recuperación vigorosa de la vitalidad, resistencia física sobresaliente y dominio consciente de los apetitos corporales y la ansiedad.",
            "espiritualidad": "La kundalini o fuego vital canalizado hacia la compasión universal. Aceptación amorosa de la propia sombra sin juicio destructivo."
        },
        "posicion_invertida": {
            "resumen": "Pérdida de paciencia, debilidad ante la tentación, ira destructiva, inseguridad paralizante o tiranía emocional.",
            "amor": "Discusiones agresivas, reproches hirientes, manipulación a través de la culpa o dejarse avasallar por miedo al conflicto.",
            "dinero_trabajo": "Ceder ante la intimidación en el trabajo o, en el polo opuesto, comportarse como un tirano arrogante con subordinados.",
            "salud": "Agotamiento inmunológico por exceso de ira o rencor acumulado. Caer en excesos adictivos o desórdenes alimenticios por descontrol emocional.",
            "espiritualidad": "Miedo a la propia intensidad vital. Desconexión del poder personal por creerse débil o indigno de respeto."
        },
        "lo_que_lo_hace_unico": (
            "Es la única carta donde un ser humano toca a una bestia salvaje no con armas, lanzas o cadenas, sino con caricias y una guirnalda de flores. "
            "A diferencia de El Emperador (que impone orden mediante la ley y el castigo), La Fuerza transforma la naturaleza salvaje desde adentro "
            "a través del amor incondicional y la presencia serena."
        ),
        "curiosidades": [
            "La lemniscata sobre su cabeza: Al igual que El Mago, porta el símbolo del infinito, revelando que la suavidad compasiva está conectada con el poder eterno de Dios.",
            "El león que lame su mano: Simboliza que el ego y el instinto no deben ser aniquilados, sino integrados como nobles aliados al servicio del alma.",
            "El cinturón de rosas: Une a la mujer con el león, representando que el puente entre la mente consciente y la fuerza biológica es la belleza del corazón."
        ],
        "historia_inspirada": {
            "titulo": "La Doncella y el Rey de la Selva",
            "relato": (
                "Un león devorador de rebaños bajó de las colinas sembrando el terror. Los caballeros del rey salieron con armaduras de acero y lanzas afiladas; "
                "el león los despedazó a todos porque olían a miedo y a sangre. Al atardecer, una tejedora del pueblo caminó descalza hacia la guarida de la bestia. "
                "Llevaba en sus manos un cuenco de agua fresca y una trenza de jazmines. El león rugió hasta hacer temblar los robles. La mujer no huyó ni parpadeó; "
                "se sentó en una piedra, lo miró a los ojos con la ternura de una madre y le habló de la soledad de la montaña. "
                "La bestia, desconcertada ante la ausencia de violencia, se acercó lentamente, agachó la testuz y apoyó su pesada cabeza en el regazo de la doncella. "
                "Desde aquel día, el león cuidaba el rebaño: había descubierto que el amor es más invencible que mil espadas."
            )
        },
        "audio": {
            "archivo": "assets/audio/la-fuerza.mp3",
            "titulo": "La Fuerza - La Alquimia de la Ternura",
            "duracion_estimada": "4:20 min"
        }
    },

    # 9. EL ERMITAÑO
    {
        "id": "el-ermitano",
        "number": 9,
        "roman": "IX",
        "name": "El Ermitaño",
        "folder": "arcanos_mayores",
        "filename": "09_el_ermitano.xml",
        "element": "Tierra / Virgo",
        "astrology": "Virgo",
        "historia": (
            "En las barajas del Renacimiento (Visconti-Sforza y Marsella), El Ermitaño solía portar un reloj de arena, identificándolo como 'El Tiempo' "
            "o el dios Saturno (Cronos), señor de la vejez y la paciencia. Con el tiempo, el reloj fue sustituido por una lámpara o linterna encendida. "
            "Arthur Edward Waite y Pamela Colman Smith lo colocaron en la cima solitaria de una cumbre nevada: un anciano venerado cubierto por una túnica gris, "
            "sosteniendo el báculo de oro del peregrino y alzando la linterna que alberga en su interior la estrella de seis puntas (el Sello de Salomón), "
            "convirtiéndolo en el faro místico que ilumina el sendero para los buscadores que ascienden detrás de él."
        ),
        "significado_fundamental": (
            "El Ermitaño es el arquetipo del sabio interior, la búsqueda de la verdad esencial, la introspección silenciosa y el retiro fecundo. "
            "Enseña que para escuchar la voz del alma es necesario acallar el bullicio del mundo exterior. No representa la soledad trágica ni el abandono, "
            "sino la bendita soledad elegida (solitud) donde se forja la sabiduría que luego servirá para guiar a la humanidad."
        ),
        "posicion_normal": {
            "resumen": "Búsqueda interior, introspección fecunda, guía sabia, madurez reflexiva, prudencia y luz en medio de la oscuridad.",
            "amor": "Tiempo de reflexión personal antes de comprometerse. Profundización emocional en la pareja a través del respeto mutuo de los espacios íntimos. Madurez afectiva que no depende de la aprobación constante del otro.",
            "dinero_trabajo": "Análisis minucioso, asesoramiento por parte de expertos veteranos, investigación académica o trabajo independiente concentrado. Evitar prisas financieras.",
            "salud": "Longevidad, necesidad de descanso reparador, desintoxicación del estrés urbano y cuidado de las articulaciones y la columna vertebral.",
            "espiritualidad": "Conexión directa con la chispa divina interior a través de la meditación, el retiro y el estudio filosófico profundo. Convertirse en la propia luz."
        },
        "posicion_invertida": {
            "resumen": "Aislamiento destructivo, misantropía amargada, soledad no deseada, terquedad de viejo ermitaño o rechazo a recibir ayuda.",
            "amor": "Frialdad afectiva, alejamiento emocional que desgasta la relación, encierro en uno mismo o miedo patológico a abrir el corazón.",
            "dinero_trabajo": "Falta de trabajo en equipo, hermetismo perjudicial en la oficina o retrasos excesivos en proyectos por perfeccionismo paralizante.",
            "salud": "Problemas relacionados con el sedentarismo, depresión por aislamiento social, deterioro de la vista o dolencias crónicas desatendidas.",
            "espiritualidad": "Arrogancia intelectual. Creer que nadie está a la altura de su nivel espiritual o perderse en filosofías áridas sin contacto con la compasión humana."
        },
        "lo_que_lo_hace_unico": (
            "Es el único arcano que se encuentra ya en la cumbre nevada más alta, pero en lugar de descansar victorioso, "
            "se gira hacia el abismo y eleva su linterna para alumbrar el camino a quienes aún están escalando en la oscuridad. "
            "A diferencia de El Hierofante (que predica ante multitudes en templos de piedra), El Ermitaño enseña desde el silencio de la montaña a quien realmente esté dispuesto a buscar la verdad."
        ),
        "curiosidades": [
            "La estrella de seis puntas en la linterna: Es la Estrella de David o Sello de Salomón, que une el triángulo del fuego con el del agua, simbolizando la verdad cósmica que ilumina las tinieblas.",
            "El báculo de la mano izquierda: Representa la columna vertebral y el soporte de la experiencia vivida, sostenido con la mano receptiva del inconsciente.",
            "La nieve inmaculada: Simboliza la mente pacificada y libre de los deseos mundanos que nublan la visión clara."
        ],
        "historia_inspirada": {
            "titulo": "La Linterna de la Cumbre Helada",
            "relato": (
                "Un joven monje subió a la montaña más alta del Tíbet buscando al anciano de la leyenda. Lo halló sentado al borde del risco, "
                "sosteniendo una pequeña llama en una lámpara de vidrio. 'Maestro', suplicó el joven con los labios morados de frío, "
                "'enséñame la doctrina secreta para salvar al mundo'. El anciano no se movió; le pasó la linterna y le dijo: "
                "'Baja la mirada hacia el sendero por el que viniste'. El joven miró hacia abajo: en medio de la ventisca nocturna, "
                "decenas de peregrinos avanzaban a ciegas guiados por el destello lejano de aquella diminuta lámpara. "
                "'No intentes salvar al mundo con palabras grandilocuentes', murmuró el anciano. 'Basta con que mantengas tu propia luz encendida "
                "en la noche más oscura; los demás encontrarán el camino'."
            )
        },
        "audio": {
            "archivo": "assets/audio/el-ermitano.mp3",
            "titulo": "El Ermitaño - La Linterna del Silencio Interior",
            "duracion_estimada": "4:40 min"
        }
    },

    # 10. LA RUEDA DE LA FORTUNA
    {
        "id": "la-rueda-de-la-fortuna",
        "number": 10,
        "roman": "X",
        "name": "La Rueda de la Fortuna",
        "folder": "arcanos_mayores",
        "filename": "10_la_rueda_de_la_fortuna.xml",
        "element": "Fuego / Júpiter",
        "astrology": "Júpiter",
        "historia": (
            "Arquetipo medieval presente en manuscritos de los Carmina Burana y en el poema 'Consolación de la Filosofía' de Boecio: "
            "la diosa Fortuna giraba su rueda con la inscripción 'Regnabo, Regno, Regnavi, Sum sine regno' (Reinaré, Reino, Reiné, Estoy sin reino). "
            "Eliphas Lévi y Arthur Edward Waite la enriquecieron con simbolismo kabbalístico, egipcio y alquímico: colocaron en las cuatro esquinas "
            "a las cuatro criaturas querubínicas aladas de la visión de Ezequiel (el Ángel, el Águila, el León y el Toro, que corresponden a los cuatro evangelistas "
            "y a los cuatro signos fijos del zodiaco: Acuario, Escorpio, Leo y Tauro), una esfinge en la cima y la serpiente Tifón y Hermanubis en los costados."
        ),
        "significado_fundamental": (
            "La Rueda de la Fortuna es el arquetipo de los ciclos de la vida, el destino en movimiento, las sincronicidades providenciales y el cambio inevitable. "
            "Nos recuerda la gran ley cósmica: todo fluye, todo sube y todo baja. Quien se identifica con los bordes de la rueda sufre con cada giro de la fortuna; "
            "quien se sitúa en el centro inmóvil de la rueda encuentra la serenidad que trasciende las circunstancias cambiantes del mundo exterior."
        ),
        "posicion_normal": {
            "resumen": "Giro favorable del destino, golpes de suerte, cambios positivos, oportunidades inesperadas y nuevo ciclo vital.",
            "amor": "Encuentros fortuitos con fuerte sensación de destino. Giro positivo en la relación, superación de viejas etapas y aire fresco en el romance.",
            "dinero_trabajo": "Ascensos sorpresivos, ganancias imprevistas, éxito en inversiones y apertura de nuevas puertas comerciales gracias a una sincronicidad afortunada.",
            "salud": "Recuperación acelerada, mejora en los biorritmos del cuerpo y vitalidad renovada. Favorable para iniciar nuevos hábitos de vida.",
            "espiritualidad": "Comprensión de las leyes del karma y de la sincronicidad. Darse cuenta de que los acontecimientos aparentemente aleatorios obedecen a un orden inteligente."
        },
        "posicion_invertida": {
            "resumen": "Racha desfavorable temporal, resistencia inútil al cambio, mala suerte aparente o aferrarse a ciclos ya agotados.",
            "amor": "Inestabilidad emocional, altibajos constantes en la pareja o dificultades para romper con dinámicas tóxicas que se repiten una y otra vez.",
            "dinero_trabajo": "Gastos imprevistos, retrasos en pagos o inversiones que no dan el fruto esperado. No es momento para especulaciones arriesgadas.",
            "salud": "Desequilibrios hormonales pasajeros, mareos o sensibilidad a los cambios estacionales. Necesidad de estabilidad emocional.",
            "espiritualidad": "Sensación de impotencia ante el destino. Culpar a la mala suerte en lugar de asumir la responsabilidad de las propias decisiones pasadas."
        },
        "lo_que_lo_hace_unico": (
            "Es una de las pocas cartas de los Arcanos Mayores donde no figura ningún ser humano en primer plano: "
            "solo entidades míticas (la Esfinge, Tifón, Hermanubis y los cuatro querubines leyendo los libros sagrados). "
            "A diferencia de La Justicia (que mide las causas y consecuencias humanas lógicas), La Rueda opera desde las leyes cósmicas universales "
            "que escapan al control del ego."
        ),
        "curiosidades": [
            "Las letras en la rueda: Alternan las letras hebreas del Tetragrámaton (YHVH) con las latinas T-A-R-O, formando los anagramas TAROT, ROTA (rueda) y TORA (ley).",
            "Los cuatro seres alados con libros: En las esquinas estudian los textos sagrados mientras la rueda gira, recordando que el conocimiento permanece mientras la materia cambia.",
            "Hermanubis y Tifón: Hermanubis (figura roja con cabeza de chacal) sube por la derecha encarnando la evolución del alma, mientras la serpiente Tifón desciende por la izquierda encarnando la involución material."
        ],
        "historia_inspirada": {
            "titulo": "El Eje del Gran Molino",
            "relato": (
                "Un mendigo y un rey caminaban por el mismo sendero cuando una tormenta los obligó a refugiarse en un antiguo molino de viento abandonado. "
                "El rey lloraba amargamente porque había perdido su castillo en la guerra; el mendigo reía a carcajadas porque había encontrado un trozo de pan. "
                "En medio del silencio, el viejo molinero señaló el gran engranaje de madera que giraba empujado por el vendaval. "
                "—Fijaos en los dientes exteriores de la rueda —dijo el molinero—: ahora están en el barro, luego en la cima del cielo, y vuelven a caer. "
                "Si os aferráis a los dientes, siempre estaréis mareados de dicha o de pánico. Pero mirad el eje central de hierro: jamás sube ni baja, "
                "permanece en calma mientras sostiene todo el peso del mundo. Sed el eje, amigos míos, nunca los dientes."
            )
        },
        "audio": {
            "archivo": "assets/audio/la-rueda-de-la-fortuna.mp3",
            "titulo": "La Rueda de la Fortuna - Los Ciclos del Destino",
            "duracion_estimada": "4:25 min"
        }
    }
]
