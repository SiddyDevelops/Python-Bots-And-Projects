import re

def process_message(message, response_array, response):
    # Split the message and the punctuation into an array
    list_message = re.findall(r"[\w']+|[.,!?;]", message.lower())

    # Scores the amount of words in the message
    score = 0
    for word in list_message:
        if word in response_array:
            score = score + 1

    # Return the response and score of the response 
    #print(score, response)
    return [score, response]


def get_response(message):
    # Add your custom reponse here
    response_list = [
        process_message(message, ['hello', 'hi', 'hey'], 'Hey there!'),
        process_message(message, ['bye', 'goodbye'], 'Goodbye!'),
        process_message(message, ['how', 'are', 'you'], 'I\'m doing fine thanks!'),
        process_message(message, ['your', 'name'], 'My name is Siddy, nice to meet you!'),
        process_message(message, ['help', 'me'], 'I will do my best to assist you!')
    ]   

    # Check all of the response and return the best matching response 
    response_score = []
    for response in response_list:
        response_score.append(response[0])

    # Get the max value for the best response and store it in the variable 
    winning_response = max(response_score)
    matching_response = response_list[response_score.index(winning_response)]  

    # Return the matching response to the user
    if winning_response == 0:
        bot_response = 'I didn\'t usnderstand what you wrote.'
    else:
        bot_response = matching_response[1]
    print("Bot response: ", bot_response)
    return bot_response

# # Test your system 
# get_response('What is your name bruv?')               