import csv
from collections import defaultdict

data = []
header = []
line_count = 0
table = defaultdict(dict)

"""
Relationships
problem solving and job satisfaction
coding language and job satisfaction
job security and job satisfaction


"""


with open('survey_results_public.csv', 'r') as infile:
	reader = csv.DictReader(infile)
	for row in reader:
		if row['ProblemSolving'] != 'NA' and row['JobSatisfaction'] != 'NA':
			row_data = row['ProblemSolving']
			column_data = row['JobSatisfaction']
			try:
				table[row_data][column_data] += 1
			except:
				table[row_data][column_data] = 1
			"""
			row['HaveWorkedLanguage'].split(',')
			if ';' in row['HaveWorkedLanguage']:
				column_data = row['HaveWorkedLanguage'].split(';')
				for item in column_data:
					try:
						table[row_data][item] += 1
					except:
						table[row_data][item] = 1

			else:
				column_data = row['HaveWorkedLanguage']
				try:
					table[row_data][column_data] += 1
				except:
					table[row_data][column_data] = 1
			"""
with open('output.csv', 'w') as outfile:
	for row_key in table.keys():
		#print(row_key)
		row = '{:^5}'.format("")
		header = table[row_key].keys()
		for key in sorted(table[row_key].keys()):
			row = ",".join([row, '{:^5}'.format(key)])
		outfile.write(row+'\n')
		break

	for row_key in table.keys():
		#print(row_key)
		row = '{:^5}'.format(row_key)
		for key in header:
			try:
				row = ",".join([row, '{:^5}'.format(table[row_key][key])])
			except:
				row = ",".join([row, '{:^5}'.format("NA")])
		outfile.write(row+'\n')
		
	"""
	for line in infile:
		if line_count == 0:
			header = line.split(',')
			line_count += 1
		else:
			split_line = line.split(',')
			row = dict()
			print(len(header))
			print(len(split_line))
			for i in range(len(split_line)):
				row[header[i]] = split_line[i]
			data.append(row)
	"""
