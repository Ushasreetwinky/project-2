import os
import subprocess

os.system("git clone --depth 1 git@code.gramener.com:vijay.yellepeddi/DRL-Scorecard.git")
proc = subprocess.Popen(["cloc DRL-Scorecard"], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
print "program output:", out
op=out.split("\n")
data=[]
parsing = False
i=0
p=0
for line in op:
    if p>7:
        parsing = True
        if line.startswith("-"):
            parsing= False
    elif line.startswith("SUM") or line.startswith("--"):
        parsing = False
    if parsing:
        #print "code: ",len(code[i])
        language=line[0:line.find('  ')]
        code=line[line.rfind(' ')+1:len(line)]
        if(language!=""):
            data.append(language+":"+code)
        i=i+1
    p+=1

print data
