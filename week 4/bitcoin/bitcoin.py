import requests
import sys
import json
"""
{
  "time": {
    "updated": "Jul 23, 2023 14:34:00 UTC",
    "updatedISO": "2023-07-23T14:34:00+00:00",
    "updateduk": "Jul 23, 2023 at 15:34 BST"
  },
  "disclaimer": "This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org",
  "chartName": "Bitcoin",
  "bpi": {
    "USD": {
      "code": "USD",
      "symbol": "&#36;",
      "rate": "29,895.5370",
      "description": "United States Dollar",
      "rate_float": 29895.537
    },
    "GBP": {
      "code": "GBP",
      "symbol": "&pound;",
      "rate": "24,980.4716",
      "description": "British Pound Sterling",
      "rate_float": 24980.4716
    },
    "EUR": {
      "code": "EUR",
      "symbol": "&euro;",
      "rate": "29,122.6178",
      "description": "Euro",
      "rate_float": 29122.6178
    }
  }
}
"""
def main():
    if len(sys.argv) == 2 and sys.argv[1].isdigit():

        r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        json_r = r.json()
        # access the price inside USD:
        bpi = json_r["bpi"]
        USD = bpi["USD"]
        rate_float = float(USD["rate_float"])
        cross = float((rate_float)*(float(sys.argv[1])))
        print(f"${cross:,.4f}")

    elif len(sys.argv) == 2 and sys.argv[1] and ("." in sys.argv[1]):
        r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        json_r = r.json()
        # access the price inside USD:
        bpi = json_r["bpi"]
        USD = bpi["USD"]
        rate_float = float(USD["rate_float"])
        cross = float((rate_float)*(float(sys.argv[1])))
        print(f"${cross:,.4f}")

    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")

    elif sys.argv[1].isalpha():
        sys.exit("Command-line argument is not a number")

if __name__=="__main__":
    main()
