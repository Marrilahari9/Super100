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

# Now, let's implement the Notepad application using the LinkedList and DoubleLinkedList classes.

class Notepad:
    def __init__(self):
        self.documents = DoubleLinkedList()
        self.current_document = None

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

    def edit_document(self):
        if self.current_document:
            print("Editing document...")
            # Implement editing logic here
        else:
            print("No document is currently open.")

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
notepad.save_document()
notepad.edit_document()
notepad.close_document()
notepad.display_documents()
