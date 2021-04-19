i = 0
sum = 0

question = input("Digitar um número? (S/N)? ")
question = question.upper()

while question == "S":
    i = i + 1
    question = float(input("Digite um número: "))

    sum = sum + question

    question = input("Digitar novo número? (S/N)? ")    
    question = question.upper()

print("%i números digitados que somados resultam em %.2f" %(i, sum)) 