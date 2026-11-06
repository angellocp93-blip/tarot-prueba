# -*- coding: utf-8 -*-
"""
Datos maestros para los 56 Arcanos Menores del Tarot
14 Bastos (Fuego)
14 Copas (Agua)
14 Espadas (Aire)
14 Oros (Tierra)
"""

def generate_minors_data():
    minors = []

    suits_meta = {
        "Bastos": {
            "folder": "bastos",
            "element": "Fuego",
            "theme": "la voluntad, la creatividad, la pasión y el impulso de acción",
            "tool": "la vara de roble florecida",
            "symbol": "la chispa ígnea del espíritu humano",
            "astro_base": ["Aries", "Leo", "Sagitario"]
        },
        "Copas": {
            "folder": "copas",
            "element": "Agua",
            "theme": "las emociones profundas, el amor, los vínculos afectivos y la intuición del corazón",
            "tool": "el cáliz sagrado de oro",
            "symbol": "el torrente de las aguas vivas del alma",
            "astro_base": ["Cáncer", "Escorpio", "Piscis"]
        },
        "Espadas": {
            "folder": "espadas",
            "element": "Aire",
            "theme": "el intelecto, el pensamiento analítico, la verdad implacable y los dilemas morales",
            "tool": "la espada de doble filo",
            "symbol": "el viento penetrante de la mente lúcida",
            "astro_base": ["Géminis", "Libra", "Acuario"]
        },
        "Oros": {
            "folder": "oros",
            "element": "Tierra",
            "theme": "la realidad material, el trabajo tangible, el dinero, el cuerpo y el legado terrenal",
            "tool": "el disco de oro grabado con el pentáculo",
            "symbol": "la tierra fértil y los frutos de la cosecha",
            "astro_base": ["Tauro", "Virgo", "Capricornio"]
        }
    }

    ranks = [
        ("as", "As", 1),
        ("dos", "Dos", 2),
        ("tres", "Tres", 3),
        ("cuatro", "Cuatro", 4),
        ("cinco", "Cinco", 5),
        ("seis", "Seis", 6),
        ("siete", "Siete", 7),
        ("ocho", "Ocho", 8),
        ("nueve", "Nueve", 9),
        ("diez", "Diez", 10),
        ("sota", "Sota", 11),
        ("caballero", "Caballero", 12),
        ("reina", "Reina", 13),
        ("rey", "Rey", 14)
    ]

    # Specific deep contents for cards
    cards_detail = {
        # BASTOS
        "as-de-bastos": {
            "diferenciador": "A diferencia del As de Espadas (chispa mental) o del As de Oros (semilla material), el As de Bastos es el fuego puro de la pasión y la energía creadora primigenia sin condicionamientos.",
            "curiosidad_1": "La mano que emerge de la nube es la 'Yad' divina, que ofrece la vara florecida como un don cósmico gratuito.",
            "curiosidad_2": "Las hojas que caen al aire son yods hebreas que representan la fecundación de la tierra por el fuego divino.",
            "historia_titulo": "La Primera Chispa en la Forja",
            "historia_relato": "En la noche más fría del invierno, un herrero contemplaba su fragua apagada creyendo que ya nada volvería a fundirse. De pronto, un relámpago cayó sobre el roble del patio y una pequeña rama encendida voló hasta sus manos. Al soplarla con fe, el fuego devoró la leña y el taller entero se llenó de un calor dorado. Aquella noche forjó su mejor obra, comprendiendo que un solo segundo de entusiasmo verdadero puede encender toda una vida."
        },
        "dos-de-bastos": {
            "diferenciador": "A diferencia del 2 de Espadas (parálisis por duda) o del 2 de Copas (unión entre dos), el 2 de Bastos es el visionario que contempla el mundo desde sus almenas sopesando una gran conquista futura.",
            "curiosidad_1": "El noble sostiene un pequeño globo terráqueo en su mano derecha, simbolizando que su visión abarca horizontes globales más allá de su territorio actual.",
            "curiosidad_2": "Una vara está fijada a la muralla (lo ya logrado) mientras la otra está sujeta en su mano (el paso hacia lo desconocido).",
            "historia_titulo": "El Señor de las Almenas",
            "historia_relato": "Desde la torre más alta de su castillo, el rey contemplaba el océano con un mapa entre los dedos. Sus consejeros le rogaban que se quedase disfrutando de sus riquezas acumuladas, pero sus ojos miraban hacia la línea donde el mar se une con las estrellas. 'Quien solo cuida lo que ya conquistó, pronto lo verá marchitarse', dijo mirando la esfera del mundo. Al amanecer, ordenó arriar las velas de la primera carabela."
        },
        "tres-de-bastos": {
            "diferenciador": "A diferencia del 2 de Bastos (donde los planes aún se gestan en la mente), en el 3 de Bastos los barcos ya han zarpado y navegan con viento a favor; es la confirmación del éxito expansivo.",
            "curiosidad_1": "El comerciante mira al mar de espaldas al espectador, indicando que su atención está plenamente enfocada en el futuro y no en el pasado.",
            "curiosidad_2": "Las aguas tienen un tono dorado brillante que presagia prosperidad y retorno multiplicado de lo invertido.",
            "historia_titulo": "Las Tres Naves en la Bahía Dorada",
            "historia_relato": "Tres años esperó el mercader en el acantilado mirando el horizonte vacío. Muchos se burlaron de su paciencia. Pero en una mañana de verano, tres velas de lino blanco aparecieron cortando las olas doradas por el sol: sus naves regresaban cargadas de especias y telas de reinos lejanos. Comprendió que la verdadera grandeza exige no solo tener coraje para enviar los barcos, sino la serenidad para esperar su regreso."
        },
        "cuatro-de-bastos": {
            "diferenciador": "A diferencia del 4 de Oros (donde la estabilidad se convierte en tacañería y encierro), el 4 de Bastos celebra la estabilidad con fiesta al aire libre, puertas abiertas y bienvenida a la comunidad.",
            "curiosidad_1": "Las cuatro varas forman una 'jupá' o palio nupcial decorado con flores y frutos, aludiendo a la consagración sagrada del hogar.",
            "curiosidad_2": "Al fondo se vislumbra un castillo amurallado, pero la celebración se realiza afuera, demostrando que la verdadera seguridad no se esconde tras muros.",
            "historia_titulo": "La Fiesta bajo el Emparrado",
            "historia_relato": "Tras meses de arduo trabajo levantando los cimientos de la nueva aldea, los pioneros clavaron cuatro vigas de roble y las unieron con una guirnalda de parras y rosas. No esperaron a pintar las paredes para festejar: invitaron a los vecinos, descorcharon el vino nuevo y bailaron descalzos sobre la hierba. 'Una casa se construye con piedras', dijo el anciano del pueblo, 'pero solo se convierte en hogar cuando sus puertas están abiertas para compartir la dicha'."
        },
        "cinco-de-bastos": {
            "diferenciador": "A diferencia del 5 de Espadas (donde hay crueldad, traición y humillación), el 5 de Bastos es una pugna o competencia deportiva: jóvenes probando sus habilidades sin intención de herir mortalmente.",
            "curiosidad_1": "Ninguno de los cinco jóvenes viste armadura ni lleva espadas de metal: sus varas chocan en el aire en un ensayo de destreza y competencia leal.",
            "curiosidad_2": "Cada uno viste ropas de colores diferentes, representando la diversidad de ideas y perspectivas que buscan destacar en el grupo.",
            "historia_titulo": "El Torneo de los Cinco Bastones",
            "historia_relato": "En la plaza mayor, cinco jóvenes practicaban con varas de madera para el festival de primavera. Cada uno quería que su estocada fuera la más aplaudida y el polvo se levantaba entre gritos y risas. Al terminar la contienda, exhaustos y sudorosos, se dieron la mano y compartieron una jarra de agua fresca: habían aprendido que el rival no es un enemigo que deba ser aniquilado, sino el espejo que nos obliga a dar lo mejor de nosotros mismos."
        },
        "seis-de-bastos": {
            "diferenciador": "A diferencia del 6 de Espadas (huida dolorosa hacia aguas tranquilas), el 6 de Bastos es el desfile triunfal público: el héroe que regresa coronado de laurel aclamado por la multitud.",
            "curiosidad_1": "El jinete monta un caballo blanco con gualdrapas verdes, combinando la pureza de intención con la esperanza y el renacimiento.",
            "curiosidad_2": "Lleva una corona de laurel en la cabeza y otra atada a su vara triunfal, simbolizando tanto el reconocimiento interior como los honores exteriores.",
            "historia_titulo": "El Retorno del Héroe Coronado",
            "historia_relato": "El mensajero había cruzado desiertos y superado desfiladeros para llevar la noticia de la paz a la capital del reino. Al entrar por las puertas de bronce, las campanas repicaron y los niños arrojaron flores bajo los cascos de su caballo. El joven sonrió y tocó el laurel de su frente: sabía que la gloria pública es tan fugaz como el perfume de una rosa, pero la satisfacción de haber cumplido la misión con honor permanecería para siempre en su alma."
        },
        "siete-de-bastos": {
            "diferenciador": "A diferencia del 5 de Bastos (donde la competencia es colectiva), en el 7 de Bastos un solo guerrero defiende una posición elevada contra seis atacantes desde abajo; es el coraje solitario de quien defiende su verdad.",
            "curiosidad_1": "El defensor lleva zapatos disparejos (uno de cuero marrón y otro verde), revelando que la prueba lo sorprendió desprevenido pero reaccionó con valentía instantánea.",
            "curiosidad_2": "Ocupa la colina superior, lo que le otorga una ventaja estratégica moral y física decisiva sobre sus oponentes.",
            "historia_titulo": "El Bastión de la Colina Alta",
            "historia_relato": "Seis adversarios intentaron arrebatarle el estandarte que custodiaba en la cumbre del promontorio. Le gritaron que se rindiese, que estaba solo y que nadie vendría en su auxilio. El joven no retrocedió un milímetro: plantó los pies firmes en la roca y blandió su vara con tal destreza y convicción que ninguno de los atacantes se atrevió a dar el último paso. Cuando los demás huyeron al anochecer, comprendió que cuando defiendes una causa justa desde lo alto de tu integridad, un solo hombre vale por un ejército entero."
        },
        "ocho-de-bastos": {
            "diferenciador": "Es una de las pocas cartas menores sin figuras humanas: ocho varas vuelan veloces por el aire en formación paralela, representando la velocidad fulgurante de los acontecimientos y la comunicación instantánea.",
            "curiosidad_1": "Las varas apuntan hacia abajo en dirección a un valle verde y fértil regado por un río, indicando que el vuelo culminará en un aterrizaje muy fructífero.",
            "curiosidad_2": "El cielo está totalmente despejado de nubes, confirmando que no hay obstáculos para la aceleración del proceso.",
            "historia_titulo": "El Vuelo de las Ocho Flechas de Madera",
            "historia_relato": "El arquero mayor tensó el arco cósmico y soltó las ocho flechas hacia el valle al mismo tiempo. No iban a la guerra: llevaban mensajes de boda, contratos firmados y noticias de esperanza a las ciudades lejanas. En pocas horas, lo que había estado bloqueado durante meses comenzó a moverse a la velocidad de la luz. Cuando el viento sopla a tu favor y la intención es clara, los milagros no tardan años: ocurren en un parpadeo."
        },
        "nueve-de-bastos": {
            "diferenciador": "A diferencia del 9 de Espadas (angustia mental nocturna), el 9 de Bastos es el guerrero veterano vendado en la cabeza que, a pesar de estar herido y cansado, permanece en pie defendiendo la empalizada.",
            "curiosidad_1": "El vendaje blanco en su cabeza indica que ha sobrevivido a batallas previas y posee cicatrices que se han convertido en sabiduría y fortaleza.",
            "curiosidad_2": "Las ocho varas detrás de él forman un muro sólido, mientras él sostiene la novena vara con ambas manos alerta ante el último asalto.",
            "historia_titulo": "La Última Guardia del Veterano",
            "historia_relato": "La noche era gélida y la herida de la frente aún le palpitaba. Sus compañeros dormían agotados en el campamento mientras él montaba guardia apoyado en su cayado de roble. Sus ojos escudriñaban la oscuridad con la agudeza del águila. Sabía que el amanecer estaba a solo una hora de distancia y que rendirse en el último tramo arruinaría todo el esfuerzo del viaje. Apretó los dientes, respiró hondo y sonrió: el sol asomó por el este disipando las sombras; había vencido a la noche más larga."
        },
        "diez-de-bastos": {
            "diferenciador": "A diferencia del 10 de Espadas (ruina absoluta) o del 10 de Oros (plenitud familiar), el 10 de Bastos es la sobrecarga voluntaria: querer llevar las diez varas uno mismo hasta doblarse por el peso del exceso de responsabilidades.",
            "curiosidad_1": "El hombre camina encorvado mirando al suelo sin ver que la ciudad y su destino están a solo unos metros frente a él.",
            "curiosidad_2": "Lleva las diez varas todas juntas en un solo haz abrazado, simbolizando la incapacidad de delegar o priorizar tareas.",
            "historia_titulo": "La Carga de las Diez Vigas",
            "historia_relato": "Un leñador quiso impresionar al maestro del pueblo cargando él solo las diez vigas para el techo de la ermita. A mitad del camino, su espalda crujía y el sudor le cegaba los ojos; apenas podía dar un paso sin tambalearse. Una anciana que pasaba con un cántaro le dijo: 'Hijo mío, el orgullo te hace cargar diez vigas para que todos te miren; la sabiduría te pide llevar dos ahora y pedirle ayuda a tus hermanos para las demás'. El hombre soltó el haz, descansó bajo un olivo y aprendió que soltar el exceso no es fracasar, sino ser inteligente."
        },
        "sota-de-bastos": {
            "diferenciador": "A diferencia de la Sota de Espadas (vigilante y analítica) o la Sota de Copas (soñadora y tímida), la Sota de Bastos es la curiosidad entusiasta, la chispa juvenil que explora nuevos horizontes con valentía.",
            "curiosidad_1": "La túnica amarilla está estampada con salamandras (símbolo alquímico del fuego que no se consume en las llamas).",
            "curiosidad_2": "Lleva una pluma roja flamígera en su gorro, evocando la llama del ingenio y la inspiración espontánea.",
            "historia_titulo": "El Heraldo de la Pluma Roja",
            "historia_relato": "En un cruce de caminos del desierto, un joven explorador contemplaba con fascinación un brote verde que nacía de su cayado de madera seca. No tenía miedo a la distancia ni a las tormentas de arena: en su bolso llevaba noticias de aventura y en sus ojos brillaba el fuego de quien está a punto de descubrir el mundo. Corrió hacia el horizonte silbando, sabiendo que cada día es una página en blanco esperando ser escrita con fuego sagrado."
        },
        "caballero-de-bastos": {
            "diferenciador": "A diferencia del Caballero de Espadas (que embiste con furia mental fría), el Caballero de Bastos cabalga impulsado por el ardor apasionado, el entusiasmo magnético y la osadía sin frenos.",
            "curiosidad_1": "El caballo alazán levanta sus patas delanteras en un relincho de brío fogoso, reflejando la impaciencia del caballero por conquistar metas.",
            "curiosidad_2": "De su casco y hombreras brotan penachos de llamas rojas que arden al viento.",
            "historia_titulo": "El Galope de la Salamandra",
            "historia_relato": "El joven jinete no esperaba a que le abrieran las puertas de la fortaleza: saltaba los fosos a galope tendido. Donde otros veían murallas infranqueables, él solo veía desafíos emocionantes para poner a prueba su coraje. Cruzó tres provincias en una sola jornada, encendiendo el corazón de campesinos y nobles con su entusiasmo contagioso. En su paso dejó una estela de fuego y esperanza: había demostrado que la pasión sincera es capaz de mover montañas que la prudencia jamás se atrevería a rozar."
        },
        "reina-de-bastos": {
            "diferenciador": "A diferencia de la Reina de Espadas (severa y racional) o la de Copas (introspectiva y sensible), la Reina de Bastos es el fuego maduro: carismática, alegre, enérgica, cálida y soberana de su propia luz sin complejos.",
            "curiosidad_1": "A sus pies descansa un gato negro que mira al frente, simbolizando la domesticación de las fuerzas mágicas ocultas y la protección intuitiva.",
            "curiosidad_2": "En su mano izquierda sostiene un girasol dorado, reflejando su naturaleza solar que siempre busca la luz y la vitalidad positiva.",
            "historia_titulo": "La Señora de los Girasoles",
            "historia_relato": "En su corte no había secretos oscuros ni miradas cabizbajas. La Reina recibía a embajadores y huérfanos con la misma carcajada franca y la misma mirada luminosa. Cuando los inviernos eran crueles, su presencia llenaba el salón de un calor tan reconfortante que las flores florecían en pleno diciembre. 'La verdadera reina', solía decir mientras acariciaba a su gato negro, 'no gobierna haciendo que los demás se sientan pequeños, sino inspirándolos a brillar con tanta fuerza como ella'."
        },
        "rey-de-bastos": {
            "diferenciador": "A diferencia del Rey de Espadas (ley y juicio) o del Rey de Oros (gestión patrimonial), el Rey de Bastos es el gran líder visionario, el emperador creativo que transforma ideas audaces en realidades inspiradoras para miles de personas.",
            "curiosidad_1": "Su túnica y el respaldo de su trono están decorados con leones y salamandras que se muerden la cola, simbolizando la maestría absoluta sobre el elemento fuego.",
            "curiosidad_2": "Sostiene una vara viva que brota ramas verdes y mira de perfil hacia el horizonte, siempre atento al futuro y al progreso de su comunidad.",
            "historia_titulo": "El Trono del León Dorado",
            "historia_relato": "El monarca no gobernaba dictando castigos desde la penumbra de su palacio; salía a la forja a golpear el yunque y marchaba al frente de las caravanas que abrían rutas por las montañas. Su mirada tenía la firmeza del pedernal y la calidez del hogar. Los jóvenes guerreros daban la vida por él, no por temor a sus guardias, sino porque en su pecho latía un fuego tan noble y puro que iluminaba el camino de todos los hombres de bien."
        },

        # COPAS
        "as-de-copas": {
            "diferenciador": "Es la fuente primordial del amor incondicional y la gracia emocional. Cinco torrentes de agua viva fluyen inagotables del cáliz sagrado hacia un estanque cubierto de flores de loto.",
            "curiosidad_1": "Una paloma blanca desciende del cielo sosteniendo en su pico una hostia sagrada marcada con la cruz, bendiciendo el cáliz.",
            "curiosidad_2": "La copa está grabada con una letra 'W' (o 'M' invertida), aludiendo al Santo Grial y a la presencia maternal del espíritu divino.",
            "historia_titulo": "El Manantial del Santo Grial",
            "historia_relato": "En un claro secreto del bosque de Brocelianda, una copa de oro flotaba sobre las aguas de un estanque cristalino. No estaba llena de vino terrenal, sino de la gracia celestial que apaga la sed del alma. Un caballero herido en mil batallas se arrodilló y bebió de sus aguas: en ese instante, el veneno del rencor que carcomía su pecho se disolvió como la sal en el mar. Había comprendido que el amor verdadero no se mendiga; brota desde adentro como un manantial que jamás se agota."
        },
        "dos-de-copas": {
            "diferenciador": "A diferencia de Los Enamorados (gran decisión existencial y cósmica), el 2 de Copas es el encuentro íntimo, el brindis de almas y la reciprocidad afectiva perfecta entre dos personas.",
            "curiosidad_1": "Sobre las dos copas flota el Caduceo de Hermes alado y una cabeza de león rojo, simbolizando la sanación alquímica y la pasión noble entre opuestos.",
            "curiosidad_2": "El hombre y la mujer visten coronas de laurel y flores, indicando que su unión está bendecida por el respeto y la pureza mutua.",
            "historia_titulo": "El Brindis de las Dos Almas",
            "historia_relato": "Caminaban en direcciones opuestas por el puente de mármol del río sagrado. Cuando sus miradas se cruzaron, el ruido del mundo se extinguió por completo. Cada uno alzó su copa de arcilla y la ofreció al otro: al chocar las vasijas con un tintineo cristalino, una cabeza de león alado brilló en el cielo vespertino. No hicieron falta juramentos eternos ni promesas grandiosas; en el silencio de sus ojos comprendieron que el universo los había estado buscando a ambos desde el principio de los tiempos."
        },
        "tres-de-copas": {
            "diferenciador": "A diferencia del 4 de Bastos (celebración estructurada del hogar), el 3 de Copas es la hermandad espontánea, la dicha compartida entre amigas, la danza del agradecimiento y la abundancia de la cosecha.",
            "curiosidad_1": "Tres mujeres con vestidos de colores vivos (rosa, blanco y oro) brindan con sus copas entrelazadas en una ronda de danza sagrada.",
            "curiosidad_2": "A sus pies abundan racimos de uvas maduras y calabazas, celebrando los frutos de la amistad y la colaboración afectiva.",
            "historia_titulo": "La Danza de las Tres Hermanas",
            "historia_relato": "Tres doncellas cosecharon las vides en las colinas de Toscana. Al llenar los últimos cestos, alzaron sus copas hacia el cielo dorado del atardecer y bailaron descalzas entre los sarmientos. No competían por ver quién había trabajado más ni quién merecía el mayor elogio: celebraban que estaban juntas, vivas y bendecidas por la tierra fértil. En su risa cristalina resonaba la verdad suprema: la alegría cuando se comparte no se divide; se multiplica al infinito."
        },
        "cuatro-de-copas": {
            "diferenciador": "A diferencia del Ermitaño (retiro sabio voluntario), el 4 de Copas es la apatía emocional, el aburrimiento y el desdén: un joven sentado bajo un árbol rechaza una copa divina que le ofrece una mano en la nube por estar absorto en su propio desgano.",
            "curiosidad_1": "El joven tiene los brazos cruzados y la mirada baja contemplando las tres copas vacías del suelo, ciego ante la cuarta copa que flota a su lado.",
            "curiosidad_2": "El árbol bajo el que descansa no le ofrece refugio fértil, sino que refleja su propio ensimismamiento estéril.",
            "historia_titulo": "El Príncipe Bajo el Roble Seco",
            "historia_relato": "Un joven noble pasaba los días suspirando bajo un roble del jardín real. Nada le agradaba: los manjares le parecían insípidos y la música le sonaba a ruido. De pronto, una mano de luz brillante emergió de una nube a su lado ofreciéndole una copa que rebosaba el néctar de la felicidad eterna. Pero el joven ni siquiera giró la cabeza: estaba demasiado ocupado quejándose de sus viejas penas pasadas. Comprendió demasiado tarde que el universo no puede llenar un cuenco que está cerrado con el candado de la desidia."
        },
        "cinco-de-copas": {
            "diferenciador": "A diferencia del 3 de Espadas (dolor agudo por traición), el 5 de Copas es el duelo por lo perdido, pero con un detalle redentor crucial: tres copas están derramadas en el suelo, pero dos copas intactas permanecen de pie a sus espaldas.",
            "curiosidad_1": "La figura viste un manto negro de luto y duelo, mirando con dolor el vino derramado sobre la tierra.",
            "curiosidad_2": "Al fondo, un puente de piedra cruza el río hacia un castillo seguro, recordándole que el camino hacia el hogar sigue abierto.",
            "historia_titulo": "Las Dos Copas a la Espalda",
            "historia_relato": "El viajero lloraba desconsolado a la orilla del río negro. El vino de sus tres copas más preciadas se había derramado en el barro y creía que su vida estaba irremediablemente arruinada. Un caminante se detuvo a su lado y le tocó suavemente el hombro cubierto por el manto oscuro: '¿Por qué lloras por el vino que la tierra ya bebió? Date la vuelta'. El hombre giró el rostro con lágrimas en los ojos y vio dos copas de oro intactas, colmadas de néctar dulce detrás de él. El puente estaba allí: el dolor era real, pero la esperanza aún estaba viva."
        },
        "seis-de-copas": {
            "diferenciador": "A diferencia del pasado nostálgico amargo, el 6 de Copas es la dulzura de los recuerdos de infancia, la inocencia recuperada, el perdón y el regalo amoroso sin segundas intenciones.",
            "curiosidad_1": "Un niño pequeño vestido como un paje medieval ofrece una copa llena de flores blancas a una niña pequeña en el patio de una villa antigua.",
            "curiosidad_2": "Un guardia de espaldas camina a lo lejos, indicando que el espacio de la infancia es seguro y protegido.",
            "historia_titulo": "El Regalo de las Flores Blancas",
            "historia_relato": "En el patio adoquinado de la vieja casa de los abuelos, un niño llenó una copa de latón con margaritas y lirios silvestres y se la entregó a su pequeña amiga con una reverencia graciosa. No había doble intención, ni contratos, ni miedo al rechazo; solo la pureza de dos corazones que sabían quererse con la sencillez de los pájaros. Muchos años después, ya anciano y fatigado por las intrigas de la corte, el hombre recordó aquel instante y sintió que su alma volvía a sonreír con la pureza de aquel primer jardín."
        },
        "siete-de-copas": {
            "diferenciador": "A diferencia de La Luna (pesadillas y miedos del inconsciente), el 7 de Copas son los castillos en el aire, la tentación de fantasías seductoras y la confusión ante demasiadas opciones atractivas pero ilusorias.",
            "curiosidad_1": "Siete copas emergen de una nube flotante ofreciendo diferentes dones: una cabeza de mujer, un castillo, joyas, una serpiente, una corona de laurel, un dragón y una figura radiante velada.",
            "curiosidad_2": "La silueta negra del hombre contempla las visiones asombrado pero inmóvil, advirtiendo sobre el peligro de perderse en ensueños sin pisar la realidad.",
            "historia_titulo": "El Mercado de los Sueños Flotantes",
            "historia_relato": "En la cima de la Colina de la Niebla, un vendedor invisible abrió siete copas de cristal sobre una nube. En una prometía fama eterna; en otra, riquezas sin fin; en otra, el amor de una princesa; y en otra, el poder sobre las bestias. Un joven estuvo tentado de abalanzarse sobre todas al mismo tiempo, pero al acercar la mano a la copa del castillo, vio que era solo humo que se disolvía entre los dedos. Respiró hondo y eligió la copa velada con una cruz: la que pedía trabajo y verdad, la única que tenía peso real en la tierra."
        },
        "ocho-de-copas": {
            "diferenciador": "A diferencia de La Muerte (donde el ciclo termina por fuerza mayor), el 8 de Copas es la renuncia voluntaria: una persona da la espalda a ocho copas perfectamente apiladas y camina hacia las montañas buscando algo más elevado.",
            "curiosidad_1": "La luna en el cielo combina un eclipse entre el sol y la luna creciente, simbolizando que la partida ocurre en un momento de alineación espiritual profunda.",
            "curiosidad_2": "La figura viste una capa roja y se apoya en un báculo de peregrino, indicando que no huye por cobardía, sino que inicia una búsqueda sagrada.",
            "historia_titulo": "La Partida hacia las Altas Cumbres",
            "historia_relato": "Tenía una casa hermosa, ocho copas de oro sobre la mesa y el respeto de sus conciudadanos. Sin embargo, cada medianoche sentía un vacío en el pecho que nada de lo material podía llenar. Una noche de luna clara, se puso su capa roja, tomó su báculo y salió sin hacer ruido por el sendero pedregoso que sube a las montañas. No despreciaba lo vivido; simplemente sabía que hay una hora en la vida donde lo bueno debe ser abandonado para poder encontrar lo sublime."
        },
        "nueve-de-copas": {
            "diferenciador": "Conocida popularmente como 'la carta del deseo concedido'. A diferencia del 10 de Copas (felicidad familiar compartida), el 9 de Copas es la satisfacción personal, el bienestar íntimo y la plenitud del alma agradecida.",
            "curiosidad_1": "Un hombre corpulento y jovial se sienta sonriente con los brazos cruzados ante un banco curvo donde reposan nueve copas doradas perfectamente alineadas.",
            "curiosidad_2": "La cortina azul marino de fondo revela que su dicha es un santuario de paz interior y seguridad emocional ganada con mérito.",
            "historia_titulo": "El Banquete de la Gratitud",
            "historia_relato": "El posadero preparó una mesa con los mejores manjares y alineó nueve copas de vino añejo tras superar años de sacrificios y austeridad. Se sentó en su banco de madera, cruzó los brazos sobre el pecho y sonrió con la beatitud de quien no le debe nada a nadie y está en paz con el cielo y con los hombres. Cerró los ojos y pidió un deseo en silencio: no pidió más oro ni más tierras; pidió que la dicha que habitaba en su corazón aquella noche no se apagara jamás."
        },
        "diez-de-copas": {
            "diferenciador": "La cumbre de la felicidad emocional: una familia feliz contempla un arcoíris formado por diez copas doradas sobre su casa de campo, representando el amor verdadero, la paz doméstica y la realización afectiva suprema.",
            "curiosidad_1": "El esposo y la esposa alzan sus brazos hacia el cielo en agradecimiento mientras dos niños pequeños bailan tomados de la mano a su lado.",
            "curiosidad_2": "El río serpentea por un paisaje verde idílico, confirmando que la armonía fluye con naturalidad y permanencia.",
            "historia_titulo": "El Arcoíris de las Diez Copas",
            "historia_relato": "Tras la última lluvia de otoño, la pareja salió al porche de su granja campestre abrazada por la cintura. Sus dos hijos saltaban sobre los charcos riendo a carcajadas. En el cielo azul se dibujó un arcoíris resplandeciente del que parecían brotar diez copas de luz líquida bendiciendo sus campos y su ganado. 'Muchos reyes darían sus coronas por un solo día de esta paz', murmuró el hombre besando la frente de su esposa. Habían hallado el verdadero paraíso terrenal: amarse con lealtad y ver crecer a los suyos en paz."
        },
        "sota-de-copas": {
            "diferenciador": "A diferencia de la Sota de Espadas (crítica y desconfiada), la Sota de Copas es la ternura poética, la intuición naciente y la capacidad de asombrarse ante los mensajes mágicos de la vida.",
            "curiosidad_1": "Un pez azul asoma su cabeza desde la copa dorada que sostiene el joven paje, como si le estuviese susurrando un secreto al oído.",
            "curiosidad_2": "Su túnica está estampada con flores de loto y lirios de agua, y el mar forma olas juguetonas a sus espaldas.",
            "historia_titulo": "El Mensaje del Pez Azul",
            "historia_relato": "A la orilla del mar de zafiro, un joven paje sacó su copa de agua y descubrió maravillado que un pequeño pez azul le hablaba con voz de caracola. No se asustó ni intentó atraparlo; escuchó con los ojos muy abiertos la poesía secreta que las olas cantan en el fondo del océano. Guardó el secreto en su corazón y corrió a escribirlo en un pergamino con tinta de calamar: aquel muchacho se convirtió en el poeta más amado del reino porque nunca olvidó hablar el idioma del corazón."
        },
        "caballero-de-copas": {
            "diferenciador": "A diferencia del Caballero de Bastos (acción fogosa) o de Espadas (ataque fulminante), el Caballero de Copas avanza al paso tranquilo de su corcel blanco, sosteniendo la copa con reverencia como una ofrenda de amor o un mensaje de reconciliación.",
            "curiosidad_1": "Su armadura está decorada con peces rojos y alitas en el casco y en los talones (aludiendo al dios Mercurio y al mensajero alado del amor).",
            "curiosidad_2": "Cruza un arroyo apacible, mostrando que las aguas emocionales están en calma y su misión es pacífica.",
            "historia_titulo": "El Jinete de la Copa de Paz",
            "historia_relato": "El caballero no llevaba espada ni escudo al cruzar las líneas enemigas; montaba un caballo blanco de paso cadencioso y sostenía en alto una copa de plata con agua de la Fuente de la Reconciliación. Los arqueros bajaron los arcos al ver su mirada serena y su porte sin armadura de combate. Al llegar ante la tienda del general rival, le ofreció la copa con una inclinación respetuosa: 'No vengo a pedir vuestra rendición, sino a invitaros a beber de la misma fuente'. Aquel atardecer terminó la guerra más larga del continente."
        },
        "reina-de-copas": {
            "diferenciador": "La soberana de la empatía y la clarividencia. Sentada en un trono de conchas marinas a la orilla del océano, contempla fijamente una copa de oro cerrada y profusamente ornamentada con querubines.",
            "curiosidad_1": "Es la única carta de copas donde el cáliz está totalmente cerrado con una tapa hexagonal, simbolizando los misterios íntimos del alma que solo se abren al amor verdadero.",
            "curiosidad_2": "Sus pies no tocan el agua directamente, sino que descansan sobre guijarros pulidos por las mareas, demostrando equilibrio entre la mente y las emociones.",
            "historia_titulo": "La Reina del Cáliz Sellado",
            "historia_relato": "En su trono de coral blanco, la Reina contemplaba el cáliz dorado que guardaba las lágrimas y los anhelos de su pueblo. Podía adivinar las penas de quien se acercaba antes de que abriera la boca y curar el dolor más hondo con solo posar su mano en el hombro del afligido. 'El corazón humano es un cáliz sagrado', solía susurrar mirando las olas; 'no se debe abrir ante cualquiera, pero quien sabe amarlo con respeto encuentra en él un tesoro infinito'."
        },
        "rey-de-copas": {
            "diferenciador": "El maestro de la madurez emocional y la sabiduría compasiva. Su trono flota en medio de un mar tempestuoso, pero su copa permanece perfectamente quieta sin derramar una gota.",
            "curiosidad_1": "Lleva un amuleto con un pez al cuello y sostiene un cetro de oro, personificando el dominio de la razón sobre las mareas del inconsciente.",
            "curiosidad_2": "A sus lados saltan un pez en el agua y navega un barco mercante sobre las olas, demostrando que sabe convivir con las emociones sin zozobrar.",
            "historia_titulo": "El Monarca del Mar en Calma",
            "historia_relato": "Las olas azotaban con furia la roca del faro real y el viento aullaba como una manada de lobos. Todos en la corte corrían aterrorizados presagiando el naufragio del reino. Solo el Rey permaneció sentado en su trono flotante, con la copa en la mano derecha y la mirada serena fija en la tormenta. No gritó órdenes desesperadas; respiró con tal hondura y paz que su propia calma se extendió como aceite sobre las olas enfurecidas. Al poco tiempo, el mar enmudeció: un líder que sabe gobernar sus propias emociones puede apagar cualquier tempestad."
        },

        # ESPADAS
        "as-de-espadas": {
            "diferenciador": "La fuerza primordial del intelecto, la verdad cortante y la claridad absoluta. Una mano divina sostiene una espada de doble filo coronada por una corona de laurel y palma.",
            "curiosidad_1": "De la corona caen seis gotas de yod luminosas, garantizando que la verdad y la justicia proceden de la sabiduría celestial.",
            "curiosidad_2": "El paisaje de fondo muestra montañas escarpadas y afiladas bajo un cielo frío y despejado, reflejando la altitud del pensamiento lúcido.",
            "historia_titulo": "La Hoja que Corta la Niebla",
            "historia_relato": "Durante décadas, el tribunal de la corte estuvo paralizado por mentiras entrelazadas y abogados que enredaban las leyes. Un joven juez, cansado de la farsa, desenvainó la espada de acero templado y la clavó en la mesa de roble: 'Basta de palabras que confunden. La verdad no tiene dos versiones; o es verdad o es mentira'. El filo de su honestidad cortó los engaños en un segundo y la luz volvió a reinar en el tribunal. Quien empuña la verdad con pureza no necesita alzar la voz."
        },
        "dos-de-espadas": {
            "diferenciador": "A diferencia del 2 de Bastos (visión de futuro) o del 2 de Copas (unión afectiva), el 2 de Espadas es el bloqueo defensivo: una mujer con los ojos vendados sostiene dos pesadas espadas cruzadas sobre su pecho protegiendo su corazón.",
            "curiosidad_1": "El mar a sus espaldas muestra islotes rocosos peligrosos y una luna creciente en el cielo, indicando que la calma es solo una tregua superficial.",
            "curiosidad_2": "La venda en sus ojos no fue impuesta por un verdugo, sino colocada por ella misma para no tener que ver una realidad dolorosa.",
            "historia_titulo": "La Dama de la Venda Blanca",
            "historia_relato": "Sentada sobre un banco de piedra frente a los arrecifes, la mujer cruzaba dos espadas de plata sobre su pecho. No quería mirar hacia la derecha (donde el deber le exigía hablar) ni hacia la izquierda (donde el deseo le pedía callar). Creía que manteniéndose inmóvil y ciega con su venda blanca evitaría el dolor del conflicto. Pero el viento nocturno le susurró al oído: 'Bajar las espadas dolerá un instante; mantenerlas en alto te dejará congelada para siempre'. Respiró hondo y comenzó a desatar el nudo de su venda."
        },
        "tres-de-espadas": {
            "diferenciador": "Una de las imágenes más emblemáticas del dolor humano: un corazón rojo puro atravesado por tres espadas de acero bajo un cielo gris de lluvia y tormenta incesante.",
            "curiosidad_1": "No hay figuras humanas en la carta: el dolor del desamor, la traición o la pérdida se experimenta como una herida universal del alma.",
            "curiosidad_2": "Las tres espadas representan el choque destructivo entre el pensamiento, la palabra hiriente y la acción desleal.",
            "historia_titulo": "El Corazón Bajo la Lluvia Gris",
            "historia_relato": "El joven sentía que su pecho sangraba tras escuchar las palabras frías y desleales de quien más amaba en el mundo. La lluvia caía sobre sus hombros empapándolo hasta los huesos y el dolor era tan agudo que creyó que moriría allí mismo. Un anciano médico se acercó y le dijo con infinita piedad: 'Llora todo lo que tengas que llorar, muchacho. El corazón roto no es el final de tu historia; es la prueba de que fuiste capaz de amar con verdad. Las heridas del acero purifican el alma de quien sabe perdonar'."
        },
        "cuatro-de-espadas": {
            "diferenciador": "A diferencia del 4 de Bastos (celebración) o del 4 de Copas (apatía), el 4 de Espadas es la tregua necesaria, el reposo del guerrero y la recuperación silenciosa en el santuario tras la batalla.",
            "curiosidad_1": "La efigie del caballero descansa sobre su tumba en actitud de oración con tres espadas colgadas en la pared y una cuarta a su lado lista para cuando despierte.",
            "curiosidad_2": "La vidriera de colores muestra a un santo bendiciendo a un suplicante, recordando el poder sanador de la fe y el retiro.",
            "historia_titulo": "La Tregua en la Cripta de Piedra",
            "historia_relato": "Con la armadura abollada y los músculos temblando tras semanas de asedio, el caballero entró en la capilla del bosque y se recostó sobre la lápida de mármol. Dejó su espada al costado, juntó las manos sobre el pecho y cerró los ojos escuchando el eco de la lluvia en las vidrieras góticas. No estaba derrotado; simplemente sabía que ningún acero puede combatir sin descanso. Durante tres días durmió en paz; al cuarto amanecer se levantó con la mente clara y la fuerza de un gigante."
        },
        "cinco-de-espadas": {
            "diferenciador": "A diferencia del 5 de Bastos (competencia leal), el 5 de Espadas es la victoria pírrica: un hombre sonríe con desdén recogiendo las espadas de sus rivales derrotados, que se alejan llorando humillados al fondo.",
            "curiosidad_1": "El cielo muestra nubes desgarradas y agitadas por un viento hostil, simbolizando la amargura que deja la soberbia y la falta de empatía.",
            "curiosidad_2": "Ha ganado la discusión y el botín, pero ha perdido la confianza, la amistad y el respeto de todos sus compañeros.",
            "historia_titulo": "La Victoria Amarga del Campo de Duelo",
            "historia_relato": "El espadachín se burló a carcajadas de sus dos contrincantes mientras recogía sus armas caídas en el lodo. Les había ganado la partida con trucos sucios y palabras hirientes. Pero al volverse para celebrar su triunfo, descubrió que estaba completamente solo en medio del páramo: nadie le aplaudía, nadie le esperaba en la posada y sus amigos se alejaban cabizbajos jurando no volver a hablarle jamás. Comprendió con un nudo en la garganta que ganar humillando a los demás es la peor de todas las derrotas."
        },
        "seis-de-espadas": {
            "diferenciador": "A diferencia del 8 de Copas (marcha solitaria a pie), el 6 de Espadas es la travesía hacia la sanación: un barquero transporta a una madre y a su hijo en una barca con seis espadas clavadas en la proa, dejando atrás aguas turbulentas hacia una orilla serena.",
            "curiosidad_1": "A la derecha de la barca el agua está agitada y con olas; a la izquierda, el agua se vuelve calma como un espejo, confirmando la mejoría.",
            "curiosidad_2": "Las seis espadas viajan en la barca, simbolizando que no se puede borrar el pasado de golpe, pero sí se puede navegar con él hacia la paz.",
            "historia_titulo": "La Barca de las Aguas Tranquilas",
            "historia_relato": "Cubiertos con mantas oscuras, la madre y el niño permanecían en silencio mientras el barquero empujaba su pértiga en el fondo del río. Dejaban atrás la ciudad en llamas donde habían sufrido tanto dolor. Al principio, las olas mecían la barca con violencia y el miedo atenazaba sus gargantas; pero a medida que avanzaban hacia la otra orilla, las aguas se volvieron mansas y el sol comenzó a asomar tras los cipreses. Las heridas del pasado aún viajaban con ellos, pero la tormenta había quedado atrás para siempre."
        },
        "siete-de-espadas": {
            "diferenciador": "Conocida como la carta de la astucia, el sigilo o la evasión. Un hombre se aleja puntillas del campamento enemigo llevándose cinco espadas en sus brazos y dejando dos clavadas en el suelo.",
            "curiosidad_1": "Mira hacia atrás con una sonrisa pícara, confiando en que no ha sido descubierto, aunque su huida revela falta de confrontación directa.",
            "curiosidad_2": "Al fondo se ven las tiendas de campaña militares con los soldados desprevenidos, simbolizando que la estrategia evitó un derramamiento de sangre.",
            "historia_titulo": "El Ladrón de las Cinco Hojas",
            "historia_relato": "El espía del rey entró a medianoche en el campamento de los invasores. En lugar de quemar las tiendas o despertar a los guardias, desarmó en silencio cinco de sus mejores espadas y se las llevó bajo el brazo caminando de puntillas entre la hierba. Cuando los invasores despertaron por la mañana, descubrieron que no podían combatir sin sus armas principales y tuvieron que retirarse sin derramar una gota de sangre. Hay batallas que no se ganan con fuerza bruta, sino con astucia silenciosa."
        },
        "ocho-de-espadas": {
            "diferenciador": "A diferencia del Colgado (sacrificio voluntario iluminado), el 8 de Espadas es la trampa mental autoimpuesta: una mujer atada y con los ojos vendados está rodeada por ocho espadas clavadas en el suelo, pero no hay verdugos y el sendero hacia la salida está libre.",
            "curiosidad_1": "Las cuerdas que la atan están flojas alrededor de sus brazos y sus pies no están atados, demostrando que su parálisis es puramente psicológica.",
            "curiosidad_2": "El agua del suelo moja sus pies, recordándole que la intuición y las emociones pueden ayudarla a despertar y liberarse.",
            "historia_titulo": "La Jaula de los Pensamientos",
            "historia_relato": "La mujer lloraba creyendo que estaba en el calabozo más oscuro del reino. Sentía ocho hojas de acero rodeándola y una venda que no la dejaba ver. Estuvo inmóvil durante días temiendo que el menor movimiento la atravesase. Pero al caer una gota de lluvia en su frente, se estremeció y movió los brazos: las cuerdas se desprendieron con facilidad y al quitarse la venda descubrió que las espadas estaban clavadas a un metro de distancia y que el camino a su casa estaba completamente despejado. Su única carcelera había sido su propia mente temerosa."
        },
        "nueve-de-espadas": {
            "diferenciador": "El tormento de la mente nocturna: una figura sentada en su cama con la cabeza entre las manos, consumida por la angustia, el insomnio, la culpa o las pesadillas, mientras nueve espadas cuelgan en la pared sobre ella.",
            "curiosidad_1": "El cobertor de la cama está decorado con rosas rojas y signos del zodiaco, recordando que la vida real sigue siendo hermosa a pesar del dolor mental.",
            "curiosidad_2": "Las espadas no tocan a la persona: representan pensamientos obsesivos y temores imaginarios que torturan más que la propia realidad.",
            "historia_titulo": "La Noche de los Nueve Fantasmas",
            "historia_relato": "A las tres de la madrugada, el anciano se despertó con el corazón desbocado. En la penumbra de su habitación, cada error del pasado parecía una espada suspendida sobre su cabeza lista para caer. Se tapó la cara con las manos y lloró de angustia creyendo que todo estaba perdido. Pero cuando el primer rayo de sol cruzó la ventana, los monstruos se disolvieron en polvo dorado y el canto de los gorriones llenó la estancia. Comprendió el gran secreto: la noche agranda los fantasmas, pero el sol siempre devuelve las cosas a su tamaño real."
        },
        "diez-de-espadas": {
            "diferenciador": "El fondo absoluto del sufrimiento mental y el fin definitivo de una pesadilla: un hombre yace boca abajo atravesado por diez espadas, pero en el horizonte el cielo negro comienza a iluminarse con una franja de oro radiante sobre el mar en calma.",
            "curiosidad_1": "Su mano derecha forma el gesto de la bendición sagrada, revelando que en la muerte del ego reside la liberación del alma.",
            "curiosidad_2": "El cielo es negro arriba pero amanece amarillo abajo: lo peor ya ha pasado y a partir de este instante solo se puede subir.",
            "historia_titulo": "El Amanecer tras la Décima Hoja",
            "historia_relato": "El viajero cayó tendido sobre la arena del páramo tras recibir el último golpe de la adversidad. Creía que aquel era el final amargo de su existencia y cerró los ojos aceptando su destino. Pero pasaron las horas y descubrió que el dolor ya no aumentaba: había tocado el fondo más profundo de la prueba. Cuando abrió los ojos, vio una franja de oro puro naciendo en el horizonte del mar. La pesadilla había terminado definitivamente; ya no había nada más que temer, porque quien ha muerto a sus ilusiones renace libre para siempre."
        },
        "sota-de-espadas": {
            "diferenciador": "A diferencia de la Sota de Bastos (entusiasta) o de Oros (trabajadora), la Sota de Espadas es la vigilancia analítica, la curiosidad intelectual afilada y la disposición a defender la verdad.",
            "curiosidad_1": "Sostiene una espada con ambas manos mirando por encima del hombro, alerta ante cualquier engaño en el horizonte ventoso.",
            "curiosidad_2": "El viento agita su pelo y las nubes vuelan rápidas en el cielo, simbolizando una mente despierta y perspicaz.",
            "historia_titulo": "El Vigía de la Colina Ventosa",
            "historia_relato": "Desde el promontorio más alto, el joven vigía escudriñaba el horizonte con su espada desenvainada. No se dejaba engañar por las banderas blancas de los mercaderes ni por los cantos de los trovadores: sus ojos afilados veían los detalles que todos pasaban por alto. Gracias a su alerta temprana, la ciudad evitó caer en una emboscada traicionera. La inteligencia no necesita años de experiencia; necesita honestidad para no engañarse a sí misma."
        },
        "caballero-de-espadas": {
            "diferenciador": "A diferencia de los otros tres caballeros, el de Espadas cabalga a toda velocidad contra el viento con la espada en alto, impulsado por una idea fija y una determinación implacable sin medir riesgos.",
            "curiosidad_1": "Su caballo parece volar sobre el terreno con la crin al viento, mientras los árboles se doblan por la fuerza del huracán mental.",
            "curiosidad_2": "La expresión del caballero es feroz y decidida, encarnando el celo por la justicia o la impaciencia destructiva si no se modera.",
            "historia_titulo": "La Carga del Viento del Norte",
            "historia_relato": "Apenas escuchó la llamada de socorro, el caballero desenvainó su espada y espoleó a su corcel hacia el desfiladero sin esperar refuerzos ni planificar la ruta. Cabalgó contra la ventisca cortando el aire como un relámpago. Su audacia desbarató los planes de los bandidos por puro efecto sorpresa; sin embargo, al mirar atrás, vio que su caballo sangraba por el sobreesfuerzo. Comprendió la gran lección de la espada: la rapidez de pensamiento es una virtud suprema, siempre que no atropelle el corazón de quienes cabalgan a tu lado."
        },
        "reina-de-espadas": {
            "diferenciador": "La soberana del discernimiento lúcido y la independencia moral. Sentada de perfil en su trono esculpido con mariposas, alza una espada vertical con su mano derecha mientras su mano izquierda invita al diálogo honesto.",
            "curiosidad_1": "Su rostro severo pero sereno refleja a alguien que ha sufrido mucho pero ha transformado el dolor en sabiduría incorruptible.",
            "curiosidad_2": "Las mariposas en su trono simbolizan la metamorfosis del pensamiento a través de la superación del sufrimiento.",
            "historia_titulo": "La Dama del Veredicto Justo",
            "historia_relato": "En la sala de audiencias, la Reina no se dejaba conmover por lamentos teatrales ni por halagos cortesanos. Su mirada gris leía el alma de los litigantes como un libro abierto. Con su mano alzada pedía silencio y con una sola frase certera desarmaba la mentira más elaborada. Sin embargo, cuando una viuda pobre se arrodilló temblando, la Reina bajó de su trono, la tomó de la mano y le ofreció cobijo: había aprendido que la verdadera justicia que no está templada por la compasión no es más que tiranía fría."
        },
        "rey-de-espadas": {
            "diferenciador": "El juez supremo del intelecto, la ética inquebrantable y la autoridad de la ley. Sentado de frente en su trono con querubines y mariposas, sostiene la espada apuntando al cielo ligeramente inclinada hacia la derecha.",
            "curiosidad_1": "Viste un manto azul y púrpura sobre una túnica carmesí, combinando la serenidad espiritual con la realeza y el juicio implacable.",
            "curiosidad_2": "El cielo a sus espaldas está casi despejado, mostrando que su mente ha purgado todas las nubes de la confusión y el sesgo emocional.",
            "historia_titulo": "El Magistrado de la Espada Recta",
            "historia_relato": "El Rey gobernaba el imperio no con ejércitos de hierro, sino con la exactitud de sus códigos de justicia y la imparcialidad de sus sentencias. Nadie podía comprar su favor ni torcer su juicio con amenazas. Incluso cuando su propio hermano cometió un delito, el Rey aplicó la misma ley sin pestañear. Pero aquella noche, en la soledad de sus aposentos, lloró en silencio por su hermano: un gobernante sabio debe ser duro como el diamante en público para sostener el orden de todos, aunque su corazón sangre en privado."
        },

        # OROS
        "as-de-oros": {
            "diferenciador": "La semilla primordial de la abundancia material, la prosperidad tangible y la salud corporal. Una mano divina ofrece un gran pentáculo de oro macizo sobre un jardín amurallado rebosante de flores blancas y un arco de lirios.",
            "curiosidad_1": "El arco de rosas y lirios al fondo abre paso hacia una montaña lejana, indicando que este regalo terrenal es la base para una gran ascensión espiritual.",
            "curiosidad_2": "El pentáculo grabado en la moneda representa los cuatro elementos integrados bajo el gobierno del espíritu divino.",
            "historia_titulo": "La Moneda del Jardín Cerrado",
            "historia_relato": "En el huerto del monasterio, un monje descalzo cavaba la tierra seca para sembrar hortalizas. Su pala golpeó algo metálico: al limpiar el barro, descubrió un gran medallón de oro puro grabado con una estrella de cinco puntas. No corrió a fundirlo ni a comprar lujos; lo usó para comprar semillas de trigo y madera para edificar un hospital para los pobres de la comarca. Al cabo de un año, el huerto alimentaba a cientos de familias. La verdadera riqueza no es la que se acumula en un cofre, sino la que se siembra para multiplicar la vida."
        },
        "dos-de-oros": {
            "diferenciador": "El arte del equilibrio dinámico en la vida cotidiana: un joven vestido de bufón hace malabares con dos monedas de oro dentro de una lemniscata infinita, mientras al fondo barcos navegan sobre olas agitadas.",
            "curiosidad_1": "La lemniscata de cinta verde conecta los dos oros, recordando que el flujo del dinero y la energía vital debe circular constantemente sin estancarse.",
            "curiosidad_2": "Los barcos al fondo suben y bajan sobre las olas sin zozobrar, simbolizando la capacidad de adaptarse a los altibajos económicos con flexibilidad y humor.",
            "historia_titulo": "El Malabarista del Puerto",
            "historia_relato": "En los muelles del puerto bullicioso, el joven estibador bailaba sobre un pie mientras hacía girar dos pesadas monedas de oro en el aire sin que cayeran jamás. Los comerciantes le gritaban agobiados por las deudas y las aduanas, preguntándole cómo podía sonreír en medio de tanta crisis. 'Si intentas sostener una moneda rígida, el barco se inclina y caes al agua', contestó riendo; 'pero si acompañas el vaivén de las olas y mantienes la energía en movimiento, hasta la peor marea se convierte en una danza'."
        },
        "tres-de-oros": {
            "diferenciador": "A diferencia del 8 de Oros (maestría en soledad), el 3 de Oros es el trabajo en equipo, la maestría reconocida y la colaboración interdisciplinaria: un artesano cantero consulta los planos de una catedral gótica con un monje y un arquitecto.",
            "curiosidad_1": "Las tres monedas de oro forman un triángulo sagrado en el arco de piedra de la catedral, simbolizando la consagración del trabajo manual a la belleza divina.",
            "curiosidad_2": "El cantero viste un delantal y se sube a un banco de madera para estar al mismo nivel que los dignatarios, demostrando que el talento artesanal tiene la misma dignidad que el clero y la nobleza.",
            "historia_titulo": "Los Tres Constructores de la Catedral",
            "historia_relato": "Un cantero humilde tallaba con esmero una gárgola de piedra en el pórtico de la nueva basílica. El abad le pidió que apresurase el trabajo y el arquitecto criticó la curvatura de la piedra. El artesano no se ofendió; desplegó el pergamino en el suelo, tomó el compás del arquitecto y escuchó las palabras del monje. Entre los tres corrigieron el ángulo y la escultura quedó tan perfecta que parecía cobrar vida con la luz del alba. Ninguna gran obra de este mundo la levantó un hombre solo; las catedrales se erigen cuando el sabio, el diseñador y el artesano unen sus talentos con humildad."
        },
        "cuatro-de-oros": {
            "diferenciador": "El apego material, la tacañería y la seguridad asfixiante: un hombre sentado corona su cabeza con una moneda, abraza otra con sus brazos y pisa dos monedas con sus pies, incapaz de moverse por miedo a perder lo que tiene.",
            "curiosidad_1": "La ciudad amurallada a sus espaldas queda lejos de su alcance: el avaro vive aislado de la sociedad por su obsesión con retener sus pertenencias.",
            "curiosidad_2": "No puede dar un solo paso porque sus propios pies están atados a las monedas, simbolizando que el dinero lo posee a él y no al revés.",
            "historia_titulo": "El Guardián del Cofre Cerrado",
            "historia_relato": "El mercader pasaba las noches sentado sobre su cofre de caudales en la torre del pueblo. Llevaba una moneda en la cabeza como corona, abrazaba otra contra su estómago y pisaba dos monedas con las suelas de sus zapatos. Tenía tanto miedo de que le robaran que no se atrevía a salir al sol, ni a comer caliente, ni a recibir a sus nietos. Murió de frío en una noche de invierno sobre su oro brillante. Al abrir el cofre, sus herederos descubrieron que la mitad de las monedas se habían enmohecido: lo que no se comparte y no circula, termina envenenando a su dueño."
        },
        "cinco-de-oros": {
            "diferenciador": "La sensación de pobreza, exclusión y desamparo material: dos mendigos harapientos caminan en la nieve frente a una vidriera iluminada de iglesia sin ver que el refugio está abierto.",
            "curiosidad_1": "Uno de los mendigos camina con muletas y lleva un cascabel al cuello (señal medieval de enfermedad o lepra), pero caminan juntos apoyándose con amor.",
            "curiosidad_2": "La vidriera de colores muestra cinco monedas de oro iluminadas con calor humano, pero los caminantes miran al suelo helado sin alzar la vista hacia la puerta abierta.",
            "historia_titulo": "La Ventana Cálida en la Ventisca",
            "historia_relato": "Dos peregrinos tiritaban en la tormenta de nieve con los pies congelados y las ropas desgarradas. Se quejaban con amargura de que el mundo era cruel y de que Dios los había abandonado a su suerte en la noche helada. Pasaron justo por delante de la vidriera dorada de la abadía donde se escuchaba el fuego de la chimenea y el canto de los frailes. Un niño abrió la puerta y les gritó con una vela en la mano: '¡Pasen, hermanos, que la sopa está servida y el fuego encendido!'. Solo tuvieron que levantar la mirada del suelo helado para descubrir que el cobijo siempre había estado a un metro de distancia."
        },
        "seis-de-oros": {
            "diferenciador": "La generosidad justa y la redistribución equilibrada: un mercader próspero reparte monedas a dos suplicantes arrodillados mientras sostiene una balanza en su mano izquierda para dar a cada uno según su necesidad real.",
            "curiosidad_1": "La balanza en su mano garantiza que su caridad no es un capricho humillante ni un acto de condescendencia egoísta, sino un acto de justicia distributiva.",
            "curiosidad_2": "Las seis monedas están repartidas en el aire entre el donante y los receptores, simbolizando el circuito sagrado del dar y el recibir.",
            "historia_titulo": "El Mercader de la Balanza Justa",
            "historia_relato": "Un sabio comerciante bajó a la plaza del mercado con una bolsa de monedas y una pequeña balanza de bronce. Se le acercaron dos hombres necesitados: uno tenía una familia enferma y el otro necesitaba herramientas para volver a labrar su tierra. El mercader pesó las monedas con cuidado y entregó a cada uno exactamente lo que requería para volver a ponerse en pie. 'La caridad que solo regala sobras humilla al que recibe', les dijo con una sonrisa afectuosa; 'la verdadera generosidad es la que te da el andamio para que vuelvas a caminar por tus propios medios'."
        },
        "siete-de-oros": {
            "diferenciador": "La paciencia del agricultor y la evaluación de la cosecha: un joven campesino se apoya en su azadón contemplando un arbusto donde cuelgan siete grandes monedas de oro que están madurando lentamente.",
            "curiosidad_1": "Su postura no es de agotamiento ni de pereza, sino de contemplación meditativa: sabe que tirar de los brotes no los hace crecer más rápido.",
            "curiosidad_2": "Una de las monedas descansa a sus pies lista para el uso inmediato, mientras las otras seis continúan en la planta acumulando dulzura.",
            "historia_titulo": "La Siembra del Viñedo Silencioso",
            "historia_relato": "El joven labrador pasó la primavera y el verano regando los sarmientos bajo el sol abrasador. Llegó el otoño y los vecinos le decían que arrancara las uvas de inmediato para venderlas antes que nadie. El muchacho se apoyó en su azadón, probó una uva y sintió que aún le faltaba un punto de acidez para alcanzar la gloria. 'Quien cosecha por codicia bebe vinagre agrio', dijo con calma; 'quien sabe esperar la última helada destila el vino de los reyes'. Esperó dos semanas más y su vino fue premiado en todas las cortes del reino."
        },
        "ocho-de-oros": {
            "diferenciador": "A diferencia del 3 de Oros (trabajo en equipo), el 8 de Oros es la maestría artesanal individual, la dedicación paciente, el aprendizaje concentrado y la devoción por el trabajo bien hecho.",
            "curiosidad_1": "El artesano está absorto cincelando una moneda con martillo y cincel, mientras seis monedas ya terminadas cuelgan alineadas en un poste y una séptima descansa en el suelo.",
            "curiosidad_2": "La ciudad se ve a lo lejos en el horizonte, indicando que el aprendiz se ha apartado temporalmente de las distracciones urbanas para perfeccionar su oficio.",
            "historia_titulo": "El Grabador de las Ocho Estrellas",
            "historia_relato": "En su pequeño taller a las afueras de la ciudad, el joven orfebre tallaba con paciencia infinita la octava moneda de oro. Llevaba días puliendo la misma arista con una lija de diamante. Un amigo entró corriendo y le dijo: '¿Por qué pierdes tanto tiempo en una moneda que nadie va a mirar con lupa? Entrégala ya y cóbrala'. El artesano sopló el polvo de oro con ternura y contestó: 'Los hombres comunes miran la prisa; los maestros miran el alma que dejas en cada trazo. Cuando amas lo que haces, cada golpe de martillo es una oración'."
        },
        "nueve-de-oros": {
            "diferenciador": "La culminación del refinamiento material y la independencia personal: una dama aristocrática pasea elegantemente por su jardín privado rebosante de viñedos y monedas de oro, llevando un halcón encapuchado en su mano enguantada.",
            "curiosidad_1": "El halcón domesticado representa los instintos salvajes y el intelecto entrenados para servir a la belleza y a la serenidad de la dama.",
            "curiosidad_2": "Un pequeño caracol cruza el camino a sus pies, simbolizando que la verdadera riqueza y la elegancia se forjan paso a paso sin prisas.",
            "historia_titulo": "La Dama del Viñedo y el Halcón",
            "historia_relato": "La mujer caminaba despacio por su viñedo dorado sintiendo la brisa suave del atardecer. Llevaba en su mano izquierda un halcón encapuchado que descansaba en perfecta calma sobre su guante de cuero bordado. No dependía de ningún mecenas ni de ningún pretendiente; había levantado aquella finca con su propia inteligencia, disciplina y esfuerzo continuado. Se detuvo a acariciar las plumas del halcón y sonrió: la mayor riqueza no son las joyas ni las tierras, sino la bendita libertad de ser dueña absoluta de tu propio destino."
        },
        "diez-de-oros": {
            "diferenciador": "La cumbre de la prosperidad familiar, la herencia multigeneracional y la estabilidad patrimonial consolidada: tres generaciones conviven en el arco señorial de un palacio junto a sus fieles perros.",
            "curiosidad_1": "Un anciano venerado cubierto con una capa de motivos mágicos acaricia a dos perros de caza mientras su hijo, su nuera y su nieto juegan bajo el arco de piedra.",
            "curiosidad_2": "Las diez monedas están dispuestas según el patrón exacto del Árbol de la Vida de la Cábala (las diez Sephiroth), demostrando que la materia ha sido plenamente consagrada a la armonía divina.",
            "historia_titulo": "El Legado del Patriarca en el Arco de Piedra",
            "historia_relato": "Bajo el arco de entrada de la antigua casona señorial, el abuelo descansaba cubierto con una manta de lana bordada. A sus pies dormitaban sus dos fieles lebreles y unos metros más allá su hijo conversaba con su esposa mientras el nieto pequeño perseguía a una paloma en el patio. El anciano contempló las diez monedas de oro grabadas en el dintel de piedra y sintió una paz infinita en el pecho: su verdadero legado no eran las tierras ni los títulos nobiliarios, sino la raíz sólida de una familia unida que continuaría su memoria con amor y dignidad por generaciones."
        },
        "sota-de-oros": {
            "diferenciador": "A diferencia de la Sota de Bastos (aventura) o de Espadas (vigilancia), la Sota de Oros es el estudiante aplicado, el joven con devoción por el estudio práctico, la naturaleza y la construcción paciente.",
            "curiosidad_1": "Sostiene una gran moneda de oro flotando sobre las palmas de sus manos, contemplándola con reverencia como si fuera un objeto de estudio sagrado.",
            "curiosidad_2": "Camina sobre un campo recién arado donde ya brotan los primeros tallos verdes, reflejando el inicio fértil de una gran vocación profesional.",
            "historia_titulo": "El Aprendiz de la Semilla de Oro",
            "historia_relato": "En la escuela de agricultura del valle, el joven estudiante no corría a jugar con los demás al terminar la clase. Se quedaba en el campo arado sosteniendo en sus manos una semilla dorada y examinándola con lupa. Sabía que dentro de aquel grano diminuto dormía un bosque entero si se le daba agua, tierra fértil y paciencia infinita. Aquel joven muchacho se convirtió con los años en el mayor botánico de su tiempo: había aprendido que para cosechar un roble centenario hay que amar primero a la pequeña semilla."
        },
        "caballero-de-oros": {
            "diferenciador": "El único caballero cuyo caballo está completamente quieto con las cuatro patas firmes en la tierra. Representa la perseverancia incansable, la lealtad, la ética del trabajo y la constancia inquebrantable.",
            "curiosidad_1": "Monta un imponente caballo negro percherón de labranza y guerra, adornado con hojas de roble, símbolo de fuerza y resistencia sobrehumana.",
            "curiosidad_2": "Lleva un penacho de espigas de trigo en su casco y contempla el pentáculo con la mirada fija en el objetivo terrenal.",
            "historia_titulo": "El Caballero del Surco Infatigable",
            "historia_relato": "Los otros caballeros del reino se burlaban de él porque su montura no saltaba zanjas ni embestía alocadamente en torneos de exhibición. Pero cuando una helada amenazó los graneros del rey y hubo que cruzar la cordillera con miles de sacos de trigo, los caballos ágiles se rompieron las patas en el hielo y solo el corcel negro del Caballero de Oros avanzó paso a paso, con paso firme y seguro, sin retroceder un solo centímetro. Llegó a destino con cada saco intacto: la constancia silenciosa siempre gana la carrera que la impaciencia pierde."
        },
        "reina-de-oros": {
            "diferenciador": "La soberana del bienestar práctico, la calidez maternal terrenal y la prosperidad generosa. Sentada en un trono de madera tallado con cabras, frutos y ángeles en medio de un prado florido, sostiene el pentáculo con ternura en su regazo.",
            "curiosidad_1": "Un conejo silvestre salta a la derecha del trono, simbolizando la fertilidad desbordante de la naturaleza y la pureza biológica.",
            "curiosidad_2": "La corona de ramas y flores en su cabeza confirma su conexión directa con la Madre Tierra y su generosidad nutricia.",
            "historia_titulo": "La Señora de la Casa Abundante",
            "historia_relato": "En la hacienda de la colina, la Reina recibía a labradores y viajeros con un plato caliente de guiso recién hecho y una sonrisa acogedora. Sus manos sabían amasar el pan, curar las fiebres con hierbas del huerto y administrar los graneros de la provincia con una precisión admirable. 'La verdadera señora de la tierra', solía decir mientras acariciaba a un conejo del jardín, 'no es la que encierra el grano en arcas blindadas, sino la que sabe hacer de su hogar un refugio cálido donde nadie pasa hambre ni frío'."
        },
        "rey-de-oros": {
            "diferenciador": "La máxima autoridad en el plano material: el monarca de la estabilidad financiera, el maestro de los negocios prósperos y el señor del éxito consolidado. Sentado en un trono adornado con cabezas de toros, su manto está estampado con racimos de uvas maduras.",
            "curiosidad_1": "Su pie calzado con armadura pisa la cabeza de un toro de piedra, simbolizando su dominio absoluto sobre el signo de Tauro y las riquezas de la tierra.",
            "curiosidad_2": "Detrás de él se alza un imponente castillo con jardines florecientes, demostrando que su imperio ha sido construido con paciencia y visión a largo plazo.",
            "historia_titulo": "El Monarca del Viñedo Imperial",
            "historia_relato": "El Rey de la Ciudad Blanca no necesitaba dictar leyes severas ni amenazar con guardias para que su pueblo prosperara. Había trazado canales de riego que convertían los pantanos en arrozales y fundado gremios que enseñaban oficios a cada huérfano del reino. Sentado en su trono de piedra entre viñedos de uva moscatel, sostenía su cetro y su moneda con la calma de un roble milenario. Su mayor orgullo no era la corona de oro que llevaba en la cabeza, sino saber que en todo su territorio ningún niño se acostaba sin pan y que cada trabajador recibía el fruto justo de su esfuerzo."
        }
    }

    for suit_name, sinfo in suits_meta.items():
        folder = sinfo["folder"]
        for slug_rank, rank_name, number in ranks:
            card_id = f"{slug_rank}-de-{folder}"
            filename = f"{slug_rank}_de_{folder}.xml"
            full_name = f"{rank_name} de {suit_name}"
            
            # Retrieve or construct detail
            detail = cards_detail.get(card_id, {})
            diferenciador = detail.get("diferenciador", f"A diferencia de otras cartas del palo de {suit_name}, {full_name} encarna una etapa fundamental en el desarrollo de {sinfo['theme']}.")
            curiosidad_1 = detail.get("curiosidad_1", f"En la baraja Rider-Waite-Smith, {full_name} contiene símbolos iconográficos consagrados a la tradición hermética de {sinfo['element']}.")
            curiosidad_2 = detail.get("curiosidad_2", f"El número {number} en la Cábala esotérica representa una emanación de las Sephiroth aplicadas al plano de {sinfo['element']}.")
            historia_titulo = detail.get("historia_titulo", f"La Parábola de {full_name}")
            historia_relato = detail.get("historia_relato", f"En las tierras donde gobierna el elemento {sinfo['element']}, un viajero descubrió el poder de {full_name} al comprender que {sinfo['theme']} se forja con constancia y pureza de corazón.")

            card_obj = {
                "id": card_id,
                "number": number,
                "roman": str(number),
                "name": full_name,
                "folder": folder,
                "filename": filename,
                "type": "Arcano Menor",
                "suit": suit_name,
                "element": sinfo["element"],
                "astrology": sinfo["astro_base"][(number - 1) % len(sinfo["astro_base"])],
                "historia": (
                    f"El palo de {suit_name} ({sinfo['element']}) tiene su origen en las barajas mamelucas del siglo XIV "
                    f"y fue incorporado a los tarots renacentistas italianos como símbolo de {sinfo['theme']}. "
                    f"En la baraja Rider-Waite-Smith de 1909, Pamela Colman Smith ilustró por primera vez escenas narrativas completas "
                    f"para esta carta, transformando {full_name} en un mapa psicológico vivo de las experiencias humanas cotidianas."
                ),
                "significado_fundamental": (
                    f"{full_name} representa la manifestación de {sinfo['theme']} en el grado {number}. "
                    f"Enseña a canalizar la energía de {sinfo['element']} con consciencia, equilibrio y propósito práctico en la vida cotidiana."
                ),
                "posicion_normal": {
                    "resumen": f"Expresión constructiva, fluida y armónica de {sinfo['theme']}.",
                    "amor": f"En los vínculos afectivos, {full_name} aporta lealtad, comunicación constructiva y comprensión profunda de las necesidades mutuas.",
                    "dinero_trabajo": f"En el plano profesional y financiero, favorece el avance metódico, la resolución de tareas y el logro de metas mediante el esfuerzo honesto.",
                    "salud": f"Bienestar físico y equilibrio energético alineado con el elemento {sinfo['element']}.",
                    "espiritualidad": f"Lección de vida que integra la experiencia cotidiana con la evolución del alma."
                },
                "posicion_invertida": {
                    "resumen": f"Bloqueo, exceso o distorsión temporal en la energía de {sinfo['theme']}.",
                    "amor": f"Malentendidos, impaciencia o falta de empatía en las relaciones que requieren diálogo sincero y reconciliación.",
                    "dinero_trabajo": f"Retrasos transitorios, distracciones o necesidad de revisar planes y presupuestos antes de actuar.",
                    "salud": f"Agotamiento o desequilibrio en los hábitos diarios; necesidad de descansar y escuchar las señales del cuerpo.",
                    "espiritualidad": f"Oportunidad de aprendizaje kármico: reconocer errores de juicio para corregir el rumbo con humildad."
                },
                "lo_que_lo_hace_unico": diferenciador,
                "curiosidades": [
                    curiosidad_1,
                    curiosidad_2,
                    f"Tradicionalmente, en la adivinación cartomántica clásica europea, {full_name} se asociaba con augurios concretos relacionados con {sinfo['theme']}."
                ],
                "historia_inspirada": {
                    "titulo": historia_titulo,
                    "relato": historia_relato
                },
                "audio": {
                    "archivo": f"assets/audio/{card_id}.mp3",
                    "titulo": f"{full_name} - Sabiduría y Reflexión",
                    "duracion_estimada": "3:45 min"
                }
            }
            minors.append(card_obj)

    return minors

if __name__ == '__main__':
    data = generate_minors_data()
    print(f"Generados exitosamente {len(data)} arcanos menores.")
