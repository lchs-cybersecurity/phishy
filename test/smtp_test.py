"""
Very simple one-message mail bot. This is basically example code
"""

import smtplib
import json

# Authenticate
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
user = "abc@gmail.com"
passwd = "abc"
server.login(user, passwd)
print("logged in as user {}.".format(user))

# Hit the yeet
recipient = ["b@gmail.com"]
content = r"- .... .. ... / .. ... / .- -. / . -- .- .. .-.. .-.-.-"
server.sendmail(user, recipient, content)

# clean up
server.close()
