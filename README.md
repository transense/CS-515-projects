Vaibhavi Shah vshah6@stevens.edu

# bugs and issues

## wc.py

gron.py

## date.py

In the date file while I was trying to get current date and current day it isn't working correctly on test cases as in the output file we have given past date and in the code it will take the current date.
In the date differene command was facing the same issue and also it wasn't matching with the output because I was preiously taking date and time formate like below
YYYY-MM-DD HH-MM-SS
so it was mismatched as I was calculating seconds as well.

# resolved issue

## wc.py
In the output for stdin , it was taking the extra chrachter at the end of the content. 

For the above issue , extra condition statement added to check and calculate the output of word count.

## date.py

For the current date and current day issue ,  the time zone was changed using the `pytz` library. and set the time zone of America , New_york.

For date difference issue, only date was taken for both the parameters i.e today's date and given date.

# Overview

This repository contains three Python scripts (`wc.py`, `gron.py`, and `date.py`) that perform various tasks related to counting lines, words, and characters, transforming JSON to a gron-like format, and providing date-related utilities, respectively.

## `date.py`

### Functionality
`date.py` is a Python script that displays current date , current day, checking the leap yer and differnce between current date and given date

### Usage

```bash
date.py [-h] [-c] [-t] [-l] [-d DATE_DIFFERENCE]
```

### options 
> -h, --help            

Show this help message and exit </br> </br>

> -c, --current_date    

Print current date </br> </br>
> -t, --current_day    

 Print current date </br> </br>
> -l, --leap_year       

print leap year </br> </br>
> -d DATE_DIFFERENCE, --date_difference


Print difference between dates </br></br>


## Extension 

Flags has been adeed in the wc.py file to check the line , chcracter and word count individually. 
 
### Usage
```bash
wc.py [-h] [-l] [-c] [-w] [input_file]
```
### Options

> input_file 

Read input from satndard input(stdin)
> -h, --help

show this help message and exit
> -l, --lines 

Print total oine count

> -w, --words 

Print total cout of words
> -c, --characters

Print total count of characters


A flag has been added to gron.py which takes a different base object names if specified or puts json as a default base object.

### Usage
```bash
wc.py [-h] [-o OBJECT] [input_file]
```
### Options

> input_file 

Flatten the file from json or from the standard input(STDIN)

Read input from satndard input(stdin)
> -h, --help

show this help message and exit
> -o, --object 

Objects of json

