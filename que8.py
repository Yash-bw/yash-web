#program - Implement a function that uses a stack to evaluate a postfix expression.
# * input - "6 5 2 3 + 8 * + 3 + *"
# * output - the result of the expression

def postfix():
    stack = ("6 5 2 3 + 8 * + 3 + *")
    post_stack = stack.postfix()
    print(post_stack)
postfix()