def palindrome(word):
  word.replace(" ", "")
  check = [i.lower() for i in word if i.isalnum()]
  check.reverse()
  broken = [i.lower() for i in word if i.isalnum()]

  if check == broken:
    print("True")
  else:
    print("False")
