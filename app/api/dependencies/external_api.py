import requests

def fetch_comment_data(comment_id: int):
    # Replace this URL with the actual endpoint of your external provider
    external_api_url = f"https://jsonplaceholder.typicode.com/comments/{comment_id}"

    try:
        # Make an HTTP GET request to the external API
        response = requests.get(external_api_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Assuming the response contains comment data in JSON format
            comment_data = response.json()
            return comment_data
        else:
            # If the request was not successful, handle the error accordingly
            # You can raise an exception or return None, depending on your needs
            return None
    except requests.exceptions.RequestException as e:
        # Handle any exceptions that may occur during the request (e.g., network issues)
        print(f"Error fetching comment data: {e}")
        return None
