
import subprocess
import sys
import os

def install_package(package):
    """Instalar paquete si no está disponible"""
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def check_and_install_dependencies():
    """Verificar e instalar dependencias automáticamente"""
    required_packages = {
        'pyrogram': 'pyrogram>=2.0.106',
        'requests': 'requests>=2.32.4'
    }

    for package_name, package_spec in required_packages.items():
        try:
            __import__(package_name)
            print(f"✅ {package_name} ya está instalado")
        except ImportError:
            print(f"⚠️ {package_name} no encontrado, instalando...")
            try:
                install_package(package_spec)
                print(f"✅ {package_name} instalado correctamente")
            except Exception as e:
                print(f"❌ Error instalando {package_name}: {e}")
                sys.exit(1)

# Verificar e instalar dependencias al inicio
check_and_install_dependencies()

import re
import time
import requests
import random
import sqlite3
import hashlib
from pyrogram import Client, enums
from banderas_bin import get_country_info, get_country_code_from_name
from api_bin_base import get_bin_info_complete
from luhn_validator import luhn_check_strict

def init_database():
    """Inicializar base de datos SQLite"""
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    
    # Tabla para tarjetas enviadas (evitar duplicados)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sent_cards (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            card_number TEXT UNIQUE NOT NULL,
            bin_number TEXT NOT NULL,
            sent_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            bank_name TEXT,
            country TEXT
        )
    ''')
    
    # Tabla para progreso de mensajes por grupo (continuar desde donde se quedó)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS group_progress (
            group_id INTEGER PRIMARY KEY,
            group_name TEXT,
            last_message_id INTEGER NOT NULL,
            last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Índices para optimizar consultas
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_card_number ON sent_cards(card_number)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_bin_number ON sent_cards(bin_number)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_group_id ON group_progress(group_id)')
    
    conn.commit()
    conn.close()
    print("✅ Base de datos SQLite inicializada correctamente")

def is_card_already_sent(card_number):
    """Verificar si una tarjeta ya fue enviada"""
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT COUNT(*) FROM sent_cards WHERE card_number = ?', (card_number,))
    exists = cursor.fetchone()[0] > 0
    
    conn.close()
    return exists

def save_sent_card(card, bin_info):
    """Guardar tarjeta enviada en la base de datos"""
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    
    try:
        cursor.execute('''
            INSERT OR REPLACE INTO sent_cards 
            (card_number, bin_number, bank_name, country) 
            VALUES (?, ?, ?, ?)
        ''', (
            card['number'],
            card['number'][:6],
            bin_info.get('bank', 'Unknown'),
            bin_info.get('country', 'Unknown')
        ))
        conn.commit()
    except sqlite3.Error as e:
        print(f"⚠️ Error guardando tarjeta: {e}")
    finally:
        conn.close()

def get_last_processed_message(group_id):
    """Obtener el último mensaje procesado de un grupo"""
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT last_message_id FROM group_progress WHERE group_id = ?', (group_id,))
    result = cursor.fetchone()
    
    conn.close()
    return result[0] if result else 0

def update_group_progress(group_id, group_name, message_id):
    """Actualizar el progreso de un grupo"""
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT OR REPLACE INTO group_progress 
        (group_id, group_name, last_message_id, last_updated) 
        VALUES (?, ?, ?, CURRENT_TIMESTAMP)
    ''', (group_id, group_name, message_id))
    
    conn.commit()
    conn.close()

def get_database_stats():
    """Obtener estadísticas de la base de datos"""
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT COUNT(*) FROM sent_cards')
    total_cards = cursor.fetchone()[0]
    
    cursor.execute('SELECT COUNT(*) FROM group_progress')
    total_groups = cursor.fetchone()[0]
    
    cursor.execute('SELECT group_name, last_message_id FROM group_progress')
    groups_progress = cursor.fetchall()
    
    conn.close()
    
    return {
        'total_cards': total_cards,
        'total_groups': total_groups,
        'groups_progress': groups_progress
    }


def format_card_message(card, bin_info):
    """Format card message with beautiful new design"""
    bin_number = card['number'][:6]
    
    # Tarjeta completa
    full_card_complete = f"{card['number']}|{card['month']}|{card['year']}|{card['cvv']}"
    
    # Tarjeta enmascarada
    masked_number = f"{card['number'][:10]}xxxx"
    full_card_masked = f"{masked_number}|{card['month']}|{card['year']}|rnd"

    # Información del banco en negrita cursiva
    bank_info = f"<b><i>{bin_info['bank']}, {bin_info['type'].upper()} {bin_info['flag']}</i></b>"

    message = f"""​(Newبوت) 𝗬𝗵𝘄𝗮𝗰𝗵 𝘀𝗰𝗿𝗮𝗽𝗽𝗲𝗿 [#{bin_number}

<a href='https://t.me/Os_cracking'>« 水 »</a> 𝙘𝙘 𝙫𝙖𝙡𝙞𝙙𝙤 » <code>{full_card_complete}</code>

<code>{full_card_masked}</code>

{bank_info}"""

    return message

