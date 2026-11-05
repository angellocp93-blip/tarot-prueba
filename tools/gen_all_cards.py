import json
import os

os.makedirs("data", exist_ok=True)

# Load majors from data/majors.json
with open("data/majors.json", "r", encoding="utf-8") as f:
    majors = json.load(f)

# Define helper to construct minor arcana
def make_card(id_slug, name, num, roman, suit, element, keywords, essence, meaning_upright, symbols, light, shadow, love, work, spirit, advice, question, rev_keywords, rev_meaning, rev_heal):
    return {
        "id": id_slug,
        "name": name,
        "number": num,
        "roman": roman,
        "type": "Arcano Menor",
        "suit": suit,
        "element": element,
        "astrology": f"Elemento {element}",
        "keywords": keywords,
        "essence": essence,
        "meaning_upright": meaning_upright,
        "symbols": symbols,
        "light_side": light,
        "shadow_side": shadow,
        "love": love,
        "work": work,
        "spirituality": spirit,
        "advice": advice,
        "reflection_question": question,
        "reversed": {
            "keywords": rev_keywords,
            "meaning": rev_meaning,
            "how_to_heal": rev_heal
        },
        "img": f"assets/cards/{id_slug}.webp"
    }

cards_list = list(majors)

# 1. BASTOS (14 cards)
bastos_data = [
    ("as-de-bastos", "As de Bastos", "As", "I", ["Inspiración", "Chispa", "Nueva pasión", "Energía vital", "Comienzo"],
     "La semilla ardiente de una nueva idea o proyecto. Fuerza motriz pura lista para encender tu camino.",
     "El As de Bastos es un torrente de energía creadora, una oportunidad dorada que te apasiona y te invita a emprender sin titubeos.",
     [{"name": "Mano de las nubes", "desc": "Don divino de la energía del fuego."}, {"name": "Brotes verdes", "desc": "Fertilidad y crecimiento vital."}, {"name": "Castillo lejano", "desc": "Meta noble a conquistar."}],
     "Entusiasmo contagioso, valentía para iniciar, proactividad e inspiración.", "Impulsividad descontrolada, arranques sin constancia, quemarse antes de empezar.",
     "Química instantánea, nuevo romance electrizante o pasión renovada en la pareja.", "Comienzo brillante de un negocio o proyecto; motivación para emprender.",
     "Despertar de la energía kundalini y de la pasión sagrada por la existencia.", "Aprovecha la chispa mientras arde. Da el primer paso con valentía.", "¿Qué proyecto hace latir tu corazón y aún no te atreves a empezar?",
     ["Falta de energía", "Demoras", "Proyectos abortados"], "Invertido indica falta de motivación o proyectos que no logran arrancar.", "Reconecta con tus motivos profundos antes de forzar acciones vacías."),

    ("dos-de-bastos", "Dos de Bastos", "2", "II", ["Planificación", "Visión de futuro", "Decisión", "Progreso", "Nuevos horizontes"],
     "El mundo en tus manos. Diseña el mapa de tu próxima gran conquista desde una posición segura.",
     "El Dos de Bastos representa la planificación estratégica. Tienes una base segura, pero sabes que tu alma pide expandirse más allá de lo conocido.",
     [{"name": "Globo terráqueo", "desc": "Ambición global y visión amplia."}, {"name": "Dos bastos", "desc": "Uno anclado en lo seguro y otro listo para avanzar."}],
     "Visión de futuro, estrategia brillante, audacia controlada y liderazgo.", "Miedo a salir de la zona de confort, arrogancia o indecisión.",
     "Planes conjuntos a futuro con la pareja; mudanzas o viajes compartidos.", "Alianzas estratégicas, expansión de mercados, visión a largo plazo.",
     "Alinear la voluntad individual con una visión más elevada de servicio.", "Planifica con audacia; no te conformes con lo que ya dominas.", "¿Estás dispuesto a dejar la comodidad de tu castillo para descubrir nuevas tierras?",
     ["Miedo a lo desconocido", "Dudas", "Falta de visión"], "Invertido señala reticencia a arriesgarse o temor a perder lo ganado.", "Acepta que crecer exige salir de lo seguro; da pasos medidos."),

    ("tres-de-bastos", "Tres de Bastos", "3", "III", ["Expansión", "Esperanza", "Barcos regresando", "Crecimiento", "Resultados iniciales"],
     "Tus barcos han zarpado y ya ves sus velas en el horizonte. Tu visión se consolida y rinde frutos.",
     "El Tres de Bastos marca la fase donde tus esfuerzos iniciales comienzan a rendir resultados tangibles. Miras el futuro con confianza y certeza.",
     [{"name": "Barcos en el mar", "desc": "Proyectos en marcha que traen beneficios."}, {"name": "Mirada al horizonte", "desc": "Confianza serena en el porvenir."}],
     "Apertura a nuevas oportunidades, confianza serena, expansión exitosa.", "Ansiedad por los frutos, impaciencia por demoras, desilusión si tarda.",
     "Relaciones a distancia que prosperan, horizontes y proyectos compartidos.", "Expansión comercial, nuevos mercados, éxito en inversiones a medio plazo.",
     "Ampliación de consciencia, integración de sabidurías de diversas culturas.", "Mantén la mirada en el horizonte. Tus esfuerzos darán fruto.", "¿Qué nuevas fronteras estás listo para explorar hoy?",
     ["Retrasos", "Frustración", "Horizontes cerrados"], "Invertido avisa de demoras en acuerdos o resultados que tardan en llegar.", "Revisa la logística y ten paciencia; las mejores cosechas toman su tiempo."),

    ("cuatro-de-bastos", "Cuatro de Bastos", "4", "IV", ["Celebración", "Hogar", "Comunidad", "Armonía", "Consolidación"],
     "Momento de festejar la llegada a un puerto seguro, la armonía hogareña y el éxito compartido.",
     "El Cuatro de Bastos anuncia celebraciones, compromisos, compra de vivienda, reuniones dichosas y sentimiento de acogida y plenitud comunitaria.",
     [{"name": "Pérgola floral", "desc": "Consolidación festiva y abundancia."}, {"name": "Figuras festejando", "desc": "Alegría compartida y hospitalidad."}],
     "Alegría sincera, gratitud, paz hogareña y sentido de pertenencia.", "Excesos en fiestas, superficialidad o incomodidad en reuniones.",
     "Compromiso feliz, boda, convivencia armoniosa y bendición familiar.", "Celebración de metas de equipo, excelente clima laboral y estabilidad.",
     "Bendición del hogar como templo sagrado y comunión fraterna.", "Abre tu casa y tu corazón para festejar con los seres que amas.", "¿Qué bendición reciente merece ser celebrada con gratitud?",
     ["Tensiones familiares", "Celebración cancelada", "Incomodidad"], "Invertido indica roces familiares menores o sensación de no encajar.", "Cultiva la paciencia en el hogar y no magnifiques detalles menores."),

    ("cinco-de-bastos", "Cinco de Bastos", "5", "V", ["Competencia", "Disputas", "Rivalidad", "Debate", "Tensión constructiva"],
     "Cinco figuras en lucha de bastos: competencia y debate acalorado que pone a prueba tus destrezas.",
     "El Cinco de Bastos refleja un entorno competitivo o discusiones de equipo. Es la oportunidad de poner a prueba tu temple sin perder la elegancia.",
     [{"name": "Jóvenes luchando", "desc": "Choque de fuerzas divergentes que buscan medirse."}, {"name": "Ropas dispares", "desc": "Diferencia de opiniones y falta de alineación."}],
     "Espíritu deportivo, debate constructivo y poner a prueba habilidades.", "Conflictos estériles por ego, peleas mezquinas y desgaste inútil.",
     "Discusiones por orgullo en la pareja; pequeños roces que exigen escucha.", "Competencia intensa en el mercado, reuniones caóticas de equipo.",
     "El conflicto interno entre las distintas voces y demandas del ego.", "No te tomes las disputas como algo personal; defiende tu postura con calma.", "¿Estás buscando una solución real o solo quieres tener la razón?",
     ["Conflicto destructivo", "Evasión del debate", "Rivalidad desleal"], "Invertido advierte de trampas en la competencia o huida de conversaciones necesarias.", "Establece reglas claras o retírate de batallas que no te aportan valor."),

    ("seis-de-bastos", "Seis de Bastos", "6", "VI", ["Victoria", "Reconocimiento", "Aclamación pública", "Orgullo merecido", "Éxito"],
     "El jinete coronado de laurel desfila ante la multitud. El reconocimiento público a tu esfuerzo.",
     "El Seis de Bastos señala que tu talento y perseverancia son finalmente aplaudidos y validados socialmente. Recompensa al trabajo bien hecho.",
     [{"name": "Corona de laurel", "desc": "Victoria indiscutible y honor ganado a pulso."}, {"name": "Multitud aclamando", "desc": "Apoyo de la comunidad y éxito visible."}],
     "Autoestima sana, liderazgo inspirador, generosidad en el triunfo.", "Arrogancia, depender del aplauso ajeno para sentirse valioso.",
     "Orgullo mutuo en la pareja, superación conjunta de pruebas difíciles.", "Ascensos, premios, felicitaciones públicas y consolidación profesional.",
     "Comprender que el éxito exterior es reflejo de la victoria interior.", "Disfruta de los aplausos con humildad y gratitud hacia quienes te apoyaron.", "¿Aceptas el reconocimiento que mereces sin falsas modestias?",
     ["Soberbia castigada", "Falta de reconocimiento", "Envidia ajena"], "Invertido avisa de orgullo herido o falta de validación de tu esfuerzo.", "Recuerda que tu valor esencial no depende de los aplausos ajenos."),

    ("siete-de-bastos", "Siete de Bastos", "7", "VII", ["Defensa de principios", "Resistencia", "Posición ventajosa", "Coraje", "Firmeza"],
     "En lo alto de la colina, una sola persona resiste con valentía el embate. Tu causa es justa y vencerás.",
     "El Siete de Bastos aparece cuando debes defender tus ideas o territorio ante presiones o críticas. Tienes la ventaja moral y estratégica.",
     [{"name": "Hombre en la colina", "desc": "Posición de ventaja ética y estratégica."}, {"name": "Bastos desde abajo", "desc": "Presión del entorno que no logra quebrarte."}],
     "Valentía indomable, defensa ética de valores, resiliencia ejemplar.", "Paranoia defensiva, terquedad agresiva, desgaste innecesario.",
     "Defender la relación contra habladurías o injerencias externas.", "Proteger tu trabajo o cuota de mercado con firmeza y profesionalismo.",
     "Firmeza espiritual ante el escepticismo o presiones mundanas.", "Mantén tu terreno con firmeza. Tienes la razón y la fuerza para resistir.", "¿Qué causa es tan valiosa para ti que vale la pena defenderla?",
     ["Agotamiento por luchar", "Rendición prematura", "Terquedad ciega"], "Invertido indica cansancio extremo por pelear batallas desgastantes.", "Elige bien tus batallas; si la posición no es justa, es sabio replegarse."),

    ("ocho-de-bastos", "Ocho de Bastos", "8", "VIII", ["Velocidad", "Noticias rápidas", "Acontecimientos acelerados", "Avance veloz", "Sincronía"],
     "Ocho bastos vuelan coordinados por el aire libre. Los acontecimientos se aceleran vertiginosamente.",
     "El Ocho de Bastos anuncia rapidez: mensajes decisivos que llegan, viajes imprevistos y resolución acelerada de asuntos pendientes.",
     [{"name": "Bastos en vuelo alineado", "desc": "Dirección clara y alineación sin obstáculos."}, {"name": "Cielo abierto", "desc": "Canal despejado para que fluya la energía veloz."}],
     "Rapidez mental, decisiones certeras, noticias favorables y dinamismo.", "Precipitación imprudente, saturación de información, prisa ciega.",
     "Mensajes apasionados sorpresa, viajes románticos y avances rápidos.", "Cierre veloz de acuerdos, respuestas inmediatas a solicitudes.",
     "Descargas de inspiración intuitiva instantánea y alineación cósmica.", "Aprovecha el viento a favor y responde con prontitud sin dispersarte.", "¿Estás listo para recibir el avance rápido que has pedido?",
     ["Retrasos frustrantes", "Mensajes cruzados", "Prisa perjudicial"], "Invertido advierte de retrasos en comunicaciones o precipitaciones torpes.", "Revisa tus mensajes y no te desesperes si el ritmo baja temporalmente."),

    ("nueve-de-bastos", "Nueve de Bastos", "9", "IX", ["Resiliencia", "Última guardia", "Perseverancia", "Fuerza residual", "A un paso de la meta"],
     "El centinela vendado en la cabeza no abandona su puesto. Has recibido golpes, pero estás a punto de vencer.",
     "El Nueve de Bastos representa la resistencia heroica en la recta final. Aunque estés cansado, tienes reservas suficientes para coronar la meta.",
     [{"name": "Centinela vendado", "desc": "Cicatrices de batallas que forjaron madurez."}, {"name": "Empalizada de bastos", "desc": "Logros previos que sostienen tu posición."}],
     "Resistencia indomable, fidelidad al deber, entereza bajo presión.", "Hipervigilancia desgastante, paranoia de ataque constante, rigidez.",
     "Sanar viejas heridas afectivas para no desconfiar injustamente de la pareja.", "Superar la recta final de un proyecto arduo con éxito garantizado.",
     "La prueba de fe del alma: perseverar en la luz en la hora previa al alba.", "Aguanta un poco más. La meta está muy cerca y tienes la fuerza necesaria.", "¿Estás confundiendo la prudencia con una desconfianza que te aísla?",
     ["Agotamiento total", "Bajar los brazos", "Paranoia destructiva"], "Invertido indica fatiga extrema o ver enemigos donde solo hay aliados.", "Date un respiro merecido; relaja las defensas con quien te ama."),

    ("diez-de-bastos", "Diez de Bastos", "10", "X", ["Sobrecarga", "Responsabilidades excesivas", "Cansancio", "Delegar", "Culminación pesada"],
     "Un hombre carga penosamente diez bastos que le tapan la vista. Llevas demasiado sobre tus hombros: delega.",
     "El Diez de Bastos advierte de agotamiento por no saber decir que no o asumir cargas ajenas. Estás cerca de la meta, pero necesitas aligerar peso.",
     [{"name": "Hombre encorvado bajo el peso", "desc": "Sobrecarga de deberes y estrés acumulado."}, {"name": "Pueblo al fondo", "desc": "El descanso está cerca si logras llegar al destino."}],
     "Capacidad titánica de trabajo, culminación de grandes esfuerzos.", "Síndrome de 'burnout', martirio inútil, incapacidad de pedir auxilio.",
     "Sentir que llevas tú solo el peso del hogar o la relación de pareja.", "Exceso de trabajo asfixiante, necesidad urgente de delegar tareas.",
     "Soltar cargas kármicas heredadas y obligaciones que no te corresponden.", "Suelta lo que no es tuyo. Pide apoyo y prioriza tu salud integral.", "¿Qué cargas ajenas estás llevando sobre tu espalda innecesariamente?",
     ["Colapso por estrés", "Incapacidad de delegar", "Liberación forzada"], "Invertido señala el colapso inminente o la sabia decisión de soltar el fardo.", "Di basta sin culpa. Reconocer los propios límites es señal de sabiduría."),

    ("sota-de-bastos", "Sota de Bastos", "Sota", "Sota", ["Curiosidad", "Entusiasmo", "Mensajes motivadores", "Espíritu explorador", "Nueva aventura"],
     "El joven explorador contemplando el basto florecido. La chispa del entusiasmo juvenil y las ganas de aprender.",
     "La Sota de Bastos personifica la curiosidad vivaz, la llegada de noticias estimulantes y el inicio entusiasta de una nueva aventura o estudio.",
     [{"name": "Túnica con salamandras", "desc": "Elemento fuego y capacidad de transformación."}, {"name": "Sombrero con pluma", "desc": "Optimismo y audacia alegre."}],
     "Curiosidad viva, optimismo fresco, ganas de aprender y simpatía.", "Inconstancia infantil, fanfarronería, abandonar tareas al poco tiempo.",
     "Coqueteo alegre, mensajes románticos llenos de ilusión y chispa.", "Noticias de cursos, propuestas de proyectos y espíritu emprendedor.",
     "Reconectar con el niño interior que mira el mundo con asombro.", "Explora sin miedo. Recibe las propuestas con mente abierta y entusiasmo.", "¿Qué habilidad nueva te despierta curiosidad y quieres explorar?",
     ["Falta de entusiasmo", "Noticias decepcionantes", "Inmadurez"], "Invertida señala falta de energía o actitud caprichosa y poco formal.", "Madura tus intenciones; lleva el entusiasmo a hechos concretos."),

    ("caballo-de-bastos", "Caballo de Bastos", "Caballo", "Caballo", ["Impulso ardiente", "Aventura", "Audacia", "Movimiento veloz", "Carisma"],
     "El caballero al galope sobre su corcel de fuego. Audacia sin límites, pasión desbordante y velocidad para conquistar metas.",
     "El Caballo de Bastos es pura acción, magnetismo y aventura. Trae mudanzas, viajes rápidos, avances decididos y una energía arrolladora.",
     [{"name": "Corcel encabritado", "desc": "Fuerza indomable que busca avanzar sin frenos."}, {"name": "Túnica de fuego", "desc": "Pasión en constante movimiento activo."}],
     "Valentía indomable, magnetismo conquistador, espíritu pionero.", "Imprudencia, agresividad temperamental, promesas vacías.",
     "Pasión electrizante, aventura ardiente pero potencialmente inestable.", "Emprendimientos audaces, ventas exitosas y viajes comerciales dinámicos.",
     "El viaje heroico del buscador que avanza con fervor hacia la verdad.", "Lánzate con decisión, pero asegúrate de ver el camino antes de acelerar.", "¿Estás canalizando tu pasión a una meta clara o quemando energía en vano?",
     ["Frustración colérica", "Frenazo brusco", "Agresividad tóxica"], "Invertido avisa de arrebatos de cólera o frenazos por exceso de velocidad.", "Tira de las riendas. Respira hondo y templa tu carácter."),

    ("reina-de-bastos", "Reina de Bastos", "Reina", "Reina", ["Magnetismo", "Confianza radiante", "Calidez", "Liderazgo inspirador", "Independencia"],
     "La soberana del fuego con su girasol y gato negro. Carisma arrollador, seguridad personal y calidez que ilumina a todos.",
     "La Reina de Bastos es dueña absoluta de su poder personal. Segura, alegre, seductora y leal; no necesita pedir aprobación a nadie.",
     [{"name": "Girasol en mano", "desc": "Vitalidad solar y amor a la luz creadora."}, {"name": "Gato negro", "desc": "Intuición domesticada y dominio de la sombra."}],
     "Autoconfianza magnética, calidez generosa, liderazgo empático y vitalidad.", "Celos egocéntricos, histeria melodramática, necesidad de atención.",
     "Mujer segura y apasionada; relación divertida, cálida y sin dependencias.", "Liderazgo motivador en empresas, carisma comercial y autonomía brillante.",
     "Confianza en la propia luz divina como herramienta de servicio y alegría.", "Adueñate de tu espacio y confía en tu magnetismo natural.", "¿En qué área de tu vida estás apagando tu luz por temor a incomodar?",
     ["Inseguridad disimulada", "Celos enfermizos", "Tiranía doméstica"], "Invertida refleja dudas sobre el propio valor o arrebatos de drama egocéntrico.", "Reconecta con tu poder interior; tu brillo es único y auténtico."),

    ("rey-de-bastos", "Rey de Bastos", "Rey", "Rey", ["Liderazgo visionario", "Autoridad inspiradora", "Grandeza", "Audacia ejecutiva", "Madurez de fuego"],
     "El gran líder sentado en su trono de leones. La madurez del fuego: no solo sueña en grande, sino que hace que las cosas sucedan.",
     "El Rey de Bastos encarna al visionario pragmático. Emprendedor nato, inspira a otros con su ejemplo, valentía y generosidad creadora.",
     [{"name": "Corona de llamas", "desc": "Pensamiento visionario y claridad de miras."}, {"name": "Basto robusto brotado", "desc": "Poder ejercido con sabiduría y regeneración."}],
     "Visión estratégica genial, liderazgo ético, coraje moral y generosidad.", "Autoritarismo intransigente, arrogancia de déspota, intolerancia.",
     "Pareja protectora y apasionada que estimula el crecimiento personal mutuo.", "Dirección de empresas, grandes emprendimientos y logros tangibles.",
     "El guerrero espiritual que usa su fortaleza para iluminar y proteger.", "Lidera con tu ejemplo. Ten grandeza de miras y no te pierdas en detalles.", "¿Cómo puedes elevar tu liderazgo para inspirar a quienes te rodean?",
     ["Tiranía egocéntrica", "Promesas rotas", "Impulsividad destructiva"], "Invertido advierte de un líder que impone por la fuerza lo que no gana con razones.", "Sustituye la imposición por el diálogo y escucha con humildad a tu equipo.")
]

