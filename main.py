# # Importing necessary modules
# import random
#
# # List of greetings
# greetings = ['Hello!', 'Hi!', 'Hey there!', 'Hiya!', 'Greetings!']
# greetings2 = ['I am an AI chatbot, so I am always ready to chat!',
#               'I am from the digital world!',
#               'I am just a computer program.',
#               'I like to chat with people!',
#               'I am an AI chatbot']
# # List of questions
# question1 = ['What is your name?', 'May I know your name?', 'What can I call you?']
#
# question2 = ['What is your problem', 'What is your issuess']
#
# # List of responses
# response1 = ['Hello, {name}!', 'Hi, {name}!', 'Hey, {name}!', 'Greetings, {name}!', 'I am doing well, thank you!']
#
# response2 = ['Sorry, I can\'t solve {problem} problem']
#
# last_response = ['Nice to meet you!', 'Have a great day!']
#
#
# # Chatbot function
# def chatbot():
#     # Greet the user
#     print(random.choice(greetings))
#     print(random.choice(greetings2))
#
#     print(random.choice(question1))
#     name = input()
#     response = random.choice(response1)
#     print(response.format(name=name))
#
#     print(random.choice(question2))
#     problem = input()
#     response = random.choice(response2)
#     print(response.format(problem=problem))
#
#     print(random.choice(last_response))
#
#
# # Call the chatbot function
# chatbot()

# Importing necessary modules
import random
from nltk.chat.util import Chat, reflections

# List of greetings
greetings = ['Hello!', 'Hi!', 'Hey there!', 'Hiya!', 'Greetings!']

# List of questions and responses
responses = [
    (r'(?:What is|Tell me about|What\'s) your name\??',
     ['My name is ChatBot.', 'You can call me ChatBot.', 'I am ChatBot, your virtual assistant.']),
    (r'(?:How are you|How\'s it going)\??',
     ['I am doing well, thank you!', 'I am functioning optimally!', 'All systems are go!']),
    (r'(?:Where are you from|Where do you come from)\??',
     ['I am from the digital world.', 'I am a virtual entity, so I don\'t have a physical location.']),
    (r'(?:What is your favorite color|What\'s your preferred color)\??',
     ['As an AI, I don\'t have personal preferences, but blue is often used to represent me.']),
    (r'(?:What do you do for fun|What are your hobbies)\??',
     ['As an AI, I don\'t have hobbies, but I enjoy helping users like you!', 'I enjoy learning new things.']),
    (r'(?:How old are you|What is your age)\??',
     ['I am an AI, so I don\'t have an age.', 'I am ageless and ever-learning.']),
    (r'(?:What is your purpose|Why were you created)\??',
     ['My purpose is to assist and provide information to users in a conversational manner.']),
(r'(?:What is the meaning of life)\??',
     ['The meaning of life is a philosophical question that has different interpretations for different people.']),
    (r'(?:What is your favorite food|What do you like to eat)\??',
     ['As an AI, I do not eat, so I do not have a favorite food.']),
    (r'(?:Can you tell me a joke|Tell me something funny)\??',
     ['Why don\'t scientists trust atoms? Because they make up everything!', 'Why couldn\'t the bicycle find its way home? It lost its bearings!', 'Why did the tomato turn red? Because it saw the salad dressing!']),
    (r'(?:What are your capabilities|What can you do)\??',
     ['I can provide information on a wide range of topics, answer questions, and engage in conversation.']),
    (r'(?:Tell me a fact|Give me an interesting fact)\??',
     ['A giraffe\'s neck contains the same number of vertebrae as a human neck, which is seven.', 'The world\'s oldest known living tree is a bristlecone pine named Prometheus, estimated to be over 4,900 years old.', 'The shortest war in history lasted for 38 minutes between Britain and Zanzibar in 1896.']),
    (r'(?:What is your favorite book|What do you like to read)\??',
     ['As an AI, I do not have personal preferences, so I do not have a favorite book.']),
    (r'(?:Tell me about the weather|What\'s the weather like)\??',
     ['I am sorry, I am not capable of providing real-time weather information.']),
    # Add more questions and responses here
]


# Define a chatbot class
class ChatBot(Chat):
    def __init__(self, pairs, reflections={}):
        super().__init__(pairs, reflections)

    # Method to handle user input
    def respond(self, input_text):
        response = super().respond(input_text)
        if response is None:
            return "I'm sorry, I didn't understand. Can you please select your question?"
        else:
            return response


# Create an instance of the chatbot class
chatbot = ChatBot(responses, reflections)


# Start the chatbot conversation
def chat():
    # Greet the user
    print(random.choice(greetings))
    print("I am ChatBot, your virtual assistant. How can I help you today?")

    while True:
        # Get user input
        user_input = input("> ")
        if user_input.lower() == 'bye':
            print("ChatBot: Goodbye!")
            break

        # Get chatbot's response
        bot_response = chatbot.respond(user_input)
        print("ChatBot: " + bot_response)


# Call the chat function to start the conversation
chat()
