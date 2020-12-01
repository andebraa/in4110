import requests as req
from bs4 import BeautifulSoup
from requesting_urls import get_html
import numpy as np



def extract_events(url):
    """
    Finding season table and making .md file   
 
    Args:
        url (string): 
    """
    
    html = get_html(url)
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find('table', attrs={"class":'wikitable'})
    new_table = table_to_2d(table)

    discipline = {'DH': 'Downhill', 'SL': 'Slalom', 'GS':'Giant Slalom', 'SG':'Super Giant Slalom', 'AC':'Alpine Combined', 'PG':'Parallel Giant Slalom'}
    f = open('betting_slip_empty.md', 'w')

    f.write('*date*|*venue*|*discipline*|Who wins?*\n')
    f.write(':-----|:-----:|:-----:|-----:')
    f.write('\n')
    for row in new_table[1:-1]:
        try:
            f.write(f"{row[2].strip()}|{row[3].strip()}|{discipline[row[4][:2]]}\n")
        except:
            pass
    f.close()




from itertools import product

def table_to_2d(table_tag):
    """
    fetched from https://www.iditect.com/how-to/52094811.html
    Couldn't find a satisfactory way of handling varying rows and collumns, so this function does it for me
    """
    rowspans = []  # track pending rowspans
    rows = table_tag.find_all('tr')

    # first scan, see how many columns we need
    colcount = 0
    for r, row in enumerate(rows):
        cells = row.find_all(['td', 'th'], recursive=False)
        # count columns (including spanned).
        # add active rowspans from preceding rows
        # we *ignore* the colspan value on the last cell, to prevent
        # creating 'phantom' columns with no actual cells, only extended
        # colspans. This is achieved by hardcoding the last cell width as 1.
        # a colspan of 0 means "fill until the end" but can really only apply
        # to the last cell; ignore it elsewhere.
        colcount = max(
            colcount,
            sum(int(c.get('colspan', 1)) or 1 for c in cells[:-1]) + len(cells[-1:]) + len(rowspans))
        # update rowspan bookkeeping; 0 is a span to the bottom.
        rowspans += [int(c.get('rowspan', 1)) or len(rows) - r for c in cells]
        rowspans = [s - 1 for s in rowspans if s > 1]

    # it doesn't matter if there are still rowspan numbers 'active'; no extra
    # rows to show in the table means the larger than 1 rowspan numbers in the
    # last table row are ignored.

    # build an empty matrix for all possible cells
    table = [[None] * colcount for row in rows]

    # fill matrix from row data
    rowspans = {}  # track pending rowspans, column number mapping to count
    for row, row_elem in enumerate(rows):
        span_offset = 0  # how many columns are skipped due to row and colspans
        for col, cell in enumerate(row_elem.find_all(['td', 'th'], recursive=False)):
            # adjust for preceding row and colspans
            col += span_offset
            while rowspans.get(col, 0):
                span_offset += 1
                col += 1

            # fill table data
            rowspan = rowspans[col] = int(cell.get('rowspan', 1)) or len(rows) - row
            colspan = int(cell.get('colspan', 1)) or colcount - col
            # next column is offset by the colspan
            span_offset += colspan - 1
            value = cell.get_text()
            for drow, dcol in product(range(rowspan), range(colspan)):
                try:
                    table[row + drow][col + dcol] = value
                    rowspans[col + dcol] = rowspan
                except IndexError:
                    # rowspan or colspan outside the confines of the table
                    pass

        # update rowspan bookkeeping
        rowspans = {c: s - 1 for c, s in rowspans.items() if s > 1}
    return table


if __name__ == '__main__':

    url = "https://en.wikipedia.org/wiki/2019%E2%80%9320_FIS_Alpine_Ski_World_Cup"
    request = req.get(url)
    assert request.status_code ==200
    soup = BeautifulSoup(request.text, "html.parser")
    soup_table = soup.find('table', attrs={"class":'wikitable'})

    extract_events(url)
