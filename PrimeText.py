from __future__ import print_function
import sys
import numpy as np
from nltk.stem.lancaster import LancasterStemmer
from autocorrect import spell
 
class PrimeText:
    
    indexedDictionary = dict()
    indexedRecords = []
 
    cleanedRecords = []
    cleanedDictionary = []
    
    st = LancasterStemmer()
     
    def cleanData(self,records):
         output = []
         recordsChecked = 0
         for sentence in records:
             recordsChecked += 1
             sys.stdout.write("\rRecords cleaned : %i" % recordsChecked)
             cleanSentence = ''
             if len(sentence) < 200:
                 words = sentence.split(' ')
                 for word in words:
                     if len(word) < 12:
                         if word.isalpha():
                             cleanSentence += self.st.stem(spell(word.lower())) + ' '
             if cleanSentence:
                 output.append(cleanSentence.strip())  
         sys.stdout.write("\n")
         sys.stdout.flush()
         self.cleanedRecords = output
    

    def assembleDictionary(self):
        uniqueWords = []
        recordsChecked = 0
        for text in self.cleanedRecords:
            recordsChecked += 1
            sys.stdout.write("\rRecords checked : %i" % recordsChecked)
            for word in text.split(' '):
                if word not in uniqueWords:
                    uniqueWords.append(word)
        sys.stdout.write("\n")
        sys.stdout.flush()
        self.cleanedDictionary = uniqueWords  
        
    def indexDictionary(self):
        primes = np.genfromtxt ('prime10000.csv', delimiter=",").astype(int)
        fitPrime = primes[1:len(self.cleanedDictionary)+1,1]
        self.indexedDictionary = dict(np.c_[self.cleanedDictionary,fitPrime])
        print('Indexed dictionary')

    def indexComments(self):
        output = []
        for comment in self.cleanedRecords:
            prod = 1
            words = comment.split(' ')
            for word in words:
                if word in self.indexedDictionary:
                    prod *= int(self.indexedDictionary[word])
            output.append(prod)
        self.indexedRecords = output
        print('Indexed comments')


    def convertWordsToProduct(self,words):
        output = 1
        for word in words:
            word = self.st.stem(word).lower()
            if word in self.indexedDictionary:
                output *= int(self.indexedDictionary[word])
        return output
#
#	def searchByPrimeFact(searchProduct):
#		return  (np.mod(indexedRecords, searchProduct) == 0)
#
#	def find(words):
#		prod = convertWordsToProduct(words)
#		return searchByPrimeFact(prod)