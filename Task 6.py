class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def delete(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                return True
            current = current.next
        return False

    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def delete(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                return True
            current = current.next
        return False

    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

class Notepad:
    def __init__(self):
        self.documents = DoubleLinkedList()
        self.current_document = None
        self.undo_stack = Stack()

    def create_document(self):
        document_name = input("Enter document name: ")
        self.documents.insert(document_name)
        self.current_document = self.documents.head

    def open_document(self, document_name):
        current = self.documents.head
        while current:
            if current.data == document_name:
                self.current_document = current
                print(f"Opened document: {document_name}")
                return
            current = current.next
        print("Document not found.")

    def save_document(self):
        if self.current_document:
            print("Saving document...")
            # Implement saving logic here
            print("Document saved.")
        else:
            print("No document is currently open.")

    def edit_document(self, text):
        if self.current_document:
            print("Editing document...")
            self.undo_stack.push(self.current_document.data)
            self.current_document.data = text
            print("Document edited.")
        else:
            print("No document is currently open.")

    def undo(self):
        if not self.undo_stack.is_empty():
            previous_text = self.undo_stack.pop()
            self.current_document.data = previous_text
            print("Undo operation performed.")
        else:
            print("Nothing to undo.")

    def close_document(self):
        self.current_document = None
        print("Document closed.")

    def display_documents(self):
        print("Documents in Notepad:")
        self.documents.display()

# Sample usage of the Notepad application
notepad = Notepad()
notepad.create_document()
notepad.open_document("Document1")
notepad.edit_document("Sample text")
notepad.save_document()
notepad.undo()
notepad.close_document()
notepad.display_documents()
