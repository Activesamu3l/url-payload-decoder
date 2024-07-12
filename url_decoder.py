import urllib.parse


def decode_url_payload(encoded_url):
    decoded_url = urllib.parse.unquote(encoded_url)
    return decoded_url


if __name__ == "__main__":
    # Example usage
    encoded_url = input("Enter the URL-encoded string: ")
    print("Decoded URL: ", decode_url_payload(encoded_url))
