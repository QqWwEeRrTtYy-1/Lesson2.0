hero0 = {
    "имя": "Василий",
    "возраст": 52,
    "здоровье": 92,
    "сытость": 0
} 

hero1 = {
    "имя": "Виталик",
    "возраст": 20,
    "здоровье": 100,
    "сытость": 18
}

def stolovaya(*heroes):
    for hero in heroes:
        """hero["сытость"] +=10"""
        hero["сытость"] = 100
        print(hero["сытость"])
        
stolovaya(hero0, hero1)