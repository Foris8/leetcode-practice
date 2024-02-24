def fuc(pwd):
    left_dict = {
        "0" : 0,
        "1" : 0
    }
    
    for i in pwd:
        left_dict[i] +=1
    
    count = 100000000
    
    right_dict = {
        "0": 0,
        "1": 0
    }
    
    for j in range(len(pwd) - 2, 0, -2):
        #update the right window dict
        left_dict[pwd[j]] -= 1
        left_dict[pwd[j+1]] -= 1
        
        right_dict[pwd[j]] += 1
        right_dict[pwd[j+1]] += 1
        
        count = min(count, min(left_dict["0"],left_dict["1"]) + min(right_dict["0"], right_dict["1"]))
        
    return count

pwd = "101011"
print(fuc(pwd))