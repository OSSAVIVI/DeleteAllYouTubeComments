from selenium import webdriver
from Google import  Google


def main():
    print("Welcome to my Python Bot (it'll delete all yer' YouTube comments. Savvy?)!\n")
    username = "DON'T ENTER USERNAME HERE - DO IT IN DeleteYTCommentsBot.py starting at line #96 (will fix later!) "
    password = "PASSWORD" # enter password here
    Google(username, password)


if __name__ == "__main__":
    main()

