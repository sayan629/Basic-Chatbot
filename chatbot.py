import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey! How can I assist you?"]
    ],
    [
        r"how are you?",
        ["I'm just a computer program, but thanks for asking!", "Doing well, how about you?"]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created to assist you.", "You can call me Chatbot."]
    ],
    [
        r"quit",
        ["Bye! Take care.", "Goodbye! Have a nice day!"]
    ],
    [
        r"(.*)",
        ["I'm sorry, I don't understand that.", "Can you please rephrase?"]
    ]
]

# Function to run the chatbot
def chatbot():
    print("Hi! I'm a chatbot. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

# Run the chatbot
if __name__ == "__main__":
    nltk.download('punkt')  # Download the necessary NLTK data files
    chatbot()