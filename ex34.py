#exact time
import argparse
import time
import urllib.request

parser=argparse.ArgumentParser()
parser.add_argument('region', type=str, help='Give your region')
parser.add_argument('city', type=str, help='Give your city')

args=parser.parse_args()

urllink=f'http://worldtimeapi.org/api/timezone/{args.region}/{args.city}'
request_url = urllib.request.urlopen(urllink)
res=request_url.read().split(b',')[2].decode('utf-8')
print(f'The exact time for {args.city} in {args.region} is :')
print(res)
