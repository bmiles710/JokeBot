"""A collection of functions for doing my project."""
import string
import random


GREETINGS_IN = ["hello", "hi", "hey", "hi there", 
                "greetings", "what is good", "yo", "sup"]

GREETINGS_OUT = ["Hello, it's nice to talk to you! Ask me to tell you a joke!",
                 'Nice to meet you! Wanna hear a joke?', 
                 "Hey - Let's chat! Ask me to tell you a joke",
                 "yoooo, wanna hear a joke", 
                 "hi there, ask me to tell you a joke", 
                 "what is good? Wanna hear a joke?", 
                 "sup ask me to tell you a joke",
                 "yo, lets share jokes","hi, ask me to tell you a joke",
                 "what is up?? Wanna hear a joke?"]


JOKE_PROMPT_IN = ['joke', 'humor','fun','yes','sure','ya','yeah','please',
                  'okay','ok', 'fine', 'k', 'tell me', 'another', 'more' ]

JOKE_PROMPT_OUT = [ "What is the best thing about Switzerland? I dont know but the flag is a big plus!", \
            "Did you hear about the knew restaurant called Karma? Theres no menu, you get what you deserve!", \
            "Did you hear about the actor that fell through the floorboards? He was just going through a stage.",\
            "Did you hear about the claustrophobic astronaut? He just needed a little space." , 
            "Why dont scientists trust atoms? They make up everything.",
            "Where are average things manufactured? The satisfactory!",
            "How do you drown a hipster? Throw him in the mainstream!",
            "What sits at the bottom of the sea and twitches? A nervous wreck!",
            "How does Moses make tea? He brews.",
            "How do you keep the bagel from getting away? Put lox on it!",
           "Why should the number 288 never be mentioned? It is two gross!",
           "What did the buddhist say to the hotdog vendor? Make me one with everything!", 
           "What did the left eye say to the right eye? Between me and you... something smells",
           "What do you call a fake noodle? An impasta!",
           "What did the 0 say to the 8? Nice belt!",
           "What do you call a pony with a cough? A little horse!",
           "Me, I am the joke", 
           "It is me. I am the joke",
           "what do you call a magic dog? A LABRACADABRADOR!!!!!",
           "What did the pirate say when he turned 80? Aye Matey!",
           "Why did the frog take the bus to work today? His car got toad...",
            "How do you get a squirrel to like you? Act like a nut",
            "Why don't eggs tell jokes? They'd crack each other up",
            "I don't trust stairs. They're always up to something",
            "What do you call someone with no body and no nose? Nobody knows.",
            "Did you hear the rumor about butter? Well, I'm not going to spread it",
            "Why couldn't the bicycle stand up by itself? It was two tired.",
            "Why can't a nose be 12 inches long? Because then it would be a foot",
            "What time did the man go to the dentist? Tooth hurt-y",
            "How many tickles does it take to make an octopus laugh? Ten tickles",
            "What concert costs just 45 cents? 50 Cent featuring Nickelback",
            "How do you make a tissue dance? You put a little boogie in it.",
            "Why did the math book look so sad? Because of all of its problems!",
            "What do you call cheese that isn't yours? Nacho cheese",
            "What kind of shoes do ninjas wear? Sneakers!",
            "How does a penguin build its house? Igloos it together.",
            "Why did the scarecrow win an award? Because he was outstanding in his field.",
            "I made a pencil with two erasers. It was pointless",
            "I'm reading a book about anti-gravity. It's impossible to put down!",
            "I've got a great joke about construction, but I'm still working on it",
            "I used to hate facial hair...but then it grew on me",
            "What's brown and sticky? A stick",
            "Did I tell you the time I fell in love during a backflip? I was heels over head!"]

LAUGHTER_IN = ['haha', 'LOL', 'ha', 'laugh','hahaha','lmao','lol','LMAO','hehe', 'omg']
LAUGHTER_OUT =['Thanks!', 'Thanks, tell me a joke now!', 'lets hear one of yours now!', 'your turn :)']

