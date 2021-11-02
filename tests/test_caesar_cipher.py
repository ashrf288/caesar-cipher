
from caesar_cipher.caeser_cipher import (encrypt,decrypt,crack)
import nltk







def test_encrypt():

   expected=encrypt("hello im ashrf",25)
   actual='gdkkn hl zrgqe '
   assert actual==expected

def test_decrepted():

   expected=decrypt("gdkkn hl zrgqe",25)
   actual='hello im ashrf '
   assert actual==expected

def test_crack():

   expected=crack("gdkkn hl zrgqe")
   actual='hello im ashrf '
   assert actual==expected