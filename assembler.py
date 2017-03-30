
import subprocess


def assembler():
	subprocess.call(['java', '-jar', 'emulator/AssemblerZ0.jar',"assembly/Abs.nasm"])

if __name__ == '__main__':
	assembler()

