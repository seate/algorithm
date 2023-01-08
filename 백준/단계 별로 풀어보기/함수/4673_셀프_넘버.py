def solve():
    def self_num(n):
        num_save = n
        
        while 0 < n:
            num_save += n % 10
            n //= 10
        
        return num_save
    
    nums = [None] * 10036
    for again1 in range(10000): nums[self_num(again1)] = 1
    for again2 in range(10000):
        if nums[again2] == None: print(again2)
    
if "__main__" == __name__: solve()