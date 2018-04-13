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
    keys = ['Race', 'Gender', 'Country', 'EducationTypes', 'MajorUndergrad', 'DeveloperType', 'CompetePeers', 'CompanySize', 'CompanyType', 'JobSatisfaction']
    reader = csv.DictReader(infile)
    total = 0
    outGraph = []
    noNull = True
    for row in reader:
        noNull = True
        for key in keys:
            #if row[key] == 'NA':
            #    noNull = False
            if "," in row[key]:
                row[key] = row[key].replace(",", " ")
        if noNull:
            outGraph.append(row)
            
with open('full_cleaned_survey_results_public.csv', 'w') as outfile:   
    
    print(len(outGraph))
    for row in outGraph:
        writeRow = ''
        for key in keys:
            writeRow = ",".join([writeRow, row[key]])
        writeRow = "\n".join([writeRow, ''])
        outfile.write(writeRow)
            
            
    
    #with open('outputGender.csv', 'w') as outfile:
    print(total)
    for row_key in table.keys():
        row = '{:^5}'.format("")
        print(row_key)
        print(table[row_key]/total)
        # header = table[row_key].keys()

