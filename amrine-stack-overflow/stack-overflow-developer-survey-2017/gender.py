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
    total = 0
    for row in reader:
        if row['Gender'] != 'NA':
            row_data = row['Gender']
            
            if row_data.upper() != "MALE" and row_data.upper() != "FEMALE":
                row_data = "Other"
            try:
                table[row_data] += 1
                total += 1
                
            except:
                table[row_data] = 1
                total += 1
   
    #with open('outputGender.csv', 'w') as outfile:
    print(total)
    for row_key in table.keys():
        row = '{:^5}'.format("")
        print(row_key)
        print(table[row_key]/total)
        # header = table[row_key].keys()

