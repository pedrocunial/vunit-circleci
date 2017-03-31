
import subprocess


def assembler():
	subprocess.call(['mkdir', 'machine_code'])
	subprocess.call(['java', '-jar', 'emulator/AssemblerZ0.jar',"assembly/Abs2.nasm","-o","machine_code/Abs2.hack"])

if __name__ == '__main__':
	assembler()