for b in bastos_data:
    cards_list.append(make_card(b[0], b[1], b[2], b[3], "Bastos", "Fuego", b[4], b[5], b[6], b[7], b[8], b[9], b[10], b[11], b[12], b[13], b[14], b[15], b[16], b[17]))

print(f"Cards after Bastos: {len(cards_list)}")

# 2. COPAS (14 cards)
copas_data = [
    ("as-de-copas", "As de Copas", "As", "I", ["Amor incondicional", "Despertar emocional", "Paz interior", "Compasión", "Plenitud"],
     "El manantial del corazón desbordándose en bendiciones. Apertura total a la ternura, la intuición y el amor divino.",
     "El As de Copas es el inicio de una etapa de gracia emocional: un nuevo amor, sanación de heridas profundas, paz de espíritu y conexión mística.",
     [{"name": "Copa desbordante", "desc": "Generosidad emocional infinita del corazón."}, {"name": "Paloma con hostia", "desc": "Paz divina y presencia del espíritu."}, {"name": "Cinco chorros de agua", "desc": "Los cinco sentidos purificados por el amor."}],
     "Amor generoso, intuición afinada, compasión sanadora y alegría profunda.", "Vulnerabilidad extrema, desborde dramático, apego dependiente.",
     "Inicio de un gran amor, declaración sincera de sentimientos, reconciliación tierna.", "Proyectos con alma, vocación de servicio, relaciones laborales afectuosas.",
     "Apertura del chakra cardíaco, comunión mística y perdón liberador.", "Abre tu corazón sin miedo. Permítete amar y recibir afecto plenamente.", "¿Qué herida pasada estás listo para bañar en compasión y perdonar?",
     ["Bloqueo afectivo", "Amor no correspondido", "Tristeza reprimida"], "Invertido indica frialdad defensiva por miedo a volver a ser herido.", "No cierres tu corazón por desengaños viejos; cúrate con ternura."),

    ("dos-de-copas", "Dos de Copas", "2", "II", ["Conexión de almas", "Afinidad mutua", "Alianza armónica", "Reconciliación", "Atracción"],
     "Dos copas brindando bajo el caduceo alado. Encuentro de iguales, sintonía perfecta y respeto mutuo correspondido.",
     "El Dos de Copas es la carta de la afinidad electiva: enamoramiento genuino, asociaciones laborales basadas en la confianza o reconciliación de amigos.",
     [{"name": "Intercambio de copas", "desc": "Reciprocidad perfecta: dar y recibir en equilibrio."}, {"name": "Caduceo de Hermes y cabeza de león", "desc": "Sanación mediante la unión de polaridades y pasión noble."}],
     "Química armónica, empatía mutua, reciprocidad y respeto sincero.", "Dependencia de pareja, idealización cegadora, no saber estar a solas.",
     "Amor correspondido, conexión mágica, pacto de pareja armonioso y dulce.", "Socios comerciales transparentes con metas y valores alineados.",
     "Reconocimiento de la chispa divina en el prójimo; el espejo del alma.", "Busca el encuentro y el diálogo. Une tus fuerzas con quien comparte tu visión.", "¿Estás dando en tus relaciones la misma reciprocidad que exiges recibir?",
     ["Desconexión", "Malentendidos afectivos", "Ruptura de pactos"], "Invertido avisa de tensiones en la comunicación o falta de reciprocidad.", "Habla desde el corazón sin reproches y restaura la confianza básica."),

    ("tres-de-copas", "Tres de Copas", "3", "III", ["Celebración", "Amistad", "Comunión", "Alegría compartida", "Hermandad"],
     "Tres doncellas brindando en círculo entre uvas y flores. La dicha de la amistad leal, el apoyo mutuo y la fiesta de la vida.",
     "El Tres de Copas celebra los lazos de amistad sincera, reuniones entrañables, brindis por buenas noticias y el consuelo de una red afectiva sólida.",
     [{"name": "Tres copas en alto", "desc": "Gratitud compartida y unión fraterna."}, {"name": "Frutas y flores en la tierra", "desc": "Abundancia gozada en comunidad."}],
     "Amistad leal, alegría contagiosa, generosidad fraterna y colaboración.", "Chismes en grupos de amigos, superficialidad festiva, exclusión de otros.",
     "Diversión en pareja con amigos, ligereza afectiva, celebración familiar.", "Éxito compartido en equipo, ambiente laboral festivo y colaborativo.",
     "Círculos de sanación, apoyo comunitario y gratitud por la tribu de almas.", "Celebra con tus amigos. Agradece la presencia de quienes te apoyan incondicionalmente.", "¿A qué amigo querido hace tiempo que no llamas para decirle cuánto lo valoras?",
     ["Distanciamiento de amigos", "Chismes de grupo", "Fiestas vacías"], "Invertido señala malos entendidos entre amigos o excesos en celebraciones.", "Aléjate de habladurías y busca la cercanía sincera de corazón a corazón."),

    ("cuatro-de-copas", "Cuatro de Copas", "4", "IV", ["Apatía", "Aburrimiento", "Oportunidad ignorada", "Descontento", "Contemplación"],
     "Un joven meditabundo bajo el árbol ignora la copa que le ofrece una mano divina. Apatía y ceguera ante las bendiciones presentes.",
     "El Cuatro de Copas refleja hastío, desencanto o estancamiento emocional. Te concentras tanto en lo que te falta o en viejas quejas que no ves lo nuevo que la vida te ofrece.",
     [{"name": "Hombre de brazos cruzados", "desc": "Postura de cerrazón y rechazo al entorno."}, {"name": "Tres copas en el suelo", "desc": "Logros o afectos pasados que ya no motivan."}, {"name": "Cuarta copa en la nube", "desc": "Oportunidad nueva ignorada por ensimismamiento."}],
     "Introspección necesaria, pausa reflexiva antes de comprometerse.", "Desagradecimiento crónico, apatía depresiva, amargura y desdén.",
     "Aburrimiento en la relación, dar por sentado el amor recibido, desinterés.", "Falta de motivación laboral, rechazar propuestas por desánimo infundado.",
     "La 'noche gris' del alma: insatisfacción que invita a buscar un sentido superior.", "Levanta la mirada. Hay una copa llena de bendiciones frente a ti; recíbela.", "¿Qué oportunidad o gesto de afecto estás ignorando por quedarte rumiando el pasado?",
     ["Despertar del letargo", "Aceptación de ayuda", "Nueva motivación"], "Invertido indica salir de la apatía, abrir los ojos y abrazar nuevas propuestas.", "Agradece lo que sí tienes hoy y ponte en marcha con renovada ilusión."),

    ("cinco-de-copas", "Cinco de Copas", "5", "V", ["Duelo", "Pérdida", "Arrepentimiento", "Esperanza intacta", "Mirar hacia adelante"],
     "Una figura enlutada llora tres copas derramadas, sin ver que a su espalda quedan dos copas intactas. Llora tu pérdida, pero no olvides lo que vive.",
     "El Cinco de Copas acompaña el dolor de la pérdida, la desilusión o el arrepentimiento. Es natural hacer duelo, pero no te quedes fijado en lo perdido: aún hay amor y futuro detrás de ti.",
     [{"name": "Tres copas volcadas en el suelo", "desc": "Lo que se perdió y no volverá a ser igual."}, {"name": "Dos copas en pie a la espalda", "desc": "Lo que sobrevive: afectos, recursos y esperanza."}, {"name": "Puente sobre el río hacia el castillo", "desc": "El camino de regreso al hogar y la sanación."}],
     "Aceptación madura del duelo, honrar las pérdidas para poder sanar.", "Victimismo desesperado, aferrarse a la culpa o al rencor del pasado.",
     "Ruptura dolorosa, decepción afectiva; necesidad de sanar antes de avanzar.", "Pérdida financiera o fracaso de un proyecto; rescatar lo aprendido.",
     "La alquimia del dolor: el sufrimiento como maestro que despierta la empatía.", "Date permiso para llorar, pero luego date la vuelta: la vida no ha terminado.", "¿Qué bendiciones o personas valiosas siguen a tu lado mientras lloras lo perdido?",
     ["Sanación del duelo", "Aceptar la pérdida y avanzar", "Reconciliación"], "Invertido marca el fin del luto: secarse las lágrimas y cruzar el puente hacia lo nuevo.", "Abraza a quienes siguen contigo y permítete sonreír de nuevo."),

    ("seis-de-copas", "Seis de Copas", "6", "VI", ["Nostalgia dulce", "Inocencia infantil", "Memorias del pasado", "Reencuentro", "Ternura"],
     "Un niño ofrece una copa llena de flores a una niña en el patio de un castillo. La inocencia recuperada, la dulzura de la infancia y recuerdos felices.",
     "El Seis de Copas trae aromas del pasado: viejos amigos que regresan, amores entrañables de juventud, o el reencuentro con la pureza y los sueños de tu niño interior.",
     [{"name": "Copas rebosantes de flores blancas", "desc": "Memorias puras, afecto desinteresado y ternura."}, {"name": "Guardián de espaldas", "desc": "Protección de las memorias sagradas de la niñez."}],
     "Ternura genuina, perdón al pasado, generosidad sin condiciones, dulzura.", "Atrapado en la nostalgia ('cualquier tiempo pasado fue mejor'), infantilismo.",
     "Reencuentro con un amor del pasado; ternura e inocencia compartida en la pareja.", "Retomar vocaciones de la niñez, negocios con amigos de toda la vida.",
     "Sanación del niño interior; recuperar la capacidad de asombro y confianza.", "Agradece tu historia con ternura, pero vive y construye en el presente.", "¿Qué sueño hermoso de tu infancia dejaste olvidado y puedes rescatar hoy?",
     ["Superar la nostalgia", "Madurar", "Dejar ir el pasado"], "Invertido indica soltar la fijación infantil con el pasado y madurar en el presente.", "Honra tus raíces pero enfoca tu energía en lo que estás creando hoy."),

    ("siete-de-copas", "Siete de Copas", "7", "VII", ["Opciones múltiples", "Ilusiones", "Fantasías", "Elección necesaria", "Espejismos"],
     "Una silueta contempla siete copas flotando en una nube, llenas de castillos, joyas, dragones y coronas. Demasiadas fantasías: aterriza tus deseos.",
     "El Siete de Copas advierte de castillos en el aire, dispersión de opciones y tentaciones engañosas. Soñar despierto es hermoso, pero debes elegir una opción real y comprometerte con ella.",
     [{"name": "Siete copas en la nube", "desc": "Deseos, miedos, ambiciones e ilusiones proyectadas."}, {"name": "Figura en sombras", "desc": "Falta de claridad y deslumbramiento ante espejismos."}],
     "Imaginación fértil, capacidad de visualizar múltiples alternativas.", "Parálisis por análisis, autoengaño, caer en estafas o fantasías tóxicas.",
     "Idealizar a personas inalcanzables, no comprometerse por miedo a perder opciones.", "Proyectos dispersos sin base sólida; castillos en el aire sin modelo de negocio.",
     "Discernimiento espiritual: distinguir entre la verdadera guía divina y las trampas del ego.",
     "Deja de fantasear y elige una opción concreta. Pon los pies en el suelo.", "¿Cuál de tus anhelos es una meta real y cuál es una simple fantasía para no actuar?",
     ["Claridad mental", "Elegir un rumbo", "Despertar del autoengaño"], "Invertido anuncia el fin de la confusión: se cae el velo y tomas una decisión lúcida.", "Comprométete con la opción elegida y trabaja en ella con disciplina."),

    ("ocho-de-copas", "Ocho de Copas", "8", "VIII", ["Retirada consciente", "Dejar atrás lo seguro", "Búsqueda de sentido", "Viaje del alma", "Evolución"],
     "Una figura con manto rojo camina de noche apoyada en su cayado, alejándose de ocho copas ordenadas. Partir en busca de algo más profundo.",
     "El Ocho de Copas es el valor de marcharte de situaciones, relaciones o metas que lograste pero ya no llenan tu alma. No huyes por despecho: buscas tu auténtica verdad.",
     [{"name": "Ocho copas en pie dejadas atrás", "desc": "Logros materiales o afectivos que ya cumplieron su ciclo."}, {"name": "Luna y sol eclipsados", "desc": "Momento de profunda transformación de consciencia."}, {"name": "Montañas escarpadas hacia donde va", "desc": "El sendero espiritual exigente pero luminoso."}],
     "Valentía para soltar, honestidad con el propio vacío, búsqueda trascendente.", "Escapismo crónico, huir cada vez que una relación exige compromiso.",
     "Terminar una relación con respeto porque ya no hay crecimiento mutuo.", "Renunciar a un empleo exitoso para seguir una auténtica vocación espiritual.",
     "La peregrinación del alma; soltar los apegos del mundo para encontrar a Dios dentro.", "Si ya no eres feliz allí, ten el valor de marcharte con dignidad.", "¿Qué situación en tu vida sigues sosteniendo solo por costumbre aunque esté vacía?",
     ["Miedo a partir", "Quedarse en lo que daña", "Regreso arrepentido"], "Invertido indica que sabes que debes irte pero el miedo te retiene atado.", "Confía en tus pies. El camino se abrirá en cuanto des el primer paso hacia tu verdad."),

    ("nueve-de-copas", "Nueve de Copas", "9", "IX", ["Satisfacción", "Deseo cumplido", "Placer sensorial", "Contentamiento", "Autocelebración"],
     "Un hombre satisfecho sonríe con los brazos cruzados ante nueve copas doradas. La carta de los deseos concedidos y la abundancia gozada.",
     "El Nueve de Copas anuncia satisfacción plena, disfrute de la buena mesa, bienestar físico y emocional, y la alegría de ver concretado un anhelo íntimo.",
     [{"name": "Nueve copas en semicírculo", "desc": "Deseos cumplidos y copa llena en todas las áreas afectivas."}, {"name": "Hombre plácido y sonriente", "desc": "Paz interior, seguridad emocional y gratitud complaciente."}],
     "Contentamiento sereno, gratitud dichosa, disfrute de la vida y generosidad.", "Autocomplacencia perezosa, hedonismo egoísta, soberbia del satisfecho.",
     "Felicidad afectiva plena, sentirse amado y valorado en la intimidad.", "Éxito profesional cómodo, metas logradas con holgura y buen ambiente.",
     "Celebrar la belleza de la creación a través de los sentidos y la dicha.", "Disfruta de tus bendiciones sin culpa. Has sembrado bien; cosecha y comparte.", "¿Qué deseo concedido tienes en tu vida hoy por el que debas dar gracias?",
     ["Insatisfacción materialista", "Gula o excesos", "Falta de plenitud real"], "Invertido avisa de buscar saciar vacíos espirituales con excesos materiales.", "La verdadera plenitud reside en el alma, no en acumular cosas o halagos."),

    ("diez-de-copas", "Diez de Copas", "10", "X", ["Felicidad familiar", "Paz duradera", "Arcoíris de bendiciones", "Hogar dichoso", "Amor pleno"],
     "Una pareja abrazada contempla un arcoíris de diez copas mientras sus hijos bailan alegres. La dicha hogareña y la plenitud emocional duradera.",
     "El Diez de Copas es la culminación de la felicidad afectiva: armonía en el hogar, amor maduro y correspondido, estabilidad familiar y paz espiritual.",
     [{"name": "Arcoíris de diez copas", "desc": "Pacto cósmico de bendición y dicha duradera."}, {"name": "Pareja abrazada y niños jugando", "desc": "Amor conyugal pleno y futuro asegurado."}, {"name": "Casa junto al río", "desc": "Refugio seguro cimentado en el afecto mutuo."}],
     "Amor incondicional, concordia familiar, paz compartida y estabilidad.", "Falsa imagen de familia perfecta hacia afuera, hipocresía doméstica.",
     "Relación soñada, matrimonio dichoso, armonía profunda y proyectos de vida en común.", "Clima de trabajo cálido como una segunda familia; metas colectivas logradas.",
     "Sintonía con la gracia divina; sentirse en casa en cualquier rincón del universo.", "Cultiva los lazos afectivos de tu hogar. El verdadero tesoro está en el amor que das.", "¿Qué puedes hacer hoy para llenar tu hogar de armonía y palabras cariñosas?",
     ["Conflictos domésticos", "Distanciamiento familiar", "Idealización rota"], "Invertido advierte de roces en la familia o desgaste de la armonía conyugal.", "Prioriza el diálogo amoroso y sana viejos resentimientos en el núcleo familiar."),

    ("sota-de-copas", "Sota de Copas", "Sota", "Sota", ["Mensaje de amor", "Sensibilidad", "Intuición tierna", "Creatividad artística", "Buenas noticias"],
     "Un joven sonriente sostiene una copa de la que asoma un pez curioso. Mensajes tiernos, noticias de amor o nacimiento de una vocación artística.",
     "La Sota de Copas personifica la ternura, la sensibilidad poética y la sorpresa afectiva. Trae mensajes cariñosos, reconciliaciones o el inicio de una propuesta sentida.",
     [{"name": "Pez asomando en la copa", "desc": "La voz de la intuición y el subconsciente que emerge con naturalidad."}, {"name": "Túnica con lirios acuáticos", "desc": "Pureza sentimental y florecimiento del alma."}],
     "Dulzura, empatía, dones intuitivos o artísticos y nobleza de sentimientos.", "Hipersensibilidad infantil, inmadurez emocional, vivir en una burbuja.",
     "Declaración de amor inocente y dulce, propuesta cariñosa, embarazo o nacimiento.", "Inspiración para escribir, pintar o diseñar; propuestas laborales ilusionantes.",
     "Escuchar la voz suave del ángel de la guarda o los presentimientos del alma.", "Exprésate con ternura. No temas mostrar tu vulnerabilidad y tu sensibilidad.", "¿Qué mensaje de cariño estás deseando expresar y te da vergüenza decir?",
     ["Inmadurez afectiva", "Heridas por hipersensibilidad", "Malas noticias"], "Invertida señala decepciones amorosas leves o susceptibilidad exagerada.", "No te tomes todo como un ataque; fortalece tu autoestima sin endurecer el corazón."),

    ("caballo-de-copas", "Caballo de Copas", "Caballo", "Caballo", ["Caballero romántico", "Mensajero del corazón", "Oferta sincera", "Idealismo", "Gracia"],
     "El caballero que avanza al paso tranquilo sobre su caballo blanco, ofreciendo su copa con elegancia. El mensajero del amor sincero y la diplomacia.",
     "El Caballo de Copas es el seductor honorable, el portador de una oferta afectiva o laboral llena de belleza. Actúa con calma, gentileza y elegancia poética.",
     [{"name": "Caballo sereno al paso", "desc": "Acción templada por el afecto y la cortesía."}, {"name": "Alas en el casco y talones (Hermes)", "desc": "Inspiración poética y mediación pacífica."}, {"name": "Copa extendida", "desc": "Ofrenda de amor, paz o colaboración sincera."}],
     "Romanticismo refinado, empatía, diplomacia pacificadora y encanto.", "Donjuán embaucador, promesas poéticas que no se cumplen, capricho.",
     "Llegada de un pretendiente romántico, invitación formal de amor, cortejo clásico.", "Ofertas laborales atractivas con propósito humano o artístico; mediaciones con éxito.",
     "El buscador del Santo Grial; el camino del devoto que sirve con amor.", "Haz tu propuesta con gentileza. La diplomacia y el afecto abrirán todas las puertas.", "¿Cómo puedes aportar mayor poesía, dulzura y belleza a tu vida cotidiana?",
     ["Desengaño con un encantador", "Promesas vacías", "Inestabilidad emocional"], "Invertido advierte de personas que deslumbran con palabras pero huyen del compromiso.", "Pide hechos y no solo hermosas poesías antes de entregar tu confianza."),

    ("reina-de-copas", "Reina de Copas", "Reina", "Reina", ["Madurez emocional", "Compasión infinita", "Intuición profunda", "Escucha sanadora", "Empatía"],
     "La reina sentada al borde del mar contemplando su copa misteriosa con querubines. El santuario del corazón compasivo y la intuición clarividente.",
     "La Reina de Copas es la madre nutricia del alma, la terapeuta nata, la mujer intuitiva y compasiva. Comprende los dolores ajenos y ofrece refugio sin juzgar.",
     [{"name": "Copa cerrada con cruz y querubines", "desc": "Misterios sagrados del corazón y secretos del alma bien custodiados."}, {"name": "Trono decorado con conchas y sirenas", "desc": "Reinado sobre las aguas del subconsciente."}, {"name": "Pies sobre guijarros en el agua", "desc": "Contacto directo con el flujo de las emociones."}],
     "Empatía sanadora, intuición certera, amor incondicional y dulzura sabia.", "Dependencia afectiva asfixiante, chantaje emocional velado, histeria.",
     "Compañera comprensiva y amorosa; relación donde impera la intimidad y la ternura.", "Vocaciones de cuidado, psicología, arte, medicina o mediación social.",
     "Mística natural, clarividencia y conexión directa con las energías sutiles.", "Escucha con el corazón sin juzgar. Tu presencia amorosa es medicina para quienes sufren.", "¿Estás cuidando de tus propias necesidades afectivas al mismo tiempo que cuidas a otros?",
     ["Desborde emocional", "Manipulación con el victimismo", "Frialdad por heridas"], "Invertida señala agotamiento por absorber penas ajenas o manipulación sentimental.", "Pon límites sanos a tu compasión; no puedes salvar a nadie a costa de hundirte."),

    ("rey-de-copas", "Rey de Copas", "Rey", "Rey", ["Equilibrio emocional", "Sabiduría compasiva", "Consejero sereno", "Dominio afectivo", "Tolerancia"],
     "El rey sentado en su trono flotante en medio de aguas turbulentas. Sostiene su copa con calma: el dominio sereno sobre las tormentas del corazón.",
     "El Rey de Copas encarna la inteligencia emocional al más alto nivel. Es el consejero sabio, el padre amoroso y ecuánime que no se deja arrastrar por el pánico ni la ira.",
     [{"name": "Trono flotante en el mar", "desc": "Estabilidad inconmovible en medio de las mareas emocionales."}, {"name": "Pez saltando y barco a vela", "desc": "Convivencia armónica entre el subconsciente y la mente consciente."}, {"name": "Amuleto de pez en el cuello", "desc": "Maestría sobre las profundidades psíquicas."}],
     "Templanza emocional, sabiduría comprensiva, generosidad justa y lealtad.", "Frialdad calculadora, represión destructiva de afectos, cinismo hiriente.",
     "Pareja madura, comprensiva, protectora y leal; apoyo incondicional en crisis.", "Liderazgo diplomático, mediación en conflictos laborales, gestión humana ejemplar.",
     "El guía espiritual compasivo que enseña a navegar las tormentas interiores.", "Mantén la calma en medio del temporal. Responde con sabiduría y no con reactividad.", "¿Cómo puedes liderar tu vida afectiva desde la calma en lugar de la queja?",
     ["Represión de sentimientos", "Inestabilidad encubierta", "Vicios para tapar dolor"], "Invertido indica desconexión con el sentir o desborde emocional mal gestionado.", "Permítete sentir sin temor; la verdadera fuerza nace de aceptar tus emociones.")
]

