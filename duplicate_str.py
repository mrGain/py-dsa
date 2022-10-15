# Using linear search
def duplicateChar(_str):
    dup = []
    _str = list(_str)
    for i in range(len(_str)):
        count = 1
        for j in range(i+1,len(_str)):
            if _str[i] != 0 and _str[i] == _str[j]:
                count += 1
                _str[j] = 0
        if count>1:        
            dup.append((_str[i], count))        
    
    return dup

# Using hash table


_str = "banjarahilll"
print(duplicateChar(_str))
