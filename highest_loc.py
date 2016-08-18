import csv
with open('loc_projects.csv','r') as csvfile:
	reader = csv.reader(csvfile, delimiter='\t')
	loc_max=0
	max_data=[]
	for row in reader:
		for r in row:
			if r.isdigit():
				a=int(r)
		print a
		if loc_max<a:
			print loc_max,"  ",a
			loc_max=a
			max_data=row
			pass
	print max_data
	print loc_max

