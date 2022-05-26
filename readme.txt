Group Members
	Eric Clark
	Sean Brzoska
	Tristan Digert

API gateway
	https://q9ziogix3f.execute-api.us-west-1.amazonaws.com/prod

Lambda Function Source and Scripts
	The source code for the lambda function is in envioronment/application
	The updated scripts to configure everything in AWS are in environment/scripts

CLI
	cli is in the environment folder.
	In the folder containing app-start.py run:

	pip install requests
	python3 app-start/py

	Then follow printed instructions in the command prompt.

Challenges

	***One skip day will be used***
	
	The most challenging part was using the calls in python to connect to the API. Since most of us had no experience using requests.get and requests.post, we troubleshot headers and trying to use get/post. After trial and error for a while we got the connections working, this took longer then expected. After that it was a simple task of filling out the features we wanted in the CLI. The only issues we had there were many simple syntax errors since we were unfamiliar with json.

Features
	From what we know, there are no missing features. Some extra features were added so you don't get kicked out of the program after making a move. You can load the last gameID used by accessing "saved game" as option 3 after logging in. Finally, you aren’t limited to one game while in the CLI. Once you make a move in one game, you can enter a different gameID and make a move there.
