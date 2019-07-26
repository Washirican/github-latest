import sys
import json

import requests

# Use Like python githubber.py JASchilz
# (or another user name)

if __name__ == "__main__":
    username = sys.argv[1]

    events = requests.get('https://api.github.com/users/{}/events'.format(username))
    event_type = events.json()[0]['type']
    created_at = events.json()[0]['created_at']

    print('GitHub user {} executed a {} on {}'.format(username, event_type, created_at))
