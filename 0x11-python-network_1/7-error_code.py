#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    # Check if a URL is provided as an argument
    if len(sys.argv) != 2:
        print("Usage: ./7-error_code.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    try:
        # Send a GET request to the specified URL
        response = requests.get(url)

        # Check the HTTP status code
        if response.status_code >= 400:
            print("Error code:", response.status_code)
        else:
            # Display the body of the response
            print(response.text)

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)
