from collections import defaultdict
with open("outputplwanted.csv", 'r') as infile:
	table = []
	counter = 0
	top_pl_data = defaultdict()
	pl_rows = defaultdict()
	print("reading")
	for line in infile:
		if counter == 0:
			counter+=1
			continue

		else:
			l = line.replace(" ", "").replace("\n", "")
			s = [item for item in l.split(",")]
			s2 = [int(item) for item in s[1:]]
			pl_rows[s[1]] = s2
			table.append(s2)
			top_pl_data[sum(s2)] = s[0]
	sorted_values = sorted(top_pl_data.keys())
	for value in sorted_values[-11:-1]:
		print("%s - %i" %(top_pl_data[value], value))
print(len(table))
print(len(table[0]))
with open("outfileplwanted.csv", 'w') as outfile:
	for i in range(len(table[0])):
		s = ""
		for j in range(len(table)):
			s += str(table[i][j])+","
		outfile.write(s+"\n")

