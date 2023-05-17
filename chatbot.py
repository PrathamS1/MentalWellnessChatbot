# Rule-based Mental Wellness Chatbot

# Define the chatbot's rules
rules = {
    'hi': 'Hello! How can I help you today?',
    'bye': 'Take care. Remember, I'm here if you need me!',
    'i feel sad': 'I'm sorry to hear that. It's important to acknowledge your feelings. Would you like to talk more about it?',
    'i feel anxious': 'I understand. Take a deep breath and try to focus on the present moment. Is there anything specific that\'s causing your anxiety?',
    'i need someone to talk to': 'I'm here for you. You're not alone. Can you tell me more about what you're going through?',
    'what can i do to feel better?': 'There are several things you can try to improve your mental well-being. Some suggestions include exercising, practicing mindfulness, talking to a trusted friend or family member, or seeking professional help. Remember, it\'s important to find what works best for you.',
    'i can't sleep': 'Insomnia can be challenging. Have you tried establishing a bedtime routine or creating a relaxing environment in your bedroom?',
    'i feel overwhelmed': 'It can be overwhelming when things pile up. Take a moment to prioritize your tasks and consider reaching out for support if needed.',
    'i feel hopeless': 'I\'m sorry you\'re feeling this way. Remember that there is always hope, and seeking professional help can provide guidance and support.',
    'default': 'I'm here to support you. Please feel free to share more about what you\'re going through.'
}

# Function to generate a response based on user input
def generate_response(user_input):
    # Convert the user input to lowercase
    user_input = user_input.lower()
    
    # Check if user input matches any of the defined rules
    for key in rules.keys():
        if key in user_input:
            return rules[key]
    
    # If no matching rule found, return default response
    return rules['default']

# Chat loop
print("Chatbot: Hi! I'm here to support you. How are you feeling today?")
print("Chatbot: If at any point you need help, feel free to say 'bye' and exit the conversation.")

while True:
    # Get user input
    user_input = input('You: ')
    
    # Generate and print the chatbot's response
    response = generate_response(user_input)
    print('Chatbot:', response)
    
    # Break the loop if user says 'bye'
    if user_input.lower() == 'bye':
        break
