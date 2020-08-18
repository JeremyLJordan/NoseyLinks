#! /usr/bin/python3

import argparse
import random
import re
import string

import bs4
import urllib3

'''
Nosey Links

By: N3ON

Description: The purpose of Nosey Links is to enumerate common url shortener's
by generating random links and getting the website's title information.
The link generated will be shown as well as the title of the page the link 
forwards to.

Follow Me On Twitter: @N3ON_ONE
'''

# parser stuff
parser = argparse.ArgumentParser()
parser.add_argument('-u', "--url", help="set shortener url, default = tinyurl", default="https://www.tinyurl.com")
parser.add_argument('-a', "--attempts", help="attempts, default = 10", type=int, default=10)
parser.add_argument('-v', "--verbose", help="enables verbose mode", default=True)
parser.add_argument('-o', "--output", help="output file for results", default="output.txt")
args = parser.parse_args()


def main():
    print('''
 ____    ___    _____   ___  __ __      _      ____  ____   __  _   _____
|    \  /   \  / ___/  /  _]|  T  T    | T    l    j|    \ |  l/ ] / ___/
|  _  YY     Y(   \_  /  [_ |  |  |    | |     |  T |  _  Y|  ' / (   \_
|  |  ||  O  | \__  TY    _]|  ~  |    | l___  |  | |  |  ||    \  \__  T
|  |  ||     | /  \ ||   [_ l___, |    |     T |  | |  |  ||     Y /  \ |
|  |  |l     ! \    ||     T|     !    |     | j  l |  |  ||  .  | \    |
l__j__j \___/   \___jl_____jl____/     l_____j|____jl__j__jl__j\_j  \___j
''')
    print('PLEASE REMEMBER THERE IS AN INHERENT RISK WITH CLICKING RANDOM LINKS FROM THE INTERNET')
    print('TWITTER: N3ON_ONE''\n''\n''\n')

    # choice logic
    for a in range(args.attempts):
        url = args.url + "/" + str(rand_alphanum())  # concatenates the domain and the random subdirectory
        title = str(web_request(url))
        if "Bitly | Page Not Found | 404" in title:
            pass
        elif "TinyURL.com - shorten that long URL into a tiny URL" in title:
            pass
        elif "None" in title:
            pass
        else:
            print(url + " | " + "Title: " + '"' + str(title) + '"')  # prints final result


# generate random seven digit alphanumeric string (standard length)
def rand_alphanum():
    subdir = ''.join(random.choices(string.ascii_lowercase +
                                    string.digits, k=7))
    return subdir


# removes html tags
def clean_results(html):
    cln = re.compile('<.*?>')
    cln_txt = re.sub(cln, '', str(html))
    return cln_txt


# takes url submitted and creates get request returning
def web_request(url):
    try:
        http = urllib3.PoolManager()
        req = http.request('GET', url, timeout=4.0, redirect=True)
        html = req.data
        soup = bs4.BeautifulSoup(html, features="html.parser")
        result = soup.find('title')
        result = clean_results(result)
        return result

    except Exception as e:  # exception too broad needs to be fixed
        if args.verbose:
            print("Load Error...")

    # start main function


if __name__ == "__main__":
    main()
