def month_to_season(n):
    if n>12 or n<1:
        print("Такого месяца нет")
    if n>2 and n<=5:
        print("весна")
    if n>5 and n<=8:
        print("лето")
    if n>=2 or n==12:
        print("зима")
while True:
    n=int(input("Введите номер месяца - "))
    month_to_season(n)