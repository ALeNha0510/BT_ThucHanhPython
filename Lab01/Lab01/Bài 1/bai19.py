def new_string(text):
  if len(text) >= 2 and text [:2] == "ls":
    return text
  return "ls" + text

print(new_string("Array"))
print(new_string("IsEmpty"))