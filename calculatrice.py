import string

hist = []


def calcul(input_string):
    if input_string == "hist":
        for item in hist:
            print(item)
        return ""
    if input_string == "clear":
        hist.clear()
        return ""
    
    if input_string == "quit" or input_string == "exit":
        return "Quitting...\n"

    calcul_list = [value for value in input_string.split(" ")]

    longueur_list = len(calcul_list)
    if longueur_list != 3:
        # return est moins disruptif que raise ValueError()
        return "Opération ou commande invalide\n"

    num_1 = calcul_list[0]
    operator = calcul_list[1]
    num_2 = calcul_list[2]

    if not (
        num_1 and num_1.replace(".", "", 1).isdigit()
        and num_2 and num_2.replace(".", "", 1).isdigit()
    ):
        return "Nombre invalide\n"

    if operator == "**":
        result = float(num_1) ** float(num_2)
    elif operator == "*":
        result = float(num_1) * float(num_2)
    elif operator == "/":
        result = float(num_1) / float(num_2)
    elif operator == "*":
        result = float(num_1) // float(num_2)
    elif operator == "*":
        result = float(num_1) % float(num_2)
    elif operator == "+":
        result = float(num_1) + float(num_2)
    elif operator == "-":
        result = float(num_1) - float(num_2)
    else:
        return f"'{operator}' est invalide\n"

    string_result = str(result)
    leftover = string_result[-2::1]
    if leftover == ".0":
        hist.append(f"{num_1} {operator} {num_2} = {string_result[0:-2]}")
        return f"= {string_result[0:-2]}\n "
    else:
        hist.append(f"{num_1} {operator} {num_2} = {string_result}")
        return f"= {string_result}\n "


print("Donnez une opération, ou tapez 'hist' pour l'historique:\n")

while True:
    prompt = input("==> ")
    resultat = calcul(prompt)
    print(resultat)
    if resultat == "Quitting...\n":
        break
