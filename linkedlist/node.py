class Node:
    """
    Node untuk menyimpan satu digit (0-9)
    dalam representasi BigInteger berbasis linked list.
    """

    def __init__(self, digit):
        if not isinstance(digit, int):
            raise TypeError("Digit harus berupa integer")

        if digit < 0 or digit > 9:
            raise ValueError("Digit harus antara 0-9")

        self.digit = digit
        self.next = None

    def __repr__(self):
        return f"Node({self.digit})"
