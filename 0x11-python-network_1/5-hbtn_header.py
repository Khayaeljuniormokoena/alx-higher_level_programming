#!/usr/bin/python3

import requests
import sys

def get_request_id(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Retrieve and display the value of the X-Request-Id header
            x_request_id = response.headers.get('X-Request-Id')
            print(x_request_id)
        else:
            print(f"Error: Unable to fetch data from {url}. Status code: {response.status_code}")

    except requests.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Check if the script is provided with a URL
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)

    # Get the URL from the command-line argument
    url = sys.argv[1]

    # Call the function to get and display the X-Request-Id
    get_request_id(url)