def extract_card_data_strict(text):
    """Extract and strictly validate credit card data from text"""
    # Multiple patterns to catch different formats
    patterns = [
        r'(\d{13,19})\|(\d{1,2})\|(\d{4})\|(\d{3,4})',  # Standard format
        r'(\d{13,19})\|(\d{1,2})\|(\d{2})\|(\d{3,4})',   # 2-digit year
        r'(\d{4}[\s\-]?\d{4}[\s\-]?\d{4}[\s\-]?\d{3,4})\|(\d{1,2})\|(\d{2,4})\|(\d{3,4})'  # Spaced cards
    ]

    for pattern in patterns:
        matches = re.findall(pattern, text)

        for match in matches:
            card_number, month, year, cvv = match

            # Remove any spaces, dashes or formatting from card number
            clean_card = re.sub(r'[\s\-]', '', card_number)
            clean_card = re.sub(r'\D', '', clean_card)

            # Strict Luhn validation
            if not luhn_check_strict(clean_card):
                continue

            # Normalize year (convert 2-digit to 4-digit if needed)
            if len(year) == 2:
                year_int = int(year)
                if year_int >= 24:  # Assuming 24+ means 2024+
                    year = f"20{year}"
                else:
                    year = f"20{year}"

            # Additional validations
            month_int = int(month)
            year_int = int(year)

            # Rechazar tarjetas con CVC "000"
            if cvv == '000':
                continue

            if 1 <= month_int <= 12 and year_int >= 2024:
                card_type = get_card_type(clean_card)

                card_info = {
                    'number': clean_card,
                    'month': month.zfill(2),  # Ensure 2 digits
                    'year': year,
                    'cvv': cvv,
                    'type': card_type
                }

                return card_info  # Return first valid card found

    return None

def load_image_cache():
    """Load and cache images in memory"""
    global CACHED_IMAGES

    if 'CACHED_IMAGES' in globals() and CACHED_IMAGES:
        return CACHED_IMAGES

    print("🖼️ Cargando imágenes en caché...")

    image_files = [
        'SaveTik.co_7442722067365104951_3.jpeg',
        'SaveTik.co_7442722067365104951_4.jpeg', 
        'SaveTik.co_7442722067365104951_5.jpeg',
        'SaveTik.co_7449025026050788614_6.jpeg',
        'SaveTik.co_7449025026050788614_8.jpeg',
        'SaveTik.co_7451622708523109650_8 (1).jpeg',
        'SaveTik.co_7459487149373558021_4.jpeg',
        'SaveTik.co_7531953203999509816_2.jpeg',
        'SaveTik.co_7531953203999509816_4.jpeg',
        'SaveTik.co_7535603264943901958_2.jpeg',
        'SaveTik.co_7535603264943901958_4.jpeg',
        'SaveTik.co_7535603264943901958_6.jpeg'
    ]

    # Cache only existing files
    CACHED_IMAGES = [img for img in image_files if os.path.exists(img)]

    print(f"✅ {len(CACHED_IMAGES)} imágenes cargadas en caché")
    return CACHED_IMAGES

def get_random_image():
    """Get a random image from cache"""
    cached_images = load_image_cache()

    if cached_images:
        return random.choice(cached_images)
    return None

def get_card_type(card_number):
    """Determine card type based on number patterns"""
    # Visa: starts with 4
    if card_number.startswith('4'):
        return 'Visa'

    # Mastercard: 51-55, 2221-2720
    elif (card_number.startswith(('51', '52', '53', '54', '55')) or
          (card_number.startswith('22') and int(card_number[:4]) >= 2221 and int(card_number[:4]) <= 2720)):
        return 'Mastercard'

    # American Express: 34, 37
    elif card_number.startswith(('34', '37')):
        return 'American Express'

    # Discover: 6011, 622126-622925, 644-649, 65
    elif (card_number.startswith('6011') or
          card_number.startswith('65') or
          (card_number.startswith('62') and int(card_number[:6]) >= 622126 and int(card_number[:6]) <= 622925) or
          (card_number.startswith(('644', '645', '646', '647', '648', '649')))):
        return 'Discover'

    # Diners Club: 300-305, 36, 38
    elif card_number.startswith(('300', '301', '302', '303', '304', '305', '36', '38')):
        return 'Diners Club'

    # JCB: 35, 2131, 1800
    elif card_number.startswith(('35', '2131', '1800')):
        return 'JCB'

    # UnionPay: 62, 81
    elif card_number.startswith(('62', '81')):
        return 'UnionPay'

    else:
        return 'Unknown'