for c in copas_data:
    cards_list.append(make_card(c[0], c[1], c[2], c[3], "Copas", "Agua", c[4], c[5], c[6], c[7], c[8], c[9], c[10], c[11], c[12], c[13], c[14], c[15], c[16], c[17]))

print(f"Cards after Copas: {len(cards_list)}")

# 3. ESPADAS (14 cards)
espadas_data = [
    ("as-de-espadas", "As de Espadas", "As", "I", ["Claridad mental", "Verdad tajante", "Victoria intelectual", "Nueva idea", "Cirugía liberadora"],
     "Una mano divina sostiene una espada coronada de olivo y palma. La verdad que corta toda ilusión y disipa las nieblas de la duda.",
     "El As de Espadas anuncia un momento de lucidez contundente, una decisión valiente que zanja conflictos y el nacimiento de una idea brillante.",
     [{"name": "Espada erguida", "desc": "La fuerza del intelecto y la justicia implacable."}, {"name": "Corona y ramas de laurel", "desc": "Victoria de la verdad y paz conquistada."}, {"name": "Paisaje montañoso frío", "desc": "Objetividad analítica sin sentimentalismos distorsionadores."}],
     "Mente afilada, discernimiento lúcido, justicia, honestidad y valentía verbal.", "Crueldad verbal, frialdad despiadada, usar la verdad para herir sin compasión.",
     "Conversación honesta y clarificadora que disipa malentendidos en la pareja.", "Resolución brillante de problemas complejos, contratos claros y victorias legales.",
     "La espada del discernimiento que corta las ataduras del engaño del ego.", "Di la verdad con respeto y firmeza. Corta lo que te resta paz mental.", "¿Qué verdad difícil necesitas pronunciar para liberarte de una situación falsa?",
     ["Confusión mental", "Palabras hirientes", "Ideas destructivas"], "Invertido advierte de errores de juicio, discusiones agresivas o engaños intelectuales.", "Revisa tus premisas con calma; no tomes decisiones definitivas con la mente nublada."),

    ("dos-de-espadas", "Dos de Espadas", "2", "II", ["Dilema difícil", "Ojos vendados", "Tregua tensa", "Bloqueo mental", "Decisión postergada"],
     "Una mujer con los ojos vendados sostiene dos pesadas espadas cruzadas ante el mar. Negarse a ver la realidad para postergar una elección dolorosa.",
     "El Dos de Espadas señala un callejón sin salida mental. Estás atrapado entre dos alternativas y prefieres cruzarte de brazos antes que decidir. La venda no te protege: solo alarga la angustia.",
     [{"name": "Venda en los ojos", "desc": "Negación voluntaria de los hechos para no sufrir."}, {"name": "Espadas en equilibrio sobre el pecho", "desc": "Conflicto interno que bloquea el corazón."}, {"name": "Mar con rocas y luna creciente", "desc": "Mareas emocionales contenidas a duras penas."}],
     "Capacidad de sopesar opciones con calma, buscar tregua en conflictos.", "Parálisis por cobardía, ignorar problemas graves hasta que explotan.",
     "Indecisión en el amor, no querer admitir incompatibilidades evidentes.", "Bloqueo ante dos ofertas laborales, postergación de decisiones clave.",
     "Superar la ilusión de la mente dual; reconciliar polaridades internas.", "Quítate la venda. Mira los hechos de frente y decide con valentía.", "¿Qué verdad evidente estás fingiendo no ver por miedo al dolor que causará?",
     ["Fin de la tregua", "Verdad inevitable", "Tomar la decisión demorada"], "Invertido indica que la venda se cae y te ves obligado a decidir sin más dilación.", "Afronta la decisión con coraje; cualquier opción firme es mejor que la parálisis."),

    ("tres-de-espadas", "Tres de Espadas", "3", "III", ["Dolor del corazón", "Desamor", "Traición", "Verdad dolorosa", "Sanación necesaria"],
     "Un corazón atravesado por tres espadas bajo nubes de lluvia y truenos. El dolor de una ruptura, una traición o una verdad amarga que quiebra ilusiones.",
     "El Tres de Espadas acompaña los momentos de pena profunda y desengaño. Aunque duele, las espadas limpian heridas ocultas: solo lo que se rompe puede sanar desde la verdad.",
     [{"name": "Corazón perforado", "desc": "Pena profunda, tristeza y duelo emocional."}, {"name": "Tres espadas cruzadas", "desc": "Pensamientos dolorosos, palabras hirientes y traición."}, {"name": "Lluvia y nubes de tormenta", "desc": "Catarsis necesaria para lavar el dolor del alma."}],
     "Sanación a través del desahogo, aprender de las decepciones, resiliencia.", "Rumiar amargura eterna, autocompasión destructiva, rencor enquistado.",
     "Ruptura sentimental, infidelidad o palabras que hieren profundamente.", "Disolución dolorosa de sociedades, despidos o traición de socios.",
     "La herida sagrada del corazón que abre paso a una empatía más profunda.", "Permítete llorar y desahogar tu pena. La tormenta pasará y tu corazón sanará más sabio.", "¿A qué dolor del pasado te sigues aferrando mediante el rencor?",
     ["Superación del dolor", "Cicatrización", "Perdón liberador"], "Invertido anuncia el inicio del alivio: las espadas se retiran y la herida comienza a cerrar.", "Perdona para liberarte a ti mismo, no por el otro. Abre tu corazón de nuevo."),

    ("cuatro-de-espadas", "Cuatro de Espadas", "4", "IV", ["Descanso necesario", "Recuperación", "Meditación", "Retiro", "Tregua mental"],
     "La efigie del caballero descansa sobre su tumba con las manos en oración mientras tres espadas cuelgan arriba y una a su lado. Alto en la batalla.",
     "El Cuatro de Espadas te exige un alto el fuego mental. Tu cuerpo y tu mente están exhaustos. No tomes decisiones ahora: descansa, medita y recupera fuerzas en el santuario de la calma.",
     [{"name": "Figura en reposo sobre el sarcófago", "desc": "Descanso sagrado, recarga física y psicológica indispensable."}, {"name": "Tres espadas en el muro y una debajo", "desc": "Los conflictos quedan en suspenso mientras se preserva una herramienta."}, {"name": "Vidriera con bendición", "desc": "Paz espiritual y refugio divino en la quietud."}],
     "Paz mental, recuperación de salud, meditación profunda y serenidad.", "Apatía estéril, aislamiento enfermizo, huir de los deberes por pereza.",
     "Darse un tiempo de respiro en la relación para bajar tensiones y pensar con calma.", "Tomar vacaciones indispensables, desconectar de correos y estrés laboral.",
     "Silencio contemplativo, retiro espiritual y reposición de la energía áurica.", "Para. No sigas forzando la máquina. Duerme, desconéctate y recarga tu espíritu.", "¿Qué área de tu vida te está pidiendo a gritos una tregua y un descanso reparador?",
     ["Fin del descanso", "Regreso a la batalla", "Insomnio por estrés"], "Invertido indica el regreso paulatino a la actividad tras la convalecencia, o insomnio.", "Vuelve al ruedo con calma; no eches a perder la recuperación acelerándote de golpe."),

    ("cinco-de-espadas", "Cinco de Espadas", "5", "V", ["Victoria pírrica", "Derrota moral", "Conflicto mezquino", "Orgullo dañino", "Retirada sabia"],
     "Un hombre sonríe con suficiencia recogiendo tres espadas ajenas mientras dos figuras derrotadas se alejan llorando. Ganar la batalla perdiendo la guerra.",
     "El Cinco de Espadas advierte de discusiones tóxicas donde querer ganar a toda costa deja un campo arrasado de resentimiento. Si para vencer debes destruir al otro, tu triunfo es una farsa amarga.",
     [{"name": "Hombre con sonrisa burlona", "desc": "La victoria mezquina del ego que saborea el dolor ajeno."}, {"name": "Dos figuras cabizbajas al fondo", "desc": "Amargura, traición y ruptura de la confianza mutua."}, {"name": "Cielo con nubes desgarradas", "desc": "Ambiente tenso y hostil tras la pelea."}],
     "Saber cuándo retirarse de una discusión destructiva; proteger la propia dignidad.", "Hostilidad, cinismo, traición, abusar del poder para aplastar a otros.",
     "Peleas hirientes de pareja donde se dicen cosas irreparables por soberbia.", "Ambiente de trabajo tóxico, zancadillas laborales, competencia desleal.",
     "Comprender la inutilidad de alimentar el ego combativo; trascender la venganza.", "Elige la paz antes que tener la razón. Retírate antes de causar heridas imborrables.", "¿Estás dispuesto a destruir un vínculo valioso solo por el capricho de tener la última palabra?",
     ["Deseo de reconciliación", "Reconocer el daño causado", "Fin de la hostilidad"], "Invertido refleja arrepentimiento por haber actuado con saña o ganas de firmar la paz.", "Pide disculpas con humildad y repara los daños morales cometidos."),

    ("seis-de-espadas", "Seis de Espadas", "6", "VI", ["Transición necesaria", "Aguas más calmas", "Viaje de sanación", "Dejar atrás la tormenta", "Esperanza sobria"],
     "Un barquero traslada a una madre y su hijo encapuchados hacia una orilla serena, llevando seis espadas clavadas en la barca. Marchar hacia la paz.",
     "El Seis de Espadas anuncia un viaje de transición: dejas atrás una etapa turbulenta y navegas hacia aguas tranquilas. Aunque llevas la memoria de lo sufrido, el horizonte es seguro y sanador.",
     [{"name": "Barquero remando", "desc": "Guía segura y esfuerzo constante hacia la estabilidad."}, {"name": "Agua rizada a la derecha y calma a la izquierda", "desc": "Transición de la crisis a la serenidad mental."}, {"name": "Seis espadas clavadas en la madera", "desc": "Los problemas se trasladan pero ya no hieren."}],
     "Superación de crisis, mudanzas favorables, recuperación gradual de la paz.", "Llevar el rencor a la nueva etapa, resistencia a soltar el drama del pasado.",
     "Superar una crisis de pareja viajando juntos; mudanza conjunta hacia la calma.", "Cambio de empleo o área laboral hacia un entorno mucho más saludable.",
     "Sanación psicológica paulatina; el alma que emerge de la tempestad interior.", "Sigue remando. La orilla de la paz está cerca; no mires atrás con pesar.", "¿Qué peso emocional del pasado estás cargando en tu barca que puedes soltar?",
     ["Viaje accidentado", "Regreso al conflicto", "Atascado en la crisis"], "Invertido advierte de dificultades en el traslado o negarse a dejar ir el problema.", "Confía en el proceso de cambio y acepta la ayuda de quienes saben guiarte."),

    ("siete-de-espadas", "Siete de Espadas", "7", "VII", ["Estrategia furtiva", "Engaño", "Plan secreto", "Astucia", "Fuga de responsabilidades"],
     "Un hombre se aleja de puntillas de un campamento militar llevándose cinco espadas y mirando atrás, dejando dos clavadas. Astucia o traición.",
     "El Siete de Espadas advierte de engaños, maniobras ocultas o la necesidad de actuar con sigilo e inteligencia estratégica en lugar de chocar de frente. Cuidado con no traicionar tus propios principios.",
     [{"name": "Ladrón de puntillas", "desc": "Acción clandestina, astucia o deshonestidad."}, {"name": "Mirada furtiva hacia atrás", "desc": "Miedo a ser descubierto o remordimiento de conciencia."}, {"name": "Dos espadas abandonadas", "desc": "Planes incompletos o dejar cabos sueltos comprometedores."}],
     "Inteligencia táctica, evitar confrontaciones directas inútiles, discreción prudente.", "Mentiras, robo intelectual, infidelidad, hipocresía y cobardía moral.",
     "Secretos en la pareja, mentiras piadosas que crecen, falta de transparencia.", "Proteger secretos industriales, espionaje corporativo o socios que ocultan cuentas.",
     "Autoengaño sutil: justificar acciones cuestionables con excusas espirituales.", "Actúa con inteligencia pero sin perder tu integridad. Las mentiras siempre salen a la luz.", "¿Estás intentando tomar un atajo deshonesto para evitar una confrontación necesaria?",
     ["Mentiras descubiertas", "Confesión honesta", "Arrepentimiento"], "Invertido indica que los secretos salen a la luz pública o decides confesar la verdad.", "Sé valiente y di la verdad. Es preferible pasar la vergüenza que vivir con el temor a ser descubierto."),

    ("ocho-de-espadas", "Ocho de Espadas", "8", "VIII", ["Prisión mental", "Victimismo", "Limitaciones autoimpuestas", "Parálisis", "Salida disponible"],
     "Una mujer atada y con los ojos vendados rodeada por ocho espadas en el fango. Sus ataduras están flojas y el camino detrás de ella está libre: la cárcel es mental.",
     "El Ocho de Espadas revela que la mayor trampa en la que estás atrapado son tus propios pensamientos limitantes y miedos. No eres una víctima impotente: si das un paso atrás y te quitas la venda, eres libre.",
     [{"name": "Cuerdas flojas en el cuerpo", "desc": "La sumisión y el bloqueo son más mentales que reales."}, {"name": "Espadas rodeándola sin tocarla", "desc": "Miedos y mandatos que asustan pero no tienen poder físico."}, {"name": "Agua en los pies", "desc": "Emociones de culpa e impotencia que nublan el juicio."}],
     "Toma de consciencia del propio autoengaño; primer paso hacia la liberación.", "Victimismo crónico, culpar siempre a los demás, resignación cobarde.",
     "Sentirse atrapado en una relación por miedo a la soledad o chantaje moral.", "Creer que no tienes opciones laborales; miedo paralizante a buscar alternativas.",
     "Desmantelar las creencias limitantes del ego que encarcelan el alma.", "Quítate la venda. Tienes el poder de liberarte en cuanto dejes de creerte tus excusas.", "¿Qué creencia sobre tu propia impotencia te está impidiendo dar el paso hacia la libertad?",
     ["Liberación de la trampa", "Apertura de ojos", "Recuperar el poder personal"], "Invertido anuncia el despertar: comienzas a soltarte las cuerdas y a caminar hacia la salida.", "Cree en tu fuerza. Da ese primer paso y verás cómo los barrotes imaginarios caen."),

    ("nueve-de-espadas", "Nueve de Espadas", "9", "IX", ["Ansiedad", "Insomnio", "Pesadillas", "Culpa lacerante", "Tormento mental"],
     "Una persona sentada en su cama en plena noche con el rostro oculto entre las manos mientras nueve espadas cuelgan en la pared oscura. La pesadilla de la mente.",
     "El Nueve de Espadas representa la angustia, el insomnio y la desesperación provocada por la mente hiperactiva. El 90% de lo que temes solo vive en tu imaginación torturada. La noche no dura para siempre: enciende la luz.",
     [{"name": "Persona llorando en la cama", "desc": "Angustia nocturna, culpa y sensación de soledad abrumadora."}, {"name": "Nueve espadas en la pared", "desc": "Pensamientos repetitivos y catastróficos que hieren la psique."}, {"name": "Colcha con rosas y símbolos astrológicos", "desc": "La vida y la belleza siguen existiendo fuera del dolor mental."}],
     "Tocar fondo para buscar ayuda psicológica, catarsis profunda que libera el dolor.", "Paranoia obsesiva, ataques de pánico, autoflagelación mental destructiva.",
     "Miedos infundados de infidelidad, celos neuróticos, angustia por perder al ser amado.", "Estrés laboral crónico, pánico a la quiebra o al despido, agotamiento mental.",
     "Enfrentar la noche oscura del alma; entregar el sufrimiento a una fuerza superior.", "Respira. La mente asustada exagera todo en la oscuridad. Habla con alguien y enciende la luz.", "¿Qué pensamiento catastrófico te está quitando el sueño y qué pruebas reales tienes de él?",
     ["Superación de la pesadilla", "Alivio de la ansiedad", "Buscar apoyo profesional"], "Invertido indica que el pánico comienza a ceder y la cordura regresa con el alba.", "Comparte tu angustia con un profesional o amigo de confianza; la soledad agranda los monstruos."),

    ("diez-de-espadas", "Diez de Espadas", "10", "X", ["Final inevitable", "Tocar fondo", "Traición consumada", "Nuevo amanecer", "Fin del sufrimiento"],
     "Un hombre yace en el suelo atravesado por diez espadas, pero en el horizonte el cielo negro comienza a dar paso a la luz dorada del sol. Lo peor ya pasó.",
     "El Diez de Espadas marca el final dramático y definitivo de una situación dolorosa. Has tocado fondo absoluto: ya no hay más espadas que clavar. A partir de ahora, todo es ascenso y reconstrucción sobre la verdad.",
     [{"name": "Diez espadas a lo largo de la columna", "desc": "Cierre total y drástico; el ciclo mental ha muerto definitivamente."}, {"name": "Manto rojo bajo el cuerpo", "desc": "La dignidad y la vida que permanecen a pesar del golpe."}, {"name": "Amanecer dorado en el mar lejano", "desc": "La certeza ineludible de que la noche oscura ha concluido."}],
     "Liberación tras tocar fondo; ya no hay nada que temer porque todo se reveló.", "Dramatismo exagerado, regodearse en la condición de víctima, rencor eterno.",
     "Ruptura sentimental definitiva y dolorosa; se acaba la agonía de la incertidumbre.", "Cierre o quiebra definitiva de un proyecto; momento de hacer borrón y cuenta nueva.",
     "Muerte definitiva de una vieja estructura del ego; renacimiento del alma purificada.", "Acepta que terminó. No intentes revivir lo que murió; levántate y mira el nuevo amanecer.", "¿Estás listo para dejar de hablar de tus heridas y empezar a construir tu nueva vida?",
     ["Renacer de las cenizas", "Alivio inmenso", "Recuperación de la esperanza"], "Invertido anuncia el inicio del renacimiento: comienzas a levantarte del suelo con alivio.", "El dolor ya cumplió su función. Sacúdete el polvo y camina hacia la luz dorada."),

    ("sota-de-espadas", "Sota de Espadas", "Sota", "Sota", ["Curiosidad analítica", "Vigilancia", "Mente despierta", "Espionaje digital", "Verdad rebelde"],
     "Un joven alerta empuña su espada en lo alto de una colina azotada por el viento, mirando por encima del hombro. Vigilancia, curiosidad y mente afilada.",
     "La Sota de Espadas personifica al observador perspicaz, el investigador o el mensajero de verdades incómodas. Mentalmente rápido pero susceptible y a veces chismoso.",
     [{"name": "Espada sostenida a dos manos", "desc": "Preparación constante para defender su punto de vista con rapidez."}, {"name": "Nubes revueltas y pájaros volando", "desc": "Mente ágil pero agitada por ráfagas de ideas y rumores."}],
     "Mente brillante, curiosidad investigadora, valentía para decir la verdad.", "Chismorreo, espiar redes sociales de otros, cinismo juvenil y agresividad verbal.",
     "Curiosidad coqueta, conversaciones intelectuales intensas; peligro de celos y vigilancia.", "Investigación minuciosa de mercado, auditorías rápidas, contratos que se analizan con lupa.",
     "El cuestionamiento filosófico de dogmas; la espada del libre pensamiento.", "Sé observador y prudente. Usa tu inteligencia para aprender y no para vigilar o herir a otros.", "¿Estás usando tu intelecto para construir o para criticar y espiar a los demás?",
     ["Chismes destructivos", "Espionaje descubierto", "Agresividad verbal"], "Invertida advierte de palabras hirientes soltadas sin pensar o ser descubierto espiando.", "Mide tus palabras. El sarcasmo y la ironía constante solo alejan a quienes te aprecian."),

    ("caballo-de-espadas", "Caballo de Espadas", "Caballo", "Caballo", ["Impulso intelectual", "Ataque rápido", "Directo al grano", "Valentía implacable", "Fanatismo"],
     "El caballero galopa a toda velocidad con su espada en ristre contra el viento huracanado. Valentía fulgurante, ideas tajantes y avance sin titubeos.",
     "El Caballo de Espadas se lanza a la batalla con determinación implacable para defender una verdad o resolver una crisis. Es rápido, directo y brillante, pero puede ser insensible y atropellar a quienes ama.",
     [{"name": "Caballo al galope desenfrenado", "desc": "Fuerza mental arrolladora que no admite demoras."}, {"name": "Espada apuntando al frente", "desc": "Enfoque implacable en el objetivo intelectual."}],
     "Rapidez resolutiva admirable, coraje para enfrentar injusticias, elocuencia brillante.", "Crueldad implacable, fanatismo ciego, arrasar sentimientos ajenos sin piedad.",
     "Discusiones intensas y acaloradas; declaraciones de intenciones sin anestesia.", "Resolución exprés de crisis empresariales, auditorías feroces, victorias legales rápidas.",
     "El guerrero de la verdad que desmantela supersticiones con la espada de la razón.", "Actúa con prontitud y decisión, pero no olvides que enfrente tienes seres humanos con corazón.", "¿Estás atropellando a los demás en tu prisa por imponer tu punto de vista?",
     ["Fracaso por precipitación", "Violencia verbal", "Fanatismo derrotado"], "Invertido avisa de choques frontales por arrogancia o argumentos fallidos por exceso de prisa.", "Frena la lengua. Escucha los argumentos contrarios antes de lanzarte al ataque."),

    ("reina-de-espadas", "Reina de Espadas", "Reina", "Reina", ["Claridad implacable", "Objetividad", "Independencia", "Discernimiento", "Límites claros"],
     "La soberana del aire sentada en su trono de querubines y mariposas extiende su mano izquierda y alza la espada recta. La verdad sin máscaras ni sensiblerías.",
     "La Reina de Espadas es la mente lúcida que ha sufrido desengaños pero ha salido fortalecida con sabiduría. No tolera mentiras, valora la honestidad por encima de todo y pone límites precisos.",
     [{"name": "Espada vertical inquebrantable", "desc": "Juicio objetivo y defensa de la justicia sin dobleces."}, {"name": "Mano extendida", "desc": "Apertura a la verdad y disposición a dialogar con franqueza."}, {"name": "Manto con nubes y querubín en el trono", "desc": "Dominio de las alturas intelectuales y claridad aérea."}],
     "Discernimiento magistral, honestidad intachable, independencia personal y dignidad.", "Amargura defensiva, frialdad glacial, cinismo castrador y juicio implacable.",
     "Relación basada en la verdad madura y el respeto; no soporta engaños ni infantilismos.", "Jueza justa, abogada brillante, editora o crítica lúcida con criterio impecable.",
     "La purificación de la mente mediante la verdad despojada de autoengaños.", "Sé claro y directo. Pon límites con respeto y no permitas que nadie manipule tu criterio.", "¿Qué límite claro necesitas marcar hoy para proteger tu dignidad y paz mental?",
     ["Frialdad castradora", "Rencor por heridas pasadas", "Aislamiento cínico"], "Invertida advierte de usar el dolor del pasado como coraza para herir a los inocentes.", "Baja la espada un momento; no todos quieren engañarte. Permite que el afecto te ablande."),

    ("rey-de-espadas", "Rey de Espadas", "Rey", "Rey", ["Autoridad intelectual", "Justicia y ley", "Lógica superior", "Ética intachable", "Mando analítico"],
     "El gran magistrado sentado en su trono con la espada ligeramente inclinada. El dominio de la ley, la ética moral, el intelecto superior y el juicio equitativo.",
     "El Rey de Espadas encarna la máxima autoridad ética y racional. Es el juez justo, el estratega brillante y el asesor de confianza que decide con base en pruebas, normas y principios universales.",
     [{"name": "Espada sostenida con aplomo", "desc": "El poder de dictar sentencia con justicia y firmeza."}, {"name": "Mariposas y ángeles en el trono", "desc": "Mente superior orientada a la verdad y la transformación."}, {"name": "Manto púrpura y túnica roja", "desc": "Sabiduría y poder terrenal al servicio de la justicia."}],
     "Imparcialidad ejemplar, lógica impecable, rectitud moral, sabiduría jurídica.", "Tiranía intelectual, crueldad legalista, falta total de empatía y dogmatismo frío.",
     "Relación basada en el respeto intelectual y el compromiso formal; pocas muestras de emoción.", "Asesoría legal exitosa, cargos de alta dirección, resolución justa de litigios.",
     "Comprensión de las leyes cósmicas que rigen el orden del universo y la mente.", "Decide con la cabeza fría. Apóyate en los hechos y mantén tu integridad inalterable.", "¿Estás juzgando la situación con objetividad o dejando que los prejuicios te nublen?",
     ["Injusticia autoritaria", "Abuso de la ley", "Frialdad cruel"], "Invertido señala corrupción moral, uso manipulador de las normas o juicios injustos.", "Reconcilia la razón con el corazón; la justicia sin compasión se convierte en crueldad.")
]

