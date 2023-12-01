import string

def input_processor(input_string):
    processed = [item for item in input_string.split(" ")]
    return processed

def num_verify(num_1, num_2):
    if (
        num_1 and num_1.replace(".", "", 1).isdigit() and
        num_2 and num_2.replace(".", "", 1).isdigit()
    ):
        return True

def calculs(operator, num_1, num_2):
    ZeroDiv = "Division par zéro pas possible"
    operators = {
        "**": num_1 ** num_2,
        "*": num_1 * num_2, 
        "/": num_1 / num_2 if num_2 != 0 else ZeroDiv,
        "//": num_1 // num_2 if num_2 != 0 else ZeroDiv,
        "%": num_1 % num_2 if num_2 != 0 else ZeroDiv,
        "+": num_1 + num_2,
        "-": num_1 - num_2,
    }

    if operator in operators:
        return operators[operator]
    else:
        return "Opérateur invalide"

while True:

    try:
        prompt = input("==> ")
        processed = input_processor(prompt)

        if len(processed) != 3:
            print("Opération invalide")
            continue

        operator = processed[1]
        num_1 = processed[0]
        num_2 = processed[2]

        if not num_verify(num_1, num_2):
            print("Il ne faut mettre que des nombres.\n")
            continue

        result = calculs(operator, float(num_1), float(num_2))
        print(f"{result}\n")

    except KeyboardInterrupt:
        print("\nCalculatrice fermée.")
        break

    except Exception as e:
        print(f"Erreur: {e}\nVeuillez réessayer.\n")