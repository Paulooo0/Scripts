import re

email = input("What's your email? ").strip().lower()

#               [a-zA-Z0-9_\.] == [\w.]
if re.search(r'^[a-zA-Z0-9_\.]+@(\w+\.)?\w+\.(com|gov|edu|net|or)$', email, re.IGNORECASE):
    print('Valid')
else:
    print('Invalid')

# Gmail_email_search = re.search(^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]
#                                 +@[a-zA-Z0-9]
#                                 (?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?
#                                 (?:\.[a-zA-Z0-9]
#                                 (?:[a-zA-Z0-9-]{0,61}
#                                 [a-zA-Z0-9])?)*$, email)




