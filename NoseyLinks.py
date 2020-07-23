#!/usr/bin/python3

import random
import string
import bs4
import urllib3
import re

'''
Short Link Enumerator

By: N3ON

Description: The purpose of SLE is to enumerate common url shorteners,
by generating random links and getting the website's title information.
The link generated will be shown as well as the title of the page the link 
forwards to.

Follow Me On Twitter: @N3ON_ONE
'''


# generate random seven digit alphanumeric string (standard length)
def rand_alphanum():
    subdirectory = ''.join(random.choices(string.ascii_lowercase +
                                          string.digits, k=7))
    return subdirectory


# removes html tags
def clean_results(html):
    cleaner = re.compile('<.*?>')
    cleantext = re.sub(cleaner, '', str(html))
    return cleantext


# takes url submitted and creates get request returning 
def web_request(full_url):
    try:
        http = urllib3.PoolManager()
        req = http.request('GET', full_url, timeout=4.0, redirect=True)
        html = req.data
        soup = bs4.BeautifulSoup(html, features="html.parser")
        result = soup.find('title')
        result = clean_results(result)
        return result
    except Exception as e: #exception too broad needs to be fixed
        print("Load Error...")


def main():
    # establishes which site to use
    domain_bool = input('Which site do you want to use?\n'
                        + '1 = TinyUrl.com\n'
                        + '2 = Bit.ly\n')
    # choice logic
    if domain_bool == '1':
        domain = str("https://tinyurl.com/")
        print('TinyUrl selected...')
    elif domain_bool == '2':
        domain = str("https://bit.ly/")
        print("Bit.ly selected...")
    else:
        print('invalid option, better luck next time!')
        main()

    # establishes if wordlist or random attempts will be used
    method_of_work = input('Would method you like to use?\n'
                           + '1 = Word list\n'
                           + '2 = Make random attempts\n')
    # choice logic
    if method_of_work == '1':
        print("coming soon")
        main()
    elif method_of_work == '2':
        num_attempts = int(input('How many attempts would you like to make?\n'))  # number of attempts
        for i in range(num_attempts):
            full_url = domain + str(rand_alphanum())  # concatenates the domain and the random subdirectory
            print(full_url + " | " + "Title: " + '"' + str(web_request(full_url)) + '"')  # prints final result

    else:
        print("invalid input")
        main()


# start main function
if __name__ == "__main__":
    main()