NICE_IN = ['funny', 'hilarious','good', 'that was good', 'nice']
NICE_OUT = ['thanks!', 'thank you', 'I got it off the internet!', 'want to hear another?'] 

USER_JOKE_IN = ['why did', 'what did', 'who did', 'did you', 'where did', 'when did']
USER_JOKE_OUT = ['hmmmm', 'I am not sure?', 'tell me!', 'ah! I give up']

KNOCK_KNOCK_IN = ["knock knock", "Knock Knock"]
KNOCK_KNOCK_OUT = ["who's there?", "who is there??"]

WELCOME_IN = ["anytime", "ur welcome", "welcome", "of course", "no problem", "course"]
WELCOME_OUT = [":-)", "well, wanna hear another?", "why do you try telling me one?"]

USER_FINISH_IN = ['because', 'he','she','they']

MEAN_IN = ["bad", "terrible", "that sucked", "you suck", "boo", "lame", "not good", "not funny", "didnt laugh",
          "dislike"]
MEAN_OUT = ["ouch", "that was not very nice", "be nicer", "oh...", 
            "Well, let me try to redeem myself", "my mom says the same thing", 
            "I happen to agree but I am just a bot, I did not make these jokes, my creator found them online",
            "whatever", "sorry!"]

HOW_ARE_YOU_IN = ["how are you" , "what's up", "how're you"]
HOW_ARE_YOU_OUT = ["I'm good, thanks!", "I am great! Thank you for asking", "great, thanks!"]

NO_IN = ['no','nope','nah']
NO_OUT = ["get out of here then", "I serve you no purpose then", 
          "That is literally my whole purpose","bruh."]

UNKNOWN = ['OMG', 'HAHAHA' , 'you are funny!', 'lol','oooo good one', 'haha','hehe','lmao','nice!','that was great', 'fantastic!']

QUESTION = ['hmmm, IDK', 'huh?', 'I dont know', 'lets hear it!']


def remove_punctuation(input_string):
    """
    Takes an input and removes the punctuation from it
    _ _ _ _ _ _ _
    Parameters:
    input = string
    
    Returns:
    output = string 
    
    """
    # setting an empty string as the output
    out_string = ''
    
    # looping through the characters in the input string
    for char in input_string:
        # if the character is not considered punctuation, add it to the output list
        if char not in string.punctuation:
            out_string = out_string + char
    return out_string


def prepare_text(input_string):
    """
    Takes a string as input and transfers all letters to lowercase, removes punctuation
    and splits each word into an element of a list
    _ _ _ _ _ _ _
    Parameters:
    input = string
    
    Returns:
    output = list 
    """
    # setting a temporary string equal to the input string, but all the letters are lowercase
    temp_string = input_string.lower()
    
    # taking that string and removing all the punctuation from the string
    temp_string = remove_punctuation(temp_string)
    
    # finally, splitting the string into elements of a list by word
    out_list = temp_string.split()
    
    return out_list


def is_question(input_string):
    """
    Checks an input for a question mark, if one is present, it will return true
    _ _ _ _ _ _ _ _ _ 
    Parameters: 
    input = string
    
    Returns:
    output = boolean 
    """
    # conditonal stating that if a question mark is in the input, to return a boolean
    if '?' in input_string:
        output = True
    else:
        output = False
    return output


def respond_echo(input_string,number_of_echoes,spacer):
    """
    Takes a string, an integer, and symbol as input. It will repeat the string the
    same number of times as specified by the integer, separated by the symbol listed.
    _ _ _ _ _ _ _ _ _
    Parameters:
    input = string, integer, symbol
    
    Returns:
    output = string 
    """
    
    # conditional stating that as long as there is an input string, add the string to the spacer 
    # and repeat it however many times is stated
    if input_string != None:
        echo_output = (input_string + spacer) * number_of_echoes
    else:
        echo_output = None
        
    return echo_output


def string_concatenator(string1,string2,separator):
    """
    Takes the input of two strings and a symbol and adds them together, separated by
    the listed symbol
    _ _ _ _ _ _ _ _ _
    Parameters:
    input = two strings, symbol
    
    Returns:
    output = string 
    """
    
    # setting the output to the additon of the two strings, separated by the string set as separator
    output = string1 + separator + string2
    
    return output


