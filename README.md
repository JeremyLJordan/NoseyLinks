# Nosey Links
Enumerates common URL shortener links by generating random links
and checking to see if they have been used before. 
If so, the title of the page linked to is returned for review..
	
## Technologies
Project is created with:
* Python 3.8
* Beautiful Soup
* Urllib3
	
## Setup
run setup.py:

## Usage
```
python NoseyLinks.py [-h] [-u URL] [-a ATTEMPTS] [-v VERBOSE] [-o OUTPUT]

optional arguments:
  -h, --help         show this help message and exit
  -u URL, --url      set shortener url, default = tinyurl
  -a, --attempts     attempts, default = 10
  -v, --verbose      enables verbose mode
  -o, --output       output file for results
```

## Example Output
```

python NoseyLinks.py -u tinyurl.com -a 6 -v -o NoseyLinksLog.txt

https://tinyurl.com/792211s | Title: "Page not found | Comanche Nation"
https://tinyurl.com/joxg0uc | Title: "99acres - Login"
https://tinyurl.com/lxwx3wz | Title: "Imobiliária Auxiliadora Predial"
https://tinyurl.com/001crv6 | Title: "Anmeldung zu Ihrer Reisen | VIATOR Reisen"
https://tinyurl.com/1b55nyo | Title: "None"
https://tinyurl.com/91rzkcv | Title: "TinyURL.com - shorten that long URL into a tiny URL"
```
