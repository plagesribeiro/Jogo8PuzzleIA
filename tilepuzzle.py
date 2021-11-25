import puzzle 
import sys
import searches

size = input("Digite o tamanho da tabela do jogo: ")
numPermutacao = input("Digite o numero de movimentos para embaralhar o jogo: ")
t=puzzle.TilePuzzle(int(size))
t.permute(int(numPermutacao))
t.printPuzzle()
s=searches.Search(t)

movBuscaGulosa0 = str(s.busca_gulosa(0))
print("Busca Gulosa 0: "+str(len(movBuscaGulosa0))+" movimentos. "+movBuscaGulosa0)

movBuscaGulosa1 = str(s.busca_gulosa(1))
print("Busca Gulosa 1: "+str(len(movBuscaGulosa1))+" movimentos. "+movBuscaGulosa1)

movAlgA0 = str(s.busca_a(0))
print("Algoritmo A* 0: "+str(len(movAlgA0))+" movimentos. "+movAlgA0)

movAlgA1 = str(s.busca_a(1))
print("Algoritmo A* 1: "+str(len(movAlgA1))+" movimentos. "+movAlgA1)