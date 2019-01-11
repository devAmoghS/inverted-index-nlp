import nltk
from collections import defaultdict
from nltk.stem.snowball import EnglishStemmer


class Index:
    """Inverted index data structure"""

    def __init__(self, tokenizer, stemmer=None, stopwords=None):
        """
        :param tokenizer: NLTK compatible tokenizer function
        :param stemmer: NLTK compatible stemmer
        :param stopwords: list of ignored words
        """
        self.tokenizer = tokenizer
        self.stemmer = stemmer
        self.index = defaultdict(list)
        self.documents = {}

        self.__unique_id = 0

        if not stopwords:
            self.stopwords = set()
        else:
            self.stopwords = set(stopwords)

    def lookup(self, word):
        """
        Lookup a word in the index
        :param word:
        :return:
        """
        word = word.lower()
        if self.stemmer:
            word = self.stemmer.stem(word)
        return [self.documents.get(id, None)
                for id in self.index.get(word)]

    def add(self, document):
        """
        Add a document string to the index
        :param document:
        :return:
        """
        for token in [t.lower() for t in nltk.word_tokenize(document)]:
            if token in self.stopwords:
                continue

            if self.stemmer:
                token = self.stemmer.stem(token)

            if self.__unique_id not in self.index[token]:
                self.index[token].append(self.__unique_id)

        self.documents[self.__unique_id] = document
        self.__unique_id += 1


index = Index(nltk.word_tokenize, EnglishStemmer(), nltk.corpus.stopwords.words('english'))
