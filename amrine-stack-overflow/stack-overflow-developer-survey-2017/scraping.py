import csv
from collections import defaultdict
import pandas

"""
Relationships

problem solving and job satisfaction
coding language and job satisfaction
job security and job satisfaction
"""

def parse_pl_have_worked_js(reader):
	data = []
	header = []
	line_count = 0
	table = defaultdict(dict)
	for row in reader:
		if row['HaveWorkedLanguage'] != 'NA' and row['JobSatisfaction'] != 'NA':
			print("found")
			row_data = row['HaveWorkedLanguage'].replace(" ", "")
			column_data = int(row['JobSatisfaction'])
			for language in row_data.split(";"):
				try:
					table[language][column_data] += 1
				except:
					table[language][column_data] = 1
	return table

def parse_pl_wanted_js(reader):
	data = []
	header = []
	line_count = 0
	table = defaultdict(dict)
	for row in reader:
		if row['WantWorkLanguage'] != 'NA' and row['JobSatisfaction'] != 'NA':
			row_data = row['WantWorkLanguage'].replace(" ", "")
			column_data = int(row['JobSatisfaction'])
			for language in row_data.split(";"):
				try:
					table[language][column_data] += 1
				except:
					table[language][column_data] = 1
	return table

def parse_gif_and_friends(reader):
	data = []
	header = []
	line_count = 0
	country_list = [""]
	table = defaultdict(dict)
	#table_dict = defaultdict(table)
	counter = 0
	for row in reader:

		if row['PronounceGIF'] != 'NA' and row['FriendsDevelopers'] != 'NA':
			counter += 1
			
			
			gif = row['PronounceGIF']
			friends = row['FriendsDevelopers']

			try:
				table[gif][friends] += 1
			except:
				table[gif][friends] = 1
			
	print(counter)
	return table

def parse_role_and_satisfaction(reader):
	data = []
	header = []
	line_count = 0
	country_list = [""]
	table = defaultdict(dict)
	ret_list = []
	#table_dict = defaultdict(table)
	counter = 0
	#satisfaction_table = defaultdict([])
	for row in reader:

		if row['DeveloperType'] != 'NA' and row['JobSatisfaction'] != 'NA':
			
			
			role_list = row['DeveloperType'].split(';')
			job_satisfaction = int(row['JobSatisfaction'])
			for role in role_list:
				try:
					table[job_satisfaction][role] += 1
				except:
					table[job_satisfaction][role] = 1
	return table

def parse_salary_and_satisfaction(reader, avg_salary):
	data = []
	header = []
	line_count = 0
	country_list = [""]
	table = defaultdict(dict)
	ret_list = []
	#table_dict = defaultdict(table)
	counter = 0
	#satisfaction_table = defaultdict([])
	for row in reader:

		if row["Salary"] != "NA" and 'e' not in row["Salary"]and row['JobSatisfaction'] != 'NA':
			
			
			sal = int(float(row["Salary"].replace(",","")))
			job_satisfaction = int(row['JobSatisfaction'])
	
			pay_grade = "Above Average"
			if sal < avg_salary:
				pay_grade = "Below Average"

			try:
				table[job_satisfaction][pay_grade] += 1
			except:
				table[job_satisfaction][pay_grade] = 1
	
	return table

def parse_nationality_and_gender(reader):
	data = []
	header = []
	line_count = 0
	country_list = [""]
	table = defaultdict(dict)
	counter = 0
	for row in reader:

		if row['Gender'] != 'NA' and row['JobSatisfaction'] != 'NA':
			counter += 1
			
			
			gender = row['Gender']
			country = row['Country']
			race = row['Race']
			job_satisfaction = int(row['JobSatisfaction'])
			job_satisfaction_str = "Unsatisfied"
			if job_satisfaction > 5:
				job_satisfaction_str = "Satisfied"
			
			try:
				table[job_satisfaction_str][country] += 1
			except:
				table[job_satisfaction_str][country] = 1
			
	print(counter)
	return table

