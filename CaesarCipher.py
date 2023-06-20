logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
""" 
print(logo)
wants_to_play = True
alphabets = "abcdefghijklmnopqrstuvwxyz"

while wants_to_play:
     def encode(message, shift):
         encodedMessage = ""
         for letter in message:
             if letter not in alphabets:
                 encodedMessage += letter
             else:
                 cipherLetterIndex = (alphabets.index(letter) + shift) % len(alphabets)
                 encryptedLetter = alphabets[cipherLetterIndex]
                 encodedMessage += encryptedLetter

         return "The encoded message is: " + encodedMessage
          

     def decode(message, shift):
         decodedMessage = ""
         for letter in message:
             if letter not in alphabets:
                 decodedMessage += letter 
             else:
                 plainLetterIndex = (alphabets.index(letter) - shift) % len(alphabets)
                 decryptedLetter = alphabets[plainLetterIndex]
                 decodedMessage += decryptedLetter
          
         return "The decoded message is: " + decodedMessage


     userChoice = input("Type 'encode' to encrypt, 'decode' to decrypt: ").lower()

     while userChoice != "encode" and userChoice != "decode":
         userChoice = input("Type 'encode' to encrypt, 'decode' to decrypt: ").lower()

     if userChoice == "encode":
         plainText = input('Type your message to be encrypted: ')
         shiftNumber = int(input("Enter the shift number for the cipher: "))
         print(encode(plainText, shiftNumber))

     elif userChoice == "decode":
         cipherText = input("Type your message to be decrypted: ")
         shift = int(input("Enter the shift number for the cipher: "))
         print(decode(cipherText, shift))

     replayPrompt = input("Would you like to have another go? Type 'y' or 'n': ").lower()
     if replayPrompt == "n":
         wants_to_play = False
         print("Thank you for trying out this program.")
     
     elif replayPrompt != "y" and replayPrompt != "n":
         break
