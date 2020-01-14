# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
"""
self refers to the object being created
Python will use the first parameter that __init__() receives to refer to the object being created; 
this is why it’s often called self, since this parameter gives the object being created its identity.
"""
class LatLon:
    def __init__ (self, lat, lon):
        self.lat = lat
        self.lon = lon

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE
#when you want to use an attribute or method from your parent class, you use the keyword super
class Waypoint(LatLon):
    def __init__ (self, name, lat, lon):    
        super().__init__(lat, lon) #we have overridden init with a Waypoint specific constructor    
        self.name = name        

    def __str__(self):
        return 'Name: ' + self.name + ' Latitude: ' + str(self.lat) + ' Longitude:  ' + str(self.lon)

        
# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from? Ans: Waypoint

# YOUR CODE HERE
class Geocache(Waypoint):
    def __init__(self, name, difficulty, size, lat, lon):  
        super().__init__(name, lat, lon)     
        self.difficulty = difficulty
        self.size = size

    def __str__(self):
        return super().__str__() + ' Difficulty: ' + str(self.difficulty) + ' Size: ' + str(self.size)
        

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE
waypoint = Waypoint("Catacombs", 41.70505, -121.51521)
print(waypoint)

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE
geocache = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)
# Print it--also make this print more nicely
print(geocache)

"""
# Note that self is only used in the __init__()
# function definition; we don't need to pass it
# to our instance objects.
"""

"""
Inheritance is the process by which one class takes on the attributes and methods of another, 
and it’s used to express an is-a relationship. For example, a Panda is a bear, so a Panda class 
could inherit from a Bear class. 
"""

"""
You can directly access the attributes or methods of a superclass with Python’s built-in super call.

The syntax looks like this:

class Derived(Base):
  def m(self):
    return super(Derived, self).m()
Where m() is a method from the base class.
"""

"""
One useful class method to override is the built-in __repr__() method, which is short for representation; 
by providing a return value in this method, we can tell Python how to represent an object of our class 
(for instance, when using a print statement).
"""

"""
def display_car(self):
    print "This is a %s %s with %s MPG." % (self.color, self.model, str(self.mpg))

    # object_name (car = Car() => car.display_car)

OR

def __repr__(self):
    return "(%d, %d, %d)" % (self.x, self.y, self.z) #print object_name (car = Car() => print car)

"""