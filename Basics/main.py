from pokerGames4 import pokerGume



from gameTypes import phone
import os

directory = r"C:\Users\jakub\OneDrive\Jakub.Personal\02.Python\02.Object-Oriented-Programming\Basics"

os.chdir(directory)

#pokerGame.instance_iterator_csv("pokerGames.csv")


#print(pokerGame.all)

"""
Now let's continue our quest
"""

# item1 = pokerGame(name = "myItem", numberOfGames=50)
# item1.name = "OtherItem"
# 
# print(item1.name)



"""
How to create ready only attributes? meaning that for me it wil not be possible
to modify the attribute directly. I can do this by creating a @property decorator
"""

#print(item1.readOnlyName)

# But now if i try to modifty this name

#item1.readOnlyName = "BBB"

#print(item1.readOnlyName)

"""
The error that we get is that the property has no setter, meaning that cannot be mod just like that
So in fact those attributes can be modified but it has to be done by a setter


LET'S MODIFY THE POKERGAMES FILE IN ORDER TO HAVE JUST READ ONLY ATTRIBUTES
"""

#item2 = pokerGame(name = "Item", numberOfGames=80)
#item2.name
#item2._name = "BBB"   # i can still set the name of _name, tihs is really dangerous in many cases
#
#print(item2.name)

# I want ot crete a PRIVATE ATTRIBUTES, and it can be done by adding two underscores to the neme of my attribute!!!

#item3 = pokerGame(name = "Item3", numberOfGames=8)
#item3.name
#item3.__name = "BBB"   # i can still set the name of _name, tihs is really dangerous in many cases
#
#print(item3.name)
#print(item3.__name)


# The output of the code is "Item3" i still can print __name and the result will be "BBB"
# IN PYTHON THERE ARE NOT PRIVATE ATTRIBUTES , WE HAVE JUST # PROPERTIES AND THIS IS A WORKAROUND ACTAULLY

#print(item3._pokerGame__name)

# I have to write obejct._class__attribute to retrive the attribute


"""
Let's define a property setter in case we want to access teh atttribute externally 
"""
item3 = pokerGume(name= "Item3", numberOfGames= 85)

item3.name = "item5"
print(item3.name)

# so i have setted the name