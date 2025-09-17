# Write a recursive function called someRecursive which accepts an array and a callback.
# The function returns true if a single value in the array returns true when passed to the callback.
# Otherwise it returns false.
# Examples
# someRecursive([1,2,3,4], isOdd) # true
# someRecursive([4,6,8,9], isOdd) # true
def is_odd(num):
    return num%2!=0

def some_recursive(arr, callback):
    if len(arr) == 0:
        return False
    if callback(arr[-1]) is True:
        return True
    return some_recursive(arr[0:-1],callback)

# print(some_recursive([1,2,3,4],is_odd))

# Write a recursive function called flatten which accepts an array of arrays and returns a new array with all values flattened.
# flatten([1, 2, 3, [4, 5]]) # [1, 2, 3, 4, 5]
# flatten([1, [2, [3, 4], [[5]]]]) # [1, 2, 3, 4, 5]

def flatten(arr):
    result = []
    for item in arr:
        if type(item) is list:
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

# print(flatten([1, 2, 3, [4, 5]]))

# Write a recursive function called capitalizeFirst. Given an array of strings, capitalize the first letter of each string in the array.
# capitalizeFirst(['car', 'taco', 'banana']) # ['Car','Taco','Banana']

def capitalize_first(arr):
    if len(arr) == 0:
        return []
    return [arr[0][0].upper()+arr[0][1:]]+capitalize_first(arr[1:])

print(capitalize_first(['car', 'taco', 'banana']))

# Write a recursive function called nestedEvenSum. Return the sum of all even numbers in an object which may contain nested objects.
obj1 = {
  "outer": 2,
  "obj": {
    "inner": 2,
    "otherObj": {
      "superInner": 2,
      "notANumber": True,
      "alsoNotANumber": "yup"
    }
  }
}

obj2 = {"a": 2, "b": {"b": 2, "bb": {"b": 3, "bb": {"b": 2}}},"c": {"c": {"c": 2}, "cc": 'ball', "ccc": 5},"d": 1,"e": {"e": {"e": 2}, "ee": 'car'}}

def nested_even_sum(nested_obj, sum =0):
    for _,val in nested_obj.items():
        if isinstance(val,int) and val%2 == 0:
            sum += val
        elif isinstance(val, dict):
            sum += nested_even_sum(val)
    return sum

# print(nested_even_sum(obj1)) # 6
# print(nested_even_sum(obj2)) # 10

#Write a recursive function called capitalizeWords. Given an array of words, return a new array containing each word capitalized.
# words = ['i', 'am', 'learning', 'recursion']
# capitalizeWords(words) # ['I', 'AM', 'LEARNING', 'RECURSION']

def capitalize_words(arr):
    if arr==[]:
        return []
    if isinstance(arr[0], str):
        return [arr[0].upper()] + capitalize_words(arr[1:])

# print(capitalize_words(['i', 'am', 'learning', 'recursion']))

# Write a function called stringifyNumbers which takes in an object 
# and finds all of the values which are numbers and converts them to strings. 
# Recursion would be a great way to solve this!
obj = {
  "num": 1,
  "test": [],
  "data": {
    "val": 4,
    "info": {
      "isRight": True,
      "random": 66
    }
  }
}
 
# stringifyNumbers(obj)
 
obj2 = {'num': '1', 
 'test': [1,2,3,4], 
 'data': {'val': '4', 
          'info': {'isRight': True, 'random': '66'}
          }
}

def stringify_numbers(obj):
    for key,val in obj.items():
        if isinstance(val, int) and not isinstance(val,bool):
            obj[key] = str(val)
        elif isinstance(val,dict):
            stringify_numbers(obj[key])
    return obj
# a better method implementation that handles lists and dictionaries is given below :
# def stringify_numbers(obj):
#     if isinstance(obj, dict):
#         return {k: stringify_numbers(v) for k, v in obj.items()}
#     elif isinstance(obj, list):
#         return [stringify_numbers(i) for i in obj]
#     elif isinstance(obj, (int, float)) and not isinstance(obj, bool):
#         return str(obj)
#     return obj

print(stringify_numbers(obj2))

# Write a function called collectStrings which accepts an object and returns an array of 
# all the values in the object that have a typeof string.
# Examples
#collectStrings(obj) # ['foo', 'bar', 'baz']
obj = {
  "stuff": 'foo',
  "data": {
    "val": {
      "thing": {
        "info": 'bar',
        "moreInfo": {
          "evenMoreInfo": {
            "weMadeIt": 'baz'
          }
        }
      }
    }
  }
}

def collect_strings(obj):
    result = []
    for _,val in obj.items():
        if isinstance(val,str):
            result.append(val)
        if isinstance(val, dict):
            result.extend(collect_strings(val))
    return result      
 
print(collect_strings(obj))