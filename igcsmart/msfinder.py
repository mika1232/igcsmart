import dropbox
import requests
import os

# In out_dir you must specify the filename as well e.g your/direcotry/to/the/file.pdf
# In dir you must also specify the filename e.g your/direcotry/to/the/file.pdf
# If any questions arise send a message to PatheticFish

def scan(code:str):

    code_data = code.split("/")
    time = code_data[2]

    if "F/M" in code:
        time = "M"

    ms_code = f"{code_data[0]}_{time}{code_data[-1]}_ms_{code_data[1]}.pdf"

    APP_KEY = '2wrrvjezmqz79y9'
    APP_SECRET = '4iixkfn384l60ow'
    REFRESH_TOKEN = 'vdBHFrMy94YAAAAAAAAAATNPuBfmTa8n7VN6br6SMGUDy8Ehtfloln6CrmSGf3-S'

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
        ACCESS_TOKEN = access_token
    else:
        print("Failed to refresh access token:", response.json())
        ACCESS_TOKEN = None

    dbx = dropbox.Dropbox(ACCESS_TOKEN)

    m, r = dbx.files_download(f"/mark_schemes/{code_data[0]}/{ms_code}")

    current_dir = os.getcwd() + "/mark_scheme.pdf"
    with open(current_dir, 'wb') as f:
        f.write(r.content)