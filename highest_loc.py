import csv
import json
from flask import Flask, render_template, request
import subprocess
import subprocess
import sys


def max_loc_data(*temp):
	s1_out = subprocess.check_output([sys.executable, "project_details.py", "34"])
	print s1_out
	s2_out = subprocess.check_output([sys.executable, "loc.py", "34"])
	print s2_out
	with open('loc_projects.csv','r') as csvfile:
		reader = csv.reader(csvfile, delimiter='\t')
		loc_max=0
		max_data=[]
		for row in reader:
			for r in row:
				if r.isdigit():
					a=int(r)
			#print a
			if loc_max<a:
				#print loc_max,"  ",a
				loc_max=a
				max_data=row
				pass
		completedata=[]
		completedata.append([max_data[0],max_data[1]])
		i=2
		language=[]
		number_of_lines=[]
		while i<len(max_data)-1:
			language.append(max_data[i].replace(":",""))
			number_of_lines.append(int(max_data[i+1]))
			i+=2
			pass
		completedata.append(language)
		completedata.append(number_of_lines)
		with open('data.txt', 'w') as outfile:
			json.dumps(completedata, outfile)
		print completedata
		return  json.dumps(completedata)
	#return render_template("loc_plot.html",dataset=completedata)

	
max_loc_data()