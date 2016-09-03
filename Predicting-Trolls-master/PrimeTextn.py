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
    
    def cleanData(self,records,labels):
         output = []
         outputLabels = []

         recordsChecked = 0
         recordsToCheck = len(records)
         for index,sentence in enumerate(records):
             recordsChecked += 1
             sys.stdout.write("\rRecords cleaned : %i / %i" % (recordsChecked,recordsToCheck))
             cleanSentence = ''
             if len(sentence) < 200:
                 words = sentence.split(' ')
                 for word in words:
                     if len(word) < 12:
                         if word.isalpha():
                             cleanSentence += self.st.stem(spell(word.lower())) + ' '
             if cleanSentence:
                 output.append(cleanSentence.strip())  
                 outputLabels.append(labels[index])
         sys.stdout.write("\n")
         sys.stdout.flush()
         self.cleanedRecords = output
         return outputLabels
    

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


    def convertWordsToProduct(self,words, stem = False):
        output = 1
        for word in words:
            if stem:
                word = self.st.stem(word).lower()
            if word in self.indexedDictionary:
                output *= int(self.indexedDictionary[word])
        return output

    def searchByPrimeFact(self,searchProduct):
        return  (np.mod(self.indexedRecords, searchProduct) == 0)

    def find(self, words):
        prod = self.convertWordsToProduct(words)
        if prod == 1:
            return False
        return self.searchByPrimeFact(prod)
        
    def findInRecords(self, words):
        data = np.asarray(self.cleanedRecords)
        return data[self.find(words)]
        
    def countInRecords(self, words):
        return self.find(words).sum()