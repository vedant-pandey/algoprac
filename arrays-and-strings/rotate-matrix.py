def main() :
    
    n,m = map(int, input().split())
    mat = [[None for l in range(m)] for _ in range(n)]
    
    for i in range(n) :
        mat[i] = list(map(int, input().split()))
    
    m = len(mat[0])
    rotmat  = [[None for z in range(n)] for _ in range(m)]
    tempmat = [[None for x in range(n)] for _ in range(m)]

    for i in range(m) :
        for j in range(n) :
            tempmat[i][j] = mat[j][i]

    for i in range(m) :
        for j in range(n) :
            rotmat[i][j] = tempmat[i][n - j - 1]
    for i in range(m):
        print(rotmat[i])

if __name__ == "__main__":
    main()