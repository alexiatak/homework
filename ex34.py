#exact time
import argparse
import time
import urllib.request

parser=argparse.ArgumentParser()
parser.add_argument('--region','--city',help='please give your region and city', required=True)
args=parser.parse_args()


request_url = urllib.request.urlopen(f'http://worldtimeapi.org/api/timezone/{args.region}/{args.city}')
print(request_url.read())
print(f'The exact time for {args.city} in {args.region} is : {}')
