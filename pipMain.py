from Crawler import Crawler
import argparse
import os
from EventClassifier import EventClassifier
from QueryClassifier import QueryClassifier

# TODO: if the input is a string which is not number, the error message doesn't comes out and loop ended

def main():
    parser = argparse.ArgumentParser(description = 'Process Parameters for searching')
    parser.add_argument('key', type = str, help= 'Input the keys of Google API')
    args = parser.parse_args()
    # command loop
    while True:
        print('1 Add new class data to events library\n'
              '2 Events classification\n'
              '3 Query classification\n'
              '4 Exit\n'
              'Please input a number:\n'
              )
        cmd = input()
        if cmd == '1':
            # create the crawler
            spider = Crawler(args.key)
            while True:
                print('\nplease enter the search item and keywords like this\n'
                      'num_of_res item keyword_1 keyword_2 ... keyword_n\n'
                      "type 'exit' to exit\n")
                cmd = input()
                print(cmd)
                # input check for cmd
                if cmd == '':
                    print('Empty string!')
                    continue
                elif cmd == 'exit':
                    break
                else:
                    cmd = cmd.split(' ')
                    if cmd[0].isdigit():
                        spider.crawl(cmd[0], cmd[2:], cmd[1])
                        print('crawling...')
                        continue
                    else:
                        print('The number of search item is invalid!\n')
                        continue
            continue

        elif cmd == '2':
            print('Events classifier in developing...\n')
            continue
        elif cmd == '3':
            print('Query classifier in developing...\n')
            continue
        elif cmd == '4' or 'exit':
            break
        else:
            print('Command error, please input your option again\n')
            continue


if __name__ == '__main__':
    main()