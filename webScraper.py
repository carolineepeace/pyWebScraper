import requests
from bs4 import BeautifulSoup
from colorama import Fore, Back, Style

#Main Web Scraper function
def start():
    URL = input(Style.BRIGHT + "\nWhat URL Would You Like To Scrape???\n" + Style.RESET_ALL)

    option = getOption()

    if option == 1:
        optionOne(URL)
    if option == 2:
        optionTwo(URL)
    if option == 3:
        optionThree(URL)    
    if option == 4:
        optionFour(URL)    


#Gets the users option value & returns the input to the start() function
def getOption():
    options = {1, 2, 3, 4}

    while True:
        try:
            option = int(input(Style.BRIGHT + """\nWhat would you like to do?\n
            [1] Scrape the entire website\n
            [2] Scrape for an element by ID\n
            [3] Scrape for an element by Class\n
            [4] Scrape for a specific element type\n
Enter an option: """ + Style.RESET_ALL))
        except:
            option = None    

        if option in options:
            print(Fore.GREEN + Style.BRIGHT + "\nScraping initiating...\n" + Style.RESET_ALL)
            return option
        else:
            print(Fore.RED + Style.BRIGHT + """\n********************************************************************
                  \nInvalid input. Please enter a valid integer from the options listed.""" + Style.RESET_ALL)
            
#Option 1 function - Scrape entire website
def optionOne(URL):
    web = requests.get(URL) #Issues HTTP GET request to the URL
    soup = BeautifulSoup(web.content, "html.parser") #Parses the raw byte contents into HTML
    prettyWeb = soup.prettify()

    print(Fore.GREEN + Style.BRIGHT + "Scraping Finalized!\n" + Style.RESET_ALL)
    print(prettyWeb)

#Option 2 function - Scrape for an element by ID
def optionTwo(URL):
    web = requests.get(URL)
    soup = BeautifulSoup(web.content, "html.parser")
    
    while True:
        try:
            webId = input(Style.BRIGHT + "What ID would you like to scrape for? " + Style.RESET_ALL)

            if webId == "Exit":
                return            
            
            webIdResults = soup.find(id = webId)
            prettyWebId = webIdResults.prettify()

            print(Fore.GREEN + Style.BRIGHT + "\nScraping Finalized!\n" + Style.RESET_ALL)
            print(prettyWebId)
            return
        except:
            webIdResults == None
            print(Fore.RED + Style.BRIGHT + """\n*******************************************************
                  \nID not found. Please try again, or type 'Exit' to exit.\n""" + Style.RESET_ALL)
                
    
#Option 3 function - Scrape for an element by class
def optionThree(URL):
    web = requests.get(URL)
    soup = BeautifulSoup(web.content, "html.parser")

    while True:
        try:
            webClass = input(Style.BRIGHT + "What class would you like to scrape for? " + Style.RESET_ALL)

            if webClass == "Exit":
                return
            
            webClassResults = soup.find_all("div", class_ = webClass)

            print(Fore.GREEN + Style.BRIGHT + "\nScraping Finalized!\n" + Style.RESET_ALL)
            print(webClassResults)
            return
        except:
            webClassResults == None
            print(Fore.RED + Style.BRIGHT + """\n**********************************************************
                  \nClass not found. Please try again, or type 'Exit' to exit.\n""" + Style.RESET_ALL)

#Option 4 function - Scrape for a specific element
def optionFour(URL):
    web = requests.get(URL)
    soup = BeautifulSoup(web.content, "html.parser")

    while True:
        webElement = input(Style.BRIGHT + "What element would you like to scrape for? " + Style.RESET_ALL)

        if webElement == "Exit":
            return

        webElementResults = soup.find_all(webElement)

        if not webElementResults:
            print(Fore.RED + Style.BRIGHT + """\n**********************************************************
                  \nElement not found. Please try again, or type 'Exit' to exit.\n""" + Style.RESET_ALL)
        else:           
            print(Fore.GREEN + Style.BRIGHT + "\nScraping Finalized!\n" + Style.RESET_ALL)
            for element in webElementResults:
                print(element.prettify())
            return   

#Initializing the main function, start()
if __name__ == "__main__":
    start()