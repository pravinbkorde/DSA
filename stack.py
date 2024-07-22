
# print("****** Implementation of the stack using the List ******")
# stack  = []
# stack.append("a")
# stack.append("b")
# stack.append("c")
# print("Initial Stack--------")
# print(stack)
#
# print("\nElements are pop from the stack----")
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
#
# print("\nStack after ekements are pop----")
# print(stack)

def balance(my_string):
    stack =[]
    open_bracket = ["(","{","["]
    close_bracket =[")","}","]"]

    for i in my_string:
        if i in open_bracket:
            stack.append(i)
        else:
            top = i.pop()
            if i :
                pass

