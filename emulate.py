
import subprocess


def emulate():
	subprocess.call(['java', '-jar', 'emulator/Elemulator.jar',"machine_code/Abs2.hack","-i","assembly/ram_in.mif","-o","machine_code/ram_out2.mif","-c","1000"])

if __name__ == '__main__':
	emulate()
