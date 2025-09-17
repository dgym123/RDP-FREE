
"""
Módulo para manejo de información de países y banderas
Contiene códigos ISO, nombres de países y sus respectivas banderas
"""

# Diccionario completo con códigos de países, nombres y banderas
COUNTRIES_DATA = {
    'AD': {'name': 'ANDORRA', 'flag': '🇦🇩'}, 'AE': {'name': 'UNITED ARAB EMIRATES', 'flag': '🇦🇪'},
    'AF': {'name': 'AFGHANISTAN', 'flag': '🇦🇫'}, 'AG': {'name': 'ANTIGUA AND BARBUDA', 'flag': '🇦🇬'},
    'AI': {'name': 'ANGUILLA', 'flag': '🇦🇮'}, 'AL': {'name': 'ALBANIA', 'flag': '🇦🇱'},
    'AM': {'name': 'ARMENIA', 'flag': '🇦🇲'}, 'AO': {'name': 'ANGOLA', 'flag': '🇦🇴'},
    'AQ': {'name': 'ANTARCTICA', 'flag': '🇦🇶'}, 'AR': {'name': 'ARGENTINA', 'flag': '🇦🇷'},
    'AS': {'name': 'AMERICAN SAMOA', 'flag': '🇦🇸'}, 'AT': {'name': 'AUSTRIA', 'flag': '🇦🇹'},
    'AU': {'name': 'AUSTRALIA', 'flag': '🇦🇺'}, 'AW': {'name': 'ARUBA', 'flag': '🇦🇼'},
    'AX': {'name': 'ALAND ISLANDS', 'flag': '🇦🇽'}, 'AZ': {'name': 'AZERBAIJAN', 'flag': '🇦🇿'},
    'BA': {'name': 'BOSNIA AND HERZEGOVINA', 'flag': '🇧🇦'}, 'BB': {'name': 'BARBADOS', 'flag': '🇧🇧'},
    'BD': {'name': 'BANGLADESH', 'flag': '🇧🇩'}, 'BE': {'name': 'BELGIUM', 'flag': '🇧🇪'},
    'BF': {'name': 'BURKINA FASO', 'flag': '🇧🇫'}, 'BG': {'name': 'BULGARIA', 'flag': '🇧🇬'},
    'BH': {'name': 'BAHRAIN', 'flag': '🇧🇭'}, 'BI': {'name': 'BURUNDI', 'flag': '🇧🇮'},
    'BJ': {'name': 'BENIN', 'flag': '🇧🇯'}, 'BL': {'name': 'SAINT BARTHELEMY', 'flag': '🇧🇱'},
    'BM': {'name': 'BERMUDA', 'flag': '🇧🇲'}, 'BN': {'name': 'BRUNEI', 'flag': '🇧🇳'},
    'BO': {'name': 'BOLIVIA', 'flag': '🇧🇴'}, 'BQ': {'name': 'BONAIRE', 'flag': '🇧🇶'},
    'BR': {'name': 'BRAZIL', 'flag': '🇧🇷'}, 'BS': {'name': 'BAHAMAS', 'flag': '🇧🇸'},
    'BT': {'name': 'BHUTAN', 'flag': '🇧🇹'}, 'BV': {'name': 'BOUVET ISLAND', 'flag': '🇧🇻'},
    'BW': {'name': 'BOTSWANA', 'flag': '🇧🇼'}, 'BY': {'name': 'BELARUS', 'flag': '🇧🇾'},
    'BZ': {'name': 'BELIZE', 'flag': '🇧🇿'}, 'CA': {'name': 'CANADA', 'flag': '🇨🇦'},
    'CC': {'name': 'COCOS ISLANDS', 'flag': '🇨🇨'}, 'CD': {'name': 'CONGO', 'flag': '🇨🇩'},
    'CF': {'name': 'CENTRAL AFRICAN REPUBLIC', 'flag': '🇨🇫'}, 'CG': {'name': 'CONGO', 'flag': '🇨🇬'},
    'CH': {'name': 'SWITZERLAND', 'flag': '🇨🇭'}, 'CI': {'name': 'IVORY COAST', 'flag': '🇨🇮'},
    'CK': {'name': 'COOK ISLANDS', 'flag': '🇨🇰'}, 'CL': {'name': 'CHILE', 'flag': '🇨🇱'},
    'CM': {'name': 'CAMEROON', 'flag': '🇨🇲'}, 'CN': {'name': 'CHINA', 'flag': '🇨🇳'},
    'CO': {'name': 'COLOMBIA', 'flag': '🇨🇴'}, 'CR': {'name': 'COSTA RICA', 'flag': '🇨🇷'},
    'CU': {'name': 'CUBA', 'flag': '🇨🇺'}, 'CV': {'name': 'CAPE VERDE', 'flag': '🇨🇻'},
    'CW': {'name': 'CURACAO', 'flag': '🇨🇼'}, 'CX': {'name': 'CHRISTMAS ISLAND', 'flag': '🇨🇽'},
    'CY': {'name': 'CYPRUS', 'flag': '🇨🇾'}, 'CZ': {'name': 'CZECH REPUBLIC', 'flag': '🇨🇿'},
    'DE': {'name': 'GERMANY', 'flag': '🇩🇪'}, 'DJ': {'name': 'DJIBOUTI', 'flag': '🇩🇯'},
    'DK': {'name': 'DENMARK', 'flag': '🇩🇰'}, 'DM': {'name': 'DOMINICA', 'flag': '🇩🇲'},
    'DO': {'name': 'DOMINICAN REPUBLIC', 'flag': '🇩🇴'}, 'DZ': {'name': 'ALGERIA', 'flag': '🇩🇿'},
    'EC': {'name': 'ECUADOR', 'flag': '🇪🇨'}, 'EE': {'name': 'ESTONIA', 'flag': '🇪🇪'},
    'EG': {'name': 'EGYPT', 'flag': '🇪🇬'}, 'EH': {'name': 'WESTERN SAHARA', 'flag': '🇪🇭'},
    'ER': {'name': 'ERITREA', 'flag': '🇪🇷'}, 'ES': {'name': 'SPAIN', 'flag': '🇪🇸'},
    'ET': {'name': 'ETHIOPIA', 'flag': '🇪🇹'}, 'FI': {'name': 'FINLAND', 'flag': '🇫🇮'},
    'FJ': {'name': 'FIJI', 'flag': '🇫🇯'}, 'FK': {'name': 'FALKLAND ISLANDS', 'flag': '🇫🇰'},
    'FM': {'name': 'MICRONESIA', 'flag': '🇫🇲'}, 'FO': {'name': 'FAROE ISLANDS', 'flag': '🇫🇴'},
    'FR': {'name': 'FRANCE', 'flag': '🇫🇷'}, 'GA': {'name': 'GABON', 'flag': '🇬🇦'},
    'GB': {'name': 'UNITED KINGDOM', 'flag': '🇬🇧'}, 'GD': {'name': 'GRENADA', 'flag': '🇬🇩'},
    'GE': {'name': 'GEORGIA', 'flag': '🇬🇪'}, 'GF': {'name': 'FRENCH GUIANA', 'flag': '🇬🇫'},
    'GG': {'name': 'GUERNSEY', 'flag': '🇬🇬'}, 'GH': {'name': 'GHANA', 'flag': '🇬🇭'},
    'GI': {'name': 'GIBRALTAR', 'flag': '🇬🇮'}, 'GL': {'name': 'GREENLAND', 'flag': '🇬🇱'},
    'GM': {'name': 'GAMBIA', 'flag': '🇬🇲'}, 'GN': {'name': 'GUINEA', 'flag': '🇬🇳'},
    'GP': {'name': 'GUADELOUPE', 'flag': '🇬🇵'}, 'GQ': {'name': 'EQUATORIAL GUINEA', 'flag': '🇬🇶'},
    'GR': {'name': 'GREECE', 'flag': '🇬🇷'}, 'GS': {'name': 'SOUTH GEORGIA', 'flag': '🇬🇸'},
    'GT': {'name': 'GUATEMALA', 'flag': '🇬🇹'}, 'GU': {'name': 'GUAM', 'flag': '🇬🇺'},
    'GW': {'name': 'GUINEA-BISSAU', 'flag': '🇬🇼'}, 'GY': {'name': 'GUYANA', 'flag': '🇬🇾'},
    'HK': {'name': 'HONG KONG', 'flag': '🇭🇰'}, 'HM': {'name': 'HEARD ISLAND', 'flag': '🇭🇲'},
    'HN': {'name': 'HONDURAS', 'flag': '🇭🇳'}, 'HR': {'name': 'CROATIA', 'flag': '🇭🇷'},
    'HT': {'name': 'HAITI', 'flag': '🇭🇹'}, 'HU': {'name': 'HUNGARY', 'flag': '🇭🇺'},
    'ID': {'name': 'INDONESIA', 'flag': '🇮🇩'}, 'IE': {'name': 'IRELAND', 'flag': '🇮🇪'},
    'IL': {'name': 'ISRAEL', 'flag': '🇮🇱'}, 'IM': {'name': 'ISLE OF MAN', 'flag': '🇮🇲'},
    'IN': {'name': 'INDIA', 'flag': '🇮🇳'}, 'IO': {'name': 'BRITISH INDIAN OCEAN', 'flag': '🇮🇴'},
    'IQ': {'name': 'IRAQ', 'flag': '🇮🇶'}, 'IR': {'name': 'IRAN', 'flag': '🇮🇷'},
    'IS': {'name': 'ICELAND', 'flag': '🇮🇸'}, 'IT': {'name': 'ITALY', 'flag': '🇮🇹'},
    'JE': {'name': 'JERSEY', 'flag': '🇯🇪'}, 'JM': {'name': 'JAMAICA', 'flag': '🇯🇲'},
    'JO': {'name': 'JORDAN', 'flag': '🇯🇴'}, 'JP': {'name': 'JAPAN', 'flag': '🇯🇵'},
    'KE': {'name': 'KENYA', 'flag': '🇰🇪'}, 'KG': {'name': 'KYRGYZSTAN', 'flag': '🇰🇬'},
    'KH': {'name': 'CAMBODIA', 'flag': '🇰🇭'}, 'KI': {'name': 'KIRIBATI', 'flag': '🇰🇮'},
    'KM': {'name': 'COMOROS', 'flag': '🇰🇲'}, 'KN': {'name': 'SAINT KITTS AND NEVIS', 'flag': '🇰🇳'},
    'KP': {'name': 'NORTH KOREA', 'flag': '🇰🇵'}, 'KR': {'name': 'SOUTH KOREA', 'flag': '🇰🇷'},
    'KW': {'name': 'KUWAIT', 'flag': '🇰🇼'}, 'KY': {'name': 'CAYMAN ISLANDS', 'flag': '🇰🇾'},
    'KZ': {'name': 'KAZAKHSTAN', 'flag': '🇰🇿'}, 'LA': {'name': 'LAOS', 'flag': '🇱🇦'},
    'LB': {'name': 'LEBANON', 'flag': '🇱🇧'}, 'LC': {'name': 'SAINT LUCIA', 'flag': '🇱🇨'},
    'LI': {'name': 'LIECHTENSTEIN', 'flag': '🇱🇮'}, 'LK': {'name': 'SRI LANKA', 'flag': '🇱🇰'},
    'LR': {'name': 'LIBERIA', 'flag': '🇱🇷'}, 'LS': {'name': 'LESOTHO', 'flag': '🇱🇸'},
    'LT': {'name': 'LITHUANIA', 'flag': '🇱🇹'}, 'LU': {'name': 'LUXEMBOURG', 'flag': '🇱🇺'},
    'LV': {'name': 'LATVIA', 'flag': '🇱🇻'}, 'LY': {'name': 'LIBYA', 'flag': '🇱🇾'},
    'MA': {'name': 'MOROCCO', 'flag': '🇲🇦'}, 'MC': {'name': 'MONACO', 'flag': '🇲🇨'},
    'MD': {'name': 'MOLDOVA', 'flag': '🇲🇩'}, 'ME': {'name': 'MONTENEGRO', 'flag': '🇲🇪'},
    'MF': {'name': 'SAINT MARTIN', 'flag': '🇲🇫'}, 'MG': {'name': 'MADAGASCAR', 'flag': '🇲🇬'},
    'MH': {'name': 'MARSHALL ISLANDS', 'flag': '🇲🇭'}, 'MK': {'name': 'NORTH MACEDONIA', 'flag': '🇲🇰'},
    'ML': {'name': 'MALI', 'flag': '🇲🇱'}, 'MM': {'name': 'MYANMAR', 'flag': '🇲🇲'},
    'MN': {'name': 'MONGOLIA', 'flag': '🇲🇳'}, 'MO': {'name': 'MACAO', 'flag': '🇲🇴'},
    'MP': {'name': 'NORTHERN MARIANA ISLANDS', 'flag': '🇲🇵'}, 'MQ': {'name': 'MARTINIQUE', 'flag': '🇲🇶'},
    'MR': {'name': 'MAURITANIA', 'flag': '🇲🇷'}, 'MS': {'name': 'MONTSERRAT', 'flag': '🇲🇸'},
    'MT': {'name': 'MALTA', 'flag': '🇲🇹'}, 'MU': {'name': 'MAURITIUS', 'flag': '🇲🇺'},
    'MV': {'name': 'MALDIVES', 'flag': '🇲🇻'}, 'MW': {'name': 'MALAWI', 'flag': '🇲🇼'},
    'MX': {'name': 'MEXICO', 'flag': '🇲🇽'}, 'MY': {'name': 'MALAYSIA', 'flag': '🇲🇾'},
    'MZ': {'name': 'MOZAMBIQUE', 'flag': '🇲🇿'}, 'NA': {'name': 'NAMIBIA', 'flag': '🇳🇦'},
    'NC': {'name': 'NEW CALEDONIA', 'flag': '🇳🇨'}, 'NE': {'name': 'NIGER', 'flag': '🇳🇪'},
    'NF': {'name': 'NORFOLK ISLAND', 'flag': '🇳🇫'}, 'NG': {'name': 'NIGERIA', 'flag': '🇳🇬'},
    'NI': {'name': 'NICARAGUA', 'flag': '🇳🇮'}, 'NL': {'name': 'NETHERLANDS', 'flag': '🇳🇱'},
    'NO': {'name': 'NORWAY', 'flag': '🇳🇴'}, 'NP': {'name': 'NEPAL', 'flag': '🇳🇵'},
    'NR': {'name': 'NAURU', 'flag': '🇳🇷'}, 'NU': {'name': 'NIUE', 'flag': '🇳🇺'},
    'NZ': {'name': 'NEW ZEALAND', 'flag': '🇳🇿'}, 'OM': {'name': 'OMAN', 'flag': '🇴🇲'},
    'PA': {'name': 'PANAMA', 'flag': '🇵🇦'}, 'PE': {'name': 'PERU', 'flag': '🇵🇪'},
    'PF': {'name': 'FRENCH POLYNESIA', 'flag': '🇵🇫'}, 'PG': {'name': 'PAPUA NEW GUINEA', 'flag': '🇵🇬'},
    'PH': {'name': 'PHILIPPINES', 'flag': '🇵🇭'}, 'PK': {'name': 'PAKISTAN', 'flag': '🇵🇰'},
    'PL': {'name': 'POLAND', 'flag': '🇵🇱'}, 'PM': {'name': 'SAINT PIERRE AND MIQUELON', 'flag': '🇵🇲'},
    'PN': {'name': 'PITCAIRN', 'flag': '🇵🇳'}, 'PR': {'name': 'PUERTO RICO', 'flag': '🇵🇷'},
    'PS': {'name': 'PALESTINE', 'flag': '🇵🇸'}, 'PT': {'name': 'PORTUGAL', 'flag': '🇵🇹'},
    'PW': {'name': 'PALAU', 'flag': '🇵🇼'}, 'PY': {'name': 'PARAGUAY', 'flag': '🇵🇾'},
    'QA': {'name': 'QATAR', 'flag': '🇶🇦'}, 'RE': {'name': 'REUNION', 'flag': '🇷🇪'},
    'RO': {'name': 'ROMANIA', 'flag': '🇷🇴'}, 'RS': {'name': 'SERBIA', 'flag': '🇷🇸'},
    'RU': {'name': 'RUSSIA', 'flag': '🇷🇺'}, 'RW': {'name': 'RWANDA', 'flag': '🇷🇼'},
    'SA': {'name': 'SAUDI ARABIA', 'flag': '🇸🇦'}, 'SB': {'name': 'SOLOMON ISLANDS', 'flag': '🇸🇧'},
    'SC': {'name': 'SEYCHELLES', 'flag': '🇸🇨'}, 'SD': {'name': 'SUDAN', 'flag': '🇸🇩'},
    'SE': {'name': 'SWEDEN', 'flag': '🇸🇪'}, 'SG': {'name': 'SINGAPORE', 'flag': '🇸🇬'},
    'SH': {'name': 'SAINT HELENA', 'flag': '🇸🇭'}, 'SI': {'name': 'SLOVENIA', 'flag': '🇸🇮'},
    'SJ': {'name': 'SVALBARD AND JAN MAYEN', 'flag': '🇸🇯'}, 'SK': {'name': 'SLOVAKIA', 'flag': '🇸🇰'},
    'SL': {'name': 'SIERRA LEONE', 'flag': '🇸🇱'}, 'SM': {'name': 'SAN MARINO', 'flag': '🇸🇲'},
    'SN': {'name': 'SENEGAL', 'flag': '🇸🇳'}, 'SO': {'name': 'SOMALIA', 'flag': '🇸🇴'},
    'SR': {'name': 'SURINAME', 'flag': '🇸🇷'}, 'SS': {'name': 'SOUTH SUDAN', 'flag': '🇸🇸'},
    'ST': {'name': 'SAO TOME AND PRINCIPE', 'flag': '🇸🇹'}, 'SV': {'name': 'EL SALVADOR', 'flag': '🇸🇻'},
    'SX': {'name': 'SINT MAARTEN', 'flag': '🇸🇽'}, 'SY': {'name': 'SYRIA', 'flag': '🇸🇾'},
    'SZ': {'name': 'ESWATINI', 'flag': '🇸🇿'}, 'TC': {'name': 'TURKS AND CAICOS ISLANDS', 'flag': '🇹🇨'},
    'TD': {'name': 'CHAD', 'flag': '🇹🇩'}, 'TF': {'name': 'FRENCH SOUTHERN TERRITORIES', 'flag': '🇹🇫'},
    'TG': {'name': 'TOGO', 'flag': '🇹🇬'}, 'TH': {'name': 'THAILAND', 'flag': '🇹🇭'},
    'TJ': {'name': 'TAJIKISTAN', 'flag': '🇹🇯'}, 'TK': {'name': 'TOKELAU', 'flag': '🇹🇰'},
    'TL': {'name': 'TIMOR-LESTE', 'flag': '🇹🇱'}, 'TM': {'name': 'TURKMENISTAN', 'flag': '🇹🇲'},
    'TN': {'name': 'TUNISIA', 'flag': '🇹🇳'}, 'TO': {'name': 'TONGA', 'flag': '🇹🇴'},
    'TR': {'name': 'TURKEY', 'flag': '🇹🇷'}, 'TT': {'name': 'TRINIDAD AND TOBAGO', 'flag': '🇹🇹'},
    'TV': {'name': 'TUVALU', 'flag': '🇹🇻'}, 'TW': {'name': 'TAIWAN', 'flag': '🇹🇼'},
    'TZ': {'name': 'TANZANIA', 'flag': '🇹🇿'}, 'UA': {'name': 'UKRAINE', 'flag': '🇺🇦'},
    'UG': {'name': 'UGANDA', 'flag': '🇺🇬'}, 'UM': {'name': 'UNITED STATES MINOR OUTLYING ISLANDS', 'flag': '🇺🇲'},
    'US': {'name': 'UNITED STATES', 'flag': '🇺🇸'}, 'UY': {'name': 'URUGUAY', 'flag': '🇺🇾'},
    'UZ': {'name': 'UZBEKISTAN', 'flag': '🇺🇿'}, 'VA': {'name': 'VATICAN', 'flag': '🇻🇦'},
    'VC': {'name': 'SAINT VINCENT AND THE GRENADINES', 'flag': '🇻🇨'}, 'VE': {'name': 'VENEZUELA', 'flag': '🇻🇪'},
    'VG': {'name': 'BRITISH VIRGIN ISLANDS', 'flag': '🇻🇬'}, 'VI': {'name': 'US VIRGIN ISLANDS', 'flag': '🇻🇮'},
    'VN': {'name': 'VIETNAM', 'flag': '🇻🇳'}, 'VU': {'name': 'VANUATU', 'flag': '🇻🇺'},
    'WF': {'name': 'WALLIS AND FUTUNA', 'flag': '🇼🇫'}, 'WS': {'name': 'SAMOA', 'flag': '🇼🇸'},
    'YE': {'name': 'YEMEN', 'flag': '🇾🇪'}, 'YT': {'name': 'MAYOTTE', 'flag': '🇾🇹'},
    'ZA': {'name': 'SOUTH AFRICA', 'flag': '🇿🇦'}, 'ZM': {'name': 'ZAMBIA', 'flag': '🇿🇲'},
    'ZW': {'name': 'ZIMBABWE', 'flag': '🇿🇼'},
    # Aliases comunes
    'UK': {'name': 'UNITED KINGDOM', 'flag': '🇬🇧'}, 'EN': {'name': 'UNITED KINGDOM', 'flag': '🇬🇧'}
}