def selector(input_list,check_list,return_list):
    """
    Takes an input list as given by user, will check list of given keywords, 
    and return an appropriate output list as a response
    _ _ _ _ _ _ _ _
    Parameters:
    input = list
    
    Returns:
    output = list
    """
    
    # intially setting the output to none
    output = None
    
    # looping through the characters in the input list
    for char in input_list:
        
        # conditional checking all of the elements in check_list, if so it will choose a random 
        # element from the return_list as the output and return it
        if char in check_list:
            output = random.choice(return_list)
            
    return output


def end_chat(input_list):
    """
    Check for keyword quit in the chat, if present, will return a boolean,
    making the chat false
    _ _ _ _ _ _ _ _ 
    Parameters:
    input = list
    
    Returns:
    output = boolean
    """
    
    # conditional that if the phrase quit is in the input, then the output will return True
    if 'quit' in input_list:
        output = True
    else:
        output = False
    
    return output


def is_in_list(list_one, list_two):
    """
    Check if any element of list_one is in list_two.
    _ _ _ _ _ _ _ _ _
    Parameters:
    input = two lists
    
    Returns:
    output= Boolean
    """
    
    # looping through the elements in the first input list, to check if any are in the second input list
    # if so, it will return True
    for element in list_one:
        if element in list_two:
            return True
    return False


def find_in_list(list_one, list_two):
    """
    Find and return an element from list_one that is in list_two, or None otherwise.
    _ _ _ _ _ _ _ _ 
    Parameters:
    input = two lists
    
    Returns:
    output = string
    """
    
    # looping through the elements in list one to check if any appear in list two, if so
    # then it will return the element that matches both lists
    for element in list_one:
        if element in list_two:
            return element
    return None


def detect_knock_knock(input_string):
    """
    Checks for the keyword knock in the input string and returns a boolean
    _ _ _ _ _ _ _ _ 
    Parameters:
    input = string
    
    Returns:
    output = boolean
    """

    # conditional that checks for the keyword 'knock' if it is present, will return True
    if 'knock' in input_string:
        return True
    else:
        return False

    
def detect_walk_into_bar(input_string):
    """
    Checks for the keyword bar in a string and returns a boolean
    _ _ _ _ _ _ _ _ _ 
    Parameters:
    input = string
    
    Returns:
    ouput = boolean
    """
    
    # conditional checking if the keyword 'bar' is in the input string, if it is, returns True
    if 'bar' in input_string:
        output = True
    else:
        output = False
        
    return output


def detect_what_do_you_call(input_list):
    """
    Takes an input list and checks that it is the same as the variable wdyc_list, if
    so, it has the key elements to be a certain type of joke, and will return a boolean
    _ _ _ _ _ _ _ _ _ 
    
    input = list
    output = string
    """
    #initializing a key list that should be matched
    wdyc_lst = ['what', 'do', 'you', 'call']
    
    # setting a variable equal to the boolean that all elements in the input list match the list desired
    result = all(element in input_list for element in wdyc_lst)
    
    if result:
        output = True
        
    else:
        output = False

        
    return output


def detect_how_are_you(input_list):
    """
    Takes an input list and checks that it is the same as the variable hay_lst or wu_lst, if
    so, it has the key elements to be a common phrase, and will return a boolean
     _ _ _ _ _ _ _ _ _ 
    Parameters:
    input = list
    
    Returns:
    output = string
    """
    hay_lst = ['how', 'are', 'you']
    wu_lst = ["what's", "up"]
    
    # setting the result equal to the boolean is all items in input_list are in hay_list
    # or if all elements in input list are in wu_lst
    result = all(element in input_list for element in hay_lst) or all(element in input_list for element in wu_lst)
    if result:
        output = True
        
    else:
        output = False

        
    return output


def receive_input():
    """
    Informs the user to input a message
    _ _ _ _ _ _ _ _ 
    Parameters:
    input = string
    
    Returns:
    output = list
    """
    # set message equal to recieving an input and typing "INPUT"
    # out_msg initialized as None
    msg = input('INPUT :\t')
    out_msg = None
     
     # return msg and out_msg   
    return msg, out_msg 


