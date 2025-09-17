"""
Módulo para validación de tarjetas de crédito usando el algoritmo Luhn
"""

import re


def luhn_check_strict(card_number):
    """Strict Luhn algorithm validation with enhanced checking"""
    # Remove any non-digit characters
    card_number = re.sub(r'\D', '', str(card_number))

    # Check length (must be between 13-19 digits)
    if len(card_number) < 13 or len(card_number) > 19:
        return False

    # Check if all digits are the same (invalid cards)
    if len(set(card_number)) <= 2:
        return False

    # Check for obvious test/fake patterns
    test_patterns = [
        '0000000000000000', '1111111111111111', '2222222222222222',
        '3333333333333333', '4444444444444444', '5555555555555555',
        '6666666666666666', '7777777777777777', '8888888888888888',
        '9999999999999999', '1234567890123456', '0123456789012345'
    ]

    for pattern in test_patterns:
        if pattern in card_number:
            return False

    # Standard Luhn algorithm
    def digits_of(n):
        return [int(d) for d in str(n)]

    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = sum(odd_digits)

    for d in even_digits:
        checksum += sum(digits_of(d * 2))

    return checksum % 10 == 0


def luhn_check_basic(card_number):
    """Basic Luhn algorithm validation (only algorithm, no additional checks)"""
    # Remove any non-digit characters
    card_number = re.sub(r'\D', '', str(card_number))
    
    # Check minimum length
    if len(card_number) < 13:
        return False
    
    # Standard Luhn algorithm
    def digits_of(n):
        return [int(d) for d in str(n)]

    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = sum(odd_digits)

    for d in even_digits:
        checksum += sum(digits_of(d * 2))

    return checksum % 10 == 0