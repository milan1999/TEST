#Function to find prime number till n
def seive(n):
    #list 'a' mark as prime or non-prime
    a=[]
    for i in range(n+1):
        #itilially all odd number and '2' marked as non-prime
        if(i%2==1 or i==2):
            a.append(1)
        else:
            a.append(0)
    i=3
    x=int(n**(0.5))
    #start from 3 to square-root(n) and mark its mutiples as non-prime
    while i<=x:
        #ingoring non-prime number as its factors already marked which it can
        if(a[i]==0):
            i+=2
            continue
        #starting from i-th multiples of i as lower than it already marked by lower values
        j=i
        y=n//i
        #ending is n/i as we requried prime number till n
        while j<=y:
            a[i*j]=0
            j+=2         #increase rate two as all even number already marked as non-prime
        i+=2      #same reason ^^
    #make a list called prime to store all prime number
    prime=[]
    for i in range (2,n+1):
        if(a[i]==1):
            prime.append(i)
    return prime    #return the list of prime number
n=int(input())
a=seive(n)
print(a)