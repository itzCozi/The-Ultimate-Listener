# If your looking into the SRC file and like the structure of my code please follow it and make code more readable.

# Packages
import time
import random

# Functions
def neg_ans():
  negvar1 = random.choice(randans_neg)
  return negvar1
def pos_ans():
  posvar1 = random.choice(randans_pos)
  return posvar1

# vars
randans_neg = ["CodeEntity: I am sorry you are feeling this way.", "CodeEntity: I can understand how that would be difficult.", "CodeEntity: I wish I could make it better.", "CodeEntity: I am sorry that must be difficult.", "CodeEntity: That must be really hard for you.", "CodeEntity: I hope you feel better...", "CodeEntity: Damn, that sounds terrible.", "CodeEntity: Seek help."]
randans_pos = ["CodeEntity: Wow thats sounds cool.", "CodeEntity: I wish I could do that.", "CodeEntity: Yea I agree.", "CodeEntity: Wish I could do that.", "CodeEntity: I am glad you said that.", "CodeEntity: Nice!", "CodeEntity: Wow, that sounds great!", "CodeEntity: I am glad to hear that!"]
rand_wait = random.choice(range(0,4))

# Label
print(" ---------------------- ")
print("| The Ultimate Listener | ")
print(" ----------------------- ")

# Start
pORn = input("Are you going to say positive or negative things? ")
if pORn == "positive" or "pos":
  time.sleep(1)
  classifier = "Positive"
if pORn == "negative" or "neg":
  time.sleep(1)
  classifier = "Negative"
else:
  print("Please enter a valid option.")
  time.sleep(1)
  exit()

# Main
def main():
  print("")
  input("You: ")
  print("------------")
  print("")
  time.sleep(rand_wait)
  if classifier == "Positive":
    print(pos_ans())
    print("------------")
  if classifier == "Negative":
    print(neg_ans())
    print("------------")

# Loop
while True:
  time.sleep(2)
  main()

