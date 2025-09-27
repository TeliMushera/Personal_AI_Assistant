from transformers import pipeline

assistant = pipeline('text2text-generation', model='google/flan-t5-large')

chat_history = []

def ask_ai(user_input):
    global chat_history
    chat_history.append(f'User: {user_input}')
    context = '\n'.join(chat_history[-5:])
    response = assistant(context)[0]['generated_text']
    chat_history.append(f'assistant: {response}')
    return response

while True:
    user_input = input('You: ')
    if user_input.lower() in ['exit', 'bye', 'quit']:
        print('assistant goodbye!')
        break
    reply = ask_ai(user_input)
    print(f'assistant: {reply}')
