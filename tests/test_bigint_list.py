import unittest
from bigint.bigint_list import BigIntegerList


class TestBigIntegerList(unittest.TestCase):

    # ========================
    # toString
    # ========================
    def test_to_string(self):
        num = BigIntegerList("12345")
        self.assertEqual(num.toString(), "12345")

    def test_to_string_zero(self):
        num = BigIntegerList("0")
        self.assertEqual(num.toString(), "0")

    # ========================
    # comparable
    # ========================
    def test_compare_equal(self):
        a = BigIntegerList("123")
        b = BigIntegerList("123")
        self.assertEqual(a.comparable(b), 0)

    def test_compare_less(self):
        a = BigIntegerList("123")
        b = BigIntegerList("456")
        self.assertEqual(a.comparable(b), -1)

    def test_compare_greater(self):
        a = BigIntegerList("999")
        b = BigIntegerList("1")
        self.assertEqual(a.comparable(b), 1)

    # ========================
    # ADD
    # ========================
    def test_add_simple(self):
        a = BigIntegerList("123")
        b = BigIntegerList("456")
        result = a.arithmetic(b, '+')
        self.assertEqual(result.toString(), "579")

    def test_add_carry(self):
        a = BigIntegerList("999")
        b = BigIntegerList("1")
        result = a.arithmetic(b, '+')
        self.assertEqual(result.toString(), "1000")

    # ========================
    # SUB
    # ========================
    def test_sub_simple(self):
        a = BigIntegerList("500")
        b = BigIntegerList("200")
        result = a.arithmetic(b, '-')
        self.assertEqual(result.toString(), "300")

    def test_sub_borrow(self):
        a = BigIntegerList("1000")
        b = BigIntegerList("1")
        result = a.arithmetic(b, '-')
        self.assertEqual(result.toString(), "999")

    # ========================
    # MUL
    # ========================
    def test_mul_simple(self):
        a = BigIntegerList("12")
        b = BigIntegerList("3")
        result = a.arithmetic(b, '*')
        self.assertEqual(result.toString(), "36")

    def test_mul_large(self):
        a = BigIntegerList("123")
        b = BigIntegerList("456")
        result = a.arithmetic(b, '*')
        self.assertEqual(result.toString(), "56088")

    # ========================
    # EDGE CASE
    # ========================
    def test_add_zero(self):
        a = BigIntegerList("0")
        b = BigIntegerList("0")
        result = a.arithmetic(b, '+')
        self.assertEqual(result.toString(), "0")

    def test_mul_zero(self):
        a = BigIntegerList("999")
        b = BigIntegerList("0")
        result = a.arithmetic(b, '*')
        self.assertEqual(result.toString(), "0")

    # ========================
    # BITWISE
    # ========================
    def test_bitwise_and(self):
        a = BigIntegerList("6")
        b = BigIntegerList("3")
        result = a.bitwise(b, '&')
        self.assertEqual(result.toString(), "2")

    def test_bitwise_or(self):
        a = BigIntegerList("6")
        b = BigIntegerList("3")
        result = a.bitwise(b, '|')
        self.assertEqual(result.toString(), "7")


if __name__ == "__main__":
    unittest.main()