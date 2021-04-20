def replace_star():
    answer = ""
    global word

    for letter in word:
        if letter == "*":
            answer +=","
        else:
            answer += letter

    word = answer

word = "a*b*c*d*"
replace_star()
print(word)