def run_scraper_mode(app, send_group_id, target_groups, target_cards=10):
    """Modo scraper: obtener tarjetas de grupos de Telegram con progreso guardado"""
    print(f"\n🔍 MODO SCRAPER ACTIVADO - Objetivo: {target_cards} tarjetas")
    print("=" * 60)

    # Seleccionar grupo aleatoriamente
    target_chat = random.choice(target_groups)
    print(f"🎯 Grupo seleccionado: {target_chat['title']} (ID: {target_chat['id']})")

    # Obtener último mensaje procesado de este grupo
    last_processed_id = get_last_processed_message(target_chat['id'])
    print(f"📍 Último mensaje procesado en este grupo: {last_processed_id}")

    cards_found = 0
    messages_processed = 0
    last_processed_msg_id = last_processed_id  # Guardar referencia del último mensaje procesado

    try:
        chat_info = app.get_chat(target_chat['id'])
        print(f"📊 Chat: {chat_info.title}")
        print(f"👥 Miembros: {getattr(chat_info, 'members_count', 'N/A')}")
        print("-" * 40)

        for msg in app.get_chat_history(target_chat['id'], limit=5000):
            if cards_found >= target_cards:
                break

            # Solo procesar mensajes más nuevos que el último procesado
            if msg.id <= last_processed_id:
                continue

            messages_processed += 1
            last_processed_msg_id = msg.id  # Actualizar el último mensaje procesado

            if msg.text:
                card = extract_card_data_strict(msg.text)

                if card:
                    # Verificar si la tarjeta ya fue enviada
                    if not is_card_already_sent(card['number']):
                        user = msg.from_user.first_name if msg.from_user else "Anónimo"

                        print(f"\n💳 TARJETA {card['type'].upper()} ENCONTRADA:")
                        print(f"   👤 Usuario: {user}")
                        print(f"   🔢 Número: {card['number'][:6]}...{card['number'][-4:]}")
                        print(f"   📅 Exp: {card['month']}/{card['year']}")
                        print(f"   🔐 CVV: {card['cvv']}")

                        try:
                            bin_number = card['number'][:6]
                            print(f"🔍 Obteniendo información del BIN {bin_number}...")
                            bin_info = get_bin_info_complete(bin_number)
                            print(f"✅ Información del BIN obtenida: {bin_info['bank']} - {bin_info['country']} {bin_info['flag']}")
                            
                            random_image = get_random_image()

                            # Enviar tarjeta
                            try:
                                print(f"📤 Enviando tarjeta...")
                                formatted_message = format_card_message(card, bin_info)
                                if random_image:
                                    app.send_photo(send_group_id, random_image, caption=formatted_message, parse_mode=enums.ParseMode.HTML)
                                else:
                                    app.send_message(send_group_id, formatted_message, parse_mode=enums.ParseMode.HTML)
                                
                                # Guardar tarjeta en base de datos
                                save_sent_card(card, bin_info)
                                
                                # Guardar progreso inmediatamente después de cada tarjeta enviada
                                update_group_progress(target_chat['id'], target_chat['title'], last_processed_msg_id)
                                
                                cards_found += 1
                                print(f"✅ Tarjeta enviada y guardada! ({cards_found}/{target_cards})")
                                print(f"🏦 {bin_info['bank']} - {bin_info['country']} {bin_info['flag']}")
                                print(f"💾 Progreso actualizado: mensaje {last_processed_msg_id}")

                                # Esperar anti-spam
                                if cards_found < target_cards:
                                    print(f"⏳ Esperando 35 segundos anti-spam...")
                                    time.sleep(35)
                                    
                            except Exception as e:
                                print(f"❌ Error enviando tarjeta: {e}")

                        except Exception as send_error:
                            print(f"❌ Error general enviando tarjeta: {send_error}")
                    else:
                        print(f"⚠️ Tarjeta {card['number'][:6]}...{card['number'][-4:]} ya fue enviada anteriormente")

            # Actualizar progreso cada 50 mensajes
            if messages_processed % 50 == 0:
                update_group_progress(target_chat['id'], target_chat['title'], last_processed_msg_id)
                print(f"💾 Progreso guardado: mensaje {last_processed_msg_id}")

            if messages_processed % 100 == 0:
                print(f"📊 Progreso scraper: {messages_processed} mensajes | {cards_found} tarjetas")

        # Guardar progreso final del grupo (el último mensaje que realmente se procesó)
        if messages_processed > 0:
            update_group_progress(target_chat['id'], target_chat['title'], last_processed_msg_id)
            print(f"💾 Progreso final guardado: mensaje {last_processed_msg_id}")
            print(f"✅ Próximo ciclo empezará desde mensaje {last_processed_msg_id + 1}")
        else:
            print("⚠️ No se procesaron mensajes nuevos en este grupo")

    except Exception as e:
        print(f"❌ Error en scraper: {e}")

    print(f"\n📊 SCRAPER COMPLETADO: {cards_found} tarjetas obtenidas")
    return cards_found

