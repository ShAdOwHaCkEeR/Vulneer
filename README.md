
# Vuln Searcher

 ✨ dont forget to set your own API key  ✨
Get it from here ~> [Vulners](https://vulners.com/)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

nothing to say about this :\

## Installation

you need python and install vulners :

USE :

```sh
pip install vulners
```

Also u need to set your API key in the configuration file
```sh
method 1 | open API.config and change whats after API= to your own API key
method 2 | delete API.config file and make another one includes your API key like that : (API=<u're key here>)
```


## USAGE

if you've got some nmap results for example and there is alot of CVE's 
you can parse all using CVE_PARSER.py that will extract CVE's in the result 

`$CVE_PARSER USAGE:`
```sh
python3 CVE_PARSER.py -f my_nmap_results.txt -s parsed.txt
```

then it's searcher turn :)

`$VULN_SEARCHER USAGE:`
```sh
python3 VULN_SEARCHER.py (-c CVE-****-***** / -f parsed.txt) -s results.txt
```

