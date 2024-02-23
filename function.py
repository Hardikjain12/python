def sum(a,b):
    s = a+b
    return s
# print(sum(84,4))

def avg(a,b,c):
    average = (a+b+c)/3
    return average
# print(avg(45,4,2)) 

cities = ["delhi","mumbai","abudabi","jaipur","gurgaon","chandigharh"]
def print_len(list):
    print(len(list))   
# print_len(cities)

def print_list(list):
    for item in list:
        print(item , end = "     ")
# print_list(cities)


n = int(input("enter number to calculate factorial : "))
# n = 5
def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i 
    print(fact) 

factorial(n)