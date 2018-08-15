#algorithm answer to this question
# what is the smallest value of n such that an alorithm whose running time is 100n^2 runs faster than an algorithm
#time is 2^n on the same machine.set the value of n either by collecting user input or assigning it yourself

n = int(input("Enter the value of n: "))# i will collect user input
#n = 15; # set n to 15


test1 = 100 *(n**2)#to test 100n^2
test2 = (2**n)#To set test  2^n

    #create an conditional statement to determine the answer
if test1 < test2 and n == 15:
    print(test1, "It is the smallest value")
  
elif test1 < test2:
    print(test1, "100n^2 is faster than 2n^2 but",n,"is not the smallest value try again")
      
else:
    print("The values of 100n^2: ", test1, "and test2: ",test2)
    print("2n^2 is greater than 100n^2,try again")
      

