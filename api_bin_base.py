
"""
Módulo para consultar información de BINs usando múltiples APIs
y archivo CSV como respaldo
"""

import requests
import csv
import os
from banderas_bin import get_country_info, get_country_code_from_name

def load_bins_csv():
    """Cargar base de datos local de BINs desde CSV"""
    bins_db = {}
    csv_file = "bins.csv"
    
    if not os.path.exists(csv_file):
        print(f"⚠️ Archivo {csv_file} no encontrado")
        return bins_db
    
    try:
        with open(csv_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                bin_number = row.get('number', '').strip()
                if bin_number and len(bin_number) >= 6:
                    bins_db[bin_number] = {
                        'bin': bin_number,
                        'bank': row.get('bank', 'Unknown Bank').upper(),
                        'scheme': row.get('vendor', 'Unknown').upper(),
                        'type': row.get('type', 'Unknown').upper(),
                        'brand': row.get('vendor', 'Unknown').upper(),
                        'country': row.get('country', 'Unknown').upper(),
                        'flag': row.get('flag', '🏳️'),
                        'level': row.get('level', '').upper(),
                        'api_used': 'local_csv'
                    }
        
        print(f"✅ Base de datos CSV cargada: {len(bins_db)} BINs")
        return bins_db
        
    except Exception as e:
        print(f"❌ Error cargando CSV: {e}")
        return bins_db

def search_bin_in_csv(bin_number, bins_db):
    """Buscar BIN en la base de datos CSV"""
    # Busca coincidencia exacta primero
    if bin_number in bins_db:
        return bins_db[bin_number]
    
    # Busca por prefijos (6 dígitos hacia abajo)
    for length in range(6, 3, -1):
        prefix = bin_number[:length]
        if prefix in bins_db:
            result = bins_db[prefix].copy()
            result['bin'] = bin_number  # Actualizar con el BIN completo buscado
            return result
    
    return None

def get_bin_info_from_apis(bin_number):
    """Consultar información de BIN usando múltiples APIs externas"""
    apis_config = [
        {
            'url': f"https://lookup.binlist.net/{bin_number}",
            'type': 'binlist',
            'headers': {},
            'timeout': 10
        },
        {
            'url': f"https://bins.antipublic.cc/bins/{bin_number}",
            'type': 'antipublic',
            'headers': {},
            'timeout': 8
        },
        {
            'url': f"https://bin-checker.net/api/{bin_number}",
            'type': 'binchecker',
            'headers': {},
            'timeout': 8
        },
        {
            'url': f"https://api.freebinchecker.com/bin/{bin_number}",
            'type': 'freebinchecker',
            'headers': {},
            'timeout': 8
        },
        {
            'url': f"https://binlookup.org/api/{bin_number}",
            'type': 'binlookup',
            'headers': {},
            'timeout': 8
        }
    ]

    print(f"🔄 Probando {len(apis_config)} APIs para BIN {bin_number}...")

    for i, api_config in enumerate(apis_config, 1):
        try:
            print(f"   API {i}/{len(apis_config)}: {api_config['type']}")

            response = requests.get(
                api_config['url'],
                headers=api_config['headers'],
                timeout=api_config['timeout']
            )

            if response.status_code == 200:
                data = response.json()

                # Parse response based on API type
                if api_config['type'] == 'binlist':
                    country_info = data.get('country', {})
                    country_code = country_info.get('alpha2', '').upper() if country_info else ''
                    country_name = country_info.get('name', 'Unknown').upper() if country_info else 'Unknown'

                    bank_info = data.get('bank', {})
                    bank_name = bank_info.get('name', 'Unknown Bank').upper() if bank_info else 'Unknown Bank'

                    # Get proper country name and flag
                    final_country_name, country_flag = get_country_info(country_code, country_name)

                    result = {
                        'bin': bin_number,
                        'bank': bank_name,
                        'scheme': data.get('scheme', 'Unknown').upper(),
                        'type': data.get('type', 'Unknown').upper(),
                        'brand': data.get('brand', data.get('scheme', 'Unknown')).upper(),
                        'country': country_code if country_code else final_country_name,
                        'flag': country_flag,
                        'api_used': api_config['type']
                    }

                elif api_config['type'] == 'antipublic':
                    country_code = data.get('country_code', '').upper()
                    country_name = data.get('country', 'Unknown').upper()

                    # Mapeo directo para casos comunes problemáticos de esta API
                    country_mappings = {
                        'UNITED STATES': 'US',
                        'UNITED STATES OF AMERICA': 'US',
                        'USA': 'US',
                        'AMERICA': 'US',
                        'MEXICO': 'MX',
                        'CANADA': 'CA',
                        'UNITED KINGDOM': 'GB',
                        'UK': 'GB',
                        'GERMANY': 'DE',
                        'FRANCE': 'FR',
                        'SPAIN': 'ES',
                        'ITALY': 'IT',
                        'BRAZIL': 'BR'
                    }

                    # Si no tenemos country_code válido, intentar obtenerlo del nombre
                    if not country_code or country_code == 'UNKNOWN':
                        if country_name in country_mappings:
                            country_code = country_mappings[country_name]
                        else:
                            country_code = get_country_code_from_name(country_name)

                    # Forzar US para casos específicos detectados
                    if any(term in country_name.lower() for term in ['united states', 'usa', 'america']):
                        country_code = 'US'

                    final_country_name, country_flag = get_country_info(country_code, country_name)

                    result = {
                        'bin': bin_number,
                        'bank': data.get('bank', 'Unknown Bank').upper(),
                        'scheme': data.get('brand', 'Unknown').upper(),
                        'type': data.get('type', 'Unknown').upper(),
                        'brand': data.get('brand', 'Unknown').upper(),
                        'country': country_code if country_code else final_country_name,
                        'flag': country_flag,
                        'api_used': api_config['type']
                    }

                elif api_config['type'] == 'binchecker':
                    country_code = data.get('country', {}).get('alpha2', '').upper()
                    country_name = data.get('country', {}).get('name', 'Unknown').upper()

                    final_country_name, country_flag = get_country_info(country_code, country_name)

                    result = {
                        'bin': bin_number,
                        'bank': data.get('bank', {}).get('name', 'Unknown Bank').upper(),
                        'scheme': data.get('scheme', 'Unknown').upper(),
                        'type': data.get('type', 'Unknown').upper(),
                        'brand': data.get('brand', 'Unknown').upper(),
                        'country': country_code if country_code else final_country_name,
                        'flag': country_flag,
                        'api_used': api_config['type']
                    }

                elif api_config['type'] == 'freebinchecker':
                    country_code = data.get('country_code', '').upper()
                    country_name = data.get('country_name', 'Unknown').upper()

                    final_country_name, country_flag = get_country_info(country_code, country_name)

                    result = {
                        'bin': bin_number,
                        'bank': data.get('bank_name', 'Unknown Bank').upper(),
                        'scheme': data.get('card_scheme', 'Unknown').upper(),
                        'type': data.get('card_type', 'Unknown').upper(),
                        'brand': data.get('card_brand', 'Unknown').upper(),
                        'country': country_code if country_code else final_country_name,
                        'flag': country_flag,
                        'api_used': api_config['type']
                    }

                elif api_config['type'] == 'binlookup':
                    country_code = data.get('country_code', '').upper()
                    country_name = data.get('country', 'Unknown').upper()

                    final_country_name, country_flag = get_country_info(country_code, country_name)

                    result = {
                        'bin': bin_number,
                        'bank': data.get('bank', 'Unknown Bank').upper(),
                        'scheme': data.get('scheme', 'Unknown').upper(),
                        'type': data.get('type', 'Unknown').upper(),
                        'brand': data.get('brand', data.get('scheme', 'Unknown')).upper(),
                        'country': country_code if country_code else final_country_name,
                        'flag': country_flag,
                        'api_used': api_config['type']
                    }

                # Validate result has meaningful data
                if (result['bank'] != 'Unknown Bank' or
                    result['country'] != 'Unknown' or
                    result['scheme'] != 'Unknown'):

                    print(f"   ✅ API {api_config['type']} exitosa!")
                    return result

        except Exception as e:
            print(f"   ❌ API {api_config['type']} falló: {str(e)[:50]}...")
            continue

    return None

def get_bin_info_complete(bin_number):
    """
    Función principal para obtener información de BIN
    Primero intenta APIs externas, si devuelve Unknown Bank consulta CSV como respaldo
    """
    # Cargar base de datos CSV
    bins_db = load_bins_csv()
    
    # Primero intentar APIs externas
    api_result = get_bin_info_from_apis(bin_number)
    
    if api_result:
        # Si el API devolvió "Unknown Bank", consultar CSV como respaldo
        if api_result.get('bank', '').upper() == 'UNKNOWN BANK':
            print(f"   🔄 API devolvió Unknown Bank, consultando base de datos local...")
            csv_result = search_bin_in_csv(bin_number, bins_db)
            
            if csv_result and csv_result.get('bank', '').upper() != 'UNKNOWN BANK':
                print(f"   ✅ Información mejorada encontrada en CSV!")
                # Combinar resultados: usar datos del CSV pero mantener info del API si es mejor
                combined_result = api_result.copy()
                combined_result['bank'] = csv_result['bank']
                if csv_result.get('scheme') != 'Unknown':
                    combined_result['scheme'] = csv_result['scheme']
                if csv_result.get('type') != 'Unknown':
                    combined_result['type'] = csv_result['type']
                if csv_result.get('brand') != 'Unknown':
                    combined_result['brand'] = csv_result['brand']
                combined_result['api_used'] = f"{api_result['api_used']}_+_csv"
                return combined_result
            else:
                print(f"   ⚠️ CSV tampoco tiene información del banco, enviando con Unknown Bank")
                
        return api_result
    
    # Si las APIs fallan completamente, buscar en CSV
    print(f"   🔄 APIs fallaron, buscando en base de datos local...")
    csv_result = search_bin_in_csv(bin_number, bins_db)
    
    if csv_result:
        print(f"   ✅ BIN encontrado en base de datos local!")
        return csv_result
    
    # Si no se encuentra en ningún lado, devolver información por defecto
    print(f"   ⚠️ BIN {bin_number} no encontrado en ninguna fuente, enviando de todas formas")
    return {
        'bin': bin_number,
        'bank': 'Unknown Bank',
        'scheme': 'Unknown',
        'type': 'Unknown',
        'brand': 'Unknown',
        'country': 'Unknown',
        'flag': '🏳️',
        'api_used': 'none'
    }
