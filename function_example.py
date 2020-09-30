inv = ["Sword","Apple"]
print (inv)
inv.append("Shield") #ADD ANYTHING
print (inv)
print(inv[0])
print(inv[1])
print(inv[2])
inv[0:1]
inv.pop (2) #DELETE LAST OBJECT(THE NUMBER FROM 0)
print (inv)
invcopy = inv
inv.append("Knife")
print(invcopy)