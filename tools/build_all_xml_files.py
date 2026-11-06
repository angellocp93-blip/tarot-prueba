# -*- coding: utf-8 -*-
"""
Constructor maestro de la colección de 78 archivos XML de Tarot
Integra:
- Datos de base (elemento, esencia, polaridad luz/sombra, símbolos, palabras clave, consejo, pregunta reflexiva)
- 7 Puntos nuevos (historia, significado fundamental, posición normal 4 planos, posición invertida 4 planos, lo que lo hace único, curiosidades, historia inspirada)
- Estructura de audiolibro (archivo mp3, título, duración)
- Sincronización automática con data/tarot_database.json y data/tarot_database.js
"""

import json
import os
import sys
import xml.sax.saxutils as saxutils

# Ensure workspace root and tools dir are in sys.path
sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('tools'))

from data_majors import MAJORS_DATA_1
from data_majors_part2 import MAJORS_DATA_2
from data_minors import generate_minors_data

def escape_xml(val):
    if val is None:
        return ""
    if isinstance(val, (int, float)):
        return str(val)
    if isinstance(val, list):
        return ", ".join(str(x) for x in val)
    return saxutils.escape(str(val))

def build_card_xml(card_db, rich_data):
    # Determine base values
    c_id = card_db["id"]
    number = card_db.get("number", rich_data.get("number", "0"))
    name = card_db.get("name", rich_data.get("name", c_id))
    c_type = card_db.get("type", rich_data.get("type", "Arcano"))
    suit = card_db.get("suit") or "Ninguno"
    element = card_db.get("element", rich_data.get("element", ""))
    astrology = card_db.get("astrology", rich_data.get("astrology", ""))
    
    essence = card_db.get("essence", rich_data.get("significado_fundamental", ""))
    keywords = card_db.get("keywords", [])
    if isinstance(keywords, list):
        keywords_str = ", ".join(keywords)
    else:
        keywords_str = str(keywords)

    light_side = card_db.get("light_side", "")
    shadow_side = card_db.get("shadow_side", "")

    # Symbols
    symbols = card_db.get("symbols", [])
    symbols_xml_lines = []
    for s in symbols:
        s_name = escape_xml(s.get("name", ""))
        s_desc = escape_xml(s.get("desc", ""))
        symbols_xml_lines.append(f"""    <simbolo>
      <nombre>{s_name}</nombre>
      <descripcion>{s_desc}</descripcion>
    </simbolo>""")
    symbols_xml = "\n".join(symbols_xml_lines)

    # Rich fields
    historia = rich_data.get("historia", "")
    significado_fundamental = rich_data.get("significado_fundamental", essence)
    
    pos_normal = rich_data.get("posicion_normal", {})
    pn_resumen = pos_normal.get("resumen", card_db.get("meaning_upright", ""))
    pn_amor = pos_normal.get("amor", card_db.get("love", ""))
    pn_trabajo = pos_normal.get("dinero_trabajo", card_db.get("work", ""))
    pn_salud = pos_normal.get("salud", "Vitalidad en equilibrio y alineamiento con la energía del arcano.")
    pn_espiritualidad = pos_normal.get("espiritualidad", card_db.get("spirituality", ""))

    pos_invertida = rich_data.get("posicion_invertida", {})
    rev_db = card_db.get("reversed", {})
    rev_keywords = rev_db.get("keywords", [])
    if isinstance(rev_keywords, list):
        rev_keywords_str = ", ".join(rev_keywords)
    else:
        rev_keywords_str = str(rev_keywords)
    
    pi_resumen = pos_invertida.get("resumen", rev_db.get("meaning", ""))
    pi_amor = pos_invertida.get("amor", "Desafíos o bloqueos en la comunicación afectiva.")
    pi_trabajo = pos_invertida.get("dinero_trabajo", "Retrasos temporales o dispersión de esfuerzos.")
    pi_salud = pos_invertida.get("salud", "Fatiga o somatización de tensiones.")
    pi_espiritualidad = pos_invertida.get("espiritualidad", "Desconexión transitoria de la guía interior.")
    pi_armonizar = pos_invertida.get("como_armonizar_desbloquear", rev_db.get("how_to_heal", "Meditar en el lado luz del arcano."))

    lo_que_lo_hace_unico = rich_data.get("lo_que_lo_hace_unico", "")
    
    curiosidades = rich_data.get("curiosidades", [])
    curiosidades_xml_lines = []
    for cur in curiosidades:
        curiosidades_xml_lines.append(f"    <item>{escape_xml(cur)}</item>")
    curiosidades_xml = "\n".join(curiosidades_xml_lines)

    advice = card_db.get("advice", "")
    reflection = card_db.get("reflection_question", "")

    historia_inspirada = rich_data.get("historia_inspirada", {})
    hi_titulo = historia_inspirada.get("titulo", f"La Lección de {name}")
    hi_relato = historia_inspirada.get("relato", "")

    audio = rich_data.get("audio", {})
    audio_file = audio.get("archivo", f"assets/audio/{c_id}.mp3")
    audio_title = audio.get("titulo", f"{name} - Audiolibro y Meditación Guiada")
    audio_duration = audio.get("duracion_estimada", "4:00 min")

    xml_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<arcano id="{escape_xml(c_id)}">
  <numero>{escape_xml(number)}</numero>
  <nombre>{escape_xml(name)}</nombre>
  <tipo>{escape_xml(c_type)}</tipo>
  <palo>{escape_xml(suit)}</palo>
  <elemento>{escape_xml(element)}</elemento>
  <astrologia>{escape_xml(astrology)}</astrologia>

  <!-- ESENCIA Y PALABRAS CLAVE -->
  <esencia>{escape_xml(essence)}</esencia>
  <palabras_clave>{escape_xml(keywords_str)}</palabras_clave>

  <!-- POLARIDAD: LUZ Y SOMBRA -->
  <polaridad>
    <lado_luz>{escape_xml(light_side)}</lado_luz>
    <lado_sombra>{escape_xml(shadow_side)}</lado_sombra>
  </polaridad>

  <!-- SÍMBOLOS VISUALES CLAVE -->
  <simbolos_visuales>
{symbols_xml}
  </simbolos_visuales>

  <!-- 1. HISTORIA Y ORIGEN SIMBÓLICO -->
  <historia>
    {escape_xml(historia)}
  </historia>

  <!-- 2. SIGNIFICADO FUNDAMENTAL -->
  <significado_fundamental>
    {escape_xml(significado_fundamental)}
  </significado_fundamental>

  <!-- 3. LA CARTA EN POSICIÓN NORMAL -->
  <posicion_normal>
    <resumen>{escape_xml(pn_resumen)}</resumen>
    <amor>{escape_xml(pn_amor)}</amor>
    <dinero_trabajo>{escape_xml(pn_trabajo)}</dinero_trabajo>
    <salud>{escape_xml(pn_salud)}</salud>
    <espiritualidad>{escape_xml(pn_espiritualidad)}</espiritualidad>
  </posicion_normal>

  <!-- 4. LA CARTA EN POSICIÓN INVERTIDA -->
  <posicion_invertida>
    <resumen>{escape_xml(pi_resumen)}</resumen>
    <palabras_clave_al_reves>{escape_xml(rev_keywords_str)}</palabras_clave_al_reves>
    <amor>{escape_xml(pi_amor)}</amor>
    <dinero_trabajo>{escape_xml(pi_trabajo)}</dinero_trabajo>
    <salud>{escape_xml(pi_salud)}</salud>
    <espiritualidad>{escape_xml(pi_espiritualidad)}</espiritualidad>
    <como_armonizar_desbloquear>{escape_xml(pi_armonizar)}</como_armonizar_desbloquear>
  </posicion_invertida>

  <!-- 5. LO QUE LO HACE ÚNICO FRENTE A SUS SIMILARES -->
  <lo_que_lo_hace_unico>
    {escape_xml(lo_que_lo_hace_unico)}
  </lo_que_lo_hace_unico>

  <!-- 6. CURIOSIDADES DEL ARCANO -->
  <curiosidades>
{curiosidades_xml}
  </curiosidades>

  <!-- CONSEJO Y PREGUNTA REFLEXIVA -->
  <consejo_y_reflexion>
    <accion_inmediata>{escape_xml(advice)}</accion_inmediata>
    <pregunta_para_ti>{escape_xml(reflection)}</pregunta_para_ti>
  </consejo_y_reflexion>

  <!-- 7. UNA HISTORIA INSPIRADA -->
  <historia_inspirada>
    <titulo>{escape_xml(hi_titulo)}</titulo>
    <relato>
      {escape_xml(hi_relato)}
    </relato>
  </historia_inspirada>

  <!-- 8. AUDIOLIBRO / GUÍA DE AUDIO -->
  <audio>
    <archivo>{escape_xml(audio_file)}</archivo>
    <titulo>{escape_xml(audio_title)}</titulo>
    <duracion_estimada>{escape_xml(audio_duration)}</duracion_estimada>
  </audio>
