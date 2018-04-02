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
        if row['Country'] != 'NA':
            row_data = row['Country']
            try:
                table[row_data] += 1
                total += 1
            except:
                table[row_data] = 1
                total += 1
   
    #with open('outputGender.csv', 'w') as outfile:
    print(total)
    other = 0
    for row_key in table.keys():
        row = '{:^5}'.format("")
        if table[row_key]/total > 0.01:
            print(row_key)
            print(table[row_key]/total)
        else: 
            other += table[row_key]
    print("Other")
    print(other/total)
        # header = table[row_key].keys()

