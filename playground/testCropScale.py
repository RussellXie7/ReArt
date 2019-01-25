import subprocess
import sys

def main():
	print "reached1"
	x = 1
	subprocess.call([sys.executable, 'CropScale.py', '%d' % x])
	print "reached2"

if __name__ == '__main__':
	main()