def count_education_type(reader):
	table = defaultdict(dict)

	for row in reader:
		if row['FormalEducation'] != 'NA' and row['JobSatisfaction'] != 'NA':
			print("found")
			row_data = row['FormalEducation'].replace(" ", "")
			# column_data = int(row['JobSatisfaction'])
			for edu in row_data.split(";"):
				try:
					table[edu] += 1
				except:
					table[edu] = 1
				total+=1
	
	for key in sorted(table.keys()):
		table[key] /= total
	return table, sorted(table.keys())

def count_undergrad_major(reader):
	table = defaultdict(dict)

	for row in reader:
		if row['MajorUndergrad'] != 'NA' and row['JobSatisfaction'] != 'NA':
			print("found")
			row_data = row['MajorUndergrad'].replace(" ", "")
			# column_data = int(row['JobSatisfaction'])
			for major in row_data.split(";"):
				try:
					table[major] += 1
				except:
					table[major] = 1
				total+=1
	
	for key in sorted(table.keys()):
		table[key] /= total
	return table, sorted(table.keys())

def count_have_worked_languages
	table = defaultdict()

	for row in reader:
		if row['HaveWorkedLanguage'] != 'NA' and row['JobSatisfaction'] != 'NA':
			print("found")
			row_data = row['HaveWorkedLanguage'].replace(" ", "")
			# column_data = int(row['JobSatisfaction'])
			for language in row_data.split(";"):
				try:
					table[language] += 1
				except:
					table[language] = 1
					total+=1
	
	for key in sorted(table.keys()):
		table[key] /= total
	return table, sorted(table.keys())
	
avg_salary = 0
salary_Count = 0
with open('survey_results_public.csv', 'r') as infile:
	reader = csv.DictReader(infile)
	for row in reader:
		if row["Salary"] != "NA"and 'e' not in row["Salary"]:
			avg_salary += int(float(row["Salary"]))
			salary_Count += 1

avg_salary = avg_salary // salary_Count

with open('survey_results_public.csv', 'r') as infile:
	reader = csv.DictReader(infile)
	education_prob, education_headers = count_education_type(reader)
	infile.seek(0)
	undergrad_prob, undergrad_headers = count_undergrad_major(reader)
	infile.seek(0)
	language_prob, language_headers = count_have_worked_languages(reader)

with open('output_ungrad_count.csv', 'w') as outfile:
	row = '{:^5}'.format("")
	for key in undergrad_headers:
		row = ",".join([row, '{:^5}'.format(key)])
	outfile.write(row+'\n')

	for row_key in undergrad_headers:
		
		row = '{:^5}'.format(row_key)
		for key in header:
			try:
				row = ",".join([row, '{:^5}'.format(undergrad_prob[row_key][key])])
			except:
				row = ",".join([row, '{:^5}'.format("NA")])
		outfile.write(row+'\n')

with open('output_language_count.csv', 'w') as outfile:
	row = '{:^5}'.format("")
	for key in language_headers:
		row = ",".join([row, '{:^5}'.format(key)])
	outfile.write(row+'\n')

	for row_key in language_headers:
		
		row = '{:^5}'.format(row_key)
		for key in header:
			try:
				row = ",".join([row, '{:^5}'.format(table[row_key][key])])
			except:
				row = ",".join([row, '{:^5}'.format("NA")])
		outfile.write(row+'\n')

with open('output_education_type_count.csv', 'w') as outfile:
	row = '{:^5}'.format("")
	for key in education_headers:
		row = ",".join([row, '{:^5}'.format(key)])
	outfile.write(row+'\n')

	for row_key in education_headers:
		
		row = '{:^5}'.format(row_key)
		for key in header:

			row = ",".join([row, '{:^5}'.format(table[row_key][key])])

		outfile.write(row+'\n')
"""
with open('outputplworked.csv', 'w') as outfile:
	for row_key in table2.keys():
		
		row = '{:^5}'.format("")
		header = sorted(table2[row_key].keys())
		for key in sorted(table2[row_key].keys()):
			row = ",".join([row, '{:^5}'.format(key)])
		outfile.write(row+'\n')
		break

	for row_key in table2.keys():
		
		row = '{:^5}'.format(row_key)
		for key in header:
			try:
				row = ",".join([row, '{:^5}'.format(table2[row_key][key])])
			except:
				row = ",".join([row, '{:^5}'.format("NA")])
		outfile.write(row+'\n')
"""