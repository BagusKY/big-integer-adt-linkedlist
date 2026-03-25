class Node:
    def __init__(self, digit):
        self.digit = digit
        self.next = None


class BigInteger:
    def __init__(self, value="0"):
        self.head = None

        # simpan digit dari LSD → MSD
        for d in reversed(value):
            self._append(int(d))

    def _append(self, digit):
        new_node = Node(digit)
        if not self.head:
            self.head = new_node
            return
        
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    # ========================
    # toString()
    # ========================
    def toString(self):
        digits = []
        curr = self.head
        while curr:
            digits.append(str(curr.digit))
            curr = curr.next
        return ''.join(reversed(digits))

    # ========================
    # comparable()
    # ========================
    def comparable(self, other):
        a = self._to_list_reversed()
        b = other._to_list_reversed()

        if len(a) < len(b):
            return -1
        if len(a) > len(b):
            return 1

        for i in range(len(a)):
            if a[i] < b[i]:
                return -1
            if a[i] > b[i]:
                return 1
        return 0

    def _to_list(self):
        res = []
        curr = self.head
        while curr:
            res.append(curr.digit)
            curr = curr.next
        return res

    def _to_list_reversed(self):
        return list(reversed(self._to_list()))

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
        p1 = self.head
        p2 = other.head
        carry = 0

        result = BigInteger("0")
        result.head = None

        while p1 or p2 or carry:
            d1 = p1.digit if p1 else 0
            d2 = p2.digit if p2 else 0

            total = d1 + d2 + carry
            carry = total // 10

            result._append(total % 10)

            if p1: p1 = p1.next
            if p2: p2 = p2.next

        return result

    # ===== SUB ===== (asumsi self >= other)
    def _sub(self, other):
        p1 = self.head
        p2 = other.head
        borrow = 0

        result = BigInteger("0")
        result.head = None

        while p1:
            d1 = p1.digit - borrow
            d2 = p2.digit if p2 else 0

            if d1 < d2:
                d1 += 10
                borrow = 1
            else:
                borrow = 0

            result._append(d1 - d2)

            p1 = p1.next
            if p2: p2 = p2.next

        return result

    # ===== MUL (basic) =====
    def _mul(self, other):
        a = self._to_list()
        b = other._to_list()

        result = [0] * (len(a) + len(b))

        for i in range(len(a)):
            carry = 0
            for j in range(len(b)):
                total = result[i+j] + a[i]*b[j] + carry
                result[i+j] = total % 10
                carry = total // 10

            if carry:
                result[i+len(b)] += carry

        res = BigInteger("0")
        res.head = None
        for d in result:
            res._append(d)

        return res

    # ========================
    # bitwise-ops()
    # (basic, via binary string)
    # ========================
    def bitwise(self, other, op):
        a = int(self.toString())
        b = int(other.toString())

        if op == '&':
            return BigInteger(str(a & b))
        elif op == '|':
            return BigInteger(str(a | b))
        elif op == '^':
            return BigInteger(str(a ^ b))
        else:
            raise ValueError("Bitwise tidak didukung")