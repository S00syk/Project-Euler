sum_set = set()#final set
for n in range(1,10000):
    if(len(set(digit for digit in str(n))) == len(str(n))):
        for x in range(2,n):
            if n % x == 0:
                full_set = set(digit for digit in str(n)).union(set(dig for dig in str(x)))
                full_set = full_set.union(set(dig for dig in str(n//x)))
                if(len(full_set)==9 and '0' not in full_set):
                    sum_set.add(n)
                    print(sum_set)
print(sum(sum_set),sum_set)
input()