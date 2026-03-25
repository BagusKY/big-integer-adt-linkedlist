from abc import ABC, abstractmethod


class BigIntegerBase(ABC):
    """
    Abstract Data Type (ADT) for BigInteger
    Semua implementasi WAJIB mengikuti method di bawah ini.
    """

    # ========================
    # Representasi
    # ========================
    @abstractmethod
    def toString(self):
        """Mengembalikan representasi string dari bilangan"""
        pass

    # ========================
    # Comparison
    # ========================
    @abstractmethod
    def comparable(self, other):
        """
        Return:
        -1 jika < other
         0 jika == other
         1 jika > other
        """
        pass

    # ========================
    # Arithmetic Operations
    # ========================
    @abstractmethod
    def arithmetic(self, other, op):
        """
        op:
        '+', '-', '*', '//', '%', '**'
        """
        pass

    # ========================
    # Bitwise Operations
    # ========================
    @abstractmethod
    def bitwise(self, other, op):
        """
        op:
        '&', '|', '^', '<<', '>>'
        """
        pass

    # ========================
    # Python Magic Methods (Optional but recommended)
    # ========================
    def __str__(self):
        return self.toString()

    def __eq__(self, other):
        return self.comparable(other) == 0

    def __lt__(self, other):
        return self.comparable(other) == -1

    def __gt__(self, other):
        return self.comparable(other) == 1