# Mapeos adicionales para casos problemáticos
SPECIAL_MAPPINGS = {
    'UNITED STATES': 'US',
    'UNITED STATES OF AMERICA': 'US',
    'USA': 'US',
    'AMERICA': 'US'
}

# Mapeo de nombres comunes de países a códigos ISO
NAME_TO_CODE = {
    'UNITED STATES': 'US',
    'UNITED STATES OF AMERICA': 'US',
    'UNITED STATES OF AMERICA (THE)': 'US',
    'USA': 'US',
    'AMERICA': 'US',
    'ESTADOS UNIDOS': 'US',

    'MEXICO': 'MX',
    'MÉXICO': 'MX',
    'MEXIKO': 'MX',

    'CANADA': 'CA',
    'CANADÁ': 'CA',

    'UNITED KINGDOM': 'GB',
    'REINO UNIDO': 'GB',
    'GREAT BRITAIN': 'GB',
    'ENGLAND': 'GB',
    'UK': 'GB',

    'GERMANY': 'DE',
    'DEUTSCHLAND': 'DE',
    'ALEMANIA': 'DE',

    'FRANCE': 'FR',
    'FRANCIA': 'FR',

    'SPAIN': 'ES',
    'ESPAÑA': 'ES',

    'ITALY': 'IT',
    'ITALIA': 'IT',

    'BRAZIL': 'BR',
    'BRASIL': 'BR',

    'ARGENTINA': 'AR',

    'COLOMBIA': 'CO',

    'VENEZUELA': 'VE',

    'PERU': 'PE',
    'PERÚ': 'PE',

    'CHILE': 'CL',

    'ECUADOR': 'EC',

    'INDIA': 'IN',

    'CHINA': 'CN',

    'JAPAN': 'JP',
    'JAPÓN': 'JP',

    'SOUTH KOREA': 'KR',
    'KOREA': 'KR',
    'COREA': 'KR',

    'AUSTRALIA': 'AU',

    'RUSSIA': 'RU',
    'RUSIA': 'RU',

    'NETHERLANDS': 'NL',
    'PAÍSES BAJOS': 'NL',

    'SWEDEN': 'SE',
    'SUECIA': 'SE',

    'NORWAY': 'NO',
    'NORUEGA': 'NO',

    'DENMARK': 'DK',
    'DINAMARCA': 'DK',

    'FINLAND': 'FI',
    'FINLANDIA': 'FI',

    'PORTUGAL': 'PT',

    'GREECE': 'GR',
    'GRECIA': 'GR',

    'TURKEY': 'TR',
    'TURQUÍA': 'TR'
}

