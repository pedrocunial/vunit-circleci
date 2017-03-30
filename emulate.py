
import subprocess


def emulate():
	subprocess.call(['java', '-jar', 'emulator/Elemulator.jar',"assembly/Abs2.hack","-i","emulator/ram_in.mif","-o","emulator/ram_out2.mif","-c","1000"])

if __name__ == '__main__':
	emulate()