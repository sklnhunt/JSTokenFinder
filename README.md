# JSTokenFinder

* jstokenfinder a Python file which takes javascript URL or URLs as a file (.txt) and find tokens from it from given regular expressions if it finds anything in js file then it will print.


## Usage

```
python3 jstokenfinder.py -h
usage: jstokenfinder.py [-h] [-u] [-c] [-f]

Token Finder:)

optional arguments:
  -h, --help           show this help message and exit
  -u , --url           URL ends with js
  -c , --concurrency   number of URLs to be processed in parallel (int)
  -f , --file          file containing js URLs (default .txt file format)

```


* Printed data can be `stdout` to the file as output.

`python3 jstokenfinder.py -u http://www.example.com/main.js | tee output.txt`



---
 * Inspired from [SecretFinder](https://github.com/m4ll0k/SecretFinder)🖤