def get_country_code_from_name(country_name):
    """Convert country name to country code"""
    country_name = country_name.upper().strip()
    return NAME_TO_CODE.get(country_name, '')

def get_country_info(country_code, country_name):
    """Get country name and flag from code or name"""
    if not country_code:
        country_code = ''

    country_upper = country_code.upper()

    # Si tenemos código de país válido, usarlo SIEMPRE del diccionario local
    if country_upper and country_upper in COUNTRIES_DATA:
        return country_upper, COUNTRIES_DATA[country_upper]['flag']

    # Si no hay código pero tenemos nombre, intentar encontrar el país
    if country_name and country_name.upper() != 'UNKNOWN':
        # Limpiar el nombre del país
        clean_name = country_name.upper().strip()

        # Primero verificar mapeos especiales
        if clean_name in SPECIAL_MAPPINGS:
            mapped_code = SPECIAL_MAPPINGS[clean_name]
            if mapped_code in COUNTRIES_DATA:
                return mapped_code, COUNTRIES_DATA[mapped_code]['flag']

        # Reemplazar nombres comunes problemáticos
        name_replacements = {
            'UNITED STATES OF AMERICA (THE)': 'US',
            'UNITED STATES OF AMERICA': 'US',
            'THE UNITED STATES': 'US'
        }

        if clean_name in name_replacements:
            mapped_code = name_replacements[clean_name]
            if mapped_code in COUNTRIES_DATA:
                return mapped_code, COUNTRIES_DATA[mapped_code]['flag']

        # Buscar por código directo en nuestro diccionario
        if clean_name in COUNTRIES_DATA:
            return clean_name, COUNTRIES_DATA[clean_name]['flag']

        # Buscar por nombre en nuestro diccionario
        for code, data in COUNTRIES_DATA.items():
            if data['name'] == clean_name:
                return code, data['flag']

        # Si no encontramos coincidencia exacta, devolver el nombre tal como viene
        return clean_name, '🏳️'

    # Fallback por defecto
    return 'UNKNOWN', '🏳️'
