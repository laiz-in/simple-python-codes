#demonstrating the function overriding or the method overriding

#creating a class my_team
class my_team:
     #creating a variable for storing the name of players
     teammates = ["messi","xavi","terstegan","raphinha","gavi"]

     #definfing a method for selecting the players
     def positions(self):
          pos = my_team.teammates
          forwards = [pos[0],pos[3],pos[1]]
          return forwards

#creating a seperate child  class for friendly matches, inheriting the my_team class as parent class
class my_team_for_friendlies(my_team):

     #defining the same method to select the players
     def positions(self):
          pos = my_team.teammates
          forwards = [pos[0], pos[1], pos[2]]
          return forwards


#creating the variable for the child class
v = my_team_for_friendlies()

# here we will be able to print the forwards which we defined in child class ,
# which is overriding the method in parent class
print("forwards for the match is ",v.positions())

