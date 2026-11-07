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
import wave
import subprocess

def parse_time_to_seconds(time_str):
    if not time_str:
        return 0
    t = str(time_str).strip().replace("min", "").replace("s", "").strip()
    parts = t.split(":")
    try:
        if len(parts) == 1:
            return int(float(parts[0]))
        elif len(parts) == 2:
            return int(parts[0]) * 60 + int(float(parts[1]))
        elif len(parts) == 3:
            return int(parts[0]) * 3600 + int(parts[1]) * 60 + int(float(parts[2]))
    except Exception:
        return 0
    return 0

def format_seconds_to_time(sec):
    mins = sec // 60
    s = sec % 60
    return f"{mins}:{s:02d}"

def probe_audio_duration(card_id, explicit_path=""):
    """
    Intenta calcular automáticamente la duración del archivo de audio buscando
    en assets/audio/ las extensiones comunes (.wav, .mp3, .m4a).
    """
    candidates = []
    if explicit_path:
        candidates.append(explicit_path)
        candidates.append(explicit_path.replace('\\', '/'))
        candidates.append(explicit_path.replace('/', '\\'))
    
    audio_dir = os.path.join("assets", "audio")
    id_clean = card_id.lower().replace('_', '-')
    id_under = card_id.lower().replace('-', '_')

    candidates.extend([
        os.path.join(audio_dir, f"{card_id}.wav"),
        os.path.join(audio_dir, f"{card_id}.mp3"),
        os.path.join(audio_dir, f"{id_under}.wav"),
        os.path.join(audio_dir, f"{id_under}.mp3"),
    ])

    # Búsqueda automática en assets/audio/ de archivos que coincidan (ej. 00_el_loco.wav)
    if os.path.isdir(audio_dir):
        for fname in os.listdir(audio_dir):
            low = fname.lower().replace('-', '_')
            if id_under in low:
                candidates.append(os.path.join(audio_dir, fname))
    
    for c_path in candidates:
        if not os.path.isfile(c_path):
            continue
        # Intento 1: Archivo WAV nativo
        if c_path.lower().endswith('.wav'):
            try:
                with wave.open(c_path, 'rb') as wf:
                    fr = wf.getframerate()
                    if fr > 0:
                        sec = int(wf.getnframes() / float(fr))
                        return f"{sec // 60}:{sec % 60:02d} min", sec
            except Exception:
                pass
        # Intento 2: ffprobe si está disponible
        try:
            cmd = ['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', c_path]
            res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=2)
            if res.returncode == 0 and res.stdout.strip():
                sec = int(float(res.stdout.strip()))
                return f"{sec // 60}:{sec % 60:02d} min", sec
        except Exception:
            pass
    return None, None

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

                # Unique differentiator (supports plain text or structured comparisons)
                unique_node = root.find("lo_que_lo_hace_unico")
                if unique_node is not None:
                    comparisons = []
                    comp_nodes = (
                        unique_node.findall(".//comparar_con")
                        + unique_node.findall(".//comparar")
                        + unique_node.findall(".//comparacion")
                    )
                    for comp in comp_nodes:
                        target_name = comp.attrib.get("carta") or comp.attrib.get("nombre") or comp.attrib.get("id")
                        if not target_name:
                            carta_child = comp.find("carta") or comp.find("nombre")
                            if carta_child is not None and carta_child.text:
                                target_name = carta_child.text.strip()
                        
                        diff_child = comp.find("diferencia") or comp.find("descripcion")
                        if diff_child is not None and diff_child.text:
                            diff_text = diff_child.text.strip()
                        else:
                            diff_text = "".join(comp.itertext()).strip()
                            if target_name and diff_text.startswith(target_name):
                                diff_text = diff_text[len(target_name):].strip().lstrip(":- ").strip()
                        
                        if target_name and diff_text:
                            comparisons.append({
                                "card": target_name,
                                "difference": diff_text
                            })

                    sum_node = unique_node.find("resumen")
                    if sum_node is None:
                        sum_node = unique_node.find("descripcion")
                    if sum_node is None:
                        sum_node = unique_node.find("esencia_diferencial")

                    if sum_node is not None and sum_node.text:
                        summary_text = sum_node.text.strip()
                    elif not comparisons:
                        summary_text = (unique_node.text or "").strip()
                    else:
                        summary_text = (unique_node.text or "").strip()

                    if comparisons:
                        card["unique_differentiator"] = {
                            "summary": summary_text,
                            "comparisons": comparisons
                        }
                    else:
                        card["unique_differentiator"] = summary_text or card.get("unique_differentiator", "")

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

                # Audio & Chapters (con cálculo automático de duración)
                audio_node = root.find("audio")
                if audio_node is not None:
                    raw_audio = get_tag_text(audio_node, "archivo", "").strip().replace('\\', '/')
                    if not raw_audio:
                        audio_file = f"assets/audio/{card_id}.wav"
                    elif not raw_audio.startswith("assets/") and not raw_audio.startswith("http"):
                        audio_file = f"assets/audio/{raw_audio.lstrip('/')}"
                    else:
                        audio_file = raw_audio.lstrip('/')

                    audio_title = get_tag_text(audio_node, "titulo", f"{card['name']} - Audiolibro")
                    est_duration = get_tag_text(audio_node, "duracion_estimada", "")
                    
                    # Calcular duración automáticamente desde el archivo físico si existe
                    auto_duration_str, auto_duration_sec = probe_audio_duration(card_id, audio_file)
                    
                    # Parsear Capítulos si existen
                    chapters = []
                    cap_node = audio_node.find("capitulos")
                    if cap_node is not None:
                        for item in cap_node.findall("capitulo") + cap_node.findall("item"):
                            time_val = (
                                item.attrib.get("tiempo")
                                or item.attrib.get("time")
                                or item.attrib.get("min")
                                or item.attrib.get("timestamp")
                                or ""
                            )
                            if not time_val:
                                t_node = item.find("tiempo") or item.find("time")
                                if t_node is not None and t_node.text:
                                    time_val = t_node.text.strip()
                            
                            title_val = (
                                item.attrib.get("titulo")
                                or item.attrib.get("nombre")
                                or item.attrib.get("title")
                                or ""
                            )
                            if not title_val:
                                t_node = item.find("titulo") or item.find("nombre")
                                if t_node is not None and t_node.text:
                                    title_val = t_node.text.strip()
                                elif item.text:
                                    title_val = item.text.strip()
                            
                            sec_val = parse_time_to_seconds(time_val)
                            formatted_time = format_seconds_to_time(sec_val)
                            
                            if title_val:
                                chapters.append({
                                    "time": formatted_time,
                                    "seconds": sec_val,
                                    "title": title_val
                                })
                    
                    # Ordenar capítulos cronológicamente
                    chapters.sort(key=lambda x: x["seconds"])
                    
                    card["audio"] = {
                        "archivo": audio_file,
                        "titulo": audio_title,
                        "duracion_estimada": est_duration or auto_duration_str or "Por calcular",
                        "duracion_calculada": auto_duration_str or "",
                        "duracion_segundos": auto_duration_sec or 0,
                        "capitulos": chapters
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

