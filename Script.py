# Morse code dictionary 
morse = { ".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E", "..-.": "F", "--.": "G", "....": "H", "..": "I", ".---": "J", "-.-": "K", ".-..": "L", "--": "M", "-.": "N", "---": "O", ".--.": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T", "..-": "U", "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y", "--..": "Z" }

# input string (continuous morse like ......-...) 

encrypted = input().strip() 

# list to store all possible decoded words 

results = []

 # recursive function
def decode(index, current): 
  # base case: reached end of string 
  if index == len(encrypted):         
   results.append(current) 
   return 
  
  # try every possible split
  for i in range(index + 1, len(encrypted) + 1):
    part = encrypted[index:i]
    if part in morse: 
     decode(i, current+morse[part])

 # start decoding

decode(0, "") 

# print results in alphabetical order 

for word in sorted(results):     
   print(word)



#Input
# -.--.

#Output
# KN
#KTE
#NG
#NME
#NTN
#NTTE
#TAN
#TATE
#TEG
#TEME
#TETN
#TETTE
#TP
#TWE
#YE
