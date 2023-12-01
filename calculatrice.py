import string

def calculs(operator, num_1, num_2):
    operators = {
        "**": num_1 ** num_2,
        "*": num_1 * num_2,
        "/": num_1 / num_2,
        "//": num_1 // num_2,
        "%": num_1 % num_2,
        "+": num_1 + num_2,
        "-": num_1 - num_2,
    }

    if operator in operators:
        return operators[operator]

while True:
    prompt = input("==> ")
    processed = [item for item in prompt.split(" ")]
    if len(processed) != 3:
        print("Invalid")
        continue
    operator = processed[1]
    num_1 = float(processed[0])
    num_2 = float(processed[2])

    result = calculs(operator, num_1, num_2)
    print(f"{result}\n")