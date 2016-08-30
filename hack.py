from subprocess import Popen, PIPE
import json
import csv

p = Popen("python new11.py", stderr=PIPE, stdout=PIPE, shell=True)
output, errors = p.communicate()
print  [errors, output]
result=[]
if output=="":
	if errors.index("\n")>0:
		er=errors.split("\n")
		result.extend(er)
	else:
		result.append(errors.split("\n"))
	pass
else:
	result.append(output)
print result
with open('ouput.csv', 'wb') as csvfile:
	writer = csv.writer(csvfile, quotechar=" ", quoting=csv.QUOTE_MINIMAL)
	writer.writerow(["output"])
	for res in result:
		writer.writerow([res])
file = open("newfile.txt", "w")
file.write(output)
file.write(errors)
file.close()