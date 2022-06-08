from multiprocessing import get_all_start_methods
import requests
import json


BASE_URL = "https://66h22fk3p8.execute-api.us-west-1.amazonaws.com/prod" #server url

def main():
    usrName = ""
    #curGame = null
    startLoop = False
    apiToken = ""
    curUserData = ""
    idToken = ""
    while startLoop == False :
        print("Welcome! Please enter \"1\" to sign in or \"2\" to sign up!")
        init_select = input(">")
        if init_select == "1":
            #login
            print("Please enter your username: ")
            usrName = input(">")
            print("Please enter your password: ")
            usrPassword = input(">")
            usrDat = {"username": usrName, "password": usrPassword}
            usrDatJson = json.dumps(usrDat)
            curUser = requests.post(BASE_URL + '/login', data = usrDatJson, headers={'Content-Type': 'application/json'})
            curUserData = json.loads(curUser.text)
            if "message" in curUserData: #error was returned
                print("Server returned error:")
                print(curUserData["message"])
            else:
                startLoop = True
                idToken = curUserData['idToken']
            
        elif init_select == "2":
            #sign up
            print("Please enter your username: ")
            usrName = input(">")
            print("Please enter your new email: ")
            usrEmail = input(">")
            print("Please enter your new password: ")
            usrPassword = input(">")
            usrDat = {'username':usrName, 'password':usrPassword, 'email':usrEmail}
            usrDatJson = json.dumps(usrDat)
            curUser = requests.post(BASE_URL + '/users', data = usrDatJson, headers={'Content-Type': 'application/json'})
            curUserData = json.loads(curUser.text)
            if "message" in curUserData: #error was returned
                print("Server returned error:")
                print(curUserData["message"])
            else:
                print("Please verify email then login")
        else:
            print("Please enter a valid selection")
    menuLoop = False
    gameId = None
    curGameData = ""
    while menuLoop == False:
        
        print("***Main Menu***")
        print("Enter 1 to start a new game\nEnter 2 to access an existing game\nEnter 3 to access saved game\nEnter 4 to exit program")
        menu_select = input(">")
        if menu_select == "1":
            print("Enter opponent: ")
            opponent = input(">")
            gameDat = {"opponent" : opponent}
            usrDatJson = json.dumps(gameDat)
            curGame = requests.post(BASE_URL + '/games', data = usrDatJson, headers = {'Content-Type': 'application/json', "Authorization" : curUserData["idToken"]})
            curGameData = json.loads(curGame.text)
            if "message" in curGameData: #error was returned
                if curGameData["message"] == "Cannot read property 'Username' of undefined":
                    print("User was not found :(\n")
                else:
                    print("Server returned error:")
                    print(curGameData["message"])
            else:
                print("Challenge Sent!")
                gameId = curGameData["gameId"]
            
        elif menu_select == "2":
            print("Enter game id: ")
            gameId = input(">")
            curGameData = requests.get(BASE_URL + '/games/' + gameId, headers = {'Content-Type': 'application/json', "Authorization" : curUserData["idToken"]})
            if curGameData.text == "":
                print("Invalid game Id\n")
            else:
                print(curGameData.text)
                curGameData = json.loads(curGameData.text)
                # need to handle case where the game has been deleted/ there is no game state.
                if "message" in curGameData:
                    print("That game ID does not exist\n")
                else:
                    performMove(curGameData, curUserData, gameId, usrName)

        elif menu_select == "3":
            print("Checking last saved game...")
            if gameId != None:
                curGameData = requests.get(BASE_URL + '/games/' + gameId, headers = {'Content-Type': 'application/json', "Authorization" : curUserData["idToken"]})
                if curGameData.text == "":
                    print("Invalid game Id\n")
                else:
                    curGameData = json.loads(curGameData.text)
                    performMove(curGameData, curUserData, gameId, usrName)
            else:
                print("No saved game :(\n")

        elif menu_select == "4":
            exit()
        else:
            print("Please enter a valid selection\n")

def performMove(curGameData, curUserData, gameId, usrName):
    gameLoop = False
    entryLoop = False

    print("Welcome! Here is the current game state:")
    board = curGameData["board"]
    
    printBoard(board)
    print("The last user to move was: " + str(curGameData["lastMoveBy"]))
    if curGameData["lastMoveBy"] == usrName:
        print("You made the last move...")
        print("Returning to menu\n")
        return
    
    moveColumn = 1
    moveRow = 1
    moveSpot = 1
    
    while entryLoop == False:
    
        print("Please enter the column you want to move in: ")
        moveColumn = input(">")
        print("Please enter the row you want to move in: ")
        moveRow = input(">")
        if (moveColumn != "1" and moveColumn != "2" and moveColumn != "3") and (moveRow != "1" and moveRow != "2" and moveRow != "3"):
            print("Invalid entry. Please enter a value between 1 and 3")
        else:
            entryLoop = True
    
    moveColumn = int(moveColumn)
    moveRow = int(moveRow) - 1
    moveSpot = (moveRow*3) + moveColumn
    print("Sending move...")
    moveDat = {"coords": moveSpot}
    moveDatJson = json.dumps(moveDat)
    send = requests.post(BASE_URL + "/games/" + gameId, data = moveDatJson, headers = {'Content-Type': 'application/json',"Authorization" : curUserData["idToken"]}) #send move data, will figure out format soon
    verifyMove = json.loads(send.text)
    if "message" in verifyMove: #error was returned
        print("Server returned error:")
        print(verifyMove["message"])
    else:
        print("Move sent!")

def printBoard(board):
    print("   |   |   ")
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("___|___|___")
    print("   |   |   ")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("___|___|___")
    print("   |   |   ")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print("   |   |   ")


if __name__ == "__main__":
    main()