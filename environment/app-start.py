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
        curUser = NULL
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
        
        #do perform move stuff (when we get the game logic up)

if __name__ == "__main__":
    main()