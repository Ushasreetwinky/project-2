import sys
import subprocess

def result(*temp):
	s2_out = subprocess.check_output([sys.executable, "new11.py", "34"])
	print s2_out
	return JSON.dumps(s2_out)