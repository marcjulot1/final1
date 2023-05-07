
from api import result
from ssa import list

response = ""

while True:
    command = input(
        "How are you feeling today (happy, sad, mad, angry, frustrated)? or'quit':")
    if command.lower() == "happy":
        response = "I am glad that you are happy"
        new = (list.sample())
        print("Lets keep the party going with a positive quote.",
              response, "\n", new)
    elif command.lower() == "sad":
        response = "To be truly happy, you must practice smiling. Go ahead and smile."
        new = (list.sample())
        print(
            "I am sorry you are feeling that way. Hope this quote cheers you up!", response, "\n", new)
    elif command.lower() == "mad":
        new = (list.sample())
        print("I am sorry that you are feeling mad, I hope this quote can lighten your mood!",
              response, "\n", new)
    elif command.lower() == "angry":
        response = "You got this, anger fades!"
        new = (list.sample())
        print("I am sorry you are feeling angry, maybe this quote will get you in a better mood.", response, "\n", new)
    elif command.lower() == "frustrated":
        new = (list.sample())
        response = "It only means that you are having a hard time right now. Tomorrow it will be better."
        print("I am sorry you are feeling frustrated. Please read this quote to help.",
              response, "\n", new)
    elif command.lower() == "quit":
        break
    else:
        print("You have made an error, please try again.")
