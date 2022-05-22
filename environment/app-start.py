from multiprocessing import get_all_start_methods
import requests
import json

def main():
    curUser = NULL
    curGame = NULL
    startLoop = False
    resp = requests.get("some-url")
    if resp != 200:
        print ("error connecting to service")
        return

    while startLoop == False :
        print("Welcome! Please enter \"1\" to sign in or \"2\" to sign up!")
        init_select = input(">")
        if init_select == "1":
            #login
            startLoop = True
            print("please enter your email: ")
            usrEmail = input(">")
            print("please enter your password: ")
            usrPassword = input(">")
            usrDat = {"email":" usrEmail", "password":"usrPassword"}
            usrDatJson = json.dumps(usrDat)
            payload = {"json_payload":usrDatJson, 'apikey': "Do we need this?"}
            curUser = requests.get('some url/users', data = payload)
            requests.post()
        elif init_select == "2":
            #sign up
            startLoop = True
            print("please enter your new email: ")
            usrEmail = input(">")
            print("please enter your new password: ")
            usrPassword = input(">")
            usrDat = {"email":" usrEmail", "password":"usrPassword"}
            usrDatJson = json.dumps(usrDat)
            payload = {"json_payload":usrDatJson, 'apikey': "Do we need this?"}
            curUser = requests.get('some url/login', data = payload)
        else:
            print("Please enter a valid selection")
    menuLoop = False
    while menuLoop == false:
        
        print("Enter 1 to start a new game, or 2 to access an existing game")
        menu_select = input(">")
        if menu_select == "1":
            menuLoop == True
            print("Enter opponent: ")
            opponent = input(">")
            gameDat = {"opponent" : opponent}
            usrDatJson = json.dumps(usrDat)
            payload = {"json_payload":usrDatJson, 'apikey': "Do we need this?"}
            curGame = requests.get('some url/games', data = payload)
        elif menu_select == 2:
            menuLoop == True
            print("Enter game id: ")
            gameId = input(">")
            curGame = requests.get('some url/games', data = payload)
    
     
gameLoop = False
entryLoop = False
print("Welcome! Here is the current game state:")
board = requests.get('get from DB')
print(board[0]+ " " +board[1]+ " " +board[2])
print(board[3]+ " " +board[4]+ " " +board[5])
print(board[6]+ " " +board[7]+ " " +board[8])

moveColumn = 1
moveRow = 1

while entryLoop == False:

    print("Please enter the column you want to move in: ")
    moveColumn = input(">")
    print("Please enter the row you want to move in: ")
    moveRow = input(">")
    if (moveColumn > 3 or moveColumn < 1) or (moveRow > 3 or moveRow < 1):
        print("Invalid entry. Please enter a value between 1 and 3")
    elif board [((moveRow-1)*3) + (moveColumn-1)] != "0":
        print("Cannot move there! Please select a valid location!")
    else:
        entryLoop = True

print("Sending move...")
send = requests.get() #send move data, will figure out format soon

if __name__ == "__main__":
    main()
