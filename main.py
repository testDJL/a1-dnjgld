## Your name:
def myName():
  '''
  Return your full name as a string.
  '''
  return "DJL"  # Replace with your actual full name

### Numbers and functions
def myMax(x, y):
  '''
  Return whichever argument is larger using if statements. If both values are equal, then return the string "Equal" instead.

  myMax(6,3) = 6
  myMax("abc", "def") = "def"
  myMax(24,24)= "Equal"
  '''
  if x == y:
    return "Equal"
  elif x > y:
    return x
  else:
    return y

def factorial(n):
  '''
  Return n factorial using recursion.

  factorial(4) = 4*3*2*1
  '''
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)

### Strings
def combineAnd(a, b):
  '''
  Return a string in the form "a and b" where a and b are the input arguments.

  combineAnd("abc", "xyz") = "abc and xyz"
  '''
  return f"{a} and {b}"

def changeXtoY(input, x, y):
  '''
  Change all occurences of "x" to "y" in the input string. You can assume all variables are strings.

  changeXtoY("hello world", "world", "GW") = "hello GW"
  '''
  return input.replace(x, y)

### Array operations
def returnNextToLast(a):
  '''
  Return the next to last element in an array.
  You should not need to find the length of the array, instead use slicing.
  You can assume the array has sufficient elements in it.
  '''
  return a[-2]

def returnSecondHalf(a):
  '''
  Return an array containing the elements in the second half of an array using slicing.
  You can assume the array has an even number of elements in it.
  '''
  return a[len(a)//2:]

def addApple(a):
  '''
  Add the string "apple" to the end of the input array and return it.

  addApple(["cat", "carrot"]) = ["cat", "carrot", "apple"]
  '''
  a.append("apple")
  return a

### Data structures
def myFavFoods():
  '''
  Return an array with three strings representing your favorite foods.
  '''
  return ["Pizza", "Sushi", "Ice Cream"]  # Replace with your actual favorite foods

def myFavFoodsTuple():
  '''
  Return a tuple with three strings representing your favorite foods.
  '''
  return ("Pizza", "Sushi", "Ice Cream")  # Replace with your actual favorite foods

def courseDict():
  '''
  Return a dictionary with keys and values as follows:
  KEY     ->    VALUE
  name    ->    Database Systems and Team Projects
  number  ->    2541
  dept    ->    CSCI
  prof    ->    Wood
  '''
  return {
    "name": "Database Systems and Team Projects",
    "number": 2541,
    "dept": "CSCI",
    "prof": "Wood"
  }

def favFoodsMenu():
  '''
  Return a dictionary that has a key for each of the elements returned by your myFavFoods() function. You should call that function from this one to find out what the foods are, rather than hard code it. The value for each key in the dictionary should be the length of the string. For example, if one of the foods returned by the myFavFoods() function is "pizza", then your dictionary should contain the element "pizza"->5
  '''
  foods = myFavFoods()  # Get the list of foods from myFavFoods function
  return {food: len(food) for food in foods}
