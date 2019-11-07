def lcs(X, Y): 

    m, n = len(X), len(Y)
    L = [[0 for x in range(n+1)] for x in range(m+1)]
    
    for i in range(m+1): 
        for j in range(n+1): 
            if i == 0 or j == 0: 
                L[i][j] = 0
            elif X[i-1] == Y[j-1]: 
                L[i][j] = L[i-1][j-1] + 1
            else: 
                L[i][j] = max(L[i-1][j], L[i][j-1]) 

    index = L[m][n] 
    lcs = [""] * (index+1) 
    lcs[index] = "" 
    i, j = m, n 

    while i > 0 and j > 0: 
        if X[i-1] == Y[j-1]: 
            lcs[index-1] = X[i-1] 
            i-=1
            j-=1
            index-=1

        elif L[i-1][j] > L[i][j-1]: i-=1
        else: j-=1

    return L, L[m][n], "".join(lcs)

def matrix(a, b, mat, sec):

	print("  ", end = "  Y ")
	for x in b:
		print(x, end = " ")
	print("\n")

	for ix, i in enumerate(mat):

		if ix != 0:
			print(a[ix - 1], end = " | ")
			for jx, __ in enumerate(i):
				print(mat[ix][jx], end = " ")
				
		else:	
			print("", end = "X | ")
			for jx, __ in enumerate(i):
				print(mat[ix][jx], end = " ")
		print('\n')
		

if __name__ == "__main__":
    
	a, b = list("ABCB"), list("BDCAB")
	#a, b = list("ABCBDAB"), list("BDCABA")



	mat, score, sec = lcs(a, b)
	matrix(a, b, mat, sec)
	
				

	print("Sequência: ", sec)
	print("Size: ", score)
