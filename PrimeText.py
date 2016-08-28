import numpy as np
from nltk.stem.lancaster import LancasterStemmer
from autocorrect import spell

class PrimeText:

    indexedDictionary = dict()
    indexedRecords = []
 
    def hw(self):
        print('sup')
        
    def assembleDictionary(self, textList):
        st = LancasterStemmer()
        uniqueWords = []
        for text in textList:
            for word in text.split(' '):
                if st.stem(spell(word)) not in uniqueWords:
                    uniqueWords.append(word)
        return uniqueWords

#	def indexDictionary(self,dictionary):
#         primes = np.genfromtxt ('primes.csv', delimiter=",").astype(int)
#         fitPrime = primes[1:len(dictionary)+1,1]
#         self.indexedDictionary = dict(np.c_[dictionary,fitPrime])
#
#	def indexComments(self,comments):
#         output = []
#         for comment in comments:
#             prod = 1
#             words = comment.split(' ')
#             for word in words:
#                 if word in self.indexedDictionary:
#                     prod *= int(self.indexedDictionary[word])
#                 output.append(prod)
#        self.indexedRecords = output
#
#	def convertWordsToProduct(self,words):
#		output = 1
#		for word in words:
#			if word in self.indexedDictionary:
#				output *= int(self.indexedDictionary[word])
#		return output
#
#	def searchByPrimeFact(self,searchProduct):
#		return  (np.mod(self.indexedRecords, searchProduct) == 0)
#
#	def find(self, words):
#		prod = convertWordsToProduct(words)
#		return searchByPrimeFact(prod)