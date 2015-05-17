myList = ['jim', 'james', 23, 12, 'car', 'bike']
#
for i, x in enumerate(myList):
    print('variable i is: {} and x is: {}'.format(i, x))
#enumerate function.......................    
#for hw 5#############################################
###################################################################


#3 programming styles.....
#1) Procedural programming
#2) Functional programming: use fcns alot
#3) OOP=Object oriented programming
#
#OOP=best for spreading out work between multiple programmers
#Programming styles can be mixed together

#object can be a household, a consumer, a firm, etc
#(object used in video games all the time)


#######################################################
#############OBJECT ORIENTED PROGRAMMING#############

#stores data together with user defined functions

data=np.array([1,1.5,3,4])
np.sum(data)
#Versus
object1=[1,1.5,3,4]
#def function that adds 1st to last element
#what you can do with OOP, you can attach function to object

#scipt file based on blueprint
import math as m

class Animal(object):
    """This is the animal class. It's the top class."""
    #triple quotes for any text

    def __init__(self, name = 'Animal Doe', weight = 0.0):
        """Initialize the dog-object with a name variable"""
        self.name = name#data the objects will carry later on
        self.weight = weight#data the objects will carry later on
        #name and weight are what the animal is
        #if i don't assign name and weight, it will fill in predefined
            #animal doe and 0lbs

    def showMyself(self):#actions are defined as a function
        """Method: showMyself()
        prints out all the variables."""
        print("\n")
        print("Hello, let me introduce myself.")
        print("-------------------------------")
        print("My name is {}".format(self.name))
        print("My weight is {} pounds".format(self.weight))
        print("-------------------------------\n")

    def eatFood(self, foodAmount = 0.0): 
    #input variables for a "function on an object"
        """Method: eatFood(foodAmount=0)
        translates food input 'foodAmount'
        into additional weight according to the
        following formula:
        new_weight = old_weight + sqrt(foodAmount)"""
        self.weight += m.sqrt(foodAmount)#so 5+3, not 5+9!!!!!!

        #animal can show itself and it can eat
###############################################################

###############################################################
help(Animal)#shows blueprint.....
#####Start example######
animal1 = Animal(name = 'Birdy', weight = 5.0)#create an object!!!

animal1.name
#Out[26]: 'Birdy'

animal1.weight
#Out[27]: 5.0

####Works yet inefficient#############
#print("The name of the first animal is {}".format(animal1.name))
#print("The weight of the first animal is {}".format(animal1.weight))

########Better!!!!!!!!!!!!!!!######################
animal1.showMyself()

animal1.eatFood(9)
print("The animal's new weight is = {}".format(animal1.weight))

animal1.showMyself()

###################################################################
###################################################################
class Bird(Animal):
    """This is the bird class, derived from the
    animal class."""
#DEF can be named anything, but smart to be descriptive
    def __init__(self, name='Bird Doe', weight=0, color='na',
speed=0):#init is....
        """Initialize the bird-object calling the animal init method
        but also adding additional variables"""
        Animal.__init__(self, name, weight)
        self.color = color
        self.speed = speed

    def showMyself(self):#already defined from earlier....
        """Method: showMyself()
        prints out all the variables."""
        print("\n")
        print("Hello, let me introduce myself.")
        print("-------------------------------")
        print("My name is {}".format(self.name))
        print("My weight is {} grams".format(self.weight))
        print("My color is {}".format(self.color))
        print("My speed is {}".format(self.speed))
        print("-------------------------------\n")

    def flyTraining(self, workoutLength=0):
        #bird specific method, only bird can do. Other animals cant do this
        """Method: flyTraining(workoutLength)
        Augments the flight speed of the bird as a function
        of the bird objects workoutLength:
        new_speed = old_speed + log(workoutLength)"""
        self.speed += m.log(workoutLength)
#        if 
#            speed>50.....:
#            print ("")

###then loop.....
birdObjectList = []
name_list = ['Birdy', 'Chip', 'Tweets', 'Feather', 'Gull']
weight_list = [4.3, 2.3, 5.6, 5.0, 15.3]

for i, (name, weight) in enumerate(zip(name_list, weight_list)):
    print("Nr. {}: name = {}, weight = {}".format(i, name, weight))
    # Here we create the bird objects and store them in
    # the birdObjectList
    birdObjectList.append(Bird(name=name, weight=weight))

# Here we print what we have so far
print(birdObjectList)
########################33
############################
#######################
bird1 = Bird('Herman', 12, 'blue', 40)
bird1.showMyself()

bird1.eatFood(foodAmount=9)
bird1.flyTraining(workoutLength=10)
bird1.showMyself()
##########################3then.....
bird2 = Bird('Tweets', speed=12)#weight will be zero and color is na
bird2.showMyself()

###################Creating multiple objects####################
birdObjectList = []
name_list = ['Birdy', 'Chip', 'Tweets', 'Feather', 'Gull']
weight_list = [4.3, 2.3, 5.6, 5.0, 15.3]

for i, (name, weight) in enumerate(zip(name_list, weight_list)):
    print("Nr. {}: name = {}, weight = {}".format(i, name, weight))
    # Here we create the bird objects and store them in
    # the birdObjectList
    birdObjectList.append(Bird(name=name, weight=weight))
#created from....Bird(name=name, weight=weight)
    
# Here we print what we have so far
print(birdObjectList)
#########################################################
#########################################################
print('birdObjectList[2] =', birdObjectList[2])
print('birdObjectList[2].name =', birdObjectList[2].name)
print('birdObjectList[2].weight =', birdObjectList[2].weight)
print('birdObjectList[2].color =', birdObjectList[2].color)
print('birdObjectList[2].speed =', birdObjectList[2].speed)
#or can do......
birdObjectList[2].showMyself()


