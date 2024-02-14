dict_1 = {"one":"1",
          "two":"2",
          "three":"3",
          "four":"4",
          "five":"5",
          "six":"6",
          "seven":"7",
          "eight":"8",
          "nine":"9",
          "zero":"0"}
strs = input("Enter the string..").lower()
#four five zero six
res = " ".join(dict_1[i] for i in strs.split())
print("The string is",res)
