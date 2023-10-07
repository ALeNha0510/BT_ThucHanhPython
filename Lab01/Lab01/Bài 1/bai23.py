def substring_copy(text, n):
  length = 2
  if length > len(text):
    length = len(text)
  substr = text[:length]
  result = ""

  for i in range(n):
    result = result + substr
  return result

print(substring_copy('Anh', 2))
print(substring_copy('T', 3))
