def common_divisor(a,b):
    q=a/b
    r=a%b
    if r == 0: return b
    return common_divisor(b,r)
    
def prime(number=121,list_of_primes=range(2,122),iters=0):
    count=0
    done=len(list_of_primes[iters:])
    for i in list_of_primes[iters+1:]:
        if i%list_of_primes[iters]==0:
            list_of_primes.remove(i)
        else: count+=1
    if count == done: return list_of_primes
    return prime(number,list_of_primes,iters+1)

def hanoi(n=3, first=([3,2,1],"first"), second=([], "second"), third=([], "third")):
    if n > 0:
        hanoi(n - 1, first, third, second)
        if first[0]:
            disk = first[0].pop()
            print "move " + str(disk) + " from " + first[1] + " to " + third[1]
            third[0].append(disk)
        hanoi(n - 1, second, first, third)