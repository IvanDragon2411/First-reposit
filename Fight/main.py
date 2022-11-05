from Charter import Charecter

Player1 = Charecter(name='POPA', health=110, damage=5, live=True)
Player2 = Charecter(name='pety', health=85, damage=15, live=True)




livePOPA = Player1.live
livepety = Player2.live




while livePOPA == True and livepety == True:
    print(Player1)
    print(Player2)

    Player1.attack(Player2)
    Player2.attack(Player1)


    Player1.is_alive()
    Player2.is_alive()

    livePOPA = Player1.live
    livepety = Player2.live

    print(Player1)
    print(Player2)


