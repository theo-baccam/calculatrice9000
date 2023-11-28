import string

def calcul(input_string):
    calcul_list = [ value for value in input_string.split(" ") ]
    print(calcul_list)
    num_1 = calcul_list[0]
    operator = calcul_list[1]
    num_2 = calcul_list[2]
    if operator == "*":
        result = (float(num_1) * float(num_2))
    elif operator == "/":
        result = (float(num_1) / float(num_2))
    elif operator == "+":
        result = (float(num_1) + float(num_2))
    elif operator == "-":
        result = (float(num_1) - float(num_2))
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
