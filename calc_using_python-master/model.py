ERROR_MSG = 'ERROR'

# Create a Model to handle the calculator's operation


def evaluateExpression(expression):
    """Evaluate an expression."""
    try:
        result = str(eval(expression, {}, {}))
    except Exception:
        result = ERROR_MSG

    return result


def convert_bits_to_bytes(expression):
    try:
        bits = int(expression)
        bytes = bits / 8
        result = str(bytes)
    except ValueError:
        result = ERROR_MSG
    return result


def convert_bytes_to_bits(expression):
    try:
        bytes = int(expression)
        bits = bytes * 8
        result = str(bits)
    except ValueError:
        result = ERROR_MSG
    return result

def convert_bytes_to_KB(expression):
    try:
        bytes = int(expression)
        KB = bytes * 0.001
        result = str(KB)
    except ValueError:
        result = ERROR_MSG
    return result

def convert_KB_to_bytes(expression):
    try:
        KB = int(expression)
        bytes = KB * 1000
        result = str(bytes)
    except ValueError:
        result = ERROR_MSG
    return result

def convert_KB_to_MB(expression):
    try:
        KB = int(expression)
        MB = KB * 0.001
        result = str(MB)
    except ValueError:
        result = ERROR_MSG
    return result

def convert_MB_to_KB(expression):
    try:
        MB = int(expression)
        KB = MB * 1000
        result = str(KB)
    except ValueError:
        result = ERROR_MSG
    return result

