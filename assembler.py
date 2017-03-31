
import subprocess
import loadTestes

def assembler():
	
	subprocess.call(['mkdir', 'machine_code'])

	nomes_testes = loadTestes.testes("testes.txt")

	for i in nomes_testes:
		subprocess.call(['java', '-jar', 'emulator/AssemblerZ0.jar',
			"assembly/{0}.nasm".format(i),"-o","machine_code/{0}.hack".format(i)])

if __name__ == '__main__':
	assembler()

