import numpy as np
import re
from requesting_urls import get_html
from filter_urls import filter_urls, find_articles

def find_dates(html, output = False):
    """
    Finds all dmy, mdy, ymd and iso date formats in given HTML file.
    Converts these to yyyy/mm/dd and returns list of string sorted ascendingly

    ARGS:
        html (string): string of HTML file to search through
        output (string, optional): Name of output file to write dates to
    RETURNS:
        dates (list of strings): sorted and converted dates
    """

    months = 'Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec'
    months_regex = r'((Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\w*)'
    month_dic = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May':'05', 'Jun': '06', 'Jul': '07', 'Aug': '08', 'Sep': '09', 'Oct':'10', 'Nov':'11', 'Dec':'12'}

    dmy_reg = r'(?:(?:[012]\d|-3[012]){1} (?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Oct|Nov|Dec){1}[a-z]* \d{4})'
    mdy_reg = r'(?:(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Oct|Nov|Dec){1}[a-z]* \d{2}, \d{4})'
    ymd_reg = r'(?:\d{4})\s(?:(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\w*)\s(?:\d{2})'
    iso_reg = r'(?:\d{4}-(?:0[1-9]|1[012){1}])(?:-[012]\d|-3[012]){0,1})'

    dmy_dates = re.findall(dmy_reg, html)
    mdy_dates = re.findall(mdy_reg, html)
    ymd_dates = re.findall(ymd_reg, html)
    iso_dates = re.findall(iso_reg, html)
    
    iso_string= ' '.join(str(elem) for elem in iso_dates)

    

    #iso
    iso_string = re.sub(r'(\d{4})-(\d{2})-(\d{2})', r'\1'+'/' +r'\2'+'/'+r'\3', iso_string)
    iso_string = iso_string.split()

    for date in dmy_dates:
        formatted = format_date(date, "DMY")
        if formatted is not None:
            iso_string.append(formatted)
    
    for date in dmy_dates:
        formatted = format_date(date, "MDY")
        if formatted is not None:
            iso_string.append(formatted)

    for date in dmy_dates:
        formatted = format_date(date, "YMD")
        if formatted is not None:
            iso_string.append(formatted)


    if output:
        #write url string to file
        f = open(output, 'w')

        for date in iso_string[:]:
            f.write(f"{date} \n \n")
        f.close()
    return iso_string

def format_date(date, from_format):
    """formats a date

    Args:
        date (string): 
        from_format (string): what format the date has

    Returns:
        string: the date in format yyyy/mm[/dd]
    """
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    if from_format == "ISO":
        return re.sub("-", "/", date) 
    try:
        if from_format == "YMD":
            if date[5:8] in months:
                if date[-1].isnumeric():
                    return f"{date[:4]}/{str(months.index(date[5:8])+1).zfill(2)}/{date[-2:]}"
                return f"{date[:4]}/{str(months.index(date[5:8])).zfill(2)}"
        if from_format == "MDY":
            return f"{date[-4:]}/{str(months.index(date[0:3])+1).zfill(2)}/{date[-8:-6]}"
        if from_format == "DMY":
            return f"{date[-4:]}/{str(months.index(date[3:6])+1).zfill(2)}/{date[:2]}"
    except: #Error in month
        pass
    
    

if __name__=='__main__':


    html = get_html('https://en.wikipedia.org/wiki/Rafael_Nadal')
    find_dates(html, output='example_rafael_nadal.txt')

    html = get_html('https://en.wikipedia.org/wiki/Linus_Pauling')
    find_dates(html, output='example_linus_pauling.txt')


    html = get_html("https://en.wikipedia.org/wiki/J._K._Rowling")
    find_dates(html, output= 'example_just_kidding_rowling.txt')


    html = get_html("https://en.wikipedia.org/wiki/Richard_Feynman")
    find_dates(html, output= 'example_richard_feynman.txt')

    html = get_html("https://en.wikipedia.org/wiki/Hans_Rosling")
    find_dates(html, output= 'example_hans_rosling.txt')
