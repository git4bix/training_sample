
play_list = []

def lagay():
    lag1 = input("Please put the song you want to add: ")
    play_list.append(lag1)
    App_z()

def tanggal():
    global play_list
    if play_list == [] :
        print("Your list is empty!!")
    else:
        for ind, kta in enumerate(play_list, start=1):
            print(f"Song: {ind}. {kta}")

        ere = int(input("please the song to remove: "))
        for indi, kta in enumerate(play_list, start=1):
            if ere == indi:
                #ere += 1
                #play_list.pop(int(indi))
                print(play_list.pop(indi-1))
                print("song has been removed")
    App_z()

def kita():
    print("Please choose the song you want to play: ")
    for ind, kta in enumerate(play_list, start=1):
        print(f"Song: {ind}. {kta}")

    ere = int(input("enter the song number: "))

    for indi, kta in enumerate(play_list, start=1):
        if ere == indi:
            # ere += 1
            # play_list.pop(int(indi))
            print("You are playing:", play_list[indi-1])
            print(play_list.pop(indi - 1))

    App_z()

def pakita():
    if play_list == [] :
        print("Your list is empty!!")
    else:
        for ind, kta in enumerate(play_list, start=1):
            print(f"Song: {ind}. {kta}")
    App_z()

def tigil():
    print("Bye bye thank you!")
    exit()



def App_z():
    print("My playlist:")
    print("choose an option below: \n")
    reco = ["Add","Remove","Play","Show all","exit"]
    for index, listahan in enumerate(reco, start=1):
        print(index, listahan)

    pili = int(input("Input number: "))
    if pili == 1:
        lagay()
    elif pili == 2:
        tanggal()
    elif pili == 3:
        kita()
    elif pili == 4:
         pakita()
    elif pili == 5:
        tigil()
    else:
        print("Wrong input try again")
        App_z()

App_z()




