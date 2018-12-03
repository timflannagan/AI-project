"""
Sources: https://medium.com/analytics-vidhya/building-a-simple-chatbot-in-python-using-nltk-7c8c8215ac6e
"""

import nltk
import numpy as np
import random
import string
import io
import nba_py
import random
import wikipedia

# from nltk.corpus import brown
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

'''Constants declarations'''
GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey",)
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]
FAIL_RESPONSES = ["I am sorry! I don't understand you.", "I wasn't able to understand that last question."]
END_INPUTS = ['bye', 'exit', 'leave', 'quit']
WIKIPEDIA_QUERIES = ['whois', 'who is', 'who was', 'who are']

'''Function declarations'''
def lem_tokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]

def lem_normalize(text):
    return lem_tokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

def download_nltk_pkgs():
    nltk.download('punkt')
    nltk.download('wordnet')

def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

def response(user_response, debug = False):
    TfidfVec = TfidfVectorizer(tokenizer = lem_normalize, stop_words = 'english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()

    req_tfidf = flat[-2]
    robo_response = ''

    if req_tfidf == 0:
        index = random.randrange(len(FAIL_RESPONSES))
        robo_response = robo_response + FAIL_RESPONSES[index]
    else:
        robo_response = robo_response + sent_tokens[idx]

    if debug:
        print("Returning '{}'".format(robo_response))

    return robo_response

def chatbot_introduction():
    print('This is the NBA Chatbot! Enter your question below: ')

def chatbot_end_response():
    print('Bye for now!')

def read_chatbot_data(data_dir, data_name, download_pkg = False):
    f = io.open(data_dir + '/' + data_name, mode = 'r', errors = 'ignore', encoding = 'utf-8')
    raw = f.read()
    raw = raw.lower()

    '''Download nltk packages as needed'''
    if download_pkg:
        download_nltk_pkgs()

    return raw

if __name__ == '__main__':
    '''Driver declaration'''

    chatbot_introduction()
    flag = True

    while flag:
        user_response = raw_input('> ').lower()

        if user_response in END_INPUTS:
            chatbot_end_response()
            break

        else:
            if any(word in user_response for word in WIKIPEDIA_QUERIES):
                '''Query wikipedia for information about a team/player'''
                try:
                    print("NBA Chatbot: {}\n".format(wikipedia.summary(user_response)))
                except:
                    if 'whois' in user_response:
                        '''### To-Do: Change str formatting with substring indexing later'''
                        print("NBA Chatbot: Did you mean 'who is {}'".format(user_response))
                    else:
                        print("NBA Chatbot: I wasn't able to find any information on the question '{}'".format(user_response))
