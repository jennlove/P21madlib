print ("Welcome to Mad Libs\n")

def get_word(part_of_speech):
    if (part_of_speech == 'noun'):
        return input("Enter a noun: ")
    elif (part_of_speech == 'verb'):
        return input("Enter a verb (not an ing form): ")
    elif (part_of_speech == 'adj'):
        return input("Enter an adjective: ")
    elif (part_of_speech == 'name'):
        return input("Enter a person's name: ")

print("My " + get_word('noun') + " has a " + get_word('adj') + " name. It's " + get_word('name') + ". "
      "You'd better not " + get_word('verb') + "!")
