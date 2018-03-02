class Chatbot:
    """ An object that can engage in rudimentary conversation with a human. """

    def __init__(self, name):
        self.name = name

    def greeting(self):
        """ Returns the Chatbot's way of introducing itself. """
        return("Hello, my name is " + self.name + ". ")

    def response(self, promp_from_human):
        """ Returns the Chatbot's response to something the human said. """
        return("It is very interesting that you say: '" + promp_from_human + "'")

class BoredChatbot(Chatbot):
    """ Bored chatbot looses patience after 20 characters. """
    def response(self, prompt_from_human):
        """ Returns the bored response or the original response. """
        if len(prompt_from_human) > 20:
            return("zzz... Oh excuse me, I dozed off reading your essay.")
        else:
            return(Chatbot.response(self, prompt_from_human))

# make a chatbot
sally = BoredChatbot("Sally")
# introduce the chatbot and allow the user to say something
human_message = input(sally.greeting())
# respond to the user
print(sally.response(human_message))