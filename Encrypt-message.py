import random
import string

class Caesar_Cyper:
    
    message = input("Write your message: ")
      
    def encrypt(self):
        self.lenght_self_encrypted_message = 0
        self.list = ""
        self.encrypted_message = random.choice(string.ascii_letters)
        while self.lenght_self_encrypted_message < len(self.message):
            self.encrypted_message = random.choice(string.ascii_letters)
            self.list += str(self.encrypted_message)
            #print(self.encrypted_message)
            self.lenght_self_encrypted_message += 1
        return self.list #self.encrypted_message   
    
    def decrypt(self):
        self.decrypted_message = self.message
        return self.decrypted_message
    
my_message = Caesar_Cyper()
print("My encrypted message is:", my_message.encrypt())
print("My decrypted message is:", my_message.decrypt())