import string

current_history = []


def input_processor(input_string):
    processed = [item for item in input_string.split(" ")]
    return processed


def num_verify(num_1, num_2):
    if (
        num_1
        and num_1.replace(".", "", 1).isdigit()
        and num_2
        and num_2.replace(".", "", 1).isdigit()
    ):
        return True


def calculs(operator, num_1, num_2):
    ZeroDiv = "Division par zéro pas possible"
    operators = {
        "**": num_1**num_2,
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


def history_append(num_1, operator, num_2, result, history_list):
    history_list.append(f"{num_1} {operator} {num_2} = {result}")


print("Calculatrice de Théo Baccam (tapez `help`): ")
while True:
    try:
        prompt = input("==> ")
        processed = input_processor(prompt)

        if processed[0] == "quit" or processed[0] == "exit":
            print("Calculatrice fermée.")
            break

        if processed[0] == "help":
            print(
                "[num_1] + [num_2]\n"
                "Opérateurs valide: `+`, `-`, `*`, `/`, `**`, `//`, `%`\n"
                "Pour quitter, `quit`, `exit` ou 'CTRL+C'\n"
            )
            continue

        if processed[0] == "hist":
            for item in current_history:
                print(item)
            print("")
            continue

        if len(processed) != 3:
            print("Erreur: Ni une commande, ni une opération valide.\n")
            continue

        operator = processed[1]
        num_1 = processed[0]
        num_2 = processed[2]

        if not num_verify(num_1, num_2):
            print("Il ne faut mettre que des nombres.\n")
            continue

        result = calculs(operator, float(num_1), float(num_2))
        history_append(num_1, operator, num_2, result, current_history)
        print(f"{result}\n")

    except KeyboardInterrupt:
        print("\nCalculatrice fermée.")
        break

    except Exception as e:
        print(f"Erreur: {e}\nVeuillez réessayer.\n")
