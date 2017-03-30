
import subprocess


def assembler():
	subprocess.call(['java', '-jar', 'emulator/AssemblerZ0.jar',"assembly/Abs2.nasm"])
	subprocess.call(['ls', "assembly"])

if __name__ == '__main__':
	assembler()

