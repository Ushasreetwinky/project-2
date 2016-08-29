from subprocess import Popen, PIPE
import json

p = Popen("python new11.py", stderr=PIPE, stdout=PIPE, shell=True)
output, errors = p.communicate()
print  [errors, output]
file = open("newfile.txt", "w")
file.write(output)
file.write(errors)
file.close()