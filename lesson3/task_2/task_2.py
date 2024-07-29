from smartphone import smartphone
catalog=[]

phone1=smartphone("samsung", "a54", "+79996666666")
phone2=smartphone("iphone", "12", "+79991234567")
phone3=smartphone("meizu", "o4", "+79519876543")
phone4=smartphone("samsung", "galaxy", "+75986547896")
phone5=smartphone("xiaomi", "11", "+79993214563")

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print(f"{phone.brand}-{phone.model}. {phone.number}")