
from pokerGames import pokerGame

# I am getting an error when if i do not import pokerGames

class phone(pokerGame):
    
    def __init__(self,
                 numberOfGames = 1.0,
                 numberOfHands = 10,
                 numberOfPlayers = 2,
                 name = "game",
                 type = 0):

        super().__init__(
            numberOfGames, numberOfHands, numberOfPlayers, name
        )



        self.type = type
    

# game1 = GameType(type = 0)

# print(GameType.all)