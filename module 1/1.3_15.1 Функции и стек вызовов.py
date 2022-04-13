"""
C(n, 0) = 1,
k > n, то C(n, k) = 0,
C(n, k) = C(n - 1, k) + C(n - 1, k - 1)

Enter:
n и k (1 ≤ n ≤ 10, 0 ≤ k ≤ 10)
Return:
C(n, k)

Sample Input 1:
3 2
Sample Output 1:
3

Sample Input 2:
10 5
Sample Output 2:
252
"""



def combination(n, k):
    if k == 0:
        return 1
    elif k > n:
        return 0
    return combination(n - 1, k) + combination(n - 1, k - 1)

def main():
    n, k = map(int, input().split())
    print(combination(n, k))



if __name__ == '__main__':
    main()