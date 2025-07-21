import art
def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : sub,
    "*" : multiply,
    "/" : divide,
}
def calculator():
    print(art.logo)
    again = True
    n1 = float(input("What's the first number?:"))

    while again:
        for symbol in operations:
            print(symbol)
        operation = input("Pick an Operation:")
        n2 = float(input("What's the next number: "))
        answer = operations[operation](n1, n2)
        print(f"{n1} {operation} {n2} = {operations[operation](n1,n2)}")


        go_again = input(f"Type 'y' to continue calculating with {answer} or type 'n' to start new calculation:\n ")
        if go_again == "y":
            n1 = answer
        else:
            again = False
            print("\n" * 100)
            calculator()

calculator()