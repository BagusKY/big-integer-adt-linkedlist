def validate_number_string(value):
    """
    Validasi bahwa input hanya berisi digit (0-9)
    """
    if not isinstance(value, str):
        raise TypeError("Input harus berupa string")

    if not value.isdigit():
        raise ValueError("Input hanya boleh berisi angka 0-9")

    return True


def strip_leading_zeros(digits):
    """
    Menghapus nol di bagian paling signifikan (MSD)
    digits dalam format LSD → MSD
    """
    if not digits:
        return [0]

    result = digits[:]

    while len(result) > 1 and result[-1] == 0:
        result.pop()

    return result


def string_to_digits(value):
    """
    Convert string angka → list digit (LSD di depan)
    """
    validate_number_string(value)
    return [int(d) for d in reversed(value)]


def digits_to_string(digits):
    """
    Convert list digit (LSD di depan) → string angka
    """
    digits = strip_leading_zeros(digits)
    return ''.join(map(str, reversed(digits)))
