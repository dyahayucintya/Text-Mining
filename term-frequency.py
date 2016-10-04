from nltk.corpus import stopwords
from collections import Counter
import re
from collections import OrderedDict
import csv
from stemming.porter2 import stem

def readfile(namafile):
	input = open(namafile).read()
	input = input.lower()
	return input

def preprocessing(input):
	text = re.sub('<title>[^>]*>','', input) #cleartitle
	text = re.sub('<dateline>[^>]*>','', text) #cleardateline
	text = re.sub('<copyright>[^>]*>','', text) #clearcopyright
	text = re.sub('<(\w)*[^>]*>', '', text) #cleartag
	text = re.sub('&(\w*);', '', text) #clear &quot;
	text = re.sub('(\d)+(\.)*(\d)*', '', text) #cleardigit
	text =  re.sub('[/+@.,%-%^*"!#-$-\']', '', text) #clearsimbol
	cachedStopWords = stopwords.words("english")
	text = ' '.join([word for word in text.split() if word not in stopwords.words("english")]) #clearstopword
	text = [stem(word) for word in text.split(" ")]
	#text = re.split(r'(?<=[a-z])\ ', text) #utk split, ternyata stemming hasilnya udah ke split
	textcounter = Counter(text) #hitung frekuensi
	return  text

def main():
	listOfDocName = ['6146.xml','18586.xml','22170.xml', '22513.xml', '26642.xml', '26847.xml']
	print("List Of Documents name : ", listOfDocName)
	listOfDoc = {}
	for i in range(len(listOfDocName)):
		listOfDoc[i] = readfile(listOfDocName[i])

	for i in range(len(listOfDoc)):
		listOfDoc[i] = Counter(preprocessing(listOfDoc[i]))

	listOfWord = []
	for key,val in listOfDoc.items():
		for word, count_w in val.items():
			if word not in listOfWord:
				listOfWord.append(word)

	print ("==SUM OF WORD == ",len(listOfWord))
	print ("==LIST OF WORD == ",listOfWord)
	print ("==SUM OF DOC == ",len(listOfDoc))
	
	with open('result.csv','wb') as csvfile:
		reswriter = csv.writer(csvfile, delimiter=',', quotechar='|')
		tempWord = [' ']
		tempWord.extend(listOfWord)
		reswriter.writerow(tempWord)
		for i in range(len(listOfDoc)):
			j = i + 1
			doctitle = "Doc "+`j`
			counterlist = [listOfDoc[i][word] for word in listOfWord]
			counterlist.insert(0, doctitle)
			print ("==NILAI WORD FREK. UTK DOC ",listOfDocName[i], " : ", counterlist)
			reswriter.writerow(counterlist)

main()

# listOfDoc[1] = readfile(listOfDocName[1])
# listOfDoc[2] = readfile('22170.xml')
# listOfDoc[3] = readfile('22513.xml')
# listOfDoc[4] = readfile('26642.xml')
# listOfDoc[5] = readfile('26847.xml')

#INI BUAT TESTING AJA#
# sentence = 'a quick brown fox jumped over the lazy dog'
# listOfDoc['D1'] = Counter(sentence.split())

# print("listOfDoc", listOfDoc)
# sentence = 'a fast paced brown man jumps over the lazy cat'
# listOfDoc['D2'] = Counter(sentence.split())
# print("listOfDoc", listOfDoc)
#===================================================sampe ini

# listOfDoc[0] = Counter(preprocessing(listOfDoc[0]))
# listOfDoc[1] = Counter(preprocessing(listOfDoc[1]))
# listOfDoc['D3'] = Counter(preprocessing(listOfDoc['D3']))
# listOfDoc['D4'] = Counter(preprocessing(listOfDoc['D4']))
# listOfDoc['D5'] = Counter(preprocessing(listOfDoc['D5']))
# listOfDoc['D6'] = Counter(preprocessing(listOfDoc['D6']))
