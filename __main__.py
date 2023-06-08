import gas

def displayDialog(dialog):
    print(dialog["dialog"])
    print("Enter option:")
    options = dialog["options"]
    for i, option in enumerate(options):
        print(f"{i}. {option[1]}")
    choice = input("> ")
    return int(choice) if choice.isdigit() else choice

def runGame():
    gameData = gas.get("game.json")
    
    currentDialogIndex = 0
    while True:
        currentDialog = gameData[currentDialogIndex]
        choice = displayDialog(currentDialog)
        
        if isinstance(choice, int) and 0 <= choice < len(currentDialog["options"]):
            nextDialogIndex = currentDialog["options"][choice][0]
            currentDialogIndex = nextDialogIndex
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    runGame()
