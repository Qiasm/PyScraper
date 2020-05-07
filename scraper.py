from time import sleep
import os
import sys
from googlesearch import search
# pip install google


def scraper():
    # Ask the user for the phrase he/she wants to search and max. number of links
    phrase = input("Type in the phrase to search for: ")
    links_number = input("How many links should be found? (More links is equal to longer searching): ")

    # Check if the given input of max. links to show contains digit(s)
    while not links_number.isdigit():
        print("You have to input the number not character(s)!")
        sleep(0.5)
        links_number = input("How many links should be found?: ")

    # Check if the links should be saved to file
    save_to_file = input("Save links to file (Y/N)? (File will be created in the same directory as the program): ")

    while save_to_file != "Y" and save_to_file != "y" and save_to_file != "N" and save_to_file != "n":
        save_to_file = input("You have to answer entering - \"Y\" - Yes or \"N\" - No: ")

    # Set save_to_file variable to True/False and ask how the file should be named
    if save_to_file == "Y" or save_to_file == "y":
        save_to_file = True
        file_name = input("Name the file: ")

        forbidden_chars = "/, \\, :, *, ?, \", <, >, |"
        while "/" in file_name or "\\" in file_name or ":" in file_name or "*" in file_name or "?" in file_name or "\"" in file_name or "<" in file_name or ">" in file_name or "|" in file_name:
            print("File name cannot contain these characters: " + forbidden_chars)
            sleep(0.5)
            file_name = input("Name the file again: ")
    else:
        save_to_file = False

    print('\n' + "Googling...")

    # Scrape links
    if save_to_file:
        f = open(file_name + ".txt", "w")
        for links in search(phrase, stop=int(links_number)):
            f.write(links + '\n')
        print("File has been created there: [" + os.path.dirname(os.path.abspath(file_name + ".txt")) + "\\" + file_name + ".txt" + "] and links have been successfully saved to file!")
        f.close()
    else:
        for links in search(phrase, stop=int(links_number)):
            print(links)

    sleep(0.3)

    restart = input("\nRestart the program (Y/N)? ")
    while restart != "Y" and restart != "y" and restart != "N" and restart != "n":
        restart = input("You have to answer entering - \"Y\" - Yes or \"N\" - No: ")

    if restart == "T" or restart == "t":
        scraper()
    else:
        sys.exit(0)


scraper()
