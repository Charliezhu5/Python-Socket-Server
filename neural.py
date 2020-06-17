import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

import numpy
import tflearn
import tensorflow
import random
import json
import pickle

#Try finding previously generated training data.
with open("NeuralNetwork/intents.json") as file:
    data = json.load(file)

try:
    with open("NeuralNetwork/data.pickle", "rb") as f:
        tokens, intents, training, output = pickle.load(f)

except:
    tokens = []
    intents = []
    patterns = []
    intentList = []

    for intent in data["intents"]:

        if intent["tag"] not in intents:
            intents.append(intent["tag"])

        for pattern in intent["patterns"]:
            currentTokens = nltk.word_tokenize(pattern)
            tokens.extend(currentTokens)
            # create a pair of pattern and tag.
            patterns.append(pattern)
            intentList.append(intent["tag"])

    tokens = [stemmer.stem(t.lower()) for t in tokens if t not in "?"]
    tokens = sorted(list(set(tokens)))
    #intentList = sorted(intentList)

    training = []
    output = []

    networkOutput = [0 for _ in range(len(intents))] #our current output is a list of 1s and 0s of labelTags, aka intents.tag

    for index, pattern in enumerate(patterns):
        bag = []
        currentPattern = nltk.word_tokenize(pattern)

        stemmedPatternList = [stemmer.stem(w) for w in currentPattern]

        for w in tokens:
            if w in stemmedPatternList: 
                bag.append(1)
            else:
                bag.append(0)
        
        outputRow = networkOutput[:]
        outputRow[intents.index(intentList[index])] = 1
        print("Pattern: {0}. Intent: {1}".format(pattern,intentList[index]))

        training.append(bag)
        output.append(outputRow)

    #Save training data to data.pickle if first time encountering.
    with open("NeuralNetwork/data.pickle", "wb") as f:
        pickle.dump((tokens, intents, training, output), f)

training = numpy.array(training)
output = numpy.array(output)

tensorflow.reset_default_graph()

net = tflearn.input_data(shape=[None, len(training[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
net = tflearn.regression(net)

model = tflearn.DNN(net)

try:
    model.load("NeuralNetwork/model.tflearn")
except:
    model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)
    model.save("NeuralNetwork/model.tflearn")

#Chatbot interface
def bag_of_words(s,tokens):
    bag = [0 for _ in range(len(tokens))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for element in s_words:
        for i, w in enumerate(tokens):
            if w == element:
                bag[i] = 1
    
    return numpy.array(bag)

def NeuralResponse(inp):

    backup_responses = ["uuuhhh what do you mean", "why", "probably....uh", "ok ok....."]

    results = model.predict([bag_of_words(inp, tokens)])
    max_index = numpy.argmax(results)
    result_tag = intents[max_index]

    if results[0][max_index] > 0.7:
        for tg in data["intents"]:
            if tg['tag'] == result_tag:
                responses = tg['responses']
                break

        return(random.choice(responses))

    else:
        return(random.choice(backup_responses))