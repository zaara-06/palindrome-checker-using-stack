# Palindrome Checker Using Stack

class Stack:
    def __init__(self):
        self.items = []

    # Push element
    def push(self, item):
        self.items.append(item)

    # Pop element
    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    # Check empty
    def is_empty(self):
        return len(self.items) == 0

    # Stack size
    def size(self):
        return len(self.items)


# Clean input
def clean_string(text):
    cleaned = ""
    for char in text:
        if char.isalnum():
            cleaned += char.lower()
    return cleaned


# Reverse using stack
def reverse_using_stack(text):
    stack = Stack()

    for char in text:
        stack.push(char)

    reverse = ""

    while not stack.is_empty():
        reverse += stack.pop()

    return reverse


# Check palindrome
def check_palindrome():
    print("\n-------- Palindrome Checker --------")

    text = input("Enter a word or sentence: ")

    if text.strip() == "":
        print("Please enter a valid string.")
        return

    cleaned = clean_string(text)

    if cleaned == "":
        print("No valid characters found.")
        return

    reverse = reverse_using_stack(cleaned)

    print("\nOriginal string :", text)
    print("Processed string:", cleaned)
    print("Reversed string :", reverse)
    print("Number of characters:", len(cleaned))

    if cleaned == reverse:
        print("Result: Palindrome")
    else:
        print("Result: Not a palindrome")


# Check number palindrome
def check_number():
    print("\n-------- Number Palindrome --------")

    number = input("Enter a number: ")

    if not number.isdigit():
        print("Please enter a valid number.")
        return

    reverse = reverse_using_stack(number)

    print("\nOriginal number:", number)
    print("Reversed number:", reverse)

    if number == reverse:
        print("Result: Palindrome number")
    else:
        print("Result: Not a palindrome number")


# Display palindrome process
def show_process():
    print("\n-------- Stack Process --------")

    text = input("Enter a word: ")

    if text.strip() == "":
        print("Please enter a valid word.")
        return

    cleaned = clean_string(text)

    if cleaned == "":
        print("Invalid input.")
        return

    stack = Stack()

    print("\nPushing characters into stack:")

    for char in cleaned:
        stack.push(char)
        print("Push:", char)

    print("\nStack size:", stack.size())

    reverse = ""

    print("\nPopping characters from stack:")

    while not stack.is_empty():
        char = stack.pop()
        reverse += char
        print("Pop:", char)

    print("\nOriginal:", cleaned)
    print("Reverse :", reverse)

    if cleaned == reverse:
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")


# Multiple checks
def multiple_checks():
    print("\n-------- Multiple String Check --------")

    count = input("Enter number of strings: ")

    if not count.isdigit() or int(count) <= 0:
        print("Enter a valid number.")
        return

    count = int(count)

    palindrome = 0
    not_palindrome = 0

    for i in range(1, count + 1):
        print("\nString", i)

        text = input("Enter string: ")

        cleaned = clean_string(text)

        if cleaned == "":
            print("Invalid input.")
            continue

        reverse = reverse_using_stack(cleaned)

        print("Original:", cleaned)
        print("Reverse :", reverse)

        if cleaned == reverse:
            print("Palindrome")
            palindrome += 1
        else:
            print("Not a palindrome")
            not_palindrome += 1

    print("\n-------- Summary --------")
    print("Palindromes :", palindrome)
    print("Not palindromes:", not_palindrome)


# Project information
def project_information():
    print("\n-------- Project Information --------")
    print("Project: Palindrome Checker Using Stack")
    print("Data Structure: Stack")
    print("Principle: LIFO")
    print("Programming Language: Python")
    print("Purpose: Checking palindromes using Stack")


# Main menu
def main():
    while True:
        print("\n" + "-" * 55)
        print(" PALINDROME CHECKER USING STACK")
        print("-" * 55)

        print("1. Check Palindrome")
        print("2. Check Number Palindrome")
        print("3. Show Stack Process")
        print("4. Check Multiple Strings")
        print("5. Project Information")
        print("6. Exit")

        print("-" * 55)

        choice = input("Enter your choice: ")

        if choice == "1":
            check_palindrome()

        elif choice == "2":
            check_number()

        elif choice == "3":
            show_process()

        elif choice == "4":
            multiple_checks()

        elif choice == "5":
            project_information()

        elif choice == "6":
            print("\nProgram terminated. Thank you!")
            break

        else:
            print("Invalid choice. Please try again.")


main()
