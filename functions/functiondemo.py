# builtin functions (predefined functions)



# print()
# range()
# type()



# sum=0
# for i in range(1,11):
#     sum+=i
# print(sum)



# total=sum(range(1,101))
# print(total)



# print
# range
# type
# sum



# low=min(range(34,50))
# print(low)



# def cube_num(num):
#     res=num**3
#     return res
# print(cube_num(3))




# def add_nums(n1,n2):
#     return n1+n2
# print(add_nums(10,20))




# def sub_nums(n1,n2):
#     return n1-n2
# print(sub_nums(10,5))




# def smart_sub(n1,n2):
#     if n1>n2:
#         return n1-n2
#     else:
#         return n2-n1
# print(smart_sub(5,10))



# def smart_sub(n1,n2):
#     return n1-n2 if n1>n2 else n2-n1            # Known as ternary operator
# print(smart_sub(5,10))




# def odd_even(n):
#     return "Even" if n%2==0 else "Odd"
# print(odd_even(7))




# startswith

# name="luminar"
# print(name.startswith("l"))



#
#
# def is_starts_witha(name):
#     return name.startswith("a")


# name="technolab"
# print(name.endswith("lab"))

# def validate_gmail(email):
#     return email.endswith("@gmail.com")
# print(validate_gmail("abc@gmail.com"))


# create a function that will return factorial of a given number

# def factorial(n):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#     return fact
# print(factorial(4))



#q1 create a function is prime(num) will return true if number is prime else return false


# def prime(num):
#     for i in range(2,num):
#         if num%i==0:
#             return False                               #here True and Flase doesnt need "" because they are boolean operations
#             break
#     else:
#         return True
# print(prime(7))

#q2 create a function prime_range(low,upp) return all prime numbers between low to upper

def prime_range(low,upp):
    for i in range(low,upp+1):
        if i>1:
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                print(i)
print(prime_range(5,15))


#          lambda function
#
# def sub_nums(n1,n2):
#     return n1-n2
# print(sub_nums(10,5))

#        instead

# sub=lambda n1,n2:n1-n2
# print(sub(10,5))

# find cube of a number

# cube=lambda n:n**3
# print(cube(2))



# def max_two(n1,n2):
#     return n1 if n1>n2 else n2
# print(max_two(2,3))


# max_two=lambda n1,n2:n1 if n1>n2 else n2
# print(max_two(2,3))

# smart_sub=lambda n1,n2:n1-n2 if n1>n2 else n2-n1
# print(smart_sub(1,3))