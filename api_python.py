import requests

# single way joke :

# response = requests.get(r"https://v2.jokeapi.dev/joke/Any?type=single")
# print(response)
# # data = response.json()
# # print(data['joke'])



# two ways joke value fetch method
# response = requests.get(r"https://v2.jokeapi.dev/joke/Any?type=twopart&amount=2")
# data = response.json()
# print(data)
# print(f"Question : {data['setup']} ")
# print(f"Answer : {data['delivery']} ")

# w={'error': False, 'amount': 2, 'jokes': 
#    [{'category': 'Dark', 'type': 'twopart', 'setup': 'How many Jews can you fit into a car?', 
#      'delivery': 'Two in the front, three in the back, and a hundred in the ashtray.',
#        'flags': {'nsfw': False, 'religious': False, 'political': False, 'racist': True, 'sexist': False, 'explicit': True},
#          'id': 173, 'safe': False, 'lang': 'en'}, {'category': 'Misc', 'type': 'twopart', 'setup': 'What does tofu and a dildo have in common?',
#          'delivery': "They're both meat substitutes.", 'flags': {'nsfw': True, 'religious': False, 'political': False, 'racist': False, 'sexist': False, 'explicit': True}, 'id': 137, 'safe': False, 'lang': 'en'}]}
def get_joke():
    type_v = input("Type of joke (single/twopart) : ")
    amount_v = int(input("enter amount of joke you want : ")) 
    url = f"https://v2.jokeapi.dev/joke/Any?type={type_v}&amount={amount_v}"

    response = requests.get(url)
    joke_data = response.json()
    joke_data["amount"] = amount_v
    if type_v=="single" or type_v == "twopart":
        i = 0
        while i < amount_v:
            if joke_data["jokes"][i]["type"]=="twopart":
                print(f"Question : {joke_data["jokes"][i]["setup"]}")
                print(f"Answer :{joke_data["jokes"][i]["delivery"]} ")
                print("-----------------------------------------------")
                i+=1
            else:
                print(f"{joke_data["jokes"][i]["joke"]}")  
                print("------------------------------------------------")
                i+=1

        else:
            print("enter valid type ")        
get_joke()

