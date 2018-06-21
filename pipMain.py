from Crawler import Crawler
import argparse

def main():
    parser = argparse.ArgumentParser(description = 'Process Parameters for searching')
    parser.add_argument('key', type = str, help= 'Input the keys of Google API')
    args = parser.parse_args()
    # command loop
    while True:
        print('Please select a number option shows below:'
              '1 Add new class data to events library\n'
              '2 Events classification\n'
              '3 Query classification\n'
              '4 Exit')
        cmd = input()
        if cmd == '1':
            # create the crawler
            spider = Crawler(args.key)
            while True:
                print('please enter the search item and keywords like this\n'
                      'item num_results keyword_1 keyword_2 ... keyword_n\n')
                cmd = input()
                print(cmd)
                # input check for cmd
                if cmd == '':
                    cmd = cmd.split(' ')
                    spider.crawl(cmd[0], cmd[2:], cmd[1])

                    continue
                elif cmd == '':
                    print('Empty string!\n')
                    continue
                elif cmd == 'exit\n':
                    break
            break

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




    #print(args.num)

