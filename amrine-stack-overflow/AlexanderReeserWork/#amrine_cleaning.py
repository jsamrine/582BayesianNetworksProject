#amrine_cleaning.py
import csv
from collections import defaultdict
def bin_search(_list, val, l_index, r_index):
        _val = _list[(r_index+l_index)//2]
        #print(_list[int((r_index+l_index)/2)])
        if(l_index <= r_index):
            if _val >= val and val > (_val-10000):
                # print("Found match %i >= %i > %s" %(_val, val, (_val-10000)))
                # print("%i less than %i" %((r_index+l_index)//2, len(_list)))
                return (r_index+l_index)//2
            elif _val > val:
                # print("val val: %i is greater than target val: %i" %(_val, val))
                # print("recursing with l_index: %i and r_index: %i" %(l_index, int((l_index + r_index)/2)-1))
                return bin_search(_list, val, l_index, (l_index + r_index)//2-1)
            elif _val < val:
                # print("val val: %i is less than target val: %i" %(_val, val))
                # print("recursing with l_index: %i and r_index: %i" %(int((l_index + r_index)/2)+1, r_index))
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
keys = ['Race', 'Gender', 'Country', 'EducationTypes', 'MajorUndergrad', \
		'DeveloperType', 'CompetePeers', 'CompanySize', 'CompanyType', 'JobSatisfaction',\
		'Salary', 'ExpectedSalary']
min_salary = 10**100
max_salary = 0
gender_keys = ['male', 'female', 'nonbinary']
index = 0
with open('survey_results_public.csv', 'r') as infile:
	reader = csv.DictReader(infile)
	ExpectedSalaryCount = 0
	SalaryCount = 0
	for row in reader:
		# for key in row.keys():
		# 	print(key)
		if row["Salary"] != "NA":
			SalaryCount += 1

			if "e" in row["Salary"]:
				row["Salary"] = try_parse_e(row["Salary"])
				# 
			elif "." in row["Salary"]:
				row["Salary"] = try_parse_dec(row["Salary"])
			
			min_salary = min(int(float(row["Salary"])), min_salary)
			max_salary = max(int(float(row["Salary"])), max_salary)		
		if row["ExpectedSalary"] != "NA":
			ExpectedSalaryCount += 1
			if "e" in row["ExpectedSalary"]:
				row["ExpectedSalary"] = try_parse_e(row["ExpectedSalary"])
				
			elif "." in row["ExpectedSalary"]:
				row["ExpectedSalary"] = try_parse_dec(row["ExpectedSalary"])

			
			min_salary = min(int(float(row["ExpectedSalary"])), min_salary)
			max_salary = max(int(float(row["ExpectedSalary"])), max_salary)
		for gender in row["Gender"].split(";"):
			if "Female" in row["Gender"]:
				row["Gender"] = "Female"
			elif "Male" in row["Gender"]:
				row["Gender"] = "Male"
			else:
				row["Gender"] = "Nonbinary"
			break
			#if gender.lower() not in gender_keys:
				#row["Gender"] = "Nonbinary"
				
		
		outlist.append(row)
print(min_salary)
print(max_salary)
salary_brackets = [x*10000 for x in range(min_salary//10000, (max_salary//10000))]
print(salary_brackets[-1])
salary_brackets.append(190000)
salary_brackets.append(200000)

salary_brackets_str = []
#print(salary_brackets)
with open("salary_brackets.txt", 'w') as outfile:
	for i in range(len(salary_brackets)-1):
		salary_brackets_str.append("%i-%i" %(salary_brackets[i]+1, salary_brackets[i+1]))

		outfile.write("S_"+salary_brackets_str[-1]+"\n")
#	print(salary_brackets_str[-1])
# print(ExpectedSalaryCount)
# print(SalaryCount)
with open('amrine_cleaned_survey_resultsv1.1.csv', 'w') as outfile:
	outfile.write(" id ," + ",".join(sorted(keys)) + "\n")
	for i in range(len(outlist)):
		writeRow = '%i' %i
		#print(i)
		for key in sorted(keys):
			if (key == "Salary" or key == "ExpectedSalary") and outlist[i][key] != "NA":
				index_of_bracket = bin_search(salary_brackets, int(outlist[i][key]), 0, len(salary_brackets))
				print("Row: %i" %i)
				print("Salary %i with bracket %i is less then %i" %(int(outlist[i][key]), index_of_bracket, salary_brackets[index_of_bracket]))
				print("Salary %i goes in bracket: %s" %(int(outlist[i][key]), salary_brackets_str[index_of_bracket-1]))

				writeRow = ",".join([writeRow, salary_brackets_str[index_of_bracket-1]])

			else:
				writeRow = ",".join([writeRow, str(outlist[i][key]).replace(",", ";")])
		writeRow = "\n".join([writeRow, ''])
		outfile.write(writeRow)
