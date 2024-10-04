import re
# print(1)

# ascii_rus_codes = [i for i in range(1040, 1103+1, 1)]
# ascii_rus_codes += [1105, 1025] # is created to check whether the letter is RUS
alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 
            'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 
            'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', 'ё']
# print(list(chr(char) for char in ascii_rus_codes))    
print(len(alphabet))


special_symbols_remover = lambda string: re.split('; |!| |, |\.|\?|-', string) 

# print(''.join(special_symbols_remover("Do u wanna! go.")).lower())

# if 1077 1105
# print(ord('а') - 1072)
# print(ord('я') - 1072)

class Caesar():
    def __init__(self) -> None:
        self.m = 32
        self.encrypted = []
        self.preprocessed_text = ''
        
    def encryption(self):
        given_text = input("Текст, который будем шифровать: ")
        print(len(given_text.split()))
        if len(given_text.split()) > 1: # for cases when we put preprocessed data
            self.preprocessed_text = ''.join(special_symbols_remover(given_text)).lower() 
        else: self.preprocessed_text = given_text
        print(self.preprocessed_text)
        en_key = int(input("Ключ шифрования: "))
        encoded = [char for char in range(len(self.preprocessed_text))]
        self.encrypted = encoded
        encrypted_text = ['' for x in self.encrypted]
        for index in range(len(self.preprocessed_text)):
            if self.preprocessed_text[index] in alphabet:   # проверка на русскую букву
                ascii_number = ord(self.preprocessed_text[index])  
                if ascii_number in {1077, 1105}:
                    encoded[index] = 5
                else: encoded[index] = ord(self.preprocessed_text[index]) - ord("а")
                # encoded[index] = 
                self.encrypted[index] = (encoded[index] + en_key) % self.m
        # encrypted = [str(char) for char in encrypted]
                encrypted_text[index] = chr(self.encrypted[index] + ord("а"))

        with open("encrypted_text.txt", "w") as f:
            f.writelines(f'Зашифрованный текст: {encrypted_text}\n')
            f.writelines(f'Ключ: {en_key}')
    def decryption(self):
        open("decrypted.txt", "w").close()
        print('---------------------')
        # 5 times if not guessing
        iterations = 0
        decoded = [char for char in self.encrypted]

        decrypted = [str(letter) for letter in decoded]
        print(f'preprocessed: {self.preprocessed_text}')
        while not (''.join(decrypted) == self.preprocessed_text):
            dec_key = int(input('Ключ расшифровки: '))
            
            for index in range(len(decoded)):
                if str(decoded[index]).isdigit():
                    decoded[index] = (self.encrypted[index] - dec_key) % self.m
                    decrypted[index] = chr(decoded[index] + ord('а'))  
            with open("decrypted.txt", "a") as f:
                f.write(f'key: {dec_key},\ndecrypted text:{decrypted} \n')
                f.write('---------------\n')
            print(decrypted)
            print(''.join(decrypted), self.preprocessed_text, ''.join(decrypted) == self.preprocessed_text)
            iterations += 1

c = Caesar() 
c.encryption()


# m = 32
# encrypted = 'юмуумфгямнмфапфъувтеипущмутмкюмфчзйпушжувмрпщмуммймчфммкъипушчмлгхихтгшщпщмтгфвьшмщмр'
# decoded = [char for char in range(len(encrypted))]
# decrypted = ['' for char in decoded]

# for key in range(1, m+1, 1):
#     for index in range(len(encrypted)):
#         ascii_number = ord(encrypted[index])
#         if ascii_number in {1077, 1105}:
#             decoded[index] = 5
#         else: decoded[index] = ord(encrypted[index]) - ord("а") # to number
#         # for index in range(len(decoded)):
#         decoded[index] = (decoded[index] - key) % m
#         decrypted[index] = chr(decoded[index] + ord('а'))  # back to ascii
#         if index == len(encrypted)-1: print(f'{key}, {''.join(decrypted)}')

# чем меньше женщину мы любим тем легче нравимся мы ей и тем ее вернее губим средь обольстительных сетей
# key - 7, new phrase to encrypt:  пушкиневгенийонегин

# 2.3
given_text = "пушкиневгенийонегин"
encrypted_text = 'цъяспфмйкмфпрхфмкпф'





# ё - 1105
# Ё - 1025  
# e - 1077 
# -> 1077 EQUALS 1105 (is gonna be coded by the ONE number)
# -> 1025 EQUALS 1045


# for i in range(1000, 1150, 1):
#     if chr(i) == "Ё":  print(i)
