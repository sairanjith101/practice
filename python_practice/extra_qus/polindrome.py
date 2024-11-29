# word = "radar"
word = "hello"

rev_word = word[::-1]

if word == rev_word:
    print(True)
else:
    print(False)

def rev_word(word):
    output = word[::-1]
    if word == output:
        print(True)
    else:
        print(False)

rev_word("radar")
    
