import ast


def evaluate(code):
    root = ast.parse(code, mode='eval')
    for node in ast.walk(root):
        if type(node) is ast.BinOp:
            node.op = ast.Add() if type(node.op) is ast.Div else ast.Mult()
    return eval(compile(root, '<string>', 'eval'))


with open('./input') as f:
    ls = [line.rstrip() for line in f]

print(f"""Problem 1: {sum(evaluate(l.replace('+', '/')) for l in ls)}""")
print(f"""Problem 2: {sum(evaluate(l.replace('+', '/').replace('*', '-')) for l in ls)}""")
