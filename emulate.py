
import subprocess
import loadTestes

def emulate():

	nomes_testes = loadTestes.testes("testes.txt")

	for i in nomes_testes:
		error_code = subprocess.call(['java', '-jar', 'emulator/Elemulator.jar',
			"machine_code/{0}.hack".format(i),"-i","test/{0}_in.mif".format(i),"-o","machine_code/{0}_out.mif".format(i),"-c","1000"])
		if(error_code!=0):
			exit(error_code)

if __name__ == '__main__':
	emulate()

