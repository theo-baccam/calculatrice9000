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

    # Si je ne gère pas les puissances à part et de cette façon, si je tente de faire
    # une opération avec nombres larges, ça va tenter de calculer n1 ** n2
    if operator == "**":
        result = pow(num_1, num_2, None)
    else:
        operators = {
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


def history_save(history_list):
    with open("history.txt", "a") as file:
        for item in history_list:
            file.write(f"{item}\n")
    history_list.clear()


def history_view(history_list):
    with open("history.txt", "r") as file:
        history_file = file.readlines()
        for item in history_file:
            clean_item = item.replace("\r", "").replace("\n", "")
            print(clean_item)
    for item in history_list:
        print(item)
    print("")


def history_clear():
    with open("history.txt", "w") as file:
        file.write("")


print("Calculatrice de Théo Baccam (tapez `help`): \n")
while True:
    try:
        prompt = input("==> ")
        processed = input_processor(prompt)

        if processed[0] == "quit" or processed[0] == "exit":
            history_save(current_history)
            print("Calculatrice fermée.")
            break

        if processed[0] == "help":
            print(
                "[num_1] + [num_2]\n"
                "Opérateurs valide: `+`, `-`, `*`, `/`, `**`, `//`, `%`\n"
                "`hist` pour voir l'historique, `save` pour le sauvegarder, "
                "il est également sauvegardé automatiquement avant de quitter."
                "Pour quitter, `quit`, `exit` ou 'CTRL+C'\n"
            )
            continue

        if processed[0] == "hist":
            history_view(current_history)
            continue

        if processed[0] == "save":
            history_save(current_history)
            print("Historique sauvegardé\n")
            continue

        if processed[0] == "clear":
            history_clear()
            print("Historique mis à zéro\n")
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
        history_save(current_history)
        print("\nCalculatrice fermée.")
        break
