import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    vertical, horizontal = IP()
    chess_in = [input().rstrip() for i in range(vertical)]
    result = float("inf")
    
    for start_y in range(vertical - 7):
        for start_x in range(horizontal - 7):
            w_count = 0; b_count = 0
            for y in range(start_y, start_y + 8):
                for x in range(start_x, start_x + 8):
                    pl = (y & 1 == x & 1)
                    if chess_in[y][x] == 'W':
                        w_count += not pl
                        b_count += pl
                    else:
                        w_count += pl
                        b_count += not pl
            result = min(result, w_count, b_count)
    
    print(result)
    
if "__main__" == __name__: solve()