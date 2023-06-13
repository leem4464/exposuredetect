import requests
import argparse

api_key = "YOUR_API_KEY_HERE"

q = {
  "elasticsearch":"product:elasticsearch port:9200",
  "mongodb":"product:MongoDB",
  "couchdb":"product:couchdb",
  "laravel debug mode":"title:Whoops! There was an error",
  "django debug mode":"DisallowedHost at",
  "kibana":"product:kibana",
  "kassandra":"product:Cassandra port:9160"
}

def args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-l','--list',help="List products you are looking for", action='store_true')
    parser.add_argument('-g','--get',help="Get a list IPs based on product name", type=str)
    return parser.parse_args()

def search_and_sort_ips(query):
    url = "https://api.criminalip.io/v1/banner/search"
    headers = {
        "x-api-key": api_key
    }
    params = {
        "query": query,
        "offset": 0
    }

    response = requests.get(url, headers=headers, params=params)
    ip_addresses = []

    if response.status_code == 200:
        data = response.json().get("data", {}).get("result", [])
        ip_addresses = list(set(item.get("ip_address") for item in data))
    else:
        print("Error:", response.status_code)

    return sorted(ip_addresses)


if __name__ == '__main__':

    if args().list:
        print("(*) List of supported products :")
        print("===============================")
        for key in q :
            print(key)

    if args().get:
        product = args().get
        if product in q :
            ips = search_and_sort_ips(q[product])
            for ip in ips :
                print(ip)
