#write a program to check whether the array elements are prime no's or not ,if yes store that index value into another array and display index values.
def prime(n,primecount):
    for i in range(2,n):
        if n<=1:
            return False
        elif(n%i==0):
            primecount=primecount+1   
    if primecount==0:
        return True     
a=[2,5,3,13,7,8]
a2=[]
primecount=0
for i in range(len(a)):
    if (prime(a[i],primecount))==True:
        a2.append(i)
for i in range(len(a2)):
    print(a2[i])
         

