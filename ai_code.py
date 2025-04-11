def chatbot_response(msg):
    msg = msg.lower()
    if "hello" in msg or "hi" in msg:
        return "Hi there! How can I help you?"
    elif "bye" in msg:
        return "Goodbye!"
    elif "name" in msg:
        return "I am a simple AI chatbot."
    else:
        return "Sorry, I didn't understand that."

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    print("Bot:", chatbot_response(user_input))
