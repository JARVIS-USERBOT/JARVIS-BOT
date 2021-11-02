from telethon.sessions import StringSession
from telethon.sync import TelegramClient
import random
from colorama import Fore, Style, Back


message = """
JARVIS BOT"""
logo = """
"""
                                                                                                            
print("")
print(Style.BRIGHT + Fore.MAGENTA + Legend)
print(Style.RESET_ALL)
print(Style.BRIGHT + Fore.BLUE + logo)
print(Style.RESET_ALL)
print(Style.BRIGHT + Fore.CYAN + Back.BLUE + bhai_bolte)
print(Style.RESET_ALL)
print("""Welcome To JARVIS String Generator""")
print("""Kindly Enter Your Details To Continue ! """)

API_KEY = input("API_KEY: ")
API_HASH = input("API_HASH: ")

while True:
    try:
        with TelegramClient(StringSession(), API_KEY, API_HASH) as client:
            print("String Sent To Your Saved Message, Store It To A Safe Place!! ")
            print("")
            session = client.session.save()
            client.send_message(
                "me",
                f"Here is your TELEGRAM STRING SESSION\n(Tap to copy it)👇 \n\n `{session}` \n\n ",
            )

            print(
                "JARVIS-USERBOT"
            )
    except:
        print("")
        print(
            "Wrong phone number \n make sure its with correct country code. Example : +919811099999 ! Kindly Retry"
        )
        print("")
        continue
    break
