import requests

def download_video(url, filename):

    r = requests.get(url)

    with open(filename, "wb") as f:

        f.write(r.content)

    return filename
