# -*- coding: utf-8 -*-
"""
Datos maestros para los Arcanos Mayores del Tarot (11 a 21)
11: La Justicia
12: El Colgado
13: La Muerte
14: La Templanza
15: El Diablo
16: La Torre
17: La Estrella
18: La Luna
19: El Sol
20: El Juicio
21: El Mundo
"""

MAJORS_DATA_2 = [
    # 11. LA JUSTICIA
    {
        "id": "la-justicia",
        "number": 11,
        "roman": "XI",
        "name": "La Justicia",
        "folder": "arcanos_mayores",
        "filename": "11_la_justicia.xml",
        "element": "Aire / Libra",
        "astrology": "Libra",
        "historia": (
            "En el Tarot de Marsella ocupaba el número VIII, pero la Orden Hermética de la Golden Dawn y Arthur Edward Waite "
            "la intercambiaron con La Fuerza para alinearla con el signo de Libra. Inspirada en la diosa griega Temis y en la romana Iustitia, "
            "aparece sentada entre dos pilares de piedra con un velo púrpura de fondo. Sostiene en su mano derecha la espada de doble filo apuntando "
            "al cielo (el discernimiento racional implacable) y en su mano izquierda la balanza de dos platillos (el peso moral exacto de cada acto humano)."
        ),
        "significado_fundamental": (
            "La Justicia encarna la ley inmutable de causa y efecto, la verdad objetiva desprovista de ilusiones emocionales, la equidad y la responsabilidad kármica. "
            "No busca el castigo vengativo, sino el restablecimiento del equilibrio cósmico. Nos recuerda que cosechamos con absoluta precisión matemática "
            "lo que sembramos con nuestras decisiones conscientes e inconscientes."
        ),
        "posicion_normal": {
            "resumen": "Verdad revelada, equilibrio kármico, resolución legal favorable, honestidad inquebrantable y decisiones justas.",
            "amor": "Claridad y honestidad en la pareja. Acuerdos justos, reciprocidad afectiva y superación de malentendidos mediante el diálogo sincero.",
            "dinero_trabajo": "Sentencias o litigios favorables, contratos equitativos, transparencia en negocios y reconocimiento justo del mérito profesional.",
            "salud": "Equilibrio homeostático en el cuerpo. Favorable para regular la dieta, hidratación renal y hábitos que compensan excesos pasados.",
            "espiritualidad": "Consciencia de la ley del karma. Aceptación serena de la propia vida como resultado de causas pasadas y siembra consciente para el futuro."
        },
        "posicion_invertida": {
            "resumen": "Injusticia, sesgos prejuiciosos, problemas legales turbios, deshonestidad o autoculpabilidad desmedida.",
            "amor": "Desequilibrio en la relación donde uno da todo y el otro solo toma. Falta de lealtad, reproches fríos o separaciones conflictivas.",
            "dinero_trabajo": "Sentencias legales desfavorables, estafas en contratos, favoritismos injustos en la empresa o penalizaciones financieras.",
            "salud": "Descompensaciones en el sistema urinario/renal o circulatorio. Dolores de espalda por cargar con culpas o tensiones no resueltas.",
            "espiritualidad": "Victimismo. Creer que el mundo o Dios son injustos en lugar de examinar la propia responsabilidad en los hechos vividos."
        },
        "lo_que_lo_hace_unico": (
            "Es la única figura del Tarot que sostiene simultáneamente el instrumento del intelecto (la espada alzada de dos filos) "
            "y el instrumento del pesaje moral (la balanza). A diferencia de El Juicio (que es una revelación espiritual final de redención cósmica), "
            "La Justicia juzga aquí y ahora en la tierra mediante la ley de las consecuencias cotidianas."
        ),
        "curiosidades": [
            "La espada de dos filos: Recuerda que la verdad corta en ambas direcciones: penetra la mentira del adversario pero también exige honestidad absoluta a quien la empuña.",
            "La piedra cuadrada en su corona: Representa la cuadratura del círculo y la estabilidad de la ley terrenal consagrada al orden divino.",
            "El zapato blanco que asoma: El pie calzado de blanco que apenas se muestra bajo la túnica roja revela que sus decisiones proceden de una base pura y desinteresada."
        ],
        "historia_inspirada": {
            "titulo": "La Balanza de Plumas y Plomo",
            "relato": (
                "En el pórtico de la Gran Ciudad, dos mercaderes acudieron ante la jueza ciega. Uno la acusaba de haberle robado una bolsa de oro; "
                "el otro juraba por los dioses que la bolsa era suya. La jueza no escuchó sus juramentos ni sus lágrimas. Pidió una pluma de lechuza "
                "y una lámina de plomo. Colocó la pluma en un platillo y el plomo en el otro, y ordenó a los mercaderes colocar las manos sobre la balanza. "
                "Bajo el peso de la mano del primer mercader, la balanza tembló con pulso agitado y culpable; bajo la mano del segundo, la balanza "
                "permaneció serena como el agua de un pozo. La jueza desenvainó la hoja de acero y dividió la bolsa: 'El oro vuelve a quien tiene la paz en las entrañas; "
                "las mentiras siempre pesan más que el plomo ante la luz'."
            )
        },
        "audio": {
            "archivo": "assets/audio/la-justicia.mp3",
            "titulo": "La Justicia - La Balanza de la Causa y el Efecto",
            "duracion_estimada": "4:30 min"
        }
    },

    # 12. EL COLGADO
    {
        "id": "el-colgado",
        "number": 12,
        "roman": "XII",
        "name": "El Colgado",
        "folder": "arcanos_mayores",
        "filename": "12_el_colgado.xml",
        "element": "Agua / Neptuno",
        "astrology": "Neptuno",
        "historia": (
            "En la Italia medieval ('L'Appeso') se llamaba 'la pittura infamante', un castigo que se pintaba en los muros públicos contra los traidores, "
            "colgándolos por un pie. Sin embargo, en la tradición esotérica y en el mazo Rider-Waite-Smith, la escena se transforma en la iniciación sagrada "
            "de Odín en el árbol Yggdrasil o en la crucifixión mística voluntaria. El joven cuelga serenamente de un patíbulo de madera viva que brota hojas verdes; "
            "su rostro no muestra agonía sino beatitud absoluta, y una aureola dorada de iluminación resplandece alrededor de su cabeza invertida."
        ),
        "significado_fundamental": (
            "El Colgado es el arquetipo de la pausa sagrada, el cambio radical de perspectiva, el sacrificio voluntario del ego y la rendición confiada. "
            "Enseña que cuando empujar y forcejear ya no sirve de nada, la única victoria reside en soltar el control y dejar que la vida obre. "
            "Al ver el mundo al revés, lo que antes parecía importante se vuelve trivial, y lo que parecía invisible se convierte en la única verdad eterna."
        ),
        "posicion_normal": {
            "resumen": "Pausa necesaria, rendición sabia, ver las cosas desde otro ángulo, soltar el control y despertar de la consciencia.",
            "amor": "Aceptar una etapa de compás de espera en la relación. Mirar el punto de vista de la otra persona con compasión. Sacrificar el orgullo para salvar el vínculo.",
            "dinero_trabajo": "Proyectos en suspensión temporal que permiten corregir errores. No forzar negociaciones; dejar madurar las propuestas sin impaciencia.",
            "salud": "Necesidad urgente de reposo, descompresión de la columna y terapias de inversión o meditación profunda. Evitar el sobreesfuerzo.",
            "espiritualidad": "La iluminación que nace de la rendición. Renunciar al deseo del ego para que la voluntad del Ser Superior tome el timón."
        },
        "posicion_invertida": {
            "resumen": "Resistencia inútil, victimismo estéril, sacrificios inútiles por personas que no lo valoran o estancamiento por cobardía.",
            "amor": "Mártir en el amor: quedarse en relaciones destructivas por apego morboso creyendo falsamente que el sufrimiento purifica.",
            "dinero_trabajo": "Parálisis profesional por miedo a tomar decisiones. Sacrificios laborales desmedidos sin recibir retribución ni reconocimiento.",
            "salud": "Problemas circulatorios en las extremidades, mareos, estancamiento linfático o fatiga por negarse a frenar a tiempo.",
            "espiritualidad": "Espiritualidad evasiva (spiritual bypassing). Usar la pasividad como excusa para no afrontar las responsabilidades del mundo terrenal."
        },
        "lo_que_lo_hace_unico": (
            "Es la única carta donde la figura principal está cabeza abajo, pero su rostro luce totalmente radiante con un halo divino de santo. "
            "Sus piernas forman un número cuatro (4) y sus brazos una tríada, simbolizando el descenso del espíritu a la materia. "
            "A diferencia de El Carro (que avanza a toda velocidad con la fuerza de la voluntad), El Colgado alcanza la victoria total deteniéndose por completo."
        ),
        "curiosidades": [
            "La madera viva del patíbulo: Las ramas tienen brotes verdes de savia viva, demostrando que este aparente sacrificio es el árbol de la vida floreciendo.",
            "La aureola solar en la cabeza: Indica que la mente que ha renunciado a la soberbia del mundo recibe la iluminación directa del espíritu.",
            "El número 12 invertido: El 12 es el espejo del 21 (El Mundo). Lo que El Colgado experimenta en soledad interior es la antesala de la plenitud universal."
        ],
        "historia_inspirada": {
            "titulo": "El Árbol del Cielo Invertido",
            "relato": (
                "Un guerrero exhausto corría huyendo de sus enemigos hasta que su pie quedó atrapado en el lazo de un árbol sagrado de la colina. "
                "Quedó colgando boca abajo sobre el abismo. Primero gritó enfurecido, maldiciendo a los dioses y forcejeando con su espada; "
                "solo consiguió agotarse y sangrar. Cuando las fuerzas lo abandonaron, soltó la espada y dejó caer los brazos. "
                "En ese instante de silencio, miró hacia arriba: lo que antes era un cielo lejano ahora parecía un océano azul sobre el que flotaba, "
                "y las raíces del árbol parecían ramas que lo acunaban hacia las estrellas. Una sonrisa de dicha celestial iluminó su rostro. "
                "Cuando sus enemigos llegaron, lo encontraron riendo con los ojos resplandecientes de luz; asustados por su aura sagrada, "
                "arrojaron sus armas y se arrodillaron ante él."
            )
        },
        "audio": {
            "archivo": "assets/audio/el-colgado.mp3",
            "titulo": "El Colgado - La Iluminación en la Rendición",
            "duracion_estimada": "4:35 min"
        }
    },

    # 13. LA MUERTE
    {
        "id": "la-muerte",
        "number": 13,
        "roman": "XIII",
        "name": "La Muerte",
        "folder": "arcanos_mayores",
        "filename": "13_la_muerte.xml",
        "element": "Agua / Escorpio",
        "astrology": "Escorpio",
        "historia": (
            "En las barajas medievales y de Marsella solía llamarse 'El Arcano Sin Nombre' (para no invocar la tragedia de la Peste Negra) "
            "y mostraba a un esqueleto segador cortando cabezas y miembros coronados en un campo negro. Arthur Edward Waite y Pamela Colman Smith "
            "revolucionaron profundamente su simbolismo: transformaron al esqueleto en un caballero con armadura negra que monta un caballo blanco puro "
            "(símbolo de vida renovada), portando un estandarte negro con la rosa mística de cinco pétalos (la vida indestructible). "
            "Ante él caen reyes y prelados, pero al fondo, entre dos torres, amanece un sol dorado y radiante sobre el río del renacimiento."
        ),
        "significado_fundamental": (
            "La Muerte es el arquetipo de la transformación radical, el fin inevitable de un ciclo para dar paso a lo nuevo, la muda de piel y la liberación profunda. "
            "No alude a la muerte física biológica, sino al desprendimiento de estructuras, apegos, identidades caducas y relaciones que han agotado su propósito vital. "
            "Para que la primavera florezca, las hojas secas del otoño deben morir y regresar a la tierra como abono."
        ),
        "posicion_normal": {
            "resumen": "Fin de un ciclo, transformación profunda, renacimiento, desapego liberador y apertura a lo nuevo.",
            "amor": "Cierre definitivo de relaciones tóxicas o transformación profunda de la dinámica de pareja. Morir a viejos rencores para renacer en un amor más auténtico.",
            "dinero_trabajo": "Cambio de rumbo profesional radical. Liquidación de viejos proyectos que ya no aportan para fundar una nueva etapa próspera.",
            "salud": "Eliminación de toxinas, superación de una crisis física y regeneración celular. Fin de un período de convalecencia.",
            "espiritualidad": "La noche oscura del alma que precede al despertar. Disolución del falso ego (muerte iniciática) y nacimiento del ser esencial."
        },
        "posicion_invertida": {
            "resumen": "Resistencia agónica al cambio, miedo al duelo, aferrarse a lo que ya está muerto y prolongación innecesaria del sufrimiento.",
            "amor": "Permanecer en una relación zombi que produce dolor por miedo a la soledad. Negación a soltar a un ex.",
            "dinero_trabajo": "Mantener vivo un negocio en quiebra por orgullo, estancamiento profesional por temor al desempleo.",
            "salud": "Enfermedades crónicas agravadas por no cambiar hábitos destructivos. Somatización de duelos no resueltos ni llorados.",
            "espiritualidad": "Terror a lo desconocido. Vivir en un letargo espiritual por no atreverse a cuestionar las viejas creencias caducas."
        },
        "lo_que_lo_hace_unico": (
            "Lleva en su estandarte la Rosa Mística de cinco pétalos blanca sobre fondo negro, símbolo de la regeneración y de la quintaesencia inmortal. "
            "A diferencia de La Torre (que destruye repentinamente mediante un rayo violento e inesperado), La Muerte es un proceso orgánico, inexorable y natural: "
            "es el río de la vida que fluye hacia el mar del renacimiento bajo un sol que siempre vuelve a nacer entre las dos torres."
        ),
        "curiosidades": [
            "El niño que mira al caballero sin miedo: Frente al caballo de la Muerte, un niño con flores en el pelo mira al jinete con inocencia y curiosidad, revelando que el alma pura no teme a la transformación.",
            "El sol entre las dos torres: En el horizonte lejano amanece el sol de la inmortalidad, demostrando que la muerte es solo la puerta de entrada a una luz mayor.",
            "La rosa de cinco pétalos: Alude al número cinco (el ser humano redimido) y al movimiento esotérico Rosacruz de la regeneración perpetua."
        ],
        "historia_inspirada": {
            "titulo": "La Rosa de la Quinta Puerta",
            "relato": (
                "Una anciana reina custodiaba con guardias armados un jardín donde las hojas nunca caían porque estaban talladas en esmeralda y oro. "
                "No había flores marchitas, pero tampoco había aroma ni canto de pájaros; el jardín era un sepulcro de lujo. "
                "Una noche de luna negra, el caballero de armadura oscura cruzó los portones. La reina imploró llorando: '¡No destruyas mi paraíso perfecto!'. "
                "El caballero desmontó de su caballo blanco, tomó la corona de oro de la reina y la enterró en el lodo del suelo. "
                "En el instante en que la corona tocó la tierra negra, las hojas de metal se desvanecieron y un torrente de rosas rojas y frescas brotó "
                "de la tierra húmeda inundando el aire de perfume embriagador. 'Yo no quito la vida', susurró el jinete con voz de viento suave; "
                "'solo aparto lo que ya está muerto para que lo vivo vuelva a respirar'."
            )
        },
        "audio": {
            "archivo": "assets/audio/la-muerte.mp3",
            "titulo": "La Muerte - El Fuego Sagrado del Renacimiento",
            "duracion_estimada": "4:40 min"
        }
    },

    # 14. LA TEMPLANZA
    {
        "id": "la-templanza",
        "number": 14,
        "roman": "XIV",
        "name": "La Templanza",
        "folder": "arcanos_mayores",
        "filename": "14_la_templanza.xml",
        "element": "Fuego / Sagitario",
        "astrology": "Sagitario",
        "historia": (
            "Una de las cuatro virtudes cardinales presentes en el Tarot desde el siglo XV. En la tradición alquímica medieval, "
            "representa la 'Solve et Coagula' (disuelve y coagula): la mezcla armoniosa de los fluidos vitales. Arthur Edward Waite "
            "y Pamela Colman Smith la encarnan en el arcángel Miguel o Rafael, un ser andrógino con alas de fuego radiante que sostiene "
            "dos copas de oro y trasvasa un chorro de agua viva de una copa a otra sin derramar una sola gota. Un pie descansa en el agua "
            "del inconsciente y el otro en la tierra firme de la realidad, mientras un sendero asciende hacia una corona resplandeciente en la montaña."
        ),
        "significado_fundamental": (
            "La Templanza es el arquetipo de la alquimia interior, la armonía, la moderación sabia, la curación de los opuestos y la paciencia divina. "
            "Enseña el arte de mezclar el fuego y el agua, la pasión y la razón, la acción y la calma en las proporciones perfectas. "
            "Es la paz que surge tras la tormenta de La Muerte, la reintegración del alma en un estado superior de equilibrio y gracia."
        ),
        "posicion_normal": {
            "resumen": "Paz interior, sanación, moderación, reconciliación, adaptabilidad y paciencia que conduce al éxito duradero.",
            "amor": "Relación armoniosa, afecto sereno, comprensión mutua y perdón sincero. Reconciliación tras disputas y comunicación fluida.",
            "dinero_trabajo": "Negociaciones equilibradas, acuerdos justos entre partes encontradas, progreso financiero sostenible y ambiente laboral tranquilo.",
            "salud": "Excelente balance en los fluidos del cuerpo (circulatorio y linfático). Recuperación serena de la salud y bienestar físico y emocional.",
            "espiritualidad": "Contacto con el ángel guardián o guía espiritual. Canalización armónica de la energía universal en la vida diaria."
        },
        "posicion_invertida": {
            "resumen": "Excesos, impaciencia destructiva, falta de balance, descontrol emocional o mezclas incompatibles que generan conflicto.",
            "amor": "Desencuentros por falta de empatía, discusiones amargas, exigencias desmedidas o frialdad alternada con estallidos dramáticos.",
            "dinero_trabajo": "Decisiones apresuradas por impaciencia, mala administración financiera por gastos compulsivos o proyectos que chocan por incompatibilidad de visiones.",
            "salud": "Deshidratación, problemas digestivos por desórdenes alimenticios o recaídas por no respetar los tiempos naturales de convalecencia.",
            "espiritualidad": "Inquietud espiritual constante. Buscar experiencias místicas extremas olvidando el valor de la paz cotidiana."
        },
        "lo_que_lo_hace_unico": (
            "Es la única carta donde un fluido desafía la gravedad física: el agua fluye diagonalmente de una copa inferior a una superior sin perder una gota. "
            "Tiene un pie en la tierra y otro en el agua, simbolizando el perfecto puente entre la materia y el espíritu. "
            "A diferencia de La Estrella (que vierte el agua en la tierra para nutrirla), La Templanza conserva y destila el agua entre dos vasijas sagradas."
        ),
        "curiosidades": [
            "El triángulo en el cuadrado de su pecho: Es el septenario sagrado (3 + 4 = 7), el triángulo del espíritu manifestándose dentro del cuadrado de la materia.",
            "El iris amarillo en la orilla: La flor de iris hace referencia a la diosa Iris, mensajera del arcoíris que unía el cielo con la tierra tras el diluvio.",
            "El sol con forma de corona: En la cima de las montañas lejanas, el sol brilla como una corona regia prometiendo la iluminación a quien transita con paciencia el sendero."
        ],
        "historia_inspirada": {
            "titulo": "El Trasvase de las Dos Copas",
            "relato": (
                "Un maestro de alquimia convocó a sus dos alumnos más brillantes. Al primero le dio una jarra de aceite hirviendo y le ordenó apagarla arrojando un balde de agua helada; "
                "el aceite estalló en llamas quemando el cobertizo. Al segundo alumno le dio las mismas vasijas y le pidió pacificarlas. "
                "El segundo joven no arrojó el agua de golpe: tomó una pluma de cisne y fue dejando caer gota a gota el agua sobre el aceite caliente, "
                "cantando una oración de serenidad. Poco a poco, el vapor ascendió como incienso fragante y el aceite se volvió un ungüento dorado y curativo. "
                "—La fuerza bruta separa los mundos —dijo el maestro sonriendo—; solo la paciencia alquímica convierte el veneno en bálsamo sagrado."
            )
        },
        "audio": {
            "archivo": "assets/audio/la-templanza.mp3",
            "titulo": "La Templanza - La Alquimia de la Paz Interior",
            "duracion_estimada": "4:30 min"
        }
    },

    # 15. EL DIABLO
    {
        "id": "el-diablo",
        "number": 15,
        "roman": "XV",
        "name": "El Diablo",
        "folder": "arcanos_mayores",
        "filename": "15_el_diablo.xml",
        "element": "Tierra / Capricornio",
        "astrology": "Capricornio",
        "historia": (
            "Presente en los tarots renacentistas como un monstruo bufonesco y grotesco. Éliphas Lévi en el siglo XIX lo reinterpretó "
            "como el Baphomet del ocultismo templario: la figura hermafrodita con cuernos de macho cabrío, alas de murciélago y una antorcha encendida. "
            "Pamela Colman Smith y Waite lo sentaron sobre un pedestal cúbico o yunque de piedra. A sus pies, encadenados por el cuello, "
            "se encuentran un hombre y una mujer desnudos con pequeños cuernos y colas; sin embargo, un detalle visual magistral revela la verdad: "
            "las cadenas que los aprisionan son tan anchas y holgadas que podrían quitárselas de la cabeza en cualquier instante con solo desearlo."
        ),
        "significado_fundamental": (
            "El Diablo es el arquetipo de la sombra junguiana, el apego material, las adicciones, el poder de los instintos reprimidos y la trampa de la ilusión. "
            "Nos confronta con aquellas cadenas invisibles que nosotros mismos hemos forjado: el miedo al dinero, la obsesión sexual, el rencor o la culpa. "
            "No es una entidad maligna externa, sino el espejo de nuestra propia ignorancia que nos hace creer que somos prisioneros cuando en realidad somos libres."
        ),
        "posicion_normal": {
            "resumen": "Apego desmedido, tentación magnética, ataduras ilusorias, sexualidad instintiva, obsesión material y confrontación con la sombra.",
            "amor": "Pasión carnal irresistible, magnetismo erótico intenso pero con riesgo de dependencia emocional, celos obsesivos y manipulación.",
            "dinero_trabajo": "Gran ambición de riquezas, éxito material a corto plazo, pero con riesgo de prácticas poco éticas, avaricia o explotación laboral.",
            "salud": "Adicciones (alcohol, drogas, azúcar, pantallas), obsesiones compulsivas o exceso de estrés derivado del apego al dinero y al estatus.",
            "espiritualidad": "Confrontación con el lado oscuro de la mente. Darse cuenta de que el poder del miedo solo existe porque nosotros le entregamos nuestra energía."
        },
        "posicion_invertida": {
            "resumen": "Ruptura de cadenas, liberación de adicciones, superación de relaciones tóxicas, despertar de la ilusión y recuperación del poder personal.",
            "amor": "Terminar con un vínculo destructivo o una dependencia afectiva. Recuperación de la dignidad y fin de chantajes emocionales.",
            "dinero_trabajo": "Rechazar tratos corruptos, saldar deudas asfixiantes y liberarse de la esclavitud de un empleo deshumanizante.",
            "salud": "Desintoxicación exitosa, superación de conductas autodestructivas y recuperación del autocontrol corporal y mental.",
            "espiritualidad": "Integración consciente de la sombra. Reconocer los propios impulsos oscuros sin miedo para transmutarlos en luz creadora."
        },
        "lo_que_lo_hace_unico": (
            "Es la parodia exacta de la carta de Los Enamorados (VI): el arcángel celestial Rafael es sustituido por el macho cabrío cornudo, "
            "y Adán y Eva, antes bendecidos en libertad, ahora aparecen encadenados al pedestal pero con cadenas holgadas que revelan que su prisión es voluntaria. "
            "A diferencia de La Torre (que rompe las prisiones con un rayo exterior), El Diablo exige que reconozcamos nuestras propias complicidades con el carcelero."
        ),
        "curiosidades": [
            "Las cadenas holgadas: Los eslabones alrededor del cuello de los amantes son tan grandes que podrían quitárselos deslizando las manos, simbolizando que nos esclavizamos por comodidad o miedo a la libertad.",
            "La antorcha hacia abajo: El Diablo sostiene la antorcha encendida apuntando hacia la tierra, quemando la cola del hombre, simbolizando el desperdicio del fuego espiritual en pasiones bajas.",
            "El pentagrama invertido: Sobre su frente luce la estrella de cinco puntas invertida, donde la materia y los instintos gobiernan sobre el espíritu."
        ],
        "historia_inspirada": {
            "titulo": "Las Cadenas de Terciopelo",
            "relato": (
                "En la cueva del Rey de Bronce, los esclavos picaban oro noche y día. Todos llevaban pesados collares de hierro atados al trono del gigante cornudo. "
                "Un joven cautivo, cansado de sangrar por unos gramos de polvo dorado, levantó la mano para rascarse el cuello adolorido. "
                "Para su asombro, descubrió que el collar no estaba cerrado con candado: era un aro abierto, forrado por dentro con terciopelo suave para que no raspase la piel. "
                "El gigante de bronce lo miró fijamente y le dijo con una risotada cavernosa: '¿Por qué no huyes? La puerta del túnel siempre ha estado abierta'. "
                "El joven miró el oro brillante en el suelo y luego la fría noche estrellada en la entrada. Tragó saliva y comprendió el gran secreto: "
                "el carcelero nunca lo había encerrado; había sido su propia codicia quien lo había mantenido de rodillas. Arrojó el collar y salió corriendo hacia la aurora."
            )
        },
        "audio": {
            "archivo": "assets/audio/el-diablo.mp3",
            "titulo": "El Diablo - El Espejo de las Cadenas Invisibles",
            "duracion_estimada": "4:40 min"
        }
    },

    # 16. LA TORRE
    {
        "id": "la-torre",
        "number": 16,
        "roman": "XVI",
        "name": "La Torre",
        "folder": "arcanos_mayores",
        "filename": "16_la_torre.xml",
        "element": "Fuego / Marte",
        "astrology": "Marte",
        "historia": (
            "Llamada 'La Maison Dieu' (La Casa de Dios) en el Tarot de Marsella. La escena evoca el mito bíblico de la Torre de Babel: "
            "la soberbia humana que intenta construir un rascacielos para alcanzar a Dios sin amor ni cimientos espirituales. "
            "Arthur Edward Waite y Pamela Colman Smith plasmaron una fortaleza de piedra alzada sobre una montaña escarpada azotada por la noche. "
            "Un rayo dorado fulmina la corona de la cúspide, lenguas de fuego brotan por las ventanas y dos figuras humanas caen al vacío en picada, "
            "mientras veintidós gotas de luz celestial (las 22 letras del alfabeto hebreo) descienden del cielo garantizando que la destrucción es obra de la gracia divina."
        ),
        "significado_fundamental": (
            "La Torre es el arquetipo del despertar súbito a través del colapso de las falsas estructuras del ego, la revelación demoledora y la liberación forzosa. "
            "Todo aquello que hemos construido sobre cimientos de mentiras, orgullo o apariencias no puede sostenerse ante la verdad divina. "
            "Aunque el rayo se experimenta como una crisis traumática, su propósito supremo no es aniquilar, sino demoler la prisión para que podamos volver a respirar aire puro."
        ),
        "posicion_normal": {
            "resumen": "Ruptura imprevista, derrumbe de ilusiones, crisis liberadora, revelación impactante y liberación de estructuras obsoletas.",
            "amor": "Verdades ocultas que salen a la luz y provocan una ruptura inevitable o una catarsis que sacude las bases de la relación para redefinirla desde cero.",
            "dinero_trabajo": "Pérdida inesperada de empleo, quiebra de una empresa insostenible o rescisión de contratos por cambios drásticos en el entorno.",
            "salud": "Crisis repentina de salud, ataques de pánico o necesidad de atención médica urgente que obliga a un cambio de vida inmediato y radical.",
            "espiritualidad": "La caída fulminante del orgullo espiritual. Despertar abrupto de la consciencia que destruye los dogmas falsos en un segundo."
        },
        "posicion_invertida": {
            "resumen": "Evitar un desastre por poco, resistencia angustiosa a una ruptura inevitable, crisis interior contenida o reconstrucción lenta tras la catástrofe.",
            "amor": "Prolongar una relación que ya está desmoronándose por miedo al escándalo o al cambio. Resentimiento contenido que envenena el alma.",
            "dinero_trabajo": "Sobrevivir a duras penas a una crisis financiera. Negarse a reconocer que un modelo de negocio ha caducado.",
            "salud": "Estrés postraumático tras un accidente o secuelas de una crisis. Alivio progresivo si se aceptan los cambios necesarios.",
            "espiritualidad": "Miedo a la verdad. Preferir vivir en una mentira cómoda antes que aceptar la libertad que ofrece el desapego radical."
        },
        "lo_que_lo_hace_unico": (
            "Es la única carta donde la intervención divina desciende en forma de un rayo de fuego fulminante del cielo que derriba la corona artificial del hombre. "
            "A diferencia de La Muerte (donde el ciclo concluye con la cadencia natural de las estaciones), La Torre actúa como una explosión fulgurante "
            "que desmantela en un segundo lo que tardó décadas en construirse sobre bases falsas."
        ),
        "curiosidades": [
            "Las 22 gotas de luz: Las chispas que caen del cielo son yods hebreas, representando los 22 senderos del Árbol de la Vida y los 22 Arcanos Mayores, confirmando que la destrucción es misericordia divina.",
            "La corona derribada: Simboliza la cabeza del ego y la soberbia del intelecto humano que cree estar por encima de las leyes universales.",
            "Los cimientos sobre la roca: La torre estaba construida sobre roca estéril y no sobre tierra fértil, revelando por qué no podía albergar vida verdadera."
        ],
        "historia_inspirada": {
            "titulo": "El Rayo del Campanario Negro",
            "relato": (
                "Un magnate construyó la torre más alta de la costa para vigilar sus flotas y aislarse de la plebe. Sus muros eran de granito de tres metros "
                "de grosor y las puertas estaban blindadas con cerrojos de hierro. Dentro, el aire era espeso y el hombre vivía devorado por la paranoia. "
                "Una noche de tormenta furiosa, el cielo se abrió y un rayo azul cayó con la potencia de mil cañones justo en la aguja de oro de la torre. "
                "Los muros colapsaron en una nube de escombros y fuego. El magnate cayó rodando sobre la arena mojada de la playa, cubierto de ceniza y con las ropas desgarradas. "
                "Miró las ruinas humeantes de su palacio y, por primera vez en cuarenta años, sintió el viento salobre del mar golpearle la cara "
                "y vio el brillo infinito de las estrellas sobre su cabeza. Comenzó a llorar y luego a reír con los brazos abiertos: "
                "el rayo no había destruido su hogar; había reventado los muros de su propia celda."
            )
        },
        "audio": {
            "archivo": "assets/audio/la-torre.mp3",
            "titulo": "La Torre - El Rayo que Rompe las Prisiones",
            "duracion_estimada": "4:35 min"
        }
    },

    # 17. LA ESTRELLA
    {
        "id": "la-estrella",
        "number": 17,
        "roman": "XVII",
        "name": "La Estrella",
        "folder": "arcanos_mayores",
        "filename": "17_la_estrella.xml",
        "element": "Aire / Acuario",
        "astrology": "Acuario",
        "historia": (
            "En las barajas primitivas italianas se la llamaba 'La Stella' y mostraba a una figura femenina guiada por una estrella brillante "
            "o sosteniendo una estrella en sus manos. Pamela Colman Smith y Arthur Edward Waite la consagraron como una de las imágenes más poéticas "
            "del mazo: una doncella totalmente desnuda se arrodilla en la orilla de un estanque bajo un cielo nocturno dominado por una gran estrella dorada "
            "de ocho puntas y siete estrellas menores. Con dos jarras de agua viva, derrama una corriente en la tierra fértil (que se divide en cinco riachuelos) "
            "y otra corriente en el propio estanque, mientras un pájaro sagrado (el ibis de Thot) reposa en un árbol cercano."
        ),
        "significado_fundamental": (
            "La Estrella es el arquetipo de la esperanza renovada, la fe inquebrantable, la inspiración cósmica, la serenidad y la generosidad desinteresada. "
            "Aparece inmediatamente después del colapso de La Torre para recordarnos que cuando todo lo falso se ha derrumbado, "
            "el alma recupera su desnudez pura y se conecta con la fuente inagotable de la gracia divina. Es la luz en la noche que nos asegura que el universo conspira a nuestro favor."
        ),
        "posicion_normal": {
            "resumen": "Esperanza brillante, fe renovada, sanación profunda, inspiración artística, claridad mental y paz de espíritu.",
            "amor": "Amor puro, reconciliación idílica, confianza mutua restaurada y conexión de almas que comparten ideales elevados y belleza compartida.",
            "dinero_trabajo": "Oportunidades profesionales prometedoras, proyectos creativos exitosos, reconocimiento por vocación genuina y generosidad financiera.",
            "salud": "Recuperación milagrosa o acelerada, purificación del organismo, bienestar emocional radiante y revitalización del sistema nervioso.",
            "espiritualidad": "Conexión directa con la guía cósmica y los planos celestiales. Sensación profunda de estar en el lugar correcto en el momento perfecto."
        },
        "posicion_invertida": {
            "resumen": "Pérdida transitoria de la fe, pesimismo, desilusión, falta de inspiración o esperar pasivamente sin actuar.",
            "amor": "Falta de ilusión en la pareja, dudas sobre el porvenir o idealizar excesivamente a personas inaccesibles desatendiendo la realidad.",
            "dinero_trabajo": "Proyectos que avanzan con lentitud, desánimo ante contratiempos temporales o promesas profesionales que se demoran.",
            "salud": "Tendencia al desánimo, tristeza o apatía física por falta de descanso y desconexión de la naturaleza.",
            "espiritualidad": "Sensación de vacío o abandono divino. Olvidar que la noche más oscura siempre es la que precede a la aurora."
        },
        "lo_que_lo_hace_unico": (
            "La doncella está completamente desnuda, sin velos, máscaras ni adornos, personificando la verdad prístina y la total vulnerabilidad sagrada. "
            "A diferencia de La Luna (cargada de miedos y espejismos) y El Sol (gloria radiante diurna), La Estrella es la serenidad nocturna silenciosa: "
            "no deslumbra con su luz, pero guía con certeza absoluta a quien mira hacia el firmamento."
        ),
        "curiosidades": [
            "La estrella de ocho puntas: Representa la octava esfera cósmica, el planeta Venus como lucero del alba y la regeneración espiritual perpetua.",
            "Los cinco riachuelos en la tierra: Simbolizan los cinco sentidos humanos que son fertilizados y purificados por el agua de la consciencia divina.",
            "El ibis sagrado en el árbol: El pájaro que reposa en el árbol del fondo es el ibis consagrado a Thot (dios egipcio de la sabiduría y la escritura)."
        ],
        "historia_inspirada": {
            "titulo": "Las Dos Jarras del Estanque de Plata",
            "relato": (
                "Tras el gran terremoto que redujo la ciudad a cenizas, una muchacha caminó descalza hacia el manantial del bosque. "
                "Llevaba dos jarras de arcilla azul. Los supervivientes le gritaban desde los escombros: '¡Guarda el agua para ti! ¡Vienen años de sequía!'. "
                "La doncella no contestó con palabras; se despojó de sus mantos polvorientos, se arrodilló sobre la hierba húmeda y comenzó a verter "
                "una jarra en la tierra seca y la otra en el estanque. '¿Por qué la derramas en el barro?', le preguntó un anciano quejumbroso. "
                "Ella levantó la mirada hacia la gran estrella de la noche y sonrió con dulzura infinita: 'El agua que se acapara por miedo se pudre en la vasija; "
                "el agua que se entrega con fe pura hace que hasta el desierto más árido vuelva a florecer'."
            )
        },
        "audio": {
            "archivo": "assets/audio/la-estrella.mp3",
            "titulo": "La Estrella - El Bálsamo de la Esperanza Cósmica",
            "duracion_estimada": "4:30 min"
        }
    },

    # 18. LA LUNA
    {
        "id": "la-luna",
        "number": 18,
        "roman": "XVIII",
        "name": "La Luna",
        "folder": "arcanos_mayores",
        "filename": "18_la_luna.xml",
        "element": "Agua / Piscis",
        "astrology": "Piscis",
        "historia": (
            "En las barajas renacentistas se mostraba a astrólogos midiendo las fases de la luna o a mujeres hilando bajo la luz nocturna. "
            "El Tarot de Marsella y Rider-Waite-Smith fijaron una de las escenas más cargadas de simbolismo psicoanalítico y mitológico: "
            "la luna llena (con un rostro melancólico de perfil dentro de un sol creciente) deja caer gotas de rocío luminiscente sobre la tierra. "
            "Desde un estanque primordial emerge un cangrejo de río o langosta (los instintos primarios arcaicos del inconsciente); "
            "en la orilla, un perro doméstico y un lobo salvaje aúllan a la luna, mientras un sendero serpenteante cruza entre dos torres oscuras "
            "hacia las montañas azules de lo desconocido."
        ),
        "significado_fundamental": (
            "La Luna es el arquetipo del subconsciente profundo, el mundo de los sueños, las ilusiones, los miedos atávicos y la intuición psíquica. "
            "Representa el viaje a través de la noche de la psique humana, donde las sombras se alargan y nada es exactamente lo que parece a simple vista. "
            "Nos enseña a no dejarnos engañar por las apariencias ni paralizar por las pesadillas imaginarias, transitando el sendero con discernimiento hasta que amanezca la verdad."
        ),
        "posicion_normal": {
            "resumen": "Intuición psíquica aguda, sueños reveladores, confusión emocional, secretos que emergen y necesidad de vencer temores ocultos.",
            "amor": "Inseguridades, celos infundados, misterios o ilusiones no correspondidas. Conexión telepática intensa pero que requiere comunicación clara para no caer en suposiciones erróneas.",
            "dinero_trabajo": "Falta de claridad en contratos, ambientes laborales turbios o decisiones que no deben tomarse hasta que se disipe la niebla informativa.",
            "salud": "Sensibilidad emocional extrema, alteraciones en los ciclos del sueño (insomnio o pesadillas vívidas) y fluctuaciones hormonales.",
            "espiritualidad": "Contacto profundo con el mundo astral y los mensajes de los sueños. Superación del miedo a la propia oscuridad interior."
        },
        "posicion_invertida": {
            "resumen": "Claridad que disipa la confusión, secretos que se revelan, superación de engaños y liberación de miedos y fobias irracionales.",
            "amor": "Descubrimiento de la verdad en la relación, fin de la desconfianza o desenmascaramiento de mentiras que permite cerrar un ciclo con dignidad.",
            "dinero_trabajo": "Aclaración de cuentas dudosas, resolución de malentendidos comerciales y salida de una etapa de incertidumbre profesional.",
            "salud": "Recuperación de la estabilidad psicológica, superación de ansiedades o ataques de pánico y regularización del sueño.",
            "espiritualidad": "Distinguir la verdadera intuición espiritual de las simples proyecciones del miedo del ego."
        },
        "lo_que_lo_hace_unico": (
            "Es la única carta donde conviven las tres etapas de la evolución animal e instintiva de la psique: "
            "el crustáceo en el agua primordial (lo más primitivo e inconsciente), el lobo (el instinto salvaje) y el perro (el instinto domesticado). "
            "A diferencia de La Sacerdotisa (que domina el misterio en paz), La Luna muestra la inquietud y el estremecimiento del alma ante las profundidades de lo desconocido."
        ),
        "curiosidades": [
            "El crustáceo que emerge del agua: Simboliza los complejos y memorias reprimidas del inconsciente que ascienden a la superficie para ser vistos y sanados.",
            "El perro y el lobo: Representan la dualidad de nuestra propia naturaleza: el lado domesticado y adaptado a la sociedad frente al lado salvaje y primitivo.",
            "Las quince gotas de yod: Caen de la luna hacia la tierra, recordando que incluso en medio de la niebla y la noche más confusa, la gracia divina nunca deja de derramarse."
        ],
        "historia_inspirada": {
            "titulo": "El Aullido del Valle Brumoso",
            "relato": (
                "Un caminante debía cruzar el Valle de las Dos Torres a medianoche para llegar a la ciudad del Sol. "
                "Apenas entró en la niebla, las sombras de las piedras parecían gigantes armados y el rumor del viento sonaba a carcajadas burlonas. "
                "A su lado, un perro blanco temblaba y un lobo negro enseñaba los dientes hacia el estanque de fango donde un cangrejo agitaba sus tenazas. "
                "El caminante sintió el hielo del pánico en su nuca y estuvo a punto de salir huyendo. Pero recordó el consejo de la abuela: "
                "'La noche nunca ataca; solo refleja lo que temes llevar dentro'. Se detuvo, cerró los ojos y abrazó al perro y acarició el lomo del lobo. "
                "Cuando abrió los ojos, la luna llena sonrió tras la niebla: los gigantes eran solo cipreses y el sendero de piedras brillaba como plata pura. "
                "Avanzó paso a paso, sabiendo que la oscuridad no se combate: se atraviesa con paso firme."
            )
        },
        "audio": {
            "archivo": "assets/audio/la-luna.mp3",
            "titulo": "La Luna - Los Espejismos de la Noche del Alma",
            "duracion_estimada": "4:45 min"
        }
    },

    # 19. EL SOL
    {
        "id": "el-sol",
        "number": 19,
        "roman": "XIX",
        "name": "El Sol",
        "folder": "arcanos_mayores",
        "filename": "19_el_sol.xml",
        "element": "Fuego / El Sol",
        "astrology": "El Sol",
        "historia": (
            "En las barajas medievales y de Marsella solía mostrar a dos niños gemelos vestidos con taparrabos abrazándose bajo una lluvia de rayos solares. "
            "Pamela Colman Smith y Arthur Edward Waite simplificaron y elevaron la escena a una belleza sublime: un niño pequeño radiante y totalmente desnudo "
            "monta sin silla ni riendas sobre un dócil caballo blanco (símbolo de la inocencia y el dominio de los instintos), llevando en su mano izquierda "
            "un gran estandarte rojo fuego que ondea con júbilo. Al fondo, sobre un muro de piedra protector, florecen cuatro grandes girasoles dorados "
            "bajo un sol inmenso de rostro sereno y compasivo rodeado de rayos rectos y ondulados."
        ),
        "significado_fundamental": (
            "El Sol es el arquetipo de la iluminación, la alegría pura, el éxito supremo, la vitalidad radiante, la claridad de la verdad y el renacimiento de la inocencia. "
            "Es la carta más positiva de toda la baraja del Tarot. Tras superar la noche incierta de La Luna, amanece el día radiante donde todo se ve con absoluta transparencia. "
            "Nos enseña a recuperar el corazón de niño, a celebrar la vida con júbilo y a irradiar calidez y generosidad sin pedir nada a cambio."
        ),
        "posicion_normal": {
            "resumen": "Éxito absoluto, alegría desbordante, vitalidad física, claridad de objetivos, triunfo merecido y plenitud compartida.",
            "amor": "Felicidad plena en la pareja, romance cálido y transparente, boda, nacimientos deseados y armonía total en el hogar.",
            "dinero_trabajo": "Triunfo en proyectos, ascensos de gran visibilidad, prosperidad económica floreciente y reconocimiento público indiscutible.",
            "salud": "Vitalidad sobresaliente, energía solar desbordante, longevidad y curación total de dolencias pasadas.",
            "espiritualidad": "Consciencia crística o solar despierta. Percepción de la unidad de toda la vida y alegría sincera por la existencia de los demás."
        },
        "posicion_invertida": {
            "resumen": "Éxito demorado pero no cancelado, exceso de orgullo o vanidad, dificultad momentánea para ver el lado positivo o nubes pasajeras.",
            "amor": "Pequeños roces por egocentrismo, exigencias de protagonismo en la pareja o felicidad que se demora por dudas menores.",
            "dinero_trabajo": "Logros que tardan un poco más en manifestarse de lo esperado o exceso de optimismo que pasa por alto detalles operativos.",
            "salud": "Insolación, fatiga temporal por exceso de actividad o necesidad de recargar energías al aire libre.",
            "espiritualidad": "Ego espiritual que busca aplausos externos en lugar de cultivar la humildad silenciosa del corazón."
        },
        "lo_que_lo_hace_unico": (
            "Es el único arcano donde el triunfador supremo no es un rey armado ni un sabio venerable, sino un niño desnudo que monta a pelo sobre un caballo blanco. "
            "A diferencia de El Carro (que necesita armadura y control férreo para triunfar), El Sol triunfa mediante la absoluta inocencia y la gracia sin esfuerzo: "
            "su fuerza es la pureza de su corazón."
        ),
        "curiosidades": [
            "Los cuatro girasoles sobre el muro: Representan los cuatro elementos de la naturaleza plenamente purificados y florecidos al calor del espíritu divino.",
            "La pluma roja en la cabeza del niño: Es la misma pluma roja que llevaba El Loco en su sombrero al inicio del viaje (0), confirmando que El Sol es El Loco que ha alcanzado la iluminación.",
            "Los rayos rectos y ondulados: Los rectos simbolizan la luz del intelecto y la verdad, mientras los ondulados representan el calor del amor y la compasión."
        ],
        "historia_inspirada": {
            "titulo": "El Niño del Corcel Blanco",
            "relato": (
                "Durante un siglo entero, los reyes del reino intentaron derrotar al Dragón de la Tristeza que vivía en las colinas. "
                "Enviaron ejércitos con catapultas, sabios con conjuros y mercenarios con arcos de acero; todos volvían derrotados y con el alma oscurecida. "
                "Una mañana de primavera, las puertas de la ciudad se abrieron y un niño de cuatro años salió cabalgando sobre un potro blanco. "
                "Iba descalzo, riendo a carcajadas mientras agitaba una tela roja al viento como si fuera una cometa. "
                "Subió a la cueva del dragón y, en lugar de empuñar un arma, le ofreció una manzana silvestre y se echó a reír con tal pureza que el eco "
                "hizo vibrar las rocas. El dragón salió de la cueva, pero al sentir el rayo del sol en los ojos del niño, sus escamas oscuras se desprendieron "
                "como ceniza seca, transformándose en una bandada de mariposas de oro. La oscuridad nunca necesitó que la combatieran: "
                "solo estaba esperando que alguien encendiera la luz con alegría."
            )
        },
        "audio": {
            "archivo": "assets/audio/el-sol.mp3",
            "titulo": "El Sol - El Triunfo de la Inocencia Dorada",
            "duracion_estimada": "4:20 min"
        }
    },

    # 20. EL JUICIO
    {
        "id": "el-juicio",
        "number": 20,
        "roman": "XX",
        "name": "El Juicio",
        "folder": "arcanos_mayores",
        "filename": "20_el_juicio.xml",
        "element": "Fuego / Plutón",
        "astrology": "Plutón",
        "historia": (
            "Inspirado en el Juicio Final bíblico y en el Apocalipsis de San Juan, presente en todos los tarots occidentales desde el siglo XV. "
            "El arcángel Gabriel desciende entre las nubes celestiales haciendo sonar su trompeta dorada adornada con un estandarte con una cruz roja "
            "(la bandera de San Jorge y el símbolo del renacimiento de la vida). Abajo, sobre un mar rodeado de montañas nevadas, tumbas de piedra se abren: "
            "un hombre, una mujer y un niño emergen desnudos con los brazos abiertos en actitud de adoración y júbilo, simbolizando la resurrección del alma "
            "y la llamada ineludible al despertar de la consciencia suprema."
        ),
        "significado_fundamental": (
            "El Juicio es el arquetipo del despertar espiritual, la llamada de la vocación superior, el perdón redentor y la elevación a un nuevo nivel de consciencia. "
            "No representa una condena punitiva, sino el momento supremo en que el alma escucha su verdad más profunda, se levanta de las tumbas del pasado "
            "y comprende el propósito global de todas las experiencias vividas. Es la segunda oportunidad que la vida nos otorga para renacer libres de culpas."
        ),
        "posicion_normal": {
            "resumen": "Despertar de la consciencia, llamada de la verdadera vocación, perdón liberador, renovación absoluta y toma de decisiones trascendentales.",
            "amor": "Renovación total en la pareja, superación de viejos rencores con madurez o decisión definitiva y liberadora sobre el futuro sentimental.",
            "dinero_trabajo": "Descubrimiento de la verdadera vocación profesional. Momento culminante de evaluación con resultados brillantes y ascensos basados en el mérito real.",
            "salud": "Recuperación milagrosa de la vitalidad física, superación de secuelas y sensación de haber nacido de nuevo.",
            "espiritualidad": "La llamada irresistible del alma. Despertar de la consciencia que transforma para siempre las prioridades de vida."
        },
        "posicion_invertida": {
            "resumen": "Sordera ante la llamada del alma, autocondena paralizante, culpa injustificada, miedo al cambio o negarse a perdonar.",
            "amor": "Rencores pasados que se niegan a morir, reproches constantes o miedo a afrontar una conversación decisiva sobre el futuro.",
            "dinero_trabajo": "Dudas ante una gran oportunidad por sentirse indigno o poco preparado. Errores de juicio por ignorar advertencias evidentes.",
            "salud": "Sentimiento de culpabilidad que somatiza en el cuerpo. Resistencia a admitir que se necesita ayuda profesional.",
            "espiritualidad": "Miedo al juicio ajeno o a la mirada de Dios. Vivir atrapado en la culpa moralista sin permitirse la redención y el perdón."
        },
        "lo_que_lo_hace_unico": (
            "Es la única carta donde los muertos se levantan de sus tumbas flotantes en el mar no con horror ni miedo, sino con beatitud y los brazos abiertos al cielo. "
            "A diferencia de La Justicia (que mide y pesa las acciones terrenales de causa y efecto), El Juicio es la gracia divina: "
            "trasciende la condena para ofrecer una resurrección total y definitiva a quien escucha la llamada del despertar."
        ),
        "curiosidades": [
            "La trompeta de siete rayos sonoros: Representa los siete tonos sagrados de la creación y los siete chakras que se activan con el despertar de la kundalini.",
            "La cruz roja sobre el estandarte blanco: Símbolo de la unión del espíritu con la materia y la victoria de la vida inmortal sobre la muerte biológica.",
            "La familia (hombre, mujer y niño): Representa la trinidad psicológica: el consciente, el inconsciente y el nuevo ser integrado que renace."
        ],
        "historia_inspirada": {
            "titulo": "El Clamor en la Cripta de Mármol",
            "relato": (
                "En el cementerio de las Oportunidades Perdidas, los hombres yacían dentro de pesadas losas de mármol grabadas con sus propios fracasos pasados: "
                "'Aquí yace el cobarde', 'Aquí yace el culpable', 'Aquí yace el que no se atrevió'. "
                "Al amanecer de un día sin calendario, un ángel de fuego lila descendió sobre las montañas y tocó una trompeta de plata con tal fuerza que el sonido "
                "no vibró en los oídos, sino en el centro exacto del corazón de cada difunto. Las losas de mármol se partieron en mil pedazos. "
                "Un hombre abrió los ojos cubierto de polvo y miró sus manos heridas: no estaban muertas, estaban llenas de sangre caliente. "
                "—¿Acaso no vas a castigar mis pecados? —preguntó temblando hacia el ángel. "
                "El arcángel bajó la trompeta y lo miró con una sonrisa que abrazaba a todo el universo: "
                "—Tu único castigo fue haber creído que tus errores del pasado eran más grandes que el amor que te creó. Levántate y vive, "
                "que el mundo aún está esperando tu verdadera canción."
            )
        },
        "audio": {
            "archivo": "assets/audio/el-juicio.mp3",
            "titulo": "El Juicio - La Llamada Ineludible del Despertar",
            "duracion_estimada": "4:45 min"
        }
    },

    # 21. EL MUNDO
    {
        "id": "el-mundo",
        "number": 21,
        "roman": "XXI",
        "name": "El Mundo",
        "folder": "arcanos_mayores",
        "filename": "21_el_mundo.xml",
        "element": "Tierra / Saturno",
        "astrology": "Saturno",
        "historia": (
            "La culminación suprema del viaje del Tarot, presente desde las barajas milanesas del siglo XV como la representación de la Jerusalén Celeste "
            "o el Triunfo de la Eternidad sobre el Tiempo. Arthur Edward Waite y Pamela Colman Smith coronaron la baraja con una imagen de júbilo cósmico: "
            "una figura andrógina danzante (que representa la totalidad del alma integrada) flota ingrávida en el centro de una gran corona elíptica de laurel verde "
            "atada con cintas rojas en forma de lemniscata. Sostiene dos varas mágicas en sus manos, mientras en las cuatro esquinas del cielo reposan los cuatro seres sagrados "
            "(el Ángel de Acuario, el Águila de Escorpio, el León de Leo y el Toro de Tauro), que han dejado los libros de estudio para contemplar la danza triunfal."
        ),
        "significado_fundamental": (
            "El Mundo es el arquetipo de la realización total, el éxito supremo, la plenitud, la integración perfecta de todas las lecciones del viaje y el fin glorioso de un gran ciclo vital. "
            "El Loco (0), que comenzó su viaje desnudo e inconsciente al borde del abismo, llega ahora al Mundo (21) desnudo pero plenamente consciente, "
            "danzando en el centro del cosmos en perfecta armonía con todas las leyes universales. Es el hogar espiritual alcanzado y la libertad absoluta."
        ),
        "posicion_normal": {
            "resumen": "Culminación exitosa, plenitud total, metas alcanzadas, viajes internacionales felices, realización del propósito y celebración gozosa.",
            "amor": "Amor pleno, armonía conyugal duradera, realización de los sueños compartidos y sensación de plenitud y bendición en el vínculo.",
            "dinero_trabajo": "Consagración profesional, culminación brillante de grandes proyectos, expansión internacional de negocios y éxito financiero consolidado.",
            "salud": "Salud integral radiante, bienestar holístico entre cuerpo, mente y alma, y longevidad plena.",
            "espiritualidad": "Iluminación e integración cósmica. La consciencia de la unidad absoluta de todo lo que existe y la danza armónica con el universo."
        },
        "posicion_invertida": {
            "resumen": "Último obstáculo antes de la meta, retraso en el cierre de un ciclo, procrastinación en el tramo final o sensación de vacío a pesar del éxito exterior.",
            "amor": "Falta de cierre definitivo con el pasado que impide disfrutar plenamente de la relación actual, o posponer un paso importante hacia el compromiso.",
            "dinero_trabajo": "Proyectos que están al 99% pero a los que les falta el último empujón para completarse con éxito. Falta de foco en los detalles finales.",
            "salud": "Agotamiento en la recta final de un tratamiento o convalecencia. Necesidad de culminar los procesos de descanso sin precipitaciones.",
            "espiritualidad": "Miedo a la plenitud. Quedarse en la antesala de la iluminación por apego a las viejas luchas del ego."
        },
        "lo_que_lo_hace_unico": (
            "Es la última carta de los Arcanos Mayores y la única donde la figura sostiene dos varas de mando al mismo tiempo "
            "(a diferencia de El Mago que solo tenía una), simbolizando la doble maestría sobre el mundo interior y el mundo exterior. "
            "Danza dentro de una corona de laurel atada con lazos en forma de ocho infinito, demostrando que el final del viaje es al mismo tiempo "
            "el inicio de una nueva espiral infinita de evolución."
        ),
        "curiosidades": [
            "La corona elíptica de laurel: Representa la mandorla o vulva cósmica de la que nace el nuevo ser iluminado, símbolo de victoria y gloria eterna.",
            "Los cuatro querubines en las esquinas: En La Rueda de la Fortuna (X) estudiaban textos; aquí, en El Mundo (XXI), ya no necesitan leer libros porque la sabiduría se ha integrado en la propia danza.",
            "Las dos varas mágicas: Una canaliza la energía descendente del cielo y la otra la energía ascendente de la tierra, convirtiendo al danzante en el centro del cosmos."
        ],
        "historia_inspirada": {
            "titulo": "La Danza en el Centro del Universo",
            "relato": (
                "Tras caminar por desiertos, subir montañas nevadas, atravesar tormentas y enfrentar dragones en cavernas oscuras, "
                "aquel que una vez fue llamado El Loco llegó a la Puerta de las Cuatro Esquinas. Los cuatro guardianes del cielo —el ángel, el águila, el león y el toro— "
                "cerraban el paso con sus alas inmensas. '¿Qué traes en tus alforjas para merecer entrar en la Jerusalén de Oro?', rugió el león. "
                "El viajero sonrió con la misma inocencia con la que había comenzado su viaje; abrió las manos vacías y no mostró gemas, ni espadas, ni pergaminos de leyes. "
                "'No traigo nada que me pertenezca a mí solo', susurró con voz de viento puro; 'traigo el abrazo de la tierra, la lágrima del mar, "
                "el fuego de las pasiones vencidas y el aliento del cielo que todo lo une'. "
                "Los cuatro guardianes plegaron sus alas y se inclinaron reverentes. La corona de laurel del portal se abrió de par en par: "
                "en el centro no había un trono de piedra donde sentarse a mandar, sino un espacio infinito de luz donde la música de las estrellas "
                "invitaba a danzar. El viajero comenzó a bailar, y en su danza el universo entero encontró su hogar."
            )
        },
        "audio": {
            "archivo": "assets/audio/el-mundo.mp3",
            "titulo": "El Mundo - La Danza Cósmica de la Plenitud",
            "duracion_estimada": "4:45 min"
        }
    }
]

print(f"Cargados {len(MAJORS_DATA_2)} arcanos mayores en lote 2.")
