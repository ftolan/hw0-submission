import os
error = False

if os.path.basename(os.path.realpath('.')) != "hw0-submission":
    print("The name of the current directory should be 'hw0-submission'")
    error = True

if not error:
    print("You did everything correctly. Congrats!")
