def check_string(text):
    if text.startswith("The"):
         return "Yes !"
    else:
         return "No!"

str1 = "The"
str2 = "Thumbs up"
str3 = "Theatre can be boring"

print(check_string(str1)) # Yes!
print(check_string(str2)) # No!
print(check_string(str3)) # Yes!

