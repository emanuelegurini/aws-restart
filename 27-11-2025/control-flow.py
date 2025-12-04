# 1. vedere la domanda X
# 2. vedere le possibili risposte X
# 3. inserire una risposta X
# 4. verificare che la risposta sia esatta X 
# 5. se la risposta che diamo e corretta fai a altrimenti fai b


question_1: str = "Qual e' il tuo trapper preferito?"
answer_1 : str = "Gue"
answer_2 : str = "Kid Yogi"
answer_3 : str = "Taxi B"
answer_4 : str = "Dark Polo"

# print(f"""
#{question_1}
#    A. {answer_1} 
#    B. {answer_2} 
#    C. {answer_3}
#    D. {answer_4}
#""")

"""
answer: str = input("Inserisci la risposta preferita:")

answer_tmp = answer.upper()

match answer_tmp:
    case "A" | "Z":
        result = f"la risposta e: {answer_tmp} - {answer_1}"

    case "B":
        result = f"la risposta e: {answer_tmp} - {answer_2}"

    case "C":
        result = f"la risposta e: {answer_tmp} - {answer_3}"

    case "D":
        result = f"la risposta e: {answer_tmp} - {answer_4}"
    case _:
        result = "Cambia cantante etc. etc."

print(result)

"""

"""
if answer_tmp == "A":
    print(f"la risposta e: {answer_tmp} - Sfera Ebbasta")

elif answer_tmp == "B":
    print(f"la risposta e: {answer_tmp} - Sfera Ebbasta")

elif answer_tmp == "C":
    print(f"la risposta e: {answer_tmp} - Sfera Ebbasta")

elif answer_tmp == "D":
    print(f"la risposta e: {answer_tmp} - Sfera Ebbasta")

else:
    print(f"Cambia cantante, tanto i trapper non cantano")
"""


input_venv : str = ""

while True:
    input_venv = input("(venv) $")
    if input_venv == "deactivate":
        break
    print("Ancora in esecuzione")

print("uscito dal venv")




