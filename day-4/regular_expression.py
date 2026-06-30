import re

text="""
this is my list of email id's
123@gmail.com
456@yahoo.com
789@outlook.com
abc@hotmail.com
zeeshan.kanuga@gmail.com
where all desired emails are stored in this file.
"""

# \b isolates the pattern to find emails anywhere in the text block
list_of_emails = re.findall(r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b", text)
print(list_of_emails)
 