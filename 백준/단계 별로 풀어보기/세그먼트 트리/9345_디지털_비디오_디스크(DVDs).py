import sys
input = sys.stdin.readline
IP = lambda: map(int, input().split())

def solve():
    for T in range(int(input())):
        N, K = IP()
        m_tree = [0] * N + list(range(N))
        M_tree = [0] * N + list(range(N))
        
        for i in range(N - 1, 0, -1):
            m_tree[i] = m_tree[2 * i] if m_tree[2 * i] < m_tree[2 * i + 1] else m_tree[2 * i + 1]
            M_tree[i] = M_tree[2 * i] if M_tree[2 * i + 1] < M_tree[2 * i] else M_tree[2 * i + 1]
        
        for i in range(K):
            choise, initial_a, initial_b = IP()
            a = initial_a + N; b = initial_b + N
            
            if choise == 1:
                result_m = float("inf"); result_M = 0; b += 1
                
                while a < b:
                    if a & 1:
                        if m_tree[a] < result_m: result_m = m_tree[a]
                        if result_M < M_tree[a]: result_M = M_tree[a]
                        a += 1
                    
                    if b & 1:
                        b -= 1
                        if m_tree[b] < result_m: result_m = m_tree[b]
                        if result_M < M_tree[b]: result_M = M_tree[b]
                    a //= 2; b //= 2
                
                print("YES" if initial_a == result_m and initial_b == result_M else "NO")
            
            else:
                m_tree[a], m_tree[b] = m_tree[b], m_tree[a]
                M_tree[a], M_tree[b] = M_tree[b], M_tree[a]
                while a:
                    m_tree[a // 2] = m_tree[a] if m_tree[a] < m_tree[a ^ 1] else m_tree[a ^ 1]
                    M_tree[a // 2] = M_tree[a] if M_tree[a ^ 1] < M_tree[a] else M_tree[a ^ 1]
                    a //= 2
                
                while b:
                    m_tree[b // 2] = m_tree[b] if m_tree[b] < m_tree[b ^ 1] else m_tree[b ^ 1]
                    M_tree[b // 2] = M_tree[b] if M_tree[b ^ 1] < M_tree[b] else M_tree[b ^ 1]
                    b //= 2
    
if "__main__" == __name__: solve()