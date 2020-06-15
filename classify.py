from neural import NeuralResponse

def neural_classify(msg):
    intent = NeuralResponse(msg)
    return f"The message is classified as: {intent}."