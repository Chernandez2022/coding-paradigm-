def flatten_and_sort(array):
    arr: []
    for item in array:
        for i in item:
            arr.append(i)
            return sorted(arr)

# This solution ensures data immutability because it doesnt change any external state or variable outside the scope 

# This solution is a pure function because it takes in whats in the array and sorts the data, it doesnt change the values

# It is not a higher order function because it does not take a function as an arguement 

# Functional programming is helpful for this type of problem because it a pure function that is just sorting data in an array.
# Meaning that the data is immutable so it helps reduce bugs and makes it easier to read for the next person 

class Podracer: 
    def _init_(self,max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price 

    def repair(self):
        self.condition = "repaired"

class AnakinsPod(Podracer):
    def _init_(self, max_speed, condition, price):
        super.init(max_speed, condition ,price)

    def boost(self):
        self.max_speed *= 2

class SebulasPod(Podracer):
    def _init_(self,max_speed, condition,price):
        super.init(max_speed,condition,price)

    def _flame_jet(self, other):
        other.condition = "trashed" 


# This solution shows the use encapsulation and inheritance through the use of classes to bundle the data of the pod 
# and inheritance through the inital podracer fucntion being passed through anakins and the others pods   

# I dont think it would have been easier to use funtional programming because these are not just calculations, we are getting states and determining data which in not immutable

# OOP helped solve this through the encapsulation and inheritance, using these pillars makes the code easier to understand and more efficient

