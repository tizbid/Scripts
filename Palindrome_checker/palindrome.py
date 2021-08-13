#Script to check whether a string is a Palindrome or not

def palindrome_check(word):
  
  if word.lower()== word.lower()[::-1] :
    print('is a Palindrome')
  else:
    print('not a Palindrome')
    
  return

if __name__=='__main__':
  palindrome_check(input('Enter a word:'))