# We're gonna read a document with a extension .txt


contries_file = open('countris.txt', 'r+')
print("This is our current country list:\n")
for linesX in contries_file.readlines():
    print(linesX)


option = input("Do you want add another country YES O NOT:")

if option.capitalize() == "yes".capitalize():
    def country_add():
        new_country = str(input("Country:"))
        contries_file.write(f"\n{new_country}")
        country_add()

    print("This is the new country list:")
    for lines in contries_file.readlines():
        print(lines)
else:
    breakpoint()


contries_file.close()
