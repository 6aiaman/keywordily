import pandas as pd
import numpy as np
import re
import urllib2 as ul
from collections import deque

def parse_google_result(search_string):
    working_str = search_string.strip('\n').split('[')[2]
    regex_pattern = "(?<=\")(.*)(?=\")"
    match = re.search(regex_pattern,working_str)
    if match:
        returned_search_string = match.group(1)
        return returned_search_string
    else:
        return ''


def fetch_data(search_string): #returns deque data
    keywords_returned = deque()
    keyword_stack= deque()
    keyword_stack.append(search_string)
    service = ["http://suggestqueries.google.com/complete/search?client=chrome&hl=${lang}&gl=${country}&callback=?&q="]

    while len(keyword_stack) < 50000:    
        url = service[0] + ul.quote(re.sub('\W',' ',keyword_stack.popleft()))
        parsed_string = parse_google_result(ul.urlopen(url).read())
        temp_result = map(lambda x:re.sub('\W',' ',x),parsed_string.strip('\n').split(","))
        keywords_returned .extend(temp_result)
        keyword_stack.extend(list(set(keywords_returned)))
        if len(keywords_returned) == 10000:
            break
    
    keywords_returned = list(keywords_returned)
    keywords_returned_df = pd.DataFrame(keywords_returned)

    return keywords_returned_df
