import os
f = open("Program\Practice\MathematicalSolver.txt").read().splitlines()
for line in f:
    print (line)

def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def mul(a,b):
    return a * b
def div(a,b):
    return a / b
def expo(a,b):
    return a ** b
def mod(a,b):
    return a // b

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
    "**": expo,
    "//": mod,
}

def calculate(f):
    if os.path.exists("Program\Practice\MathematicalSolverResult.txt"):
        file = open("Program\Practice\MathematicalSolverResult.txt", "w+").close()
    length = len(f)
    for i in range(0, length):
        data = f[i]
        line = data.split(" ")
        for ele in line:
            if ele in operations:
                operation_symbol = ele
                try:
                    num1 = float(line[0])
                    num2 = float(line[2])
                    calculation_function = operations[operation_symbol]
                    answer = calculation_function(num1, num2)

                    if os.path.exists("Program\Practice\MathematicalSolverResult.txt"):
                        file = open("Program\Practice\MathematicalSolverResult.txt", "a")
                        file.write(
                            f"{num1} {operation_symbol} {num2} = {answer}\n")
                        file.close()
                    else:
                        print("File not found")
                        break
                except:
                    if os.path.exists("Program\Practice\MathematicalSolverResult.txt"):
                        file = open("Program\Practice\MathematicalSolverResult.txt", 'a')
                        file.write(f"Error operand missing\n")
                    else:
                        print("File not found")
                        break


calculate(f)