</arcano>
"""
    return xml_content

def main():
    print("Iniciando construcción de la colección de 78 archivos XML...")

    # Load existing tarot database
    with open('data/tarot_database.json', 'r', encoding='utf-8') as f:
        db = json.load(f)

    # Collect all rich data
    all_rich = {}
    for m in MAJORS_DATA_1:
        all_rich[m["id"]] = m
    for m in MAJORS_DATA_2:
        all_rich[m["id"]] = m
    
    minors_list = generate_minors_data()
    for mn in minors_list:
        all_rich[mn["id"]] = mn

    print(f"Total datos enriquecidos cargados: {len(all_rich)} cartas.")

    # Ensure folders
    folders = [
        'cartas_xml/arcanos_mayores',
        'cartas_xml/bastos',
        'cartas_xml/copas',
        'cartas_xml/espadas',
        'cartas_xml/oros',
        'assets/audio'
    ]
    for fold in folders:
        os.makedirs(fold, exist_ok=True)

    generated_count = 0
    updated_cards = []

    for idx, card in enumerate(db["cards"]):
        cid = card["id"]
        rich = all_rich.get(cid, {})

        # Build XML
        xml_str = build_card_xml(card, rich)

        # Determine target file path
        if card.get("type") == "Arcano Mayor":
            # order prefix from rich or idx
            num_int = rich.get("number", idx)
            filename = f"{int(num_int):02d}_{cid.replace('-', '_')}.xml"
            filepath = os.path.join("cartas_xml", "arcanos_mayores", filename)
        else:
            suit = card.get("suit", "bastos").lower()
            suit_folder = suit
            if "basto" in suit:
                suit_folder = "bastos"
            elif "copa" in suit:
                suit_folder = "copas"
            elif "espada" in suit:
                suit_folder = "espadas"
            elif "oro" in suit:
                suit_folder = "oros"
            
            filename = f"{cid.replace('-', '_')}.xml"
            filepath = os.path.join("cartas_xml", suit_folder, filename)

        with open(filepath, "w", encoding="utf-8") as xf:
            xf.write(xml_str)
        
        generated_count += 1

        # Also enrich card in DB for seamless web app access
        card["history"] = rich.get("historia", "")
        card["fundamental_meaning"] = rich.get("significado_fundamental", card.get("essence", ""))
        card["normal_position"] = rich.get("posicion_normal", {
            "resumen": card.get("meaning_upright", ""),
            "amor": card.get("love", ""),
            "dinero_trabajo": card.get("work", ""),
            "salud": "Vitalidad en equilibrio.",
            "espiritualidad": card.get("spirituality", "")
        })
        card["reversed_position"] = rich.get("posicion_invertida", {
            "resumen": card.get("reversed", {}).get("meaning", ""),
            "amor": "Desafíos afectivos.",
            "dinero_trabajo": "Retrasos temporales.",
            "salud": "Descanso necesario.",
            "espiritualidad": "Introspección."
        })
        card["unique_differentiator"] = rich.get("lo_que_lo_hace_unico", "")
        card["curiosities"] = rich.get("curiosidades", [])
        card["inspired_story"] = rich.get("historia_inspirada", {
            "titulo": f"La Parábola de {card['name']}",
            "relato": ""
        })
        card["audio"] = rich.get("audio", {
            "archivo": f"assets/audio/{cid}.mp3",
            "titulo": f"{card['name']} - Audiolibro",
            "duracion_estimada": "4:00 min"
        })

        updated_cards.append(card)

    db["cards"] = updated_cards

    # Save updated DB
    with open('data/tarot_database.json', 'w', encoding='utf-8') as f:
        json.dump(db, f, ensure_ascii=False, indent=2)

    js_content = f"window.TAROT_DB = {json.dumps(db, ensure_ascii=False, indent=2)};\n"
    with open('data/tarot_database.js', 'w', encoding='utf-8') as f:
        f.write(js_content)

    print(f"✨ ¡Éxito rotundo! Se han generado {generated_count} archivos XML enriquecidos.")
    print("✨ Base de datos data/tarot_database.json y data/tarot_database.js sincronizadas.")

if __name__ == '__main__':
    main()
