import sys 


text_from_node_server = str(sys.argv[1])

if(text_from_node_server == "hi"):
	response = "Hi and welcome to UML first every NBA Chatbot!!"
else:
	response = "I'm sorry I don't understand what you are talking about" 


print(response)
sys.stdout.flush()