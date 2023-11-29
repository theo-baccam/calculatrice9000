import string

def calcul(input_string):
    calcul_list = [ value for value in input_string.split(" ") ]
    longueur_list = len(calcul_list)
    if longueur_list != 3:
        # return est moins disruptif que raise ValueError()
        return "Avez vous bien mis des espaces entre tous les éléments?"
    num_1 = calcul_list[0]
    operator = calcul_list[1]
    num_2 = calcul_list[2]

    if not (num_1 and num_1.replace(".", "", 1).isdigit() and
            num_2 and num_2.replace(".", "", 1).isdigit()):
        return "Nombre invalide"

    if operator == "*":
        result = (float(num_1) * float(num_2))
    elif operator == "/":
        result = (float(num_1) / float(num_2))
    elif operator == "+":
        result = (float(num_1) + float(num_2))
    elif operator == "-":
        result = (float(num_1) - float(num_2))
    else:
        return f"'{operator}' est invalide"

    string_result = str(result)
    leftover = string_result[-2::1]
    if leftover == ".0":
        return string_result[0:-2]
    else:
        return string_result


while True:
    prompt = input("Donnez une opération: ")

    resultat = calcul(prompt)
    print(resultat)
