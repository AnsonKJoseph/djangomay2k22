# error handling

# try => block doubtful code
# except => block handling code  ( how to handle error )
# raise => key word custom error throw (  )
# finally => block clean up processing

# num1=int(input("Enter num 1: "))    # num1=10
# num2=int(input("Enter num 2: "))    # num2=0
# try:                                                      # we gave try here because we know an error can happen
#     res=num1/num2   # 10/0
#     print("Result =",res)
# except Exception as e:                                    # we gave except to how to handle the error
#     print(e)
# print("db transaction")
# print("file operation")



num1=int(input("Enter num 1: "))
num2=int(input("Enter num 2: "))

lst=[]
try:
    res=num1/num2
    print("Result =",res)
except Exception as e:
    num2=int(input("Enter value for num2: "))
    print(num1/num2)

try:
    a,*b=lst
except Exception as e:
    print(e)


finally:                          # finally is given that if any errors occur in the above program db transaction and file operation should execute
    print("db transactions")
    print("file operation")