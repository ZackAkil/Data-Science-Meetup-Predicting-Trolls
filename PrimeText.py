import numpy as np

class PrimeText:

	indexedDictionary = dict()
	indexedRecords = []

	 

	def indexDictionary(dictionary):
		primes = np.genfromtxt ('primes.csv', delimiter=",").astype(int)
		fitPrime = primes[1:len(dictionary)+1,1]
		indexedDictionary = dict(np.c_[dictionary,primeFit])

	def indexComments(comments):
		for comment in comments:
			prod = 1
			words = comment.split(' ')
			for word in words:
				if word in indexedDictionary:
					prod *= int(indexedDictionary[word])
			output.append(prod)
		indexedRecords = output

	def convertWordsToProduct(words):
		output = 1
		for word in words:
			if word in indexedDictionary:
				output *= int(indexedDictionary[word])
		return output

	def searchByPrimeFact(searchProduct):
		return  (np.mod(indexedRecords, searchProduct) == 0)

	def find(words):
		prod = convertWordsToProduct(words)
		return searchByPrimeFact(prod)