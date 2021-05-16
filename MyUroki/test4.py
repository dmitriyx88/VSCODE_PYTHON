Mat= [[1,2,3],[4,5,6],[7,8,9]]

Dia1=[Mat[i][i] for i in [0,1,2]]
Dia2=[Mat[i][len(Mat[i])-1-i] for i in [0,1,2]]


print(Mat)
print(Dia1)
print(Dia2)