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