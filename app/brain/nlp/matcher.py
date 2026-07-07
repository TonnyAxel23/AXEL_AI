from app.brain.nlp.synonyms import *


class Matcher:

    @staticmethod
    def contains(words, vocabulary):

        return any(word in vocabulary for word in words)