
hero0 = {
    "имя": "Василий",
    "возраст": 52,
    "здоровье": 92,
}

hero1 = {
    "имя": "Виталик",
    "возраст": 60,
    "здоровье": 75,
}

hero2 = {
    "имя": "Арсен",
    "возраст": 42,
    "здоровье": 100,
}

def show_hero(*hero_kortezh):
	for hero in hero_kortezh:
		print(hero["имя"], hero["возраст"], hero["здоровье"])

show_hero(hero0, hero1, hero2)
