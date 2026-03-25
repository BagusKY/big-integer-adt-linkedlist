from linkedlist.node import Node


class SinglyLinkedList:
    """
    Singly Linked List untuk menyimpan digit BigInteger
    (LSD di head, MSD di tail)
    """

    def __init__(self):
        self.head = None

    # ========================
    # Append (ke belakang)
    # ========================
    def append(self, digit):
        new_node = Node(digit)

        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    # ========================
    # Convert ke list Python
    # ========================
    def to_list(self):
        result = []
        current = self.head

        while current:
            result.append(current.digit)
            current = current.next

        return result

    # ========================
    # Length (opsional tapi berguna)
    # ========================
    def __len__(self):
        count = 0
        current = self.head

        while current:
            count += 1
            current = current.next

        return count

    # ========================
    # Debug view
    # ========================
    def __repr__(self):
        return " -> ".join(map(str, self.to_list())) + " -> None"