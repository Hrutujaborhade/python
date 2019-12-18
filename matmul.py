a1=[[1,0,1],[2,1,1],[4,2,3]]
a2=[[1,1,2],[0,0,1],[4,1,5]]
re=[[0,0,0],[0,0,0],[0,0,0]]

for i in range (len(a1)):#counting row
    for j in range (len(a1[0])):#counting colmn
        for k in range (len(a2)):#counting colmn
            re[i][j]+=a1[i][k]*a2[k][j]
print("matrix 1 is: ")
for i in a1:
    print(i)
print("matrix 2 is: ")
for i in a2:
    print(i)
print("multiplication of matrices is :")
for i in re:
    print(i)
    
