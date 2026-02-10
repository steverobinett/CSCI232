HASH_TABLE_SIZE = 11
def main():


    hash_table = [None] * HASH_TABLE_SIZE
    
    values = [73, 91, 33, 194]#73 and 194 will collide on 7
    print(73%HASH_TABLE_SIZE)
    
    hash_table[hash_function(values[0])] = values[0]
    i =0
    for i in range(len(values)):
        hash_table[hash_function(values[i])] = values[i]
        
    
 
    print(hash_table)
def hash_function(key): 
     return key % HASH_TABLE_SIZE
 
    
main()

