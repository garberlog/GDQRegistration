import time

import lxml.html
import requests

# create session
s = requests.session()

# get the login page and then grabbing hidden form fields
login = s.get('https://gamesdonequick.com/auth/login')
login_html = lxml.html.fromstring(login.text)
hidden_inputs = login_html.xpath(r'//form//input[@type="hidden"]')
form = {x.attrib['name']: x.attrib['value'] for x in hidden_inputs}

# login using the hidden forms
form['email'] =  # 'me@example.com'
form['password'] =  # 'password'
response = s.post('https://gamesdonequick.com/auth/login', data=form)

while True:
    # get the amount of registration slots remaining
    profile = s.get('https://gamesdonequick.com/profile')
    profile_html = lxml.html.fromstring(profile.text)
    profile_object = profile_html.xpath(r'//div[@class="col-lg-4"]/p[@class="text-center"]')
    profile_text = profile_object[0].text_content().strip()
    profile_text = profile_text.split(' / ')
    num_registrants = profile_text[0]
    num_allowed = profile_text[1]

    # checks if registration slots are open
    if num_registrants < num_allowed:
        break
    else:
        time.sleep(60)

print('register now')
