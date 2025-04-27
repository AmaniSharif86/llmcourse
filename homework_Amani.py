# function list_stats(nums: list[int]) -> dict that takes a list of integers
# and returns a dictionary with keys: 

def list_stats(nums:list[int]) ->dict:
    sum=0
    max=min=nums[0]
    for i in range(len(nums)):
        sum+=nums[i-1]
    if nums[i]<min:
        min=nums[i]
    if nums[i]> max:
        max=nums[i]
    
    mean=sum/len(nums)
    dict={'min':min,'max':max,'mean':mean,'sum':sum}
    return dict
#l=[2,5,1,8]
d=list_stats([2,5,1,8])
print (d)
########################################
def fact(n):   
    if n ==1:
        return 1 
    else:
        return n * fact(n - 1)
print( fact(5))
######################################
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 2) + fib(n - 1)
print(fib(6))
#################################3
def calculate(opera: str, *args: float) ->float:
    if opera=='div':
        try:
             return args[0] /args[1]
        except ZeroDivisionError as e:
            print("Got an error -->ZeroDivisionError")
    #if opera=='add':
print (calculate('div',10,0))


