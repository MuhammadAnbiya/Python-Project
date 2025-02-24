# Program yang mensimulasikan permainan batu-gunting-kertas antara dua pemain dan menentukan pemenangnya.

playerOne = input("Masukan pilihan dari pemain satu (kertas/gunting/batu) : ")
playerTwo = input("Masukan pilihan dari pemain dua (kertas/gunting/batu) : ")

if playerOne == "kertas":
    if playerTwo == "batu":
        print("pemain satu menang, kertas mengalahkan batu")
    elif playerOne == playerTwo == "kertas":
        print("Draw sama sama kertas")
    else:
        print("pemain dua menang , gunting mengalahkan kertas")
elif playerOne == "gunting":
    if playerTwo == "kertas":
        print("pemain satu menang, gunting mengalahkan kertas")
    elif playerOne == playerTwo == "gunting":
        print("Draw sama sama gunting!")
    else:
        print("pemain dua menang, batu mengalahkan gunting")
else:
    if playerTwo == "gunting":
        print("pemain satu menang, batu mengalahkan gunting")
    elif playerOne == playerTwo == "batu":
        print("Draw sama sama batu!")
    else:
        print("pemain dua menang, kertas mengalahkan batu")