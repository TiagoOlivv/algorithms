parent = dict()

def make_set(vertice):
	parent[vertice] = vertice

# Retorna o primeiro elemento do conjunto, que inclui 'vertice'
def find_set(vertice):
	if parent[vertice] != vertice:
		parent[vertice] = find_set(parent[vertice])
	return parent[vertice]

# Junta dois conjuntos: conjunto que inclui 'vertice1' e 'vertice2'
def union(u, v, edges):
	ancestor1 = find_set(u)
	ancestor2 = find_set(v)
	# Se u e v nao estiverem conectados por um caminho
	if ancestor1 != ancestor2:
		for edge in edges:
			parent[ancestor1] = ancestor2


def kruskal(graph):
	mst = set()
	# Coloca todos os vertices em conjuntos separados
	for vertice in graph['V']:
		make_set(vertice)

	edges = list(graph['E'])
	# Classifica as arestas em ordem crescente
	edges.sort()
	for edge in edges:
		weight, u, v = edge
		# Verifica se a borda atual nao fecha o ciclo
		if find_set(u) != find_set(v):
			mst.add(edge)
			union(u, v, edges)

	return mst

# Grafo de entrada
graph = {
'V': ['1', '2', '3', '4', '5', '6', '7', '8'],
'E': set([
	(240, '1', '2'),
	(210, '1', '3'),
	(340, '1', '4'),
	(280, '1', '5'),
	(200, '1', '6'),
	(345, '1', '7'),
	(120, '1', '8'),
	(265, '2', '3'),
	(175, '2', '4'),
	(215, '2', '5'),
	(180, '2', '6'),
	(185, '2', '7'),
	(155, '2', '8'),
	(260, '3', '4'),
	(115, '3', '5'),
	(350, '3', '6'),
	(435, '3', '7'),
	(195, '3', '8'),
	(160, '4', '5'),
	(330, '4', '6'),
	(295, '4', '7'),
	(230, '4', '8'),
	(360, '5', '6'),
	(400, '5', '7'),
	(170, '5', '8'),
	(175, '6', '7'),
	(205, '6', '8'),
	(305, '7', '8'),
	])
}

print("Entrada:\n")
print(graph)

print("\n")
print("Saida:\n")

mst = kruskal(graph)
print("Arvore Geradora Minima:")
print(mst)
mst_weight = 0
for edge in mst:
	weight, u, v = edge
	mst_weight += weight

print("Custo: ")
print(mst_weight)