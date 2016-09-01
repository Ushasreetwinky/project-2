from subprocess import Popen, PIPE
import json
import csv
import sys

def main(argv):
	print "argu received",argv[0]
	if argv[0]=="output.js":
		commandLine="node output.js"
		pass
	else:
		commandLine="python output.py"
	p = Popen(commandLine, stderr=PIPE, stdout=PIPE, shell=True)
	output, errors = p.communicate()
	result=[]
	if output=="":
		if errors!="":
			if argv[0]=="output.js":
				er=errors.split(errors[41])
				result.extend(er)
				pass
			elif errors.index("\n")>0:
				er=errors.split("\n")
				result.extend(er)
			else:
				result.append(errors.split("\n"))
		pass
	else:
		result.append(output)
	with open('ouput.csv', 'wb') as csvfile:
		writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
		writer.writerow(["output"])
		for res in result:
			writer.writerow([res])


if __name__ == "__main__":
   main(sys.argv[1:])