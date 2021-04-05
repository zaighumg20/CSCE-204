friends = ["Amy", "Bobby", "Jackson" , "Andy" , "Brian"]


with open(friends.txt, "w") as file:
    for friends in friends:
        file.write(f"friends}\n")