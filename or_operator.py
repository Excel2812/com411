# Ask user for what type of adventure

print("What type of adventure should i have?")
adventure_type = input()

# Determine what message to display
if (adventure_type == "scary") or (adventure_type == "short"):
    print("Entering the dark forest!")

elif (adventure_type == "safe") or (adventure_type == "long"):
    print("Taking the safe route!")

else:
    print("Not sure which route to take.")



