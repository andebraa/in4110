import numpy as np
import re
from requesting_urls import get_html

def filter_urls(html, base_url, output = False):
    """
    uses regex to identify valid urls in HTML code
    args:
        html (file): file with HTML code
        base_url (string, optional): url from which html argument is fetched
        output (string, optional): name of output file urls are written to
    returns:
        urls (list): List of valid urls in string format
    """
    if html == None and base_url!=None: #only website argument passed.
        try:
            html =get_html(base_url)
        except TypeError:
            print("could not fetch html from base_url argument.")


    #regular_links = re.findall(r"<a\s+href=\"(https:\/\/.\w+.\w+.\w{2,3}[\/\w+]*)", html) Does not work
    regular_links = re.findall("(?=<a).*href=\"([h|\/]{1}[^\"#]*)", html)
    for ind, url in enumerate(regular_links):
        if url[0] == '/' and url[1] != '/':
            regular_links[ind] = base_url + url
        elif url[0] == '/':
            regular_links[ind] = "https:" + url

    if output:
        #write url string to file
        f = open(output, 'w')
        for elem in regular_links:
            f.write(f"{elem}\n")
        f.close()
    return regular_links
    #re.findall()



def find_articles(html, base_url, output=False):
    """
    calls filter_urls and get_html to find all wikipeida articles in the given url
    args:
        html (file): file with HTML code
        base_url (string, optional): url from which html argument is fetched
        output (string, optional): name of output file urls are written to
    returns:
        wiki_articles (list): List of valid urls in string format
    """
    urls = filter_urls(html, base_url, False)
    urls_string = ' '.join(str(elem) for elem in urls)

    regex = r"\s(?=.*)(\/wiki\/[^\s:]*|\S*\.wikipedia\.org[^\s:]*){1}\s"
    wiki_articles = re.findall(regex, urls_string)
    if output:
        #write url string to file
        f = open(output, 'w')

        for url in wiki_articles:
            f.write(f"{url} \n")
        f.close()
    return wiki_articles

if __name__ =="__main__":
    url1 = "https://en.wikipedia.org/wiki/Nobel_Prize"
    html = get_html(url1)
    urls = filter_urls(html, url1, 'Nobel_Prize.txt')
    find_articles(html,url1, 'Nobel_Prize_wikiarticles.txt')
    url2 = "https://en.wikipedia.org/wiki/Bundesliga"
    html2 = get_html(url2)
    urls=filter_urls(html2, url2, 'bundesliga.txt')
    find_articles(html2, url2, 'bundesliga_wikiarticles.txt')
    url3 = "https://en.wikipedia.org/wiki/2019%E2%80%9320_FIS_Alpine_Ski_World_Cup"
    html3 = get_html(url3)
    urls = filter_urls(html3, url3, 'FIS_alpine_ski_2019.txt')
    find_articles(html3, url3, 'FIS_alpine_ski_2019_wikiarticles.txt')
