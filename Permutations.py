from itertools import permutations
import cProfile

#
#make permutation of array 
#

list = [1,2,3,4]

listPermutations =  permutations(list)
for permutation in listPermutations:
    print(permutation)
    
#
#count number of permutations
#

listPermutations =  permutations(list)
count = 0 
for permutation in listPermutations:
    count += 1
print(len(list), count)

#
#check the performance and undestand 
# how fast the space of permutations grows
#

def faculty(n):
    if n <= 1:
        return n
    else:
        return faculty(n-1)+n 
    
    
def counter(n):
    count = 0 
    for i in range(n):
        count += 1
        
    return count    


cProfile.run("counter(faculty(10))")