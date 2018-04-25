#amrine_cleaning.py
import csv
from collections import defaultdict
def bin_search(_list, val, l_index, r_index):
        _val = _list[(r_index+l_index)//2]
        #print(_list[int((r_index+l_index)/2)])
        if(l_index <= r_index):
            if _val >= val and val > (_val-10000):
                return (r_index+l_index)//2
            elif _val > val:
                return bin_search(_list, val, l_index, (l_index + r_index)//2-1)
            elif _val < val:
                return bin_search(_list, val, (l_index + r_index)//2+1, r_index)
        else:
        	return len(_list)-1

def try_parse_e(string):
	split_val = string.split("e")
	ret_val = split_val[0]
	if len(split_val) > 1:
		first_digit = int(split_val[0])
		tens = int(split_val[1])

		ret_val = first_digit * (10**tens)


	return ret_val


def try_parse_dec(string):
	split_val = string.split(".")
	ret_val = int(split_val[0][0])*(10**(len(split_val[0])-1))
	return ret_val

outlist = []
"""
keys = ['Race', 'Gender', 'Country', 'MajorUndergrad', \
		'DeveloperType', 'CompetePeers', 'CompanySize', 'CompanyType', 'JobSatisfaction',\
		'Salary', 'ExpectedSalary']
"""
#'ProgramHobby', 'HomeRemote', 'YearsProgram',
keys = ['Race', 'Gender', 'Country', 'MajorUndergrad', 'DeveloperType', \
		'CompetePeers', 'CompanySize', 'CompanyType', 'JobSatisfaction',\
		'Salary', "ContinueWorkingLanguage", "LearnNewLanguage",  \
		'WorkStart', 'Overpaid', 'ChangeWorld', 'ChallengeMyself', 'CheckInCode',\
		'HomeRemote', 'YearsProgram', "FormalEducation"]
language_keys = set(["PHP", "Perl", "Python", "SQL",\
"Swift", "TypeScript", "C", "C#", "C++", "Java", "JavaScript", "Other"])
language_keys2 = set()
data_science_types = set(["Data scientist", "Machine learning specialist", "Developer with a statistics or mathematics background"])
developer_types = set(["Mobile developer", "Desktop applications developer", "DevOps specialist","Database administrator","Systems administrator"])

min_salary = 10**100
max_salary = 0

index = 0
with open('survey_results_public.csv', 'r') as infile:
	reader = csv.DictReader(infile)
	ExpectedSalaryCount = 0
	SalaryCount = 0
	for row in reader:
        # Clean dev type
		if row["DeveloperType"] != "NA":
			row["DeveloperType"] = row["DeveloperType"].split(";")[0]
        # parse out salary
		if row["Salary"] != "NA":
			SalaryCount += 1
			if "e" in row["Salary"]:
				row["Salary"] = try_parse_e(row["Salary"])
				#
			elif "." in row["Salary"]:
				row["Salary"] = try_parse_dec(row["Salary"])

			min_salary = min(int(float(row["Salary"])), min_salary)
			max_salary = max(int(float(row["Salary"])), max_salary)
        # parse out expected salary
		if row["ExpectedSalary"] != "NA":
			ExpectedSalaryCount += 1
			if "e" in row["ExpectedSalary"]:
				row["ExpectedSalary"] = try_parse_e(row["ExpectedSalary"])
			elif "." in row["ExpectedSalary"]:
				row["ExpectedSalary"] = try_parse_dec(row["ExpectedSalary"])

			min_salary = min(int(float(row["ExpectedSalary"])), min_salary)
			max_salary = max(int(float(row["ExpectedSalary"])), max_salary)
        # assigns single gender as either gender conforming or nonbinary
		if "Female" in row["Gender"]: row["Gender"] = "Female"
		elif "Male" in row["Gender"]: row["Gender"] = "Male"
		elif "NA" in row["Gender"]: row["Gender"] = ""
		else: row["Gender"] = "Nonbinary"

		if row["DeveloperType"] != "NA":
			split_row = row["DeveloperType"].replace(",","").split(";")
			for dev_type in split_row:
				# print("%s - %s " %(row["WebDeveloperType"], dev_type))
				if dev_type == "Web developer" and row["WebDeveloperType"] != "NA":
					row["DeveloperType"] = row["WebDeveloperType"].replace(" ", "").replace(",","").split(";")[0]
					break
				elif dev_type in developer_types:
					row["DeveloperType"] = row["DeveloperType"].replace(" ", "").replace(",","").split(";")[0]
					break
				elif dev_type in data_science_types:
					row["DeveloperType"] = "DataScientist"
				else:
					row["DeveloperType"] = "Other"
					break

		if row["HaveWorkedLanguage"] != "NA" and row["WantWorkLanguage"] != "NA":
			split_have_languages = row["HaveWorkedLanguage"].replace(" ", "").replace(",","").split(";")
			split_want_languages = row["WantWorkLanguage"].replace(" ", "").replace(",","").split(";")
			continue_working_language = False
			learn_new_language = False

			for language in split_have_languages:
				if language in split_want_languages:
					continue_working_language = True
					break

			for language in split_want_languages:
				if language not in split_have_languages:
					learn_new_language = True
					break

			if continue_working_language: row["ContinueWorkingLanguage"] = 1
			else: row["ContinueWorkingLanguage"] = 0
			if learn_new_language: row["LearnNewLanguage"] = 1
			else: row["LearnNewLanguage"] = 0

		if row["Race"] == "": row["Race"] = ""
		"""
		if row["HaveWorkedLanguage"] != "NA":
			split_languages = row["HaveWorkedLanguage"].replace(" ", "").replace(",","").split(";")
			for language in split_languages:
				if language in language_keys:
					language_keys2.add("Have%s"%language)
					row["Have%s"%language] = 1
				else:
					language_keys2.add("HaveOther")
					row["HaveOther"] = 1

		if row["WantWorkLanguage"] != "NA":
			split_languages = row["WantWorkLanguage"].replace(" ", "").replace(",","").split(";")
			for language in split_languages:
				if language in language_keys:
					language_keys2.add("Want%s"%language)
					row["Want%s"%language] = 1
				else:
					language_keys2.add("WantOther")
					row["WantOther"] = 1
		"""
		for key in row.keys():
			#if row[key] == "NA" or row[key] == "I don't know" or row[key] == "I prefer not to say":
			if row[key] == "I don't know" or row[key] == "I prefer not to say" or row[key] == "NA":
				row[key] = ""

		outlist.append(row)
"""
for key in language_keys2:
	keys.append(key)
"""
salary_brackets = [x*10000 for x in range(min_salary//10000, (max_salary//10000))]
salary_brackets.append(190000)
salary_brackets.append(200000)

salary_brackets_str = []

for i in range(len(salary_brackets)-1):
	salary_brackets_str.append("%i-%i" %(salary_brackets[i]+1, salary_brackets[i+1]))

sorted_keys = sorted(keys)
outlist_len = len(outlist)
with open('amrine_cleaned_survey_resultsv1.6.nullvals.csv', 'w') as outfile:
	outfile.write(" id ," + ",".join(sorted(keys)) + "\n")
	for i in range(outlist_len):
		writeRow = '%i' %i
		#print(i)
		for key in sorted_keys:
			if (key == "Salary" or key == "ExpectedSalary") and outlist[i][key] != "":
				index_of_bracket = bin_search(salary_brackets, int(outlist[i][key]), 0, len(salary_brackets))
				writeRow = ",".join([writeRow, salary_brackets_str[index_of_bracket-1]])

			else:
				try:
					writeRow = ",".join([writeRow, str(outlist[i][key]).replace(",", "")])
				except:
					if outlist[i]["HaveWorkedLanguage"] == "" and "Have" in key:
						writeRow = ",".join([writeRow, ""])
					elif outlist[i]["WantWorkLanguage"] == "" and "Want" in key:
						writeRow = ",".join([writeRow, ""])
					else:
						writeRow = ",".join([writeRow, "0"])
		if outlist[i]["JobSatisfaction"] != "":
			writeRow = "\n".join([writeRow, ''])
			outfile.write(writeRow)
