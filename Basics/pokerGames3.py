import csv 


class pokerGame:
    
    # We decide a game rate
    
    game_rate = 0.2   # this is just to see how a class attribute works
    
    # Here we can create an "all lsit that will store the inforamtions about our crated instances"

    all = []

    # Definition of the attributes of our instances
    
    def __init__(self,
                 numberOfGames = 1,
                 numberOfHands = 10,
                 numberOfPlayers = 2,
                 name = "Game"):
        
         
        
    # Data validation of the input
    
        assert numberOfGames >= 1, f"Minimum numberOfGames >= 1, Current: {numberOfGames}"
        assert numberOfHands >= 1, f"Minimum numberOfHands >= 1, Current: {numberOfHands}"
        assert numberOfPlayers >= 2, f"Minimum numberOfPlayers >= 2, Current: {numberOfPlayers}"
        
    # Assignation of the arguments to self
    
        self.numberOfGames = numberOfGames
        self.numberOfHands = numberOfHands
        self.numberOfPlayers = numberOfPlayers
        self.__name = name   # I USE A __ TO MAKE THE ATTRIBUTE PRIVATE
    
    # We can append whatever inforamtion we want from our object to the new list
    

   # WE can extract all the INSTANCE instead of just the name
        
        if self not in pokerGame.all:    # Check if the name is already in the list

            pokerGame.all.append(self)

    # Let's set the read only attributes here
    @property
    def name(self):
        return self.__name

    # Methods

    def totalNumberOfGames(self):
        return self.numberOfGames * self.numberOfHands
    
    def reduceNumberOfGames(self):
        self.numberOfGames = self.numberOfGames * (1 - self.game_rate)
    
    @classmethod
    def instance_iterator_csv(cls, file):
        with open(file, 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:

            existing_instance = next(
                (instance for instance in cls.all if instance.name == item.get("name")), None)
            
            if existing_instance is None:
                
                pokerGame(                
                float(item.get("numberOfGames")),
                int(item.get("numberOfHands")),
                int(item.get("numberOfPlayers")),
                str(item.get("name"))

            )
    # we are addding another method to check if the number is integer or float
   
    # STATIC METHODS DO NOT RECEIVE THE BJECT AS THE FIRST PARAMETER, THEY WORK JUST LIKE REGULAR FUNCTIONS 
    # THUS IN ORDER TO USE THEM WE NEED TO PROVIDE A SET OF ARGUMENTS, IN FACT IF WE LOOK AT IT THE "self" ARGUMENT 
    # IS COLORED DARK BLUE AS UNLIKE OTHER METHODES DEFINED IN THE CLASS HERE WE ARE NOT PASSING THE SELF PARAMETER AUTOMATICALLY
   
    @staticmethod
    def is_integer(num):  

    # I cannopt use the self parameter
    # We will count out the flaots that are point zero
        
        if isinstance(num, float):
            return num.is_integer()
        
        elif isinstance(num, int):
            return True
        
        else:
            return False

    # it is ggood practive to prepresent the instances the same way they are created!!!!
    # for example game1 = pokerGame(1,100,3,"Game1")
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self.numberOfGames},{self.numberOfHands}, {self.numberOfPlayers}, '{self.name}')"


