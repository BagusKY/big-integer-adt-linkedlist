from bigint.bigint_linkedlist import BigInteger as BigIntegerLL
from bigint.bigint_list import BigIntegerList


def demo_linkedlist():
    print("=== BIGINTEGER (LINKED LIST) ===")

    a = BigIntegerLL("45839")
    b = BigIntegerLL("12345")

    print("A =", a.toString())
    print("B =", b.toString())

    # Comparable
    comp = a.comparable(b)
    print("Compare (A vs B):", comp)

    # Arithmetic
    print("\n-- Arithmetic --")
    print("A + B =", a.arithmetic(b, '+').toString())
    print("A - B =", a.arithmetic(b, '-').toString())
    print("A * B =", a.arithmetic(b, '*').toString())

    # Bitwise (jika sudah diimplementasikan)
    print("\n-- Bitwise --")
    try:
        print("A & B =", a.bitwise(b, '&').toString())
        print("A | B =", a.bitwise(b, '|').toString())
        print("A ^ B =", a.bitwise(b, '^').toString())
    except:
        print("Bitwise belum diimplementasikan sepenuhnya")


def demo_list():
    print("\n=== BIGINTEGER (PYTHON LIST) ===")

    x = BigIntegerList("45839")
    y = BigIntegerList("12345")

    print("X =", x.to_string())
    print("Y =", y.to_string())

    # Compare
    print("Compare (X vs Y):", x.compare(y))

    # Arithmetic
    print("\n-- Arithmetic --")
    print("X + Y =", x.add(y).to_string())

    # (Opsional, tergantung implementasi kamu)
    try:
        print("X - Y =", x.sub(y).to_string())
        print("X * Y =", x.mul(y).to_string())
    except:
        print("Operasi lanjutan belum lengkap")


def main():
    demo_linkedlist()
    demo_list()


if __name__ == "__main__":
    main()