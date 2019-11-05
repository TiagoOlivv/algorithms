def lcs(a, b):
	# Valores de uma coluna
	tamLinha = len(a)
	tamColuna = len(b)

	# inicializa o matriz com zeros
	matriz = [ [0 for j in range(tamColuna + 1)] for i in range(tamLinha + 1)]


	# Comeca o laco dentro das linhas
	for i in range(0, tamLinha):

		# Comeca os lados pegando todas as colunas
		for j in range(0, tamColuna):
			# Pega os valores atuais da string e os compara
			atualLetraLinha = a[i]
			atualLetraColuna = b[j]

			# Se os valores atuais da string forem iguais
			# Eles adicionam na diagonal, somando um valore existente na matriz
			if atualLetraLinha == atualLetraColuna:
				matriz[i+1][j+1] = matriz[i][j] + 1
			else:
				# Caso nao conseguisse, a diagonal 
				# Eh o maximo entre o proxima linha na mesma coluna 
				# ou na proxima coluna na mesma linha
				matriz[i+1][j+1] = max(matriz[i+1][j], matriz[i][j+1])

	# Pega o ultimo valor da matriz
	# Que mostra a quantidade da maxima subsequencia.
	maximaSubSequencia = matriz[tamLinha][tamColuna]
	return str(maximaSubSequencia)

print(lcs("AGGasdasCAT", "asdfasfCATGGC"))

