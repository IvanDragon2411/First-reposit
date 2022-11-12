from Fight.Charter import Charecter
from derserk import Berserk
from knight import Knight
from Asasin import Asasin
from Ninja import  Ninja
from Vimpire import Vimpire

Player1 = Berserk(name='Biba', health=100, damage=15, live=True)
Player2 = Vimpire(name='Boba', health=100, damage=10, live=True)


livebiba = Player1.live
liveboba = Player2.live




for i in range(1):
    print(Player1)
    print(Player2)


    Player2.attack(Player1)
    Player2.heal(health=100)
    print(Player1.count_add_damage())
    Player1.attack(Player2)

    Player1.is_alive()
    Player2.is_alive()

    livebiba = Player1.live
    liveboba = Player2.live

    print(Player1)
    print(Player2)