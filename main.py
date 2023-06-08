import logo

alphabet = [
  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
  'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',   'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
  'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

print(logo.logo)

def caesar(text, shift, direction):
  shift = shift % 26
  new_text = ""
  if direction == "decode":
    shift *= -1
  for letter in text:
    if letter not in alphabet:
      new_text += letter
    else:
      new_text += alphabet[alphabet.index(letter) + shift]  
  return new_text

keep_going = True

while keep_going:

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  print(caesar(text, shift, direction))
  if input("Continue? ") != "yes":
    keep_going = False
