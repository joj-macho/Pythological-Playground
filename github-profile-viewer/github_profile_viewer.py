import requests
import json

API_URL = 'https://api.github.com/users/'

def main():
    '''Main function to execute the GitHub Profile Viewer.'''

    print('\nWelcome to GitHub Profile Viewer\n')
    
    username = input('Enter a GitHub username: ')
    
    user_data = get_user(username)
    display_user(user_data)

def get_user(username):
    '''Fetches user information and repositories from the GitHub API.'''
    try:
        user_response = requests.get(API_URL + username)
        user_response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)

        user_data = user_response.json()

        repos_response = requests.get(API_URL + username + '/repos')
        repos_response.raise_for_status()

        repos_data = repos_response.json()

        return {'user': user_data, 'repos': repos_data[:10]}
    except requests.exceptions.RequestException as e:
        print(f'Error fetching data: {e}')
        return None
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:  # User not found
            print(f'User not found: {username}')
            return {'user': None, 'repos': []}
        else:
            print(f'HTTPError: {e}')
            return None

def display_user(user_data):
    '''Displays user information and top repositories.'''
    if user_data:
        print('\nUser Information:')
        print(f"Name: {user_data['user'].get('name', 'N/A')}")
        print(f"Bio: {user_data['user'].get('bio', 'N/A')}")
        print(f"Followers: {user_data['user'].get('followers', 0)}")
        print(f"Following: {user_data['user'].get('following', 0)}")
        
        print('\nTop Repositories:')
        for repo in user_data['repos']:
            print(f"{repo['name']}: {repo['html_url']}")
    else:
        print('User not found.')


if __name__ == '__main__':
    main()
