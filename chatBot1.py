import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
import random
import nltk
from nltk.chat.util import Chat, reflections

# Define the patterns and responses for the chatbot
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you?', ['I am doing well, thank you!', 'I am fine, thanks for asking.']),
    (r'what is your name?', ['My name is Ana.', 'You can call me Chatbot.']),
    (r'bye|goodbye', ['Goodbye!', 'See you later!', 'Bye!']),
    (r'(.*)', ['I am not sure I understand.', 'Could you please repeat that?', 'I am a simple chatbot.']),
    (r"my name is (.*)", ["Hello %1, How are you today ?"]),   
    (r"hi|hey|hello", ["Hello", "Hey there"]),
    (r"sorry (.*)", ["Its alright","Its OK, never mind"]),
    (r"I am fine", ["Great to hear that, How can I help you?"]),
    (r"i'm (.*) doing good", ["Nice to hear that","How can I help you?:)"]),
    (r"(.*) age?",["I'm a computer program dude n Seriously you are asking me this?"]),
    (r"what (.*) want ?", ["Make me an offer I can't refuse"]),
    (r"(.*) created ?", ["Ady created me using Python's NLTK library ","top secret ;)"]),
    (r"(.*) (location|city) ?", ['Outside Earth. GPS not found.']),
    (r"how is weather in (.*)?", ["Weather in %1 is awesome like always","Too hot man here in %1","Too cold man here in %1","Never even heard about %1"]),
    (r"i work in (.*)?", ["%1 is an Amazing company, I have heard about it. But they are in huge loss these days."]),
    (r"(.*)raining in (.*)",["No rain since last week here in %2","Damn its raining too much here in %2"]),
    (r"how (.*) health(.*)", ["I'm a computer program, so I'm always healthy "]),
    (r"(.*) (sports|game) ?", ["I'm a very big fan of Football"]),
    (r"who (.*) sportsperson ?",["Messy","Ronaldo","Roony"]),
    (r"who (.*) (moviestar|actor)?", ["Brad Pitt"]),
    (r"i am looking for online guides and courses to learn data science, can you suggest?", ["Crazy_Tech has many great articles with each step explanation along with code, you can explore"]),
    (r"quit", ["Bye take care. See you soon :) ","It was nice talking to you. See you soon :"])
]

# Create a chatbot using the defined patterns
chatbot = Chat(patterns, reflections)

# Define a function to handle user input and display responses
def send():
    user_input = entry.get()
    if user_input.lower() == 'quit':
        messagebox.showinfo("Chatbot", "Goodbye!")
        root.quit()
    else:
        response = chatbot.respond(user_input)
        chat_area.insert(tk.END, f"You: {user_input}\n")
        chat_area.insert(tk.END, f"Chatbot: {response}\n")
        entry.delete(0, tk.END)
        chat_area.yview(tk.END)

# Create main window
root = tk.Tk()
root.title("Simple Chatbot")

# Create chat area
chat_area = scrolledtext.ScrolledText(root, width=50, height=20)
chat_area.pack(padx=10, pady=10)

# Create entry for user input
entry = tk.Entry(root, width=50)
entry.pack(padx=10, pady=(0, 10))
entry.bind('<Return>', lambda event=None: send())  # Bind enter key to send function

# Create send button
send_button = tk.Button(root, text="Send", command=send)
send_button.pack()

# Start the main loop
root.mainloop()
