
from caesar_cipher.caeser_cipher import (encrypt,decrypt,crack)








def test_encrypt():

   expected=encrypt("hello im ashrf",25)
   actual='gdkkn hl zrgqe'
   assert actual==expected

def test_decrepted():

   expected=decrypt("gdkkn hl zrgqe",25)
   actual='hello im ashrf'
   assert actual==expected

def test_crack():

   expected=crack("hs vzr sgd adrs ne shldr, hs vzr sgd vnqrs ne shldr.")
   actual='it was the best of times, it was the worst of times.'
   assert actual==expected