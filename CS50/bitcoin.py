import sys
import requests

def main():
    btc = check_sysargv()
    amount = btc*sys.argv[1]
    print(f'${amount:,.4f}')
    
def check_sysargv():
    try:
        if len(sys.argv) < 2 or len(sys.argv) > 2:
            print('Missing command-line argument')
            sys.exit()
        try:
            sys.argv[1] = float(sys.argv[1])
            index = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
            object = index.json()
            usd = object['bpi']
            rate = usd['USD']
            sys.argv[1] = float(sys.argv[1])
            return rate['rate_float']
        except ValueError:
            print('Command-line argument is not a number')
            sys.exit()
            
    except requests.RequestException:
        sys.exit()
        
if __name__ == '__main__':
    main()