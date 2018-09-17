from fuzzywuzzy import fuzz
import csv

with open('Documents/test_CSV_1.csv', 'r') as t1, open('Documents/test_CSV_2.csv', 'r') as t2:
   	fileone = t1.readlines()
	filetwo = t2.readlines()

with open('update.csv', 'w') as outFile:
	for i in fileone:
		for j in filetwo:
			outFile.write(i + j+ str(fuzz.ratio(i,j)) + ", " + "\n")
		

		





#print fuzz.ratio('Testing FuzzyWuzzy', 'Testing FuzzyWuzzy!!')
#print fuzz.partial_ratio('Testing FuzzyWuzzy', 'Testing FuzzyWuzzy!!') 
#print fuzz.token_sort_ratio('Testing FuzzyWuzzy', 'Testing FuzzyWuzzy!!')
#print fuzz.token_set_ratio('Testing FuzzyWuzzy', 'Testing FuzzyWuzzy!!')


