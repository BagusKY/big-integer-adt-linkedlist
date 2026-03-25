from .bigint_base import BigIntegerBase


class BigIntegerList(BigIntegerBase):
    def __init__(self, value="0"):
        # simpan digit (LSD di depan)
        self.digits = [int(d) for d in reversed(value)]

    # ========================
    # toString()
    # ========================
    def toString(self):
        return ''.join(map(str, reversed(self.digits)))

    # ========================
    # comparable()
    # ========================
    def comparable(self, other):
        a = self._normalized()
        b = other._normalized()

        if len(a) < len(b):
            return -1
        if len(a) > len(b):
            return 1

        for i in range(len(a)-1, -1, -1):
            if a[i] < b[i]:
                return -1
            if a[i] > b[i]:
                return 1
        return 0

    def _normalized(self):
        # hapus leading zero
        res = self.digits[:]
        while len(res) > 1 and res[-1] == 0:
            res.pop()
        return res

    # ========================
    # arithmetic()
    # ========================
    def arithmetic(self, other, op):
        if op == '+':
            return self._add(other)
        elif op == '-':
            return self._sub(other)
        elif op == '*':
            return self._mul(other)
        else:
            raise ValueError("Operator tidak didukung")

    # ===== ADD =====
    def _add(self, other):
        result = []
        carry = 0

        max_len = max(len(self.digits), len(other.digits))

        for i in range(max_len):
            d1 = self.digits[i] if i < len(self.digits) else 0
            d2 = other.digits[i] if i < len(other.digits) else 0

            total = d1 + d2 + carry
            carry = total // 10

            result.append(total % 10)

        if carry:
            result.append(carry)

        return self._from_digits(result)

    # ===== SUB ===== (asumsi self >= other)
    def _sub(self, other):
        result = []
        borrow = 0

        for i in range(len(self.digits)):
            d1 = self.digits[i] - borrow
            d2 = other.digits[i] if i < len(other.digits) else 0

            if d1 < d2:
                d1 += 10
                borrow = 1
            else:
                borrow = 0

            result.append(d1 - d2)

        return self._from_digits(result)

    # ===== MUL =====
    def _mul(self, other):
        result = [0] * (len(self.digits) + len(other.digits))

        for i in range(len(self.digits)):
            carry = 0
            for j in range(len(other.digits)):
                total = (
                    result[i + j]
                    + self.digits[i] * other.digits[j]
                    + carry
                )
                result[i + j] = total % 10
                carry = total // 10

            if carry:
                result[i + len(other.digits)] += carry

        return self._from_digits(result)

    # ========================
    # bitwise() (basic version)
    # ========================
    def bitwise(self, other, op):
        # sementara masih pakai int (nanti bisa kita upgrade)
        a = int(self.toString())
        b = int(other.toString())

        if op == '&':
            return BigIntegerList(str(a & b))
        elif op == '|':
            return BigIntegerList(str(a | b))
        elif op == '^':
            return BigIntegerList(str(a ^ b))
        else:
            raise ValueError("Bitwise tidak didukung")

    # ========================
    # Helper
    # ========================
    def _from_digits(self, digits):
        obj = BigIntegerList("0")
        obj.digits = digits
        return obj