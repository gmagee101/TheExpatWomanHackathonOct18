import re
import logging
from .models import Highlight
# given a list of words, look in db for matching keys
# return a dict of words to db highlight obejects present
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logging.basicConfig(level=logging.DEBUG, format='%(relativeCreated)6d %(threadName)s %(message)s')
def analyze_word_list(list):
    logger.info("Starting analyze function")
    output = dict()
    for word in list:
        logger.info("found word {}".format(word))
        query_set = Highlight.objects.filter(key=word)
        logger.info("got queryset {}".format(query_set))
        if len(query_set) > 0:
            if word in output:
                if query_set not in output[word]:
                    output[word].append(query_set)
            else:
                output[word] = [query_set]
    return output

# https://stackoverflow.com/questions/6181763/converting-a-string-to-a-list-of-words
def create_list(input_string):
    logger.info("Starting create list function")
    wordList = re.sub("[^\w]", " ",  input_string).split()
    return wordList
