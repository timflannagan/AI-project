"""
Sources: https://medium.com/analytics-vidhya/building-a-simple-chatbot-in-python-using-nltk-7c8c8215ac6e
"""

import nltk
import numpy as np
import random
import string
import io
import nba_py

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

'''Constants declarations'''
GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey",)
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]

'''Function declarations'''
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

def download_nltk_pkgs():
    nltk.download('punkt')
    nltk.download('wordnet')

def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

def response(user_response):
    robo_response = ''
    TfidfVec = TfidfVectorizer(tokenizer = LemNormalize, stop_words = 'english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]

    if(req_tfidf == 0):
        robo_response = robo_response + "I am sorry! I don't understand you"
        return robo_response
    else:
        robo_response = robo_response + sent_tokens[idx]
        return robo_response

'''Driver declaration'''
if __name__ == '__main__':
    f = io.open('data/chatbot.txt', mode = 'r', errors = 'ignore', encoding = 'utf-8')
    raw = f.read()
    raw = raw.lower()

    sent_tokens = nltk.sent_tokenize(raw)
    word_tokens = nltk.word_tokenize(raw)
    lemmer = nltk.stem.WordNetLemmatizer()

    remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
    flag = True

    print('This is the NBA Chatbot! Enter your question below: ')

    while(flag == True):
        user_response = raw_input()
        user_response = user_response.lower()

        if user_response != 'bye':
            if user_response == 'thanks' or user_response == 'thank you'):
                flag = False
                print('NBA Chatbot: You are welcome!')
            else:
                if (greeting(user_response) != None):
                    print("NBA Chatbot: " + greeting(user_response))
                else:
                    sent_tokens.append(user_response)
                    word_tokens = word_tokens + nltk.word_tokenize(user_response)
                    final_words = list(set(word_tokens))

                    chatbot_response = response(user_response)

                    '''Check if the chatbot did not understand that input'''
                    if chatbot_response is not 'I am sorry':
                        print(chatbot_response)
                    else:
                        print('NBA Chatbot: {}'.format(chatbot_response))

                    sent_tokens.remove(user_response)
        else:
            '''Exiting the chatbot here.'''
            flag = False
            print("NBA Chatbot: Bye! take care..")
