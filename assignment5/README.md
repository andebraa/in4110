
# Assignment 5 - regex

## How to run programs:
- To run the programs with requested urls just run with - python3 "filename".py.
- Remember to install dependecies before you run programs. 

## Dependencies:
- pandas - pip3 install pandas
- BeautifulSoup - pip3 install beautifulsoup
- requests - pip3 install requests
- matplotlib - pip install matplotlib


_Ass5.py_ 
	 
	_get html_:
		returns html code of given website, with parameters
		args:
			url(string): url of website 
			params (touple of strings): arguments passed to requests.get 
			output (string):optional, name of test file to write html to
		returns:
			html code (string): the return values of requests.get 
_filter urls:_
	uses regex to identify valid urls in HTML code 
		args:
			html (string): file with HTML code
			base url (string, optional): url from which html argument is fetched 
			output (string, optional): name of output file urls are written to 
		returns:
			urls (list): List of valied urls in string format 

_find dates_
	Finds all dmy, mdy, ymd and iso date formats in given HTML file. 
	Converts these to yyy/mm/dd and returns list of string sorted ascendingly
	
		args:
			html (string): string of HTML file to search through 
			output (sting, optional): Name of output file to write dates to 
		returns:
			dates (list of strings): sorted and converted dates 

_time planner.py_ 
	extract_events:
		Finds date, venue and discipline of the 2020 ski world cup,
		and writes it to file.
		
		args:
			url (string): urls of the 2020 ski world cup wikipedia page 
		
			

