def square(x):

    x1=float(x)
    x2=int(x)
    if x1-float(x2)>=0.5:
        x=round(x1)
        return x*x
    elif x1-float(x2)<0.5 and x1-float(x2)>0:
        x=round(x1)+1
        return x*x
    else:
        x=x2
        return x*x
x=input("Введите число - ")
s=x*x
print(s)