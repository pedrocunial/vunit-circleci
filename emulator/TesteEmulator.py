# Testador de emulação
# Luciano Soares

import sys, getopt
import unittest

class TesteAssembly(unittest.TestCase):

	path = "assembly/"
	debug = False

	def setUp(self):
		pass

	def test_Abs(self):
		teste(self.path+"ram_out2.mif", self.path+"testeAbs1.txt", self.debug)

	def test_Div(self):
		teste(self.path+"ram_out2.mif", self.path+"testeAbs1.txt", self.debug)

	def test_Factorial(self):
		teste(self.path+"ram_out2.mif", self.path+"testeAbs1.txt", self.debug)


def parametros(argv):
	resultado = ''
	teste = ''
	debug = False
	try:
		opts, args = getopt.getopt(argv[1:],"hdr:t:",["help","debug","resultado=","teste="])
	except getopt.GetoptError:
		print(argv[0]+" -r <arquivo_com_resultado> -t <arquivo_com_teste>")
		sys.exit(2)
	for opt, arg in opts:
		if opt in ("-h","--help"):
			print(argv[0]+" -r <arquivo_com_resultado> -t <arquivo_com_teste>")
			sys.exit()
		if opt in ("-d","--debug"):
			debug = True
		elif opt in ("-r","--resultado"):
			resultado = arg
		elif opt in ("-t","--teste"):
			teste = arg
	return resultado, teste, debug

def teste(resultado, teste, debug):

	ram = {}
	validacao = {}

	# rotina de leitura do resultado da emulação
	with open(resultado, 'r') as arquivo:
		linhas = arquivo.read().splitlines()

		for linha in linhas:
			alocacao = linha.split(":")
			ram[int(alocacao[0].strip())] = int("0b"+alocacao[1].strip(),2)
		
		if debug:
			print("RAM")
			for e,v in ram.items():
				print("|{0}|  =>  |{1:016b}|".format(e,v))
			print("\n")

	# rotina do teste da emulação
	with open(teste, 'r') as arquivo:
		linhas = arquivo.read().splitlines()

		for linha in linhas:
			alocacao = linha.split(":")
			validacao[int(alocacao[0].strip())] = int("0b"+alocacao[1].strip(),2)
		
		if debug:
			print("Teste")
			for e,v in validacao.items():
				print("|{0}|  =>  |{1:016b}|".format(e,v))
			print("\n")

		for e,v in validacao.items():
			assert (v==ram[e]),"Erro RAM[{0}]={1:016b}, valor esperado ({2:016b})".format(e,ram[e],v)	

if __name__ == '__main__':
    #teste(parametros(sys.argv))
	suite = unittest.TestLoader().loadTestsFromTestCase(TesteAssembly)
	unittest.TextTestRunner(verbosity=3).run(suite)
	
