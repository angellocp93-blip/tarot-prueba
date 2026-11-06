# -*- coding: utf-8 -*-
"""
Sincronizador bidireccional XML -> Base de Datos
Lee todos los archivos XML en 'cartas_xml/' y actualiza:
- data/tarot_database.json
- data/tarot_database.js
Permite al usuario editar cualquier texto en XML y ver reflejado
el cambio en la plataforma web al instante.
"""

import json
import os
import xml.etree.ElementTree as ET

def get_tag_text(root, tag, default=""):
    node = root.find(tag)
    if node is not None and node.text:
        return node.text.strip()
    return default

def sync():
    db_json_path = os.path.join('data', 'tarot_database.json')
    db_js_path = os.path.join('data', 'tarot_database.js')

    if not os.path.exists(db_json_path):
        print(f"Error: No se encontró {db_json_path}")
        return

    with open(db_json_path, 'r', encoding='utf-8') as f:
        db = json.load(f)

    cards_map = {c["id"]: c for c in db.get("cards", [])}

    xml_base_dir = "cartas_xml"
    parsed_count = 0

    for root_dir, _, files in os.walk(xml_base_dir):
        for fname in files:
            if not fname.endswith('.xml'):
                continue
            xml_path = os.path.join(root_dir, fname)
            try:
                tree = ET.parse(xml_path)
                root = tree.getroot()
                card_id = root.attrib.get('id')
                if not card_id or card_id not in cards_map:
                    continue

                card = cards_map[card_id]

                # Update core fields if present
                card["name"] = get_tag_text(root, "nombre", card.get("name"))
                card["element"] = get_tag_text(root, "elemento", card.get("element"))
                card["astrology"] = get_tag_text(root, "astrologia", card.get("astrology"))
                card["essence"] = get_tag_text(root, "esencia", card.get("essence"))

                # Keywords
                kw_text = get_tag_text(root, "palabras_clave", "")
                if kw_text:
                    card["keywords"] = [k.strip() for k in kw_text.split(",") if k.strip()]

                # Polarity
                pol_node = root.find("polaridad")
                if pol_node is not None:
                    card["light_side"] = get_tag_text(pol_node, "lado_luz", card.get("light_side", ""))
                    card["shadow_side"] = get_tag_text(pol_node, "lado_sombra", card.get("shadow_side", ""))

                # Symbols
                sym_node = root.find("simbolos_visuales")
                if sym_node is not None:
                    parsed_symbols = []
                    for s in sym_node.findall("simbolo"):
                        s_name = get_tag_text(s, "nombre")
                        s_desc = get_tag_text(s, "descripcion")
                        if s_name:
                            parsed_symbols.append({"name": s_name, "desc": s_desc})
                    if parsed_symbols:
                        card["symbols"] = parsed_symbols

                # History & Fundamental meaning
                card["history"] = get_tag_text(root, "historia", card.get("history", ""))
                card["fundamental_meaning"] = get_tag_text(root, "significado_fundamental", card.get("fundamental_meaning", ""))

                # Normal position
                pn_node = root.find("posicion_normal")
                if pn_node is not None:
                    pn_resumen = get_tag_text(pn_node, "resumen", card.get("meaning_upright", ""))
                    pn_amor = get_tag_text(pn_node, "amor", card.get("love", ""))
                    pn_trabajo = get_tag_text(pn_node, "dinero_trabajo", card.get("work", ""))
                    pn_salud = get_tag_text(pn_node, "salud", "Vitalidad en equilibrio.")
                    pn_espiritualidad = get_tag_text(pn_node, "espiritualidad", card.get("spirituality", ""))

                    card["meaning_upright"] = pn_resumen
                    card["love"] = pn_amor
                    card["work"] = pn_trabajo
                    card["spirituality"] = pn_espiritualidad
                    card["normal_position"] = {
                        "resumen": pn_resumen,
                        "amor": pn_amor,
                        "dinero_trabajo": pn_trabajo,
                        "salud": pn_salud,
                        "espiritualidad": pn_espiritualidad
                    }

                # Reversed position
                pi_node = root.find("posicion_invertida")
                if pi_node is not None:
                    rev_obj = card.get("reversed", {})
                    pi_resumen = get_tag_text(pi_node, "resumen", rev_obj.get("meaning", ""))
                    pi_kw_text = get_tag_text(pi_node, "palabras_clave_al_reves", "")
                    if pi_kw_text:
                        rev_obj["keywords"] = [k.strip() for k in pi_kw_text.split(",") if k.strip()]
                    pi_amor = get_tag_text(pi_node, "amor", "")
                    pi_trabajo = get_tag_text(pi_node, "dinero_trabajo", "")
                    pi_salud = get_tag_text(pi_node, "salud", "")
                    pi_espiritualidad = get_tag_text(pi_node, "espiritualidad", "")
                    pi_armonizar = get_tag_text(pi_node, "como_armonizar_desbloquear", rev_obj.get("how_to_heal", ""))

                    rev_obj["meaning"] = pi_resumen
                    rev_obj["how_to_heal"] = pi_armonizar
                    card["reversed"] = rev_obj
                    card["reversed_position"] = {
                        "resumen": pi_resumen,
                        "amor": pi_amor,
                        "dinero_trabajo": pi_trabajo,
                        "salud": pi_salud,
                        "espiritualidad": pi_espiritualidad,
                        "como_armonizar_desbloquear": pi_armonizar
                    }

                # Unique differentiator
                card["unique_differentiator"] = get_tag_text(root, "lo_que_lo_hace_unico", card.get("unique_differentiator", ""))

                # Curiosities
                cur_node = root.find("curiosidades")
                if cur_node is not None:
                    cur_items = [item.text.strip() for item in cur_node.findall("item") if item.text]
                    if cur_items:
                        card["curiosities"] = cur_items

                # Advice and Reflection
                cr_node = root.find("consejo_y_reflexion")
                if cr_node is not None:
                    card["advice"] = get_tag_text(cr_node, "accion_inmediata", card.get("advice", ""))
                    card["reflection_question"] = get_tag_text(cr_node, "pregunta_para_ti", card.get("reflection_question", ""))

                # Inspired Story
                hi_node = root.find("historia_inspirada")
                if hi_node is not None:
                    card["inspired_story"] = {
                        "titulo": get_tag_text(hi_node, "titulo", "Historia del Arcano"),
                        "relato": get_tag_text(hi_node, "relato", "")
                    }

                # Audio
                audio_node = root.find("audio")
                if audio_node is not None:
                    card["audio"] = {
                        "archivo": get_tag_text(audio_node, "archivo", f"assets/audio/{card_id}.mp3"),
                        "titulo": get_tag_text(audio_node, "titulo", f"{card['name']} - Audiolibro"),
                        "duracion_estimada": get_tag_text(audio_node, "duracion_estimada", "4:00 min")
                    }

                parsed_count += 1
            except Exception as e:
                print(f"Error procesando {xml_path}: {e}")

    # Save to JSON
    with open(db_json_path, 'w', encoding='utf-8') as f:
        json.dump(db, f, ensure_ascii=False, indent=2)

    # Save to JS
    js_content = f"window.TAROT_DB = {json.dumps(db, ensure_ascii=False, indent=2)};\n"
    with open(db_js_path, 'w', encoding='utf-8') as f:
        f.write(js_content)

    print(f"✅ Sincronización completada exitosamente: {parsed_count} archivos XML leídos y actualizados en la base de datos.")

if __name__ == '__main__':
    sync()
