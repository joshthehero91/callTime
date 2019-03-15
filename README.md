# firstCall.py

This is a simple script to crawl our internal phones system to check the first time an admin logs into their phone each day.

tl;dr:
Use Python3:
```
python3 -m pip install --upgrade pip
python3 -m pip install beautifulsoup4 requests
```


### Prerequisites

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
If you're using Python 2.7; don't. Use Python 3. If for whatever reason you would like to be wrong and run Python 2, it probably won't work:

Python 2.7:
 - First install 'pip' Python's package manager:
1. https://pip.pypa.io/en/stable/installing/
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
pip install -U pip
```
 - Next, install BeautifulSoup:
2. https://www.crummy.com/software/BeautifulSoup/bs4/doc/
```
pip install beautifulsoup4
```
 - And last, requests:
3. http://docs.python-requests.org/en/master/user/install/
```
pip install requests
```

But don't do that ^^. Use Python 3:

Python 3:
```
python3 -m pip install --upgrade pip
python3 -m pip install beautifulsoup4 requests
```
pip is installed by default in Python 3 so just make sure it is updated then install Requests and BeautifulSoup.

Last, copy the script: https://git.liquidweb.com/jmaul/tools/blob/master/firstCall/firstCall.py


## Built With

* Python 3, Requests For Humans, and BeautifulSoup


## Authors

* **Joshua Maul** - *Initial work*

### Todo

 - [ ] - Make it prettier