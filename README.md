## Trading 212 Extended-Hours Price Googler
This is a simple Python script used for looking up the pre-market and after-hours price action of your Trading 212 holdings.

### Motivation

Annoyingly, Trading 212 does not show stock price action in the extended hours sessions in markets such as the US. Luckily, Google does show this price action. So let's automate this search! 

### Getting started

All you need to do is insert your username and password into either the `prices_Chrome.py` or `prices_Firefox.py` file (depending on your browser): 
![Image2](Screenshots/Example.png?raw=true)
Then run the file and it will complete an automated Google search of every holding on your Trading 212 account.

#### How it works

- The Python script uses Selenium to login to your Trading 212 account.
- It then queries the page source and extracts the names of your holdings from the HTML.

#### Prerequisites

The dependencies for this script are:
- Python 3.6>
- Selenium
- Chrome or Firefox Browser
- chromedriver _(for Chrome)_ or geckodriver _(for Firefox)_

#### Licensing

This software is under the MIT license.

#### Contact
If you have any issues or ideas, get in touch or submit an issue :)