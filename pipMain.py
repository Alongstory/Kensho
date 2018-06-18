from Crawler import Crawler
import argparse as parser

if __name__ == '__main__':
    spider = Crawler('severe weather')
    spider.crawl()
