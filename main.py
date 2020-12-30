import classes as c

def main():
    global player
    player = c.Player("Иван", "Иванов", 1, 100, 2)
    player.print_stats()
    
    def fight():
        def create_enemy():
            global enemy
            enemy = c.Enemy(1)
            enemy.print_stats()
            
        def battle(player, enemy):
            enemy.change_stats(player.attack)
            
        create_enemy()
        battle(player, enemy)
    fight()

main()