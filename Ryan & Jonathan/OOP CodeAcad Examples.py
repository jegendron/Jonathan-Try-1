#-----------------------------------------------------------------------------
#OOP!!!!!!
#-----------------------------------------------------------------------------
#1st example
class Fruit(object):
    """A class that makes various tasty fruits."""
    def __init__(self, name, color, flavor, poisonous):
        self.name = name
        self.color = color
        self.flavor = flavor
        self.poisonous = poisonous

    def description(self):
        print "I'm a %s %s and I taste %s." % (self.color, self.name, self.flavor)

    def is_edible(self):
        if not self.poisonous:
            print "Yep! I'm edible."
        else:
            print "Don't eat me! I am super poisonous."

lemon = Fruit("lemon", "yellow", "sour", False)

lemon.description()
lemon.is_edible()
#----------------------------------------------------------------------------
#create a class called animal that names itself
class Animal(object):
    def __init__(self, name):
        self.name=name
#create a zebra named Jeff and then print his name
zebra = Animal("Jeffrey")
print zebra.name
###################################
#Animals now have age and can be hungry (T/F)
class Animal(object):
    """Makes cute animals."""
    # For initializing our instance objects
#1st method
    def __init__(self, name, age):#, is_hungry (T/F)
        self.name = name
        self.age = age
        #self.is_hungry=is_hungry
#2nd method
    def description(self):
        print (self.name)
        print (self.age)
#add animals into the class
zebra = Animal("Jeffrey", 2)
giraffe = Animal("Bruce", 1)
panda = Animal("Chad", 7)

hippo = Animal("Po", 3)
sloth = Animal("Meme", 2)
ocelot = Animal("Barry", 4)

#for 1st method...
print (zebra.name, zebra.age, zebra.is_hungry)
print (giraffe.name, giraffe.age, giraffe.is_hungry)
print (panda.name, panda.age, panda.is_hungry)
#for 2nd method...
panda.description()

#To show the health...
print hippo.health
print sloth.health
print ocelot.health
#-----------------------------------------------------------------------------
#SHOPPING CART OOP
class ShoppingCart(object):
    """Creates shopping cart objects
    for users of our fine website."""
    items_in_cart = {}
    def __init__(self, customer_name):
        self.customer_name = customer_name

    def add_item(self, product, price):
        """Add product to the cart."""
        if not product in self.items_in_cart:
            self.items_in_cart[product] = price
            print (product + " added.")
        else:
            print (product + " is already in the cart.")

    def remove_item(self, product):
        """Remove product from the cart."""
        if product in self.items_in_cart:
            del self.items_in_cart[product]
            print (product + " removed.")
        else:
            print (product + " is not in the cart.")

#???????????????????
#my_cart = ShoppingCart("Bob")
#my_cart.add_item("Ukelele", 10)
#############################3
#Extended
class Customer(object):
    """Produces objects that represent customers."""
    def __init__(self, customer_id):
        self.customer_id = customer_id

    def display_cart(self):
        print ("I'm a string that stands in for the contents of your shopping cart!")

class ReturningCustomer(Customer):
    """For customers of the repeat variety."""
    def display_order_history(self):
        print ("I'm a string that stands in for your order history!")
#Print to see how it works...
monty_python = ReturningCustomer("ID: 12345")
monty_python.display_cart()
monty_python.display_order_history()
#########################################################
#The class TRIANGLE inherits from the class SHAPE
class Shape(object):
    """Makes shapes!"""
    def __init__(self, number_of_sides):
        self.number_of_sides = number_of_sides

# Add your Triangle class below!
class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
###########################################
#The triangle 2 angles should add up to 180
class Triangle(object):
    number_of_sides = 3
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
    def check_angles(self):
        if self.angle1+self.angle2+self.angle3==180:
            return True
        else:
            return False   
#Now make an object of this class and print 2 things
my_triangle = Triangle(90,30,60)
   
print (my_triangle.number_of_sides)#HOW MANY sides does it have?
print (my_triangle.check_angles())#DOES it have 3 sides?
#################EQUILATERAL TRIANGLE!!!!!!
class Equilateral(Triangle):
    angle = 60
    def __init__ (self):
        self.angle1 = self.angle
        self.angle2 = self.angle
        self.angle3 = self.angle
###########################################
#Employee class model; 1st full time, then pt time takes attributes of full time
class Employee(object):
    """Models real-life employees!"""
    def __init__(self, employee_name):
        self.employee_name = employee_name

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00

# Add your code below!
class PartTimeEmployee(Employee):
    def __init__(self, hours):
        self.employee_name = employee_name

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 12.00        
#-----------------------------------------------------------------------------
#######CONFUSING EXAMPLE
class Employee(object):
    """Models real-life employees!"""
    def __init__(self, employee_name):
        self.employee_name = employee_name

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00

# Add your code below!
class PartTimeEmployee(Employee):
    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 12.00
    def full_time_wage(self, hours):
        return super(PartTimeEmployee, self).calculate_wage(hours)

milton = PartTimeEmployee('milton')
print milton.full_time_wage(10)
#-----------------------------------------------------------------------------
class Car(object):
    condition = "new"
#Now create a new object that is an instance of the original class "CAR"
#my_car = Car()
#
#print (my_car.condition)
#displays the condition of my_car
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg = mpg
#This method allows the car to go in a display window
    def display_car(self):
        return ("This is a " +self.color+ " " +self.model+ " with " +str(self.mpg)+" MPG.")

    def drive_car(self):
        self.condition = "used"
        return self.condition

my_car.display_car()

#add a single delorean to the class
my_car = Car("DeLorean","silver","88")

#and show the details of the object my_car
print (my_car.model)
print (my_car.color)
print (my_car.mpg)

#prints original condition of the car
print my_car.condition
#prints condition of the car through the drive_car method (used)
print my_car.drive_car()

class ElectricCar(Car):
    def __init__(self, model, color, mpg, battery_type):
        self.model = model
        self.color = color
        self.mpg   = mpg
        self.battery_type = battery_type
#2nd method, drive the electric car, now like new    
    def drive_car(self):
        self.condition = "like new"
        return self.condition
        
my_2nd_car = ElectricCar("Tesla", "blue", 120, "molten salt")

#prints the orginal condition and the condition after you drive it
print (my_car.condition)
my_car.drive_car()
print (my_car.condition)