def main():
    # Inicializar base de datos
    init_database()

    # Telegram API credentials
    api_id = 24383778
    api_hash = "cf2a1c18609b86cc93ed8ab024d67436"
    phone_number = "+573215438084"

    # Target group to send cards
    send_group_id = -1002395617812

    app = Client(
        "scraper_session",
        api_id=api_id,
        api_hash=api_hash,
        phone_number=phone_number
    )

    with app:
        print("🔍 SCRAPER DE TARJETAS DE CRÉDITO")
        print("=" * 60)
        print("🎯 Modo: SOLO SCRAPER")
        print("📊 Objetivo: 10 tarjetas por ciclo")
        print("🔍 Obtención: Solo de grupos de Telegram")
        print("💾 Base de datos: SQLite (base.db)")
        print("=" * 60)

        # Lista todos los chats disponibles
        available_chats = []
        try:
            for dialog in app.get_dialogs():
                chat = dialog.chat
                if chat.type.name in ['SUPERGROUP', 'GROUP']:
                    available_chats.append({
                        'id': chat.id,
                        'title': chat.title,
                        'type': chat.type.name
                    })
                    print(f"🏷️  {chat.title} (ID: {chat.id})")
        except Exception as e:
            print(f"❌ Error al listar chats: {e}")
            return

        # GRUPOS ESPECÍFICOS PARA SCRAPING
        target_group_ids = [
            -1002395617812,  # Grupo original 1
            -1002688859296,  # 𝑪𝒉𝒂𝒕 𝒀𝒖𝒎𝒆𝒌𝒐あ
            -1002848973190,  # YoshiFree
            -1002489292226,  # OX_Users  
            -1003035368779,  # Chisachk
            -1002254611693   # ryas_chat
        ]
        target_groups = [chat for chat in available_chats if chat['id'] in target_group_ids]

        if not target_groups:
            print("❌ No se encontraron los grupos objetivo")
            return

        print(f"🔄 Grupos disponibles para scraping: {[g['title'] for g in target_groups]}")

        # Cargar sistemas y mostrar estadísticas
        print("\n📂 Cargando sistemas...")
        load_image_cache()
        
        # Mostrar estadísticas de la base de datos
        stats = get_database_stats()
        print(f"💾 Base de datos SQLite:")
        print(f"   📊 Tarjetas únicas: {stats['total_cards']}")
        print(f"   📊 Grupos con progreso: {stats['total_groups']}")
        
        for group_name, last_msg_id in stats['groups_progress']:
            print(f"   📍 {group_name}: último mensaje {last_msg_id}")

        total_cards_sent = 0
        cycle = 1

        # LOOP PRINCIPAL DE SCRAPING
        while True:
            print(f"\n🔄 CICLO {cycle} - MODO SCRAPER")
            print("=" * 50)

            print("📡 MODO SCRAPER ACTIVADO")
            print("🔍 Obteniendo tarjetas de grupos de Telegram")

            cards_in_cycle = run_scraper_mode(
                app, send_group_id, target_groups, target_cards=10
            )

            total_cards_sent += cards_in_cycle

            # Mostrar estadísticas actualizadas
            stats = get_database_stats()

            print(f"\n📊 RESUMEN CICLO {cycle}:")
            print(f"   Tarjetas enviadas en este ciclo: {cards_in_cycle}")
            print(f"   Total acumulado: {total_cards_sent}")
            print(f"   Tarjetas únicas en BD: {stats['total_cards']}")

            cycle += 1

            # Pausa entre ciclos
            print(f"\n⏱️ Pausa entre ciclos: 60 segundos...")
            time.sleep(60)
            print("🔄 Iniciando siguiente ciclo...")

if __name__ == "__main__":
    main()
