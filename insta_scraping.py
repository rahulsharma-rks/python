import requests
from bs4 import BeautifulSoup

URL = "https://www.instagram.com/{}/"
def parse_data(s):
    data = {}
    s = s.split("-")[0]
    s = s.split(" ")
    data['Followers'] = s[0]
    data['Following'] = s[2]
    data['Posts'] = s[4]
    return data

def scrape_data(username):
    try:
        r = requests.get(URL.format(username))
        s = BeautifulSoup(r.text,"html.parser")
        meta = s.find('meta',property ="og:description")
        return parse_data(meta.attrs['content'])
    except:
        pass

if __name__ == "__main__":
    username = input("Enter Valid Username:")
    data = scrape_data(username)
    print("-------INSTAGRAM USER-DATA-------")
    print("Username:", username)
    print("This Account Has:", data["Followers"],"followers.")
    print("This Account Has", data["Following"],"following.")
    print("This Account Has", data["Posts"],"posts.")
