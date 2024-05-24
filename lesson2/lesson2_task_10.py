def bank(x, y):
    for m in range (0, y): #пополнение вклада
        x=x+x*0.1*m
    for i in range (1, y+1): #проценты по вкладу
        x=x+x*0.1*i
    
    print(x)

while True:
    x=int(input("Введите сумму - "))
    y=int(input("Введите срок вклада - "))
    bank(x, y)