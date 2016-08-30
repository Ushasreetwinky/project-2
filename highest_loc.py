import csv
import json
from flask import Flask, render_template, request
import subprocess
import subprocess
import sys


def max_loc_data(*temp):
	#s1_out = subprocess.check_output([sys.executable, "project_details.py", "34"])
	#print s1_out
	#s2_out = subprocess.check_output([sys.executable, "loc.py", "34"])
	#print s2_out
	with open('loc_projects.csv','r') as csvfile:
		reader = csv.reader(csvfile, delimiter='\t')
		loc_max=0
		max_data=[]
		max_5=[[],[],[],[],[]]
		loc_5=[0,0,0,0,0]
		print len(loc_5)
		#a= [[int(ro) for ro in row if ro.isdigit()] for row in reader]
		for row in reader:
			for r in row:
				if r.isdigit():
					a=int(r)
			if all(i >= a for i in loc_5):
				pass
			else:
				min_val=min(loc_5)
				index=loc_5.index(min_val)
				loc_5[index]=a
				max_5[index]=row
				
			if loc_max<a:
				#print loc_max,"  ",a
				loc_max=a
				max_data=row
				pass
		print max_5
		print loc_5
		completedata=[]
		i=2
		language=[]
		number_of_lines=[]
		while i<len(max_data)-1:
			_data=[]
			_data.append(max_data[0])
			_data.append(max_data[1].replace("-"," "))
			_data.append(max_data[i].replace(":",""))
			_data.append(int(max_data[i+1]))
			i+=2
			completedata.append(_data)
			pass
		with open('loc.csv', 'wb') as csvfile:
			writer = csv.DictWriter(csvfile, fieldnames = ["name", "project", "language","loc"])
			writer.writerow({'name': "name", 'project': "project", 'language': "language",'loc':"loc"})
			writer.writerows({'name': row[0], 'project': row[1], 'language': row[2],'loc':row[3] } for row in completedata)
		return  json.dumps(completedata)
	#return render_template("loc_plot.html",dataset=completedata)

	
max_loc_data()