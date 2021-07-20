# importing the library
import pyperclip,re

#Phone Regex 
phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))?                      # area code
(\s|-|\.)?                              # seperator
(\d{3})                                 # first three digit
(\s|-|\.)                               # seperator
(\d{4})                                 # last 4 digits
(\s*(ext|x|ext.)\s*(\d{2,5}))?          # extension
)''', re.VERBOSE)

#Email Regex
emailRegex = re.compile(r'''(
[a-zA-Z0-9._%+-]+           # username
@                           # @ symbol
[a-zA-Z0-9.-]+              # domain name
(\.[a-zA-Z]{2,4})           # dot-something
)''', re.VERBOSE)

#copy  to clipboard
# Find matches in clipboard text.
def find_matches():
    text = str(pyperclip.paste())
    matches = []
    for groups in phoneRegex.findall(text):
        phoneNum ='-'.join([groups[1],groups[3],groups[5]])
        if groups[8] != '':
            phoneNum += ' x' + groups[8]
        matches.append(phoneNum)
    for groups in emailRegex.findall(text):
        matches.append(groups[0])
    
    return matches
    
    

# Copy results to the clipboard.
def copy_results():
    matches = find_matches()
    if len(matches) > 0:
        pyperclip.copy('\n'.join(matches))
        print('Copied to clipboard:')
        print('\n'.join(matches))
    else:
        print('No phone numbers or email addresses found.')
    
    return

if __name__ == '__main__':
    find_matches()
    copy_results()
