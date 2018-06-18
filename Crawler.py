"""Simple command-line example for Custom Search.
Command-line application that does a search.
"""
import pprint
from googleapiclient.discovery import build


class Crawler:
    """ • Important optional parameters:
        ○ dateRestrict: Restricts results to URLs based on date.
        ○ exactTerms: Identifies a phrase that all documents in the search results must contain.
        ○ excludeTerms: Identifies a word or phrase that should not appear in any documents in the search results.
        ○ fileType
        ○ lowRange, highRange: Use lowRange and highRange to append an inclusive search range of lowRange...highRange  to the query.
        ○ lr: Restricts the search to documents written in a particular language (e.g., lr=lang_ja). 
        ○ Num: Number of search results to return.
        ○ orTerms: Provides additional search terms to check for in a document, where each document in the search results must contain at least one of the additional search terms.
        # Build a service object for interacting with the API. Visit
        # the Google APIs Console <http://code.google.com/apis/console>
        # to get an API key for your own application.
    """

    def __init__(self, item, num = 10, key = '005808576341306023160:yojc6z7o63u'):
        self.item = item
        self.key = key
        self.num = num


    def crawl(self):
        service = build("customsearch", "v1",
                        developerKey = "AIzaSyC1o8pJAwMvaRugaRp9nWtvrGQs2_llEps")

        res = service.cse().list(
            q = self.item,
            cx = self.key,
            #'005808576341306023160:yojc6z7o63u'
            num = self.num,
        ).execute()
        pprint.pprint(res)

