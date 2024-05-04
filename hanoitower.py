def hanoi_tower(num_block:int, col1:int=1, col2:int=2, col3:int=3):
    if num_block==1: print(col1, col3)
    else:
        hanoi_tower(num_block-1, col1, col3, col2)
        print(col1, col3)
        hanoi_tower(num_block-1, col2, col1, col3)

n = 5
print(2**n-1)
hanoi_tower(n)