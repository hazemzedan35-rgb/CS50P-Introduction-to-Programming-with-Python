import sys
import requests

def main():
    n = get_user()
    get_price(n)

def get_user():
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")

    try:
        n = float(sys.argv[1])

    except ValueError:
        sys.exit("Command-line argument is not a number")
    
    else:
        return n
    

def get_price(n):

    try:
        response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=fded99536c3697935e35d517aca5c353e015edb00040e781c47b1e288a038f6f").json()
        price_string = float(response["data"]["priceUsd"])
    
    except requests.RequestException:
        sys.exit()
    
    else:
        amount = price_string * n
        print(f"${amount:,.4f}")

    
if __name__=="__main__":
    main()
