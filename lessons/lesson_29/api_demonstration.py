import requests
from assertpy import assert_that

#https://reqres.in
def get_user(user_id):
    """GET request to retrieve a user."""
    response = requests.get(f'https://reqres.in/api/users/{user_id}')
    print("\n--- GET User Request ---")
    print_response(response)
    extracted_user_id = response.json()['data']['id']
    if response.status_code == 200:
        assert_that(response.json()).contains_key("data")
    return response.json()

def create_user(name, job):
    """POST request to create a user."""
    payload = {'name': name, 'job': job}
    response = requests.post('https://reqres.in/api/users', json=payload)
    print("\n--- Create User Request ---")
    print_response(response)
    assert_that(response.status_code).is_equal_to(201)
    return response.json()

def update_user(user_id, name, job):
    """PUT request to update a user."""
    payload = {'name': name, 'job': job}
    response = requests.put(f'https://reqres.in/api/users/{user_id}', json=payload)
    print("\n--- Update User Request ---")
    print_response(response)
    return response.json()

def delete_user(user_id):
    """DELETE request to remove a user."""
    response = requests.delete(f'https://reqres.in/api/users/{user_id}')
    print("\n--- Delete User Request ---")
    print_response(response)
    return response.status_code

def print_response(response):
    """Utility function to print formatted response."""
    print(f"Status Code: {response.status_code}")
    try:
        print("Response JSON:", response.json())
    except ValueError:
        print("No Content")

# Example usage:
if __name__ == "__main__":
    user_id = 2  # Use a known user id for GET, PUT and DELETE
    # Get user details for a known user
    get_user(user_id)

    # Create a new user
    new_user = create_user('John Doe', 'Leader')

    # Update the user (here we will use a static id for demonstration)
    update_user(user_id, 'John Updated', 'Updated Leader')

    # Delete the user
    delete_user(user_id)
