from neural import NeuralResponse

def neural_classify(msg):
    intent = NeuralResponse(msg)
    return intent