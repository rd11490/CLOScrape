from bs4 import BeautifulSoup
import requests
from urllib.request import urlretrieve
import sys

def main(argv):
    if len(argv) >1:
        print('Too many arguments passed. Input the folder where you wish to save the files (ex. D:\CLO)')
    elif len(argv) == 0:
        print('No argument passed. Input the folder where you wish to save the files (ex. D:\CLO)')
    else:
        addr = str(argv[0])

        link = 'http://www.chineselearnonline.com/feed'
        for i in range(1, 8):
            l = link+str(i)+'/'
            r = requests.get(l)
            soup = BeautifulSoup(r.text)
            files = soup.find_all('enclosure')
            for f in files:

                url = f['url']
                name = url[url.rfind('/')+1:]
                print(name)
                urlretrieve(f['url'], addr+name)

if __name__ == "__main__":
   main(sys.argv[1:])