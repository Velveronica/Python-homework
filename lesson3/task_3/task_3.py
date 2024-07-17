from adress import adress
from mailing import mailing

to_adress=adress("66666", "Novosibirsk", "Geroev Truda", "20", "50")
from_adress=adress("12345", "Tomsk", "Sibisckaya", "20", "50")
mailing=mailing(to_adress, from_adress, 400, "zxc123")

print(f"otpravlenie {mailing.track} iz {mailing.from_adress.index},"
      f"{mailing.from_adress.city}, {mailing.from_adress.street},"
      f"{mailing.from_adress.home}-{mailing.from_adress.floor}"
      f"v {mailing.to_adress.index},{mailing.to_adress.city},"
      f"{mailing.to_adress.street},{mailing.to_adress.home}-"
      f"{mailing.from_adress.floor}. stoimost {mailing.cost} rybley.")
                   