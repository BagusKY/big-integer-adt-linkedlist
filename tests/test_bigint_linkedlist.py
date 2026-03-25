import unittest
from bigint.bigint_linkedlist import BigInteger


class TestBigIntegerLinkedList(unittest.TestCase):

    # ========================
    # toString
    # ========================
    def test_to_string(self):
        num = BigInteger("12345")
        self.assertEqual(num.toString(), "12345")

    def test_to_string_zero(self):
        num = BigInteger("0")
        self.assertEqual(num.toString(), "0")

    # ========================
    # comparable
    # ========================
    def test_compare_equal(self):
        a = BigInteger("123")
        b = BigInteger("123")
        self.assertEqual(a.comparable(b), 0)

    def test_compare_less(self):
        a = BigInteger("123")
        b = BigInteger("456")
        self.assertEqual(a.comparable(b), -1)

    def test_compare_greater(self):
        a = BigInteger("999")
        b = BigInteger("1")
        self.assertEqual(a.comparable(b), 1)

    # ========================
    # ADD
    # ========================
    def test_add_simple(self):
        a = BigInteger("123")
        b = BigInteger("456")
        result = a.arithmetic(b, '+')
        self.assertEqual(result.toString(), "579")

    def test_add_carry(self):
        a = BigInteger("999")
        b = BigInteger("1")
        result = a.arithmetic(b, '+')
        self.assertEqual(result.toString(), "1000")

    # ========================
    # SUB
    # ========================
    def test_sub_simple(self):
        a = BigInteger("500")
        b = BigInteger("200")
        result = a.arithmetic(b, '-')
        self.assertEqual(result.toString(), "300")

    def test_sub_borrow(self):
        a = BigInteger("1000")
        b = BigInteger("1")
        result = a.arithmetic(b, '-')
        self.assertEqual(result.toString(), "999")

    # ========================
    # MUL
    # ========================
    def test_mul_simple(self):
        a = BigInteger("12")
        b = BigInteger("3")
        result = a.arithmetic(b, '*')
        self.assertEqual(result.toString(), "36")

    def test_mul_large(self):
        a = BigInteger("123")
        b = BigInteger("456")
        result = a.arithmetic(b, '*')
        self.assertEqual(result.toString(), "56088")

    # ========================
    # EDGE CASE
    # ========================
    def test_add_zero(self):
        a = BigInteger("0")
        b = BigInteger("0")
        result = a.arithmetic(b, '+')
        self.assertEqual(result.toString(), "0")

    def test_mul_zero(self):
        a = BigInteger("999")
        b = BigInteger("0")
        result = a.arithmetic(b, '*')
        self.assertEqual(result.toString(), "0")

    # ========================
    # BITWISE (basic)
    # ========================
    def test_bitwise_and(self):
        a = BigInteger("6")   # 110
        b = BigInteger("3")   # 011
        result = a.bitwise(b, '&')
        self.assertEqual(result.toString(), "2")

    def test_bitwise_or(self):
        a = BigInteger("6")
        b = BigInteger("3")
        result = a.bitwise(b, '|')
        self.assertEqual(result.toString(), "7")


if __name__ == "__main__":
    unittest.main()
