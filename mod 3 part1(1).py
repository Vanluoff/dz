x=float(input("Введите размер вклада"))
y=float(input("Введите желаемую сумму"))
p=float(input("Введите размер процента"))

Bank=0
while True:
    Bank=x/100*p+x
    if x>=y:
        print(Bank)
    break
print("Подождите,пожалуйста,мы занимаемся вашим вопросом")

