import nltk

fileName = 'sample.txt'
fileNameOut = 'output.txt'

File = open(fileName) #open file
lines = File.read() #read all lines
sentences = nltk.sent_tokenize(lines) #tokenize sentences
nouns = [] #empty to array to hold all nouns

for sentence in sentences:
     for word,pos in nltk.pos_tag(nltk.word_tokenize(str(sentence))):
         if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS'):
             nouns.append(word)

fileNameOut  = open(fileNameOut, 'w')

for sentence in sentences:
    for word in sentence.split():
        if word in nouns:
            word = "gn" + word
        fileNameOut.write(word +  " ")