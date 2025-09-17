def recursive(n):
    assert n>=0 and int(n) == n , "Positive integer only"
    if n<1:
        print(" n is less than 1")
    else:
        recursive(n-1)
        print(n)
        
def factorial(n):
    if n ==1 or n ==0:
        return 1
    else:
        return n*factorial(n-1)

def fibonacci(n):
    assert n>=0 and int(n) == n , "Positive integer only"
    if n==0 or n==1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)


def sum_digits(n):
    assert n>=0 and int(n) == n , "Positive integer only"
    if n//10 == 0:
        return n
    else:
        return n%10 + sum_digits(n//10)

def power_of(base, exp):
    assert int(exp)==exp , "exponentials to be positive integer only"
    if exp==0:
        return 1
    elif exp <0:
        return 1/base * power_of(base, exp+1)
    else:
        return base*power_of(base,exp-1)

def find_gcd(num1, num2):
    assert int(num1)==num1 and int(num2)==num2 , "numbers should be integer only"
    assert num1>=num2>0, "num1 should be greater than num2 and both should be positive"
    if num2 ==0:
        return num1
    else:
        return find_gcd(num2,num1%num2)
    
# print(find_gcd(48,18))

def convert_decimal_to_binary(num, bin_representation = ''):
    assert int(num)==num , "number should be integer"
    if not num:
        return bin_representation
    else:
        return convert_decimal_to_binary(num//2,str(num%2)+bin_representation)

# print(convert_decimal_to_binary(10))

# Write a function called productOfArray which takes in an array of numbers and returns the product of them all.
# Examples
# productOfArray([1,2,3]) #6
# productOfArray([1,2,3,10]) #60

def product_of_array(arr, product = 1):
    if len(arr)==1:
        return product*arr[0]
    else:
        return product_of_array( arr, product*arr.pop())
    
# print(product_of_array([1,2,3]))

# Write a function called recursiveRange which accepts a number and adds up all the numbers from 0 to the number passed to the function.
# Examples
# recursiveRange(6) # 21
# recursiveRange(10) # 55

def recursive_range(num, sum=0): #tail recursion with accumulator . result is computed fully before returning
    if num==0:
        return sum
    else:
        return recursive_range(num-1,sum+num)

def recursiveRange(num): # compute after recursion call returns
    if num ==1:
        return num
    return num+recursiveRange(num-1)
    
# print(recursiveRange(6))

#Write a recursive function called fib which accepts a number and returns the nth number in the Fibonacci sequence.

def fib(n):
    if n in [0,1]:
        return n
    else:
        return fib(n-1)+fib(n-2)

#print(fib(10))

# Write a recursive function called reverse which accepts a string and returns a new string in reverse.
# reverse('python') # 'nohtyp'
# reverse('appmillers') # 'srellimppa'
def reverse(s):
    if s =="":
        return s
    return reverse(s[1:])+ s[0]

# Write a recursive function called isPalindrome which returns true 
# if the string passed to it is a palindrome (reads the same forward and backward). 
# Otherwise it returns false.
# isPalindrome('awesome') # false

def is_palindrome(s):
    if len(s) <=1:
        return True
    if s[0]!=s[-1]:
        return False
    return is_palindrome(s[1:-1])

# is_palindrome("racecar")

def sum_recursively(arr,total=0): #tail recursion used
    if not arr:
        return total
    else:
        return sum_recursively(arr[1:],total+arr[0])

def recursive_sum(arr):
    """Return sum of numbers in arr. Works for empty lists too."""
    if not arr:           # base case: empty list
        return 0
    return arr[0] + recursive_sum(arr[1:])

def sum_array_recursively(arr):
    if not arr:
        return 0
    return arr[0]+sum(arr[1:])

# print(sum_array_recursively([1,2,3,4,5]))

def count_items(items):
    if not items:
        return 0
    else:
        return 1+count_items(items[1:])
    
# Write a recursive function to find the maximum number in a list
def max_number(arr):
    if len(arr) ==1:
        return arr[0]
    else:
        sub_max = max_number(arr[1:])
        return arr[0] if sub_max<arr[0] else sub_max
    
print(f"maximum number is {max_number([7,20,56,34])}")

# binary search using divide and conquer in a recursive form
# base case when low = high return  
def binary_search(arr, val, low=0, high=None):
    if high is None:
        high = len(arr)-1
    if low>high:
        return False
    mid = (low+high)//2
    if arr[mid] == val:
        return True
    elif val<arr[mid]:
        return binary_search(arr,val,low,mid-1)
    else:
        return binary_search(arr,val,mid+1,high)

    
    
print(binary_search([1,2,3,4,5,6,7,8,9,10,11,12], 8))