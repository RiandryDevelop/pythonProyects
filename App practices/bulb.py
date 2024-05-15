import tkinter
 import image

def switch_bulb():
    switch = str(input("Turn off / turn on:"))


switch_bulb()

def bulb(switch):
    if switch == "turn off":
        switch = False

    if switch == "turn on":
        switch = True

    else:
        try:
            switch_bulb()
        except EOFError:
            print(EOFError)



    if switch == True:
      image = Image.open('Img/bulb-off-icon-25991.png')
      print("This bulb is on")

    else:
      image = Image.open("Img/bulb-off-icon-25991.png")
      print("This bulb is on")