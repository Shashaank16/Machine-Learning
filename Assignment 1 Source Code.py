# Question1
# list
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()  # sorting the list
print("Sorted List is ", ages)
# min and max age
print("Max age is : ", max(ages))  # Max age
print("Min age is : ", min(ages))  # Min age
# Add min age and max age of list to the ages list
ages.append(min(ages))  # adding min age in the list
print("After adding of the min age again to the ages list :", ages)
ages.append(max(ages))  # adding max age in the list
print("After adding of the min age again to the ages list :", ages)
# Median of the list age
import statistics  # Find the median age (one middle item or two middle item divided by two
print("Median of the list : ", statistics.median(ages))
# Average age (sum of all items divided by their number)
def Average(ages):
    return sum(ages) / len(ages)
average = Average(ages)
print("Average age =", round(average, 2))
# Range of the age (max minus min)
max_value = max(ages)
min_Value = min(ages)
range_ = max(ages) - min(ages)
print("Range of ages :", range_)

# Question 2 Dictionary
# empty dictionary
dog = {}
dog["name"] = "Harry"
dog["colour"] = "white"
dog["breed"] = "samoyed"
dog["legs"] = "four"
dog["age"] = "five"
print(dog)
# dct = {'key1':'value1', 'key2':'value2','key3':'value3'}
student = {"first_name": "Jon",
           "lastname": "Stark",
           "gender": "male",
           "age": "23",
           "martial status": "Single",
           "skills": "Python",
           "country": "India",
           "city": "Kerala",
           "address": "#369 st"}
print("Student", student)
print("Length of Student dictionary:", len(student))  # length of the student dictionary
print("Student skill value:", student["skills"])  # Student skill value
print("Data type :", type(student["skills"]))  # checking data type
student["skills"] = "Python,Java"  # adding skill value
print("After Modifying skills values", student)
keys_list = (student.keys())
print("Keys as a List:", keys_list)
keys_list = (student.values())
print("Values as a List:", keys_list)

# Question3
# Create a tuple containing names of your sisters and your brothers
brothers_tuple = ('ram', 'krishna')
sisters_tuple = ('sita', 'radha')
sib = brothers_tuple + sisters_tuple  #Find the total siblings
print(sib)
print("Number of siblings: ", len(sib))  # Number of siblings
family_members = sib + ('vishnu', 'lakshmi') #Adding father and mother to the family
print("Family members :", family_members)

# Question 4
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
print("The length of the set is:", len(it_companies))
company = ('twitter')
it_companies.add(company)  # Adding twitter company to the set
print("After adding a company to the set: ", it_companies)
multiple_companies = ('TCS', 'Deloitte')
it_companies.update(multiple_companies)  # inserting multiple companies to the set
print("After adding multiple companies to the set", it_companies)
it_companies.remove('Facebook')  # Removing a company from the set
print("After Removing a company from the set:", it_companies)
# Join A and B
C = A.union(B)
print("Join A and B:", C)
# Find A intersection B
print("A intersection B is:", A.intersection(B))
# Is A subset of B
print("Is A subset of B:", A.issubset(B))
# Are A and B disjoint sets
print("Are A and B disjoint sets:", A.isdisjoint(B))
# Join A with B and B with A
A.update(B)  # A with B
print("Join A with B", A)
B.update(A)  # B with A
print("Join B with A", B)
# What is the symmetric difference between A and B
symmetry = A.symmetric_difference(B)
print("The Symmetry between A and B is ", symmetry)
# Delete the sets completely
A.clear()
print("After Deleting the A set: ", A)
B.clear()
print("After Deleting the B set: ", B)

# Question 5
PI = 3.14
radius = float(input('please Enter the radius of a circle: '))  # Radius as User input
diameter = 2 * radius
circumference = 2 * PI * radius
area = PI * radius * radius
print("_circum_of_circle_ = %.2f" % circumference)  # circumference of a circle
print("_area_of_circle_ %.2f" % area)  # area of a circle

# Question 6
# Sentence is I am a teacher and I love to inspire and teach people
a = input("Please enter a sentence: ")
unique = set(a.split(' '))
b = len(unique)  # No of unique words
print("The number of unique words used in this sentence: ", b)

# Question 7
# Using tab escape sequence
a = ('Name     \tAge\tCountry\tCity')
b = ('Asabeneh\t250\tFinland\tHelsink')
print(a)
print(b)

# Question 8
# using string formatting method to display
radius = 10
area = 3.14 * radius * radius
print(f'The area of the circle with radius 10 is {area:.0f} meters square')

# Question 9
# number of students
# L1: [150, 155, 145, 148]
# Output: [68.03, 70.3, 65.77, 67.13]
n = int(input("Enter number of students : "))
# This line read inputs from user using map() function
a = list(map(int, input("\nEnter weights of students :").strip().split()))[:n]
print("\nL1 : ", a)
b = [i/2.2048364154 for i in a]
b = ['%2f' % elem for elem in b]
print(b)



