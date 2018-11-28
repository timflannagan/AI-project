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

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

'''Constants declarations'''
GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey",)
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]
FAIL_RESPONSES = ["I am sorry! I don't understand you.", "I wasn't able to understand that last question."]
END_INPUTS = ['bye', 'exit', 'leave']

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
    raw = read_chatbot_data('data', 'chatbot.txt')
    sent_tokens = nltk.sent_tokenize(raw)
    word_tokens = nltk.word_tokenize(raw)
    lemmer = nltk.stem.WordNetLemmatizer()

    remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
    flag = True

    chatbot_introduction()

    while flag:
        user_response = raw_input()
        user_response = user_response.lower()

        if user_response not in END_INPUTS:
            if user_response == 'thanks' or user_response == 'thank you':
                flag = False
                print('> NBA Chatbot: You are welcome!')
            else:
                if (greeting(user_response) != None):
                    print("> NBA Chatbot: " + greeting(user_response))
                else:
                    sent_tokens.append(user_response)
                    word_tokens = word_tokens + nltk.word_tokenize(user_response)
                    final_words = list(set(word_tokens))

                    chatbot_response = response(user_response)

                    '''Check if the chatbot did not understand that input'''
                    if chatbot_response in FAIL_RESPONSES:
                        print('[ERROR] NBA Chatbot: {}'.format(chatbot_response))
                    else:
                        print('> NBA Chatbot: {}'.format(chatbot_response))

                    sent_tokens.remove(user_response)
        else:
            '''Exiting the chatbot here.'''
            print("[EXIT] NBA Chatbot: Bye! take care..")
            break