for e in espadas_data:
    cards_list.append(make_card(e[0], e[1], e[2], e[3], "Espadas", "Aire", e[4], e[5], e[6], e[7], e[8], e[9], e[10], e[11], e[12], e[13], e[14], e[15], e[16], e[17]))

print(f"Cards after Espadas: {len(cards_list)}")

# 4. OROS / PENTÁCULOS (14 cards)
oros_data = [
    ("as-de-oros", "As de Oros", "As", "I", ["Prosperidad tangible", "Nueva oportunidad financiera", "Semilla de riqueza", "Salud sólida", "Manifestación"],
     "Una mano divina ofrece un gran pentáculo dorado sobre un jardín exuberante con arco de rosas. La semilla de la abundancia material y el éxito práctico.",
     "El As de Oros anuncia una oportunidad económica inmejorable: un nuevo empleo, una inversión rentable, un regalo valioso o la base para un negocio próspero.",
     [{"name": "Mano con moneda de oro", "desc": "Don divino de prosperidad terrenal y bendición material."}, {"name": "Jardín con lirios y rosas", "desc": "Tierra fértil lista para hacer germinar cualquier proyecto."}, {"name": "Arco floral hacia las montañas", "desc": "Camino abierto hacia la solidez y la riqueza perdurable."}],
     "Pragmatismo fértil, salud física radiante, estabilidad económica y visión práctica.", "Avaricia prematura, materialismo ciego, no valorar lo espiritual.",
     "Relación sólida, segura y con planes prácticos de futuro; estabilidad compartida.", "Comienzo de un negocio muy rentable, subida de sueldo, firma de contratos jugosos.",
     "Comprender la materia y el cuerpo como templos sagrados de la divinidad.", "Aprovecha la oportunidad práctica que se te presenta. Siembra con esmero.", "¿Qué oportunidad concreta tienes frente a ti para mejorar tu economía y tu salud?",
     ["Oportunidad perdida", "Gasto imprevisto", "Materialismo insaciable"], "Invertido indica retraso en pagos o dejar pasar una buena oferta por miedo a arriesgar.", "Cuida tus finanzas y no derroches en caprichos superfluos; asegura tus ahorros."),

    ("dos-de-oros", "Dos de Oros", "2", "II", ["Equilibrio dinámico", "Malabares financieros", "Adaptabilidad", "Prioridades múltiples", "Flexibilidad"],
     "Un joven baila haciendo malabares con dos grandes pentáculos unidos por una cinta de infinito mientras barcos navegan olas gigantes. Fluidez en el cambio.",
     "El Dos de Oros te invita a mantener la flexibilidad y el buen humor mientras gestionas múltiples responsabilidades, presupuestos o proyectos a la vez. No te agobies: fluye con el vaivén.",
     [{"name": "Cinta de infinito (Lemniscata)", "desc": "Capacidad infinita de adaptación a las fluctuaciones de la vida."}, {"name": "Barcos navegando olas altas", "desc": "Altibajos de la economía y la vida cotidiana gestionados con destreza."}, {"name": "Paso de danza del malabarista", "desc": "Levedad y alegría ante la complejidad del día a día."}],
     "Adaptabilidad brillante, ingenio para hacer rendir los recursos, buen humor.", "Desorganización financiera, estrés por sobrecarga de tareas, deudas por descuido.",
     "Equilibrar el tiempo de pareja con el trabajo; juegos y dinamismo compartido.", "Hacer malabares con dos empleos o clientes; versatilidad y rapidez para diversificar ingresos.",
     "Aprender a danzar con los ritmos cambiantes del cosmos sin apegarse a la rigidez.", "Sé flexible como el junco. Organiza tus prioridades y tómate las dificultades con deportividad.", "¿Estás intentando abarcar demasiado a la vez descuidando lo verdaderamente importante?",
     ["Descontrol financiero", "Colapso por estrés", "Pérdida del equilibrio"], "Invertido avisa de cheques que rebotan, deudas descontroladas o desorden en la agenda.", "Simplifica tu vida. Reduce compromisos y atiende un asunto a la vez hasta estabilizarte."),

    ("tres-de-oros", "Tres de Oros", "3", "III", ["Trabajo en equipo", "Maestría técnica", "Reconocimiento profesional", "Colaboración", "Construcción sólida"],
     "Un joven escultor trabaja en los arcos de una catedral consultando los planos con un monje y un arquitecto. El éxito de la maestría colaborativa.",
     "El Tres de Oros celebra el trabajo bien hecho, la profesionalidad y la sinergia entre talentos complementarios. Tus habilidades técnicas son reconocidas y recompensadas con nuevos encargos.",
     [{"name": "Tres pentáculos tallados en el arco", "desc": "La obra maestra construida con dedicación y excelencia."}, {"name": "Planos en pergamino", "desc": "Diseño inteligente, método riguroso y planificación experta."}, {"name": "Monje y arquitecto consultando", "desc": "Respeto mutuo y sinergia entre visión teórica y habilidad práctica."}],
     "Excelencia profesional, trabajo en equipo impecable, aprendizaje con maestros.", "Soberbia del artesano, negarse a escuchar críticas constructivas, chapuzas.",
     "Construir bases sólidas en la pareja con paciencia y comunicación cotidiana.", "Éxito en proyectos multidisciplinarios, ascensos por méritos técnicos, encargos importantes.",
     "La consagración del trabajo diario como servicio sagrado a la belleza cósmica.", "Une tus talentos a los de otros. Escucha la opinión de los expertos y pule tu obra con amor.", "¿Qué habilidad necesitas seguir perfeccionando para alcanzar la maestría en tu área?",
     ["Falta de coordinación en equipo", "Trabajo mediocre", "Críticas merecidas"], "Invertido señala problemas de comunicación en el equipo o proyectos mal ejecutados.", "Sé humilde para aprender de tus errores y busca coordinarte mejor con tus colegas."),

    ("cuatro-de-oros", "Cuatro de Oros", "4", "IV", ["Apego material", "Avaricia", "Seguridad rígida", "Miedo a la escasez", "Control"],
     "Un hombre sentado abraza con fuerza un pentáculo en el pecho, dos bajo sus pies y uno sobre la corona, inmóvil en su ciudadela. Avaricia y miedo a perder.",
     "El Cuatro de Oros advierte de una obsesión por la seguridad económica que te paraliza. Aferrarte al dinero, a las personas o a tus ideas por miedo a la escasez bloquea el flujo natural de la abundancia.",
     [{"name": "Pentáculos bajo los pies, pecho y cabeza", "desc": "Bloqueo total del movimiento, del corazón y de la mente por el apego."}, {"name": "Ciudad a la espalda", "desc": "Aislamiento voluntario dentro de las murallas del propio egoísmo."}],
     "Prudencia financiera, ahorro metódico, protección legítima de los bienes.", "Avaricia enfermiza, tacañería afectiva, celos posesivos y miedo neurótico a gastar.",
     "Posesividad, celos asfixiantes, tratar a la pareja como si fuera una propiedad privada.", "Acumular capital sin invertirlo por temor, estancamiento de negocios por tacañería.",
     "Comprender que la energía divina es circulación constante; soltar el miedo a la carencia.", "Abre las manos. Quien retiene con pánico no puede recibir nada nuevo. Comparte con generosidad.", "¿A qué posesión, dinero o relación te estás aferrando con miedo desesperado a perderlo?",
     ["Apertura a compartir", "Gasto liberador", "Quiebra por rigidez"], "Invertido indica empezar a soltar el control y compartir, o pérdidas por terquedad.", "Aprende a fluir con el dinero: gástalo con prudencia pero sin angustia de carencia."),

    ("cinco-de-oros", "Cinco de Oros", "5", "V", ["Dificultad material", "Sensación de exclusión", "Frío y pobreza", "Refugio cercano", "Prueba de fe"],
     "Dos mendigos heridos caminan en la nieve bajo una tormenta, sin ver la vidriera iluminada y cálida del templo arriba. La ayuda está a tu lado: búscala.",
     "El Cinco de Oros acompaña periodos de aprieto financiero, sensación de soledad o rechazo social. Lo más importante es que hay un santuario cálido justo a tu lado: no te encierres en tu orgullo y pide auxilio.",
     [{"name": "Vidriera iluminada del templo con cinco pentáculos", "desc": "Refugio espiritual y ayuda material disponible a pocos pasos."}, {"name": "Mendigo con muletas y campana", "desc": "Heridas visibles y sensación de aislamiento o marginación."}, {"name": "Nieve fría", "desc": "Adversidad temporal que pone a prueba la humildad y la fraternidad."}],
     "Humildad profunda, solidaridad entre quienes sufren, resiliencia ante la escasez.", "Victimismo desesperado, orgullo que impide pedir ayuda, autocompasión amarga.",
     "Apoyarse mutuamente en vacas flacas; o sentirse abandonado emocionalmente por la pareja.", "Pérdidas económicas temporales, desempleo; momento de recurrir a la red de apoyo.",
     "La prueba de la indigencia del ego: descubrir que el verdadero tesoro es interior.", "No te quedes en el frío de tu orgullo. Llama a la puerta del templo; la ayuda te espera.", "¿Qué ayuda o consuelo tienes disponible a tu alcance que te niegas a pedir por vergüenza?",
     ["Superación de la crisis", "Llegada de auxilio", "Fin de la escasez"], "Invertido anuncia la salida del bache: encuentras trabajo, recibes apoyo y recuperas calor.", "Agradece la ayuda recibida y recuerda con compasión a quienes siguen en el frío."),

    ("seis-de-oros", "Seis de Oros", "6", "VI", ["Generosidad", "Dar y recibir", "Caridad justa", "Equilibrio financiero", "Mecenazgo"],
     "Un mercader próspero sostiene una balanza con una mano mientras reparte monedas con la otra a dos personas humildes. La economía sagrada de la reciprocidad.",
     "El Seis de Oros representa la circulación justa de la abundancia: ayudas recibidas en el momento oportuno, mecenazgo, aumentos de sueldo justos o el don de compartir con quien lo necesita.",
     [{"name": "Balanza en equilibrio", "desc": "Justicia distributiva y discernimiento al otorgar recursos."}, {"name": "Monedas entregadas con la mano derecha", "desc": "Generosidad activa y bendición material compartida."}],
     "Generosidad noble, filantropía, solvencia para ayudar, gratitud al recibir.", "Condescendencia soberbia, dar para humillar o crear dependencias, clientelismo.",
     "Equilibrio de afectos y cuidados en la pareja; apoyo mutuo en momentos clave.", "Créditos concedidos en excelentes condiciones, becas, subidas de sueldo merecidas.",
     "La ley cósmica del diezmo y la circulación: cuanto más das de corazón, más recibes.", "Comparte con generosidad si tienes abundancia; y si necesitas ayuda, recíbela con dignidad.", "¿Estás en este momento en posición de dar con nobleza o de recibir con humildad?",
     ["Deudas impagadas", "Egoísmo", "Caridad humillante o interesada"], "Invertido advierte de préstamos no devueltos, favores con trampa o tacañería encubierta.", "Sé claro en los acuerdos económicos con amigos o familiares para evitar resentimientos."),

    ("siete-de-oros", "Siete de Oros", "7", "VII", ["Paciencia", "Evaluación de la cosecha", "Crecimiento lento pero seguro", "Inversión a largo plazo", "Frutos en camino"],
     "Un campesino apoyado en su azadón contempla pensativo las siete monedas que crecen en su vid. El fruto está madurando: ten paciencia y no arranques la planta.",
     "El Siete de Oros te pide paciencia y evaluación serena. Has sembrado con esfuerzo y los resultados van por buen camino, pero no puedes acelerar la naturaleza. Evalúa si debes ajustar algo y dale tiempo al fruto.",
     [{"name": "Hombre apoyado en el azadón", "desc": "Pausa reflexiva tras una intensa jornada de trabajo."}, {"name": "Vid con siete pentáculos", "desc": "Inversión que fructifica de forma orgánica y progresiva."}, {"name": "Moneda en el suelo", "desc": "Recompensa inmediata ya asegurada mientras madura el resto."}],
     "Paciencia sabia, perseverancia constante, visión a largo plazo, madurez agrícola.", "Impaciencia destructiva, desánimo porque las cosas tardan, abandonar antes de cosechar.",
     "Relación que madura paso a paso; evaluar con calma hacia dónde va el vínculo.", "Inversiones a medio plazo, proyectos que requieren constancia y no desesperación.",
     "Comprender los tiempos del alma; no se puede forzar el florecimiento de la flor.", "No te impacientes. Tu cosecha va bien; sigue cuidando la tierra y confía en el tiempo.", "¿Estás a punto de tirar la toalla en un proyecto valioso solo porque tarda en dar frutos?",
     ["Frustración por retrasos", "Mala inversión", "Cosecha descuidada"], "Invertido avisa de impaciencia que arruina cosechas o de insistir en proyectos estériles.", "Evalúa con frialdad si vale la pena seguir regando esa planta o si es mejor cambiar de cultivo."),

    ("ocho-de-oros", "Ocho de Oros", "8", "VIII", ["Dedicación", "Artesanía minuciosa", "Aprendizaje enfocado", "Perfeccionamiento", "Pasión por el oficio"],
     "Un artesano trabaja concentrado en su banco tallando pentáculos uno a uno, colgando los terminados en el poste. El amor por el detalle y la mejora continua.",
     "El Ocho de Oros representa la dedicación apasionada al perfeccionamiento de tu oficio. Sin atajos ni prisas: maestría adquirida mediante la práctica constante y el amor por los detalles.",
     [{"name": "Artesano con martillo y cincel", "desc": "Concentración total y trabajo disciplinado con las propias manos."}, {"name": "Siete pentáculos expuestos y uno en faena", "desc": "Progreso visible y compromiso con la excelencia paso a paso."}, {"name": "Pueblo lejano", "desc": "Aislamiento temporal fecundo para concentrarse en la obra."}],
     "Ética de trabajo ejemplar, disciplina constructiva, amor por el oficio, perfeccionamiento.", "Perfeccionismo neurótico, adicción al trabajo, descuidar la vida afectiva por el detalle.",
     "Construir la relación en los pequeños gestos diarios de cuidado y atención mutua.", "Cursos de especialización técnica, trabajo de orfebrería, programación o diseño de alta calidad.",
     "El trabajo como meditación activa (Karma Yoga); santificar la tarea cotidiana.", "Pon tu mente y tu corazón en lo que haces. La constancia diaria te convertirá en maestro.", "¿En qué habilidad estás dispuesto a invertir tiempo y práctica diaria para dominarla?",
     ["Trabajo chapucero", "Falta de disciplina", "Agotamiento por perfeccionismo"], "Invertida advierte de pereza, atajos mediocres o desmotivación en el aprendizaje.", "Vuelve a lo básico con paciencia. Los verdaderos logros no se consiguen de la noche a la mañana."),

    ("nueve-de-oros", "Nueve de Oros", "9", "IX", ["Independencia económica", "Autosuficiencia", "Disfrute refinado", "Soledad dichosa", "Abundancia merecida"],
     "Una dama elegante pasea por su viñedo rebosante con un halcón adiestrado en su muñeca enjoyada. La dicha de la mujer u hombre autosuficiente que goza de su esfuerzo.",
     "El Nueve de Oros celebra la independencia, la solidez económica y el buen gusto cosechados gracias a tu propia disciplina. Tienes un hogar hermoso y disfrutas de tu propia compañía sin depender de nadie.",
     [{"name": "Halcón encapuchado en la mano", "desc": "Instintos refinados y dominados por la elegancia y la inteligencia."}, {"name": "Vestido adornado con flores y conchas", "desc": "Belleza, dignidad y contacto pleno con la naturaleza fecunda."}, {"name": "Viñedo cargado de nueve pentáculos dorados", "desc": "Patrimonio sólido fruto del esfuerzo personal autónomo."}],
     "Autosuficiencia serena, solvencia económica, refinamiento, disfrute de la soledad sana.", "Aislamiento elitista, esnobismo vanidoso, frialdad que no deja entrar a nadie al jardín.",
     "Soltería dichosa y plena; o relación entre iguales maduros que no dependen el uno del otro.", "Éxito profesional brillante como independiente; patrimonio consolidado y holgura.",
     "La paz del alma que ha aprendido a disfrutar de su propio jardín interior sin mendigar afectos.", "Disfruta de lo que has ganado con tu esfuerzo. Te mereces el confort, la paz y la belleza.", "¿Reconoces el valor de tu propia independencia y autosuficiencia sin culpa?",
     ["Dependencia económica", "Ostentación superficial", "Soledad amarga"], "Invertida advierte de gastos por encima de las posibilidades para aparentar, o miedo a la soledad.", "Aprende a sostenerte sobre tus propios pies; la verdadera elegancia nace de la autenticidad."),

    ("diez-de-oros", "Diez de Oros", "10", "X", ["Legado familiar", "Prosperidad duradera", "Patrimonio generacional", "Raíces sólidas", "Estabilidad plena"],
     "Tres generaciones de una familia y sus perros descansan bajo el arco blasonado de una mansión donde los diez pentáculos forman el Árbol de la Vida. Plenitud total.",
     "El Diez de Oros es la culminación de la riqueza material y familiar a largo plazo. Herencias favorables, empresas familiares florecientes, tradiciones queridas y seguridad para las futuras generaciones.",
     [{"name": "Diez pentáculos en el Árbol de la Cábala", "desc": "Manifestación perfecta de la riqueza divina en el plano terrenal."}, {"name": "Anciano sabio con manto bordado", "desc": "Patriarca que contempla con satisfacción el fruto de toda una vida."}, {"name": "Pareja, niño y perros jugando", "desc": "Armonía intergeneracional, lealtad y futuro garantizado."}],
     "Solidez patrimonial inquebrantable, legado perdurable, armonía familiar, generosidad.", "Disputas por herencias, mandatos familiares asfixiantes, dinero que divide a la familia.",
     "Relación consolidada con apoyo de ambas familias; planes a largo plazo y estabilidad.", "Empresas consolidadas, fondos de jubilación seguros, inversiones inmobiliarias de éxito.",
     "Honrar a los ancestros y el linaje; comprender que somos administradores temporales de la abundancia.",
     "Construye para el largo plazo. Piensa en el legado que dejarás a quienes vienen detrás de ti.", "¿Qué legado de valores y estabilidad estás construyendo hoy para tu futuro?",
     ["Disputas por herencias", "Pérdida de patrimonio", "Ruptura con la familia"], "Invertido señala problemas por dinero en la familia o pérdida de bienes por mala gestión.", "Pon los papeles en regla y no permitas que la avaricia envenene los afectos familiares."),

    ("sota-de-oros", "Sota de Oros", "Sota", "Sota", ["Estudiante aplicado", "Nueva oportunidad de negocio", "Pragmatismo joven", "Ganas de aprender", "Diligencia"],
     "Un joven camina por un campo verde contemplando con devoción un pentáculo dorado entre sus manos. La mente aplicada del aprendiz concienzudo.",
     "La Sota de Oros representa la dedicación al estudio, el inicio de una formación práctica o una propuesta de trabajo modesta pero con gran futuro. Metódico, prudente y responsable.",
     [{"name": "Mirada atenta fija en la moneda", "desc": "Concentración total en aprender a valorar y gestionar los recursos."}, {"name": "Campo arado y árboles al fondo", "desc": "Tierra lista para el trabajo metódico y la cosecha futura."}],
     "Diligencia metódica, ganas de aprender, fiabilidad práctica, honestidad.", "Procrastinación, pereza mental, apego a minucias, falta de visión de conjunto.",
     "Amor prudente y realista; gestos de cuidado prácticos más que palabras apasionadas.", "Ofertas de becas, cursos prácticos, comienzos de contratos en puestos de aprendizaje.",
     "Aprender a contemplar la presencia de Dios en la materia cotidiana y en la naturaleza.", "Aplica tu atención al estudio. Sé disciplinado y aprende bien las bases antes de apresurarte.", "¿Qué materia o conocimiento práctico necesitas estudiar a fondo para avanzar?",
     ["Pereza", "Falta de concentración", "Oportunidad de estudio desaprovechada"], "Invertida avisa de descuido en los estudios, desinterés por el trabajo o gastos tontos.", "Recupera la disciplina diaria; los grandes edificios se construyen ladrillo a ladrillo."),

    ("caballo-de-oros", "Caballo de Oros", "Caballo", "Caballo", ["Constancia inquebrantable", "Trabajador incansable", "Método y paciencia", "Fiabilidad", "Progreso seguro"],
     "El caballero sobre su corcel negro y pesado se detiene en medio de los campos arados contemplando su pentáculo. El avance lento pero seguro que nunca retrocede.",
     "El Caballo de Oros es el trabajador más fiable de todo el Tarot. No tiene la velocidad de Bastos ni las poesías de Copas, pero su perseverancia, paciencia y ética aseguran un triunfo indestructible.",
     [{"name": "Caballo negro y robusto con pies firmes", "desc": "Poder terrenal inagotable, estabilidad y ausencia de precipitaciones."}, {"name": "Campos recién arados", "desc": "Trabajo minucioso de preparación que garantiza una gran cosecha."}, {"name": "Ramas de roble en el casco", "desc": "Fuerza, longevidad y resistencia ante las adversidades."}],
     "Fiabilidad total, perseverancia de hierro, honestidad intachable, puntualidad y método.", "Terquedad obsesiva, lentitud desesperante, pesadez mental, no saber descansar.",
     "Pareja leal, comprometida y proveedora; amor seguro que se demuestra con hechos y no palabras.", "Gestión financiera impecable, cumplimiento riguroso de contratos, éxito por constancia.",
     "El servicio silencioso y fiel; la espiritualidad de quien cumple sus deberes sin quejarse.", "No te apresures. Sigue con tu método constante y riguroso; la victoria está garantizada.", "¿Estás teniendo la paciencia y disciplina necesarias para sostener tus compromisos diarios?",
     ["Rutina asfixiante", "Lentitud que pierde oportunidades", "Terquedad estéril"], "Invertido indica estancamiento por rigidez mental o pereza disfrazada de prudencia.", "Acepta innovaciones en tu método; ser constante no significa ser terco e inflexible."),

    ("reina-de-oros", "Reina de Oros", "Reina", "Reina", ["Madre nutricia terrenal", "Abundancia práctica", "Sentido común", "Hospitalidad cálida", "Prosperidad hogareña"],
     "La reina sentada en un trono tallado con frutos y cabras en medio de flores silvestres contempla su pentáculo con ternura maternal mientras un conejo salta cerca. Prosperidad amorosa.",
     "La Reina de Oros es la anfitriona perfecta, la administradora sabia del hogar y los negocios. Combina practicidad terrenal con calidez afectuosa: hace que todo prospere a su alrededor.",
     [{"name": "Conejo en la hierba", "desc": "Fertilidad desbordante, vida silvestre y agilidad práctica."}, {"name": "Trono con ángeles y animales", "desc": "Gobierno sabio y amoroso sobre el reino natural y doméstico."}, {"name": "Pentáculo sostenido en el regazo", "desc": "Cuidado amoroso de la abundancia para nutrir a todos."}],
     "Sentido común impecable, generosidad cálida, solvencia financiera y autocuidado.", "Materialismo absorbente, obsesión por la limpieza o el dinero, sobreprotección física.",
     "Pareja leal, cariñosa y excelente administradora; hogar acogedor y vida segura.", "Dirección financiera eficiente, negocios gastronómicos o inmobiliarios florecientes.",
     "Reconocimiento de lo divino en la belleza del cuerpo, la comida sana y la Madre Tierra.", "Cuida tu cuerpo y tu hogar con amor. Administra tus recursos con sentido común y generosidad.", "¿Cómo puedes hacer de tu espacio un lugar más acogedor, bello y nutritivo hoy?",
     ["Descuido doméstico", "Avaricia mezquina", "Estrés por dinero"], "Invertida avisa de ansiedad por temas materiales o descuido del propio cuerpo y descanso.", "Regálate un respiro en la naturaleza; la abundancia verdadera empieza por la paz interior."),

    ("rey-de-oros", "Rey de Oros", "Rey", "Rey", ["Maestría financiera", "Éxito material consolidado", "Pragmatismo sabio", "Generosidad protectora", "Estabilidad regia"],
     "El rey sentado en su trono decorado con cabezas de toros y viñedos, con cetro en mano y el pie sobre los tesoros de su castillo. El soberano del éxito material.",
     "El Rey de Oros encarna al gran empresario consolidado, al mecenas generoso y al líder pragmático. Ha conquistado la cima financiera gracias a su disciplina y sabe disfrutar de la vida con madurez.",
     [{"name": "Trono decorado con toros (Tauro)", "desc": "Fuerza telúrica, tenacidad y fecundidad material inquebrantable."}, {"name": "Manto con racimos de uvas maduras", "desc": "Cosecha abundante y disfrute de los mejores placeres terrenales."}, {"name": "Castillo y murallas a la espalda", "desc": "Imperio económico sólido construido piedra a piedra."}],
     "Maestría financiera sobresaliente, fiabilidad incondicional, generosidad protectora.", "Codicia insaciable, medir el valor de las personas por su cuenta bancaria, rigidez.",
     "Pareja estable, protectora y generosa; compromiso sólido con comodidades compartidas.", "Grandes negocios exitosos, dirección de patrimonio, inversiones de alto rendimiento.",
     "Ser un buen administrador de los bienes de la tierra al servicio del bienestar colectivo.", "Actúa con madurez práctica. Consolida tus cimientos y disfruta con sensatez de lo ganado.", "¿Estás utilizando tus recursos materiales para construir seguridad o solo para alimentar el ego?",
     ["Quiebra por soberbia", "Avaricia destructiva", "Corrupción material"], "Invertido advierte de negocios turbios, especulación imprudente o tacañería despótica.", "Vuelve a la ética en los negocios; el verdadero éxito deja un rastro de honestidad y paz.")
]

for o in oros_data:
    cards_list.append(make_card(o[0], o[1], o[2], o[3], "Oros", "Tierra", o[4], o[5], o[6], o[7], o[8], o[9], o[10], o[11], o[12], o[13], o[14], o[15], o[16], o[17]))

print(f"Total cards created: {len(cards_list)}")

# Verify all 78 card IDs match the images downloaded
missing_imgs = []
for c in cards_list:
    if not os.path.exists(c["img"]):
        missing_imgs.append((c["id"], c["img"]))

if missing_imgs:
    print(f"WARNING: {len(missing_imgs)} missing card images!")
    for m in missing_imgs:
        print("Missing:", m)
else:
    print("ALL 78 CARDS MATCH LOCAL WEBP IMAGES PERFECTLY!")

# Save full cards dataset
with open("data/cards_78.json", "w", encoding="utf-8") as f:
    json.dump(cards_list, f, ensure_ascii=False, indent=2)

print("cards_78.json saved.")
