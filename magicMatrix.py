nString=input("enter n value..: ")
n=int(nString)
matrix=[[0 for x in range(n)] for y in range(n)]
if(n%2!=0):
    start=int(n/2)
    value=1
    count=0
    j=0
    while(count<=n*n-1):
        if(matrix[j][start]==0):
            matrix[j][start]=value
            start = (start + 1) % n
            j = (j + n + n - 1) % n
            value=value+1
            count=count+1
        else:
            start=(start+n-1)%n
            j=(j+n-1)%n
    for i in range(0,n):
        print(matrix)
if(n%4==0):
    quo=int(n/4)
    for i in range(0,quo):
        for j in range(0, quo):
            matrix[i][j]=i*n+j+1
    for i in range(0, quo):
        for j in range(n-quo,n):
            matrix[i][j]=i*n+j+1
    for i in range(n-quo, n):
        for j in range(0,quo):
            matrix[i][j]=i*n+j+1
    for i in range(n-quo, n):
        for j in range(n-quo,n):
            matrix[i][j]=i*n+j+1
    for i in range(quo, n-quo):
        for j in range(quo,n-quo):
            matrix[i][j]=i*n+j+1
    for i in range(0,n):
        for j in range(0, n):
            if(matrix[i][j]==0):
                matrix[i][j]=n*n-i*n-j
    for i in range(0,n):
        print(matrix[i])