import requests

# The API endpoint for fetching users
users_api_url = "https://jsonplaceholder.typicode.com/users"

print(f"Attempting to fetch data from: {users_api_url}\n")

try:
    #Make a GET request to the API
    response = requests.get(users_api_url)

    #Check the status code of our response

    if response.status_code == 200:
        print("Successfully called the API")

        users_data = response.json()

        if isinstance(users_data, list):
            print(f"Found {len(users_data)} users")

            for user in users_data:
                user_id = user.get('id', 'N/A')
                name = user.get('name', 'N/A')
                username = user.get('username', 'N/A')
                email = user.get('email', 'N/A')
                city = user.get('address', {}).get('city', 'N/A')

                print(f"  ID: {user_id}")
                print(f"  Name: {name}")
                print(f"  Username: {username}")
                print(f"  Email: {email}")
                print(f"  City: {city}")
                print("-" * 30) # Separator for readability
        else:
            print("Expected a list of users but received a different format.")
            print(f"Raw response content: {response.text[:200]}...")
    elif response.status_code == 404:
        print(f"Error: 404 Not Found. The endpoint might be incorrect: {users_api_url}")
    elif response.status_code == 401:
        print("Error: 401 Unauthorized. This API does not require authentication, so this is unexpected.")
    else:
        # For any other non-200 status code
        print(f"Error fetching data. Status Code: {response.status_code}")
        print(f"Response text: {response.text}")

except requests.exceptions.ConnectionError as e:
    print(f"Connection Error: Could not connect to the API. Check your internet connection or the URL.")
    print(e)
except requests.exceptions.Timeout as e:
    print(f"Timeout Error: The request took too long to respond.")
    print(e)
except requests.exceptions.RequestException as e:
    print(f"An unexpected error occurred during the request: {e}")
    print(e)
except ValueError as e:
    # This might happen if response.json() tries to parse non-JSON content
    print(f"Error parsing JSON response. Response content was not valid JSON.")
    print(f"Raw response content: {response.text[:200]}...")
    print(e)
