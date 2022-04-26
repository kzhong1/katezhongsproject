import random 

def print_message_for_subscribers(): 
    """From a list of names, ages, and phone numbers 
    prints info sorted by sur name--of people who subscribe with their phone number."""

    subscribers=[]

    #First Subscriber
    subscriber1={}
    subscriber1['name']='Kate Star'
    subscriber1['age']=21
    subscriber1['phone']=9788447009
    subscriber1['gender']='Female'
    subscriber1['topic']=['self-love','mental health']
    subscribers.append(subscriber1)

    #Second Subscriber
    subscriber2={}
    subscriber2['name']='Joy Wu'
    subscriber2['age']=24
    subscriber2['phone']=9788446571
    subscriber2['gender']='Female'
    subscriber2['topic']=['self love']
    subscribers.append(subscriber2)

    #Affirmation Library, randomly generate affirmation using index 0-2
    quotes_library={}
    quotes_library['self love']=['I am good', 'I am perfect', 'I am beautiful']
    quotes_library['mental health']=['Everything will be okay', 'Anxiety is temporary', 'Positive thoughts only']
    print(quotes_library, subscriber1, subscriber2)
    print(quotes_library)


    # for subscriber in subscribers:
    #     # Next 3 lines gets the current subscriber's information 
    #     name = subscriber['name']
    #     topics = subscriber['topic']
    #     phone_number = subscriber['phone']
    #     messages_to_print = []

    #     for topic in topics:
    #         if topic == quotes_library.get(topic):

    #         # TODO Figure out how to get the individual topics from the dictionary of quotes
    #         # quotes = quotes_library[topic]
    #         quotes = quotes_library.get(topic)
    #         print(quotes)
    #         # affirmation_index = random.randint(0, 2)
    #         # message_to_print = messages_to_print.append(quotes[affirmation_index])
        
    #     print(f'Good morning {name} here is your reminder for today {message_to_print}!')





    # # subscriber_names = [
    # #     'Kate Zhong', 'Lora Stancheva', 'Jean Pi', 'Julia Portis', 'Rachel Ip', 'Yang Liu', 'Joy Zhong', 'Dimitri Borlous', 'Ryan Laverty', 'Jana Godbole', 'Emily Chu', 'Suning Wang'
    # # ]
    # # subscriber_age = [
    # #     20, 21, 40, 35, 60, 13, 12, 19, 18, 11, 31, 29
    # # ]
    # # subscriber_numbers = [
    # #     9788447009, 3392043227, 7874133504, 432576898, 456444777, 908765743, 6502150740, 9788087658, 413234567, 5678903215, 5143564756
    # # ]

    # names_and_numbers = {} # Creating dictionary 
    # for key in subscriber_names: 
    #     for value in subscriber_numbers:
    #         names_and_numbers[key] = value
    #         subscriber_numbers.remove(value)
    #         break
    # # print(names_and_numbers)
    # # print(sorted(names_and_numbers.keys()))
    # print('Here is a list of current subscribers who signed up to receive notifications from the Sunshine App:')
    # # sorted_list = sorted(names_and_numbers.keys()) # Sorts names by 1st name
    # for key in sorted_list:
    #     print(key ,':', names_and_numbers[key])

    # sorted_list_by_first_name = sorted(names_and_numbers.keys()) # Sorts names by sur name
    # sorted_list_by_last_name = sorted(sorted_list_by_first_name, key=lambda sorted_names:sorted_names.split(' ')[-1])
    # for key in sorted_list_by_last_name:
    #     print(key ,':', names_and_numbers[key])

    # # for i in names_and_numbers:
    # #     sorted_names_with_numbers.append(i)
    # # # print(sorted(sorted_names, key=lambda sorted_names:sorted_names.split(' ')[-1])) 
    # # return sorted(sorted_names_with_numbers, key=lambda sorted_names:sorted_names.split(' ')[-1]) # Sorts name by surname

print_message_for_subscribers()

# def get_subscriber_phone_number():
#     """Returns a sorted """
    

