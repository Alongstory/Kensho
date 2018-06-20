from Crawler import Crawler
import argparse
import os


if __name__ == '__main__':
    # Parse the input
    parser = argparse.ArgumentParser(description = 'Process Parameters for searching')
    parser.add_argument('search', type = str, help = 'the search item')
    parser.add_argument('search_kw', type = str, help = 'the search keywords')
    parser.add_argument('key', type = str, help= 'Input the keys of Google API')
    parser.add_argument('--num', type = int, help = 'the number of returned items')
    args = parser.parse_args()

    key_words = args.search_kw.split(',')

    spider = Crawler(args.key)
    spider.crawl(args.search, key_words, args.num)
    #print(args.num)

