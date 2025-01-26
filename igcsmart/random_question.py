# Code for the random question generator thing

import dropbox
import requests
import random

def generate(syl_code):
    APP_KEY = '2wrrvjezmqz79y9'
    APP_SECRET = '4iixkfn384l60ow'
    REFRESH_TOKEN = 'vdBHFrMy94YAAAAAAAAAATNPuBfmTa8n7VN6br6SMGUDy8Ehtfloln6CrmSGf3-S'

    def refresh_access_token():
        token_url = "https://api.dropboxapi.com/oauth2/token"
        payload = {
            'grant_type': 'refresh_token',
            'refresh_token': REFRESH_TOKEN,
            'client_id': APP_KEY,
            'client_secret': APP_SECRET
        }
        response = requests.post(token_url, data=payload)
        if response.status_code == 200:
            access_token = response.json().get('access_token')
            print("Access token refreshed successfully.")
            return access_token
        else:
            print("Failed to refresh access token:", response.json())
            return None

    ACCESS_TOKEN = refresh_access_token()

    dbx = dropbox.Dropbox(ACCESS_TOKEN)

    files = []
    result = dbx.files_list_folder(f"/past_papers/{syl_code}")
    files.extend(result.entries)
    folders = [entry.name for entry in files if isinstance(entry, dropbox.files.FolderMetadata)]

    random_folder = random.choice(folders)

    filesf = []

    resultf = dbx.files_list_folder(f"/past_papers/{syl_code}/{random_folder}")
    filesf.extend(resultf.entries)
    file_names = [entry.name for entry in filesf if isinstance(entry, dropbox.files.FileMetadata)]

    random_question = random.choice(file_names)

    m, r = dbx.files_download(f"/past_papers/{syl_code}/{random_folder}/{random_question}")
    with open('question.png', 'wb') as f:
        f.write(r.content)