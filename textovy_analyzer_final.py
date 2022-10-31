

from curses.ascii import isalpha, isdigit, islower, isupper
from unittest import result
from data import TEXTS, customers
import os, time
from getpass import getpass

# TEXTOVY ANALYZER

# Vase zadanie na stranke ENGETO vypisovalo vysledky na zaklade analyzy prveho
# textu. Porovnal som si ich s mojimi vysledkami a najprv mi to sedelo, no 
# neskor som si pri testoch vsimol, ze napriklad pri TITLECASE words ukazuje
# 12 slov. Myslim si, ze tam zaratava aj retazec US, ktory sa vzapati 
# vyhodnoti aj ako UPPERCASE. Asi sa u vas tiez kontroluje iba prvy znak. Ponechal
# som to podla vasho vypoctu, aby sedeli vysledky. Inak by bol zapis na kontrolu :
# 
# count_of_words_title = 0
# for word in words :
#    if word[0].isupper() and word[1:].islower() :
#        count_of_words_title += 1
#
# Takisto som si vsimol, ze medzi LOWERCASE words sa mi nezapocitalo
# slovo v druhom texte "buff-to-white" kvoli pomlckam, pretoze som to
# kontroloval iba s islower(). To by sa dalo osetrit napriklad :
#
# if "-" in word :
#   word = word.replace("-","")
#
# Pisem to sem vlastne kvoli tomu, keby to boli nahodou chytaky :DDD

"""

projekt_1.py: první projekt do Engeto Online Python Akademie
author: Juraj Batoška
email: juraj.batoska@gmail.com
discord: juraj.batoska#9280

"""

def clrscr() :
    os.system('clear')
    #os.system('cls') # PRE INE OPERACNE SYSTEMY 

def title():
    clrscr()
    print()
    print("-" * 55)
    print("|" + f"{status_txt:^53}" + "|")
    TXT = "TEXT ANALYZER"
    print("-" * 55)
    print("|" + f"{TXT:^53}" + "|")
    print("-" * 55)

def login():
    print("\nLOGIN :")
    user_name = input("Username : ")
    user_password = getpass("Password : ")
    
    customers_keys = customers.keys()
    customers_values = customers.values()
    customers_items = customers.items()
    
    for customers_keys, customers_values in customers_items :
        
        if customers_keys == user_name and customers_values == user_password :
            login_status = True
            return login_status, user_name
        
        else :
            continue

    login_status = False
    return login_status, user_name

def option_menu() :
    title()
    print("|" + "  text", end="")
    print(f"\033[1;33;33m1 ", end="")
    print("\033[1;33;0m| text",end="")
    print(f"\033[1;33;33m2 ", end="")
    print("\033[1;33;0m| text",end="")
    print(f"\033[1;33;33m3 ", end="")
    print("\033[1;33;0m| an",end="")
    print(f"\033[1;33;33ma", end="")
    print("\033[1;33;0mlyse | ",end="")
    print(f"\033[1;33;33ml", end="")
    print("\033[1;33;0mog out  |  ",end="")
    print(f"\033[1;33;33me", end="")
    print("\033[1;33;0mnd  |")
    print("-" * 55)

def analyse(analyse_option) :   
    if analyse_option == 1 :
        text_to_analyze = TEXTS[0]
    
    elif analyse_option == 2 :
        text_to_analyze = TEXTS[1]
    
    elif analyse_option == 3 :
        text_to_analyze = TEXTS[2]
      
    temp_words = text_to_analyze.split()
    words = []

    for word in temp_words :
        word = word.strip(",")
        word = word.strip(".")
        word = word.strip(":") # v pripade analyzy ineho textu, kde by sa ':' vyskytovala
        words.append(word)

    # TEST VSETKY SLOVA
    # print()
    # for word in words :
    #     print("Word : ",word)

    count_of_words = len(words)

    count_of_words_title = [w for w in words if w[0].isupper()]
    #count_of_words_title = [print("Title : ",w) for w in words if w[0].isupper()] # TEST TITTLE 
    count_of_words_title = len(count_of_words_title)

    count_of_words_upper = 0
    for word in words :   
        if word.isalpha() and word.isupper() :
            #print("Uppercase : ",word) # TEST UPPERCASE
            count_of_words_upper +=1

    count_of_words_lower = 0
    for word in words : 
        if word.isalpha() and word.islower() :
            #print("Lowercase : ", word) # TEST LOWERCASE
            count_of_words_lower += 1

    count_of_numeric_strings = 0
    numbers = []
    for number in words :
        if number.isdigit():
            number = int(number)
            #print("Number : ",number) # TEST NUMERIC STRINGS
            count_of_numeric_strings += 1
            numbers.append(number)
    
    sum_of_numbers = sum(numbers)
    print()

    ### SINGULAR VS PLURAL V ANGLICTINE ###
    
    if count_of_words == 0 :
        count_of_words_txt = "There are not any words."
    elif count_of_words == 1 :
        count_of_words_txt = "There is 1 word."
    else :
        count_of_words_txt = f"There are {count_of_words} words."
    
    if count_of_words_title == 0 :
        count_of_words_title_txt = "There are not any titlecase words.."
    elif count_of_words_title == 1 :
        count_of_words_title_txt = "There is 1 titlecase word."
    else :
        count_of_words_title_txt = f"There are {count_of_words_title} titlecase words."
        
    if count_of_words_upper == 0 :
        count_of_words_upper_txt = "There are not any uppercase words."
    elif count_of_words_upper == 1 :
        count_of_words_upper_txt = "There is 1 uppercase word."
    else :
        count_of_words_upper_txt = f"There are {count_of_words_upper} uppercase words."
    
    if count_of_words_lower == 0 :
        count_of_words_lower_txt = "There are not any lowercase words."
    elif count_of_words_lower == 1 :
        count_of_words_lower_txt = "There is 1 lowercase word."
    else :
        count_of_words_lower_txt = f"There are {count_of_words_lower} lowercase words."

    if count_of_numeric_strings == 0 :
        count_of_numeric_strings_txt = "There are not any numeric strings."
    elif count_of_numeric_strings == 1 :
        count_of_numeric_strings_txt = "There is 1 numeric string."
    else :
        count_of_numeric_strings_txt = f"There are {count_of_numeric_strings} numeric strings."
 
    print(f"\n*** ANALYSE OF TEXT{analyse_option} ***\n")
    print(f"{count_of_words_txt}")
    print(f"{count_of_words_title_txt}")
    print(f"{count_of_words_upper_txt}")
    print(f"{count_of_words_lower_txt}")
    print(f"{count_of_numeric_strings_txt}")
    print(f"The sum of all the numbers is {sum_of_numbers}.")
    
    letters_in_word = { 1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0, 6 : 0, 7 : 0,
     8 : 0, 9 : 0, 10 : 0, 11 : 0, 12 : 0, 13 : 0, "more" : 0
     }
    
    for letter in words:
        if len(letter) > 13 :
            letters_in_word["more"] +=1
            continue
        letters_in_word[len(letter)] += 1

    print()
    print("-" * 49)
    print("|   LEN   |    OCCURENCES             |   NR.   |")
    print("-" * 49)

    letters_in_word_keys = letters_in_word.keys()
    letters_in_word_values = letters_in_word.values()
    letters_in_word_items = letters_in_word.items()

    for letters_in_word_keys, letters_in_word_values in letters_in_word_items :
        if letters_in_word_values > 0 :
        
            if letters_in_word_values > 20 :
                asterix = letters_in_word_values # maximalny pocet hviezdiciek, po prekroceni zobrazi cislo miesto hviezdiciek
            else :
                asterix = "*" * letters_in_word_values

            print(f"|{letters_in_word_keys:^9}|    {asterix:<23}|{letters_in_word_values:^9}|")

    print("-" * 49)
    print()
    input()
    
def enter_to_return() :
    print("\nENTER to return ...", end="")
    input()

def wrong_option() :
    print("\033[1;33;31m\nWrong option !", end="")
    print("\033[1;33;0m",end="")
    time.sleep(2.5)

status_txt = "Status : Not logged in"  
login_status = False

while True :
    title()
    result = login()
    login_status = result[0]
    user_name = result[1]

    if login_status:
        print(f"\033[1;33;32m\nLogin sucessful !", end="")
        print("\033[1;33;0m",end="")
        time.sleep(2.5)

    else : 
        print("\033[1;33;31m\nWrong username, or password !", end="")
        print("\033[1;33;0m",end="")
        time.sleep(2.5)
        continue

    while True :
        status_txt = f"Welcome to the app, {user_name.capitalize()}!"
        option_menu()    
        option = input("\nOption : ")
        option = option.lower().strip()
        
        if option == "end" or option == "e" :
            print(f"\nUser '{user_name.capitalize()}' logged out!\n")
            time.sleep(2.5)
            clrscr()
            quit()
        
        elif option == "logout" or option == "log out" or option == "l" :
            login_status = False
            status_txt = "Status : Not logged out"  
            print(f"\nUser '{user_name.capitalize()}' logged out!\n")
            time.sleep(2.5)
            break
        
        elif option == "text1" or option == "1" :
            option_menu()
            print(f"{TEXTS[0]}")
            enter_to_return()    

        elif option == "text2" or option == "2" :
            option_menu()
            print(f"\n{TEXTS[1]}")
            enter_to_return()          

        elif option == "text3" or option == "3" :
            option_menu()
            print(f"\n{TEXTS[2]}")
            enter_to_return()           
            
        elif option == "analyse" or option == "a" :
            while True :
                option_menu()
                print("\nEnter a number btw. 1 and 3 to select : ")
                analyse_option = (input("\n( or press ENTER to return ) : "))

                if analyse_option == "" :
                    break
                elif not analyse_option.isdigit() :
                    wrong_option()
                    continue
                else :
                    analyse_option = int(analyse_option)
                    if analyse_option > 0 and analyse_option < 4 :
                        pass
                    else :
                        wrong_option()
                        continue
                
                analyse(analyse_option)
            
        else :
            wrong_option()
            continue
        