from Crawler import Crawler
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Process Parameters for searching')
    parser.add_argument('--search', type = str, help = 'the search item')
    parser.add_argument('--num', type = int, help = 'the number of returned items')
    parser.add_argument('--key', type = str, help = 'if available, show the keys of Google API')
    args = parser.parse_args()

    spider = Crawler('severe weather')
    spider.crawl()
