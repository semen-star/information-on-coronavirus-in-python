from covid import Covid
print("Добро пожаловать\nЭто инфо-стенд про коронавирус")
country = input("Введите страну на английском:")
info = Covid().get_status_by_country_name(country)

print("Заболело:"+str(info["active"]))
print("Выздоровело:"+str(info['recovered']))
print("Умерло:"+str(info['deaths']))
