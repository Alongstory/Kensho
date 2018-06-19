from Crawler import Crawler
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Process Parameters for searching')
    parser.add_argument('search', type = str, help = 'the search item')
    parser.add_argument('key', type=str, help='Input the keys of Google API')
    #parser.add_argument('num', type = int, help = 'the number of returned items')
    args = parser.parse_args()

    spider = Crawler(args.search ,args.key)
    spider.crawl()
    #print(args.num)