def detect_appreciate(input_list):
    """
    Takes an input list and checks that it is the same as the variable ty_lst or thank_lst, if
    so, it has the key elements to be a common phrase, and will return a boolean
    _ _ _ _ _ _ _ _ _
    
    input = list
    output = string
    """
    ty_lst = ['thank', 'you']
    thank_lst = ['thanks']
    
    # setting the result equal to the boolean is all items in input_list are in ty_list
    # or if all elements in input list are in thank_lst
    result = all(element in input_list for element in ty_lst) or all(element in input_list for element in thank_lst)
    if result:
        output = True
        
    else:
        output = False

     # return the boolean output from above   
    return output


def lets_chat():
    
    chat = True
    while chat:
        
        # Recieve an input message from user
        msg, out_msg = receive_input()
        

        # Check if the input is a question
        question = is_question(msg)
        
        
        # Prepare the input message
        msg = prepare_text(msg)

        # Check for an end msg 
        if end_chat(msg):
            out_msg = 'Bye!'
            chat = False
            
        # Check for a certain common joke phrase, and respond properly    
        if detect_what_do_you_call(msg):
            out_msg = "I don't know"
            
        # Checks to see if the user asks how bot is, responds appropriately  
        if detect_how_are_you(msg):
            out_msg = "good, thanks!"
            
        # Check if the input from the user is a type of appreciation, add a kind
        #output if so   
        if detect_appreciate(msg):
            out_msg = "no problem!"
            

        # Checking for a plethora of topics that I have defined for the bot to respond to
        if not out_msg:

            # Initialize to collect a list of possible outputs
            outs = []

            
            # Check if the input looks like a greeting, add a greeting output if so
            outs.append(selector(msg, GREETINGS_IN, GREETINGS_OUT))

            
            # Check if the input asks for a joke, add a joke output if so
            outs.append(selector(msg, JOKE_PROMPT_IN, JOKE_PROMPT_OUT))
           
            
            # Check if the input asks how the bot is, respond with the answer
            outs.append(selector(msg, HOW_ARE_YOU_IN, HOW_ARE_YOU_OUT))
            
            
            # Check if the user inputs any keywords saying 'you're welcome', respond appropriately
            outs.append(selector(msg, WELCOME_IN, WELCOME_OUT))
                        
            
            # Use functions to identify certain common joke phrases

            if detect_knock_knock(msg) == True:
                print("who's there?")
                temp = input()
                outs.append(temp + " " + "who?" )
            
            def knock_knock_echo(input_string):
    
                if out_msg == "who's there?":
                    output = respond_echo(input_string, 1, " , who? ")
        
                return output

            
            if detect_walk_into_bar(msg) == True:
                outs.append("that was a good one")
                

            # check if user input a type of laughter, if so, use an appropriate output
            outs.append(selector(msg, LAUGHTER_IN, LAUGHTER_OUT))
            

            # Check if the input looks like the user telling a joke, add an appropriate response if so
            outs.append(selector(msg, USER_JOKE_IN, USER_JOKE_OUT))

            
            # Check if the input refuses to hear a joke, express frustration         
            outs.append(selector(msg, NO_IN, NO_OUT))
            
            
            # Check if the input is not very nice, express sadness if so
            outs.append(selector(msg, MEAN_IN, MEAN_OUT))
            
            
            # check if the input is nice, if so, say thank you!
            outs.append(selector(msg, NICE_IN, NICE_OUT))
                
                 
            #   The bot may have appended None for certain inputs, meaning there was no reply
            #   To manage this, an output will be randomly selected from a list of outputs
            options = list(filter(None, outs))
            if options:
                out_msg = random.choice(options)

            # If there is no output yet, but the input was a question, return msg related to it being 
            # a question
        if not out_msg and question:
            out_msg = random.choice(QUESTION)

        # Catch-all to respond with something if the bot does not recognize the input
        if not out_msg:
            out_msg = random.choice(UNKNOWN)
            


        print('OUTPUT:', out_msg)