import requests
def save_to_wayback(url):
    save_url = f"https://web.archive.org/save/{url}"
    response = requests.get(save_url)
    return response.status_code == 200
import requests
import time
from collections import deque
def log(text):
    print(text)
def get_following(username):
    """指定ユーザーがフォローしている最大100人のユーザー名を取得"""
    url = f"https://api.scratch.mit.edu/users/{username}/following"
    log(url+"にリクエストを送信中")
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return [user['username'] for user in data[:50]]
    return []

def Scratch_flwer_5():
    """Scratchでtomakareから始まる5階層のフォローネットワークを取得して返す"""
    start_user = "tomakare"
    max_depth = 3
    visited = set()
    queue = deque([(start_user, 0)])
    network = {}

    while queue:
        current_user, depth = queue.popleft()
        if depth > max_depth or current_user in visited:
            continue

        visited.add(current_user)
        following = get_following(current_user)
        network[current_user] = following

        for user in following:
            if user not in visited:
                queue.append((user, depth + 1))

        time.sleep(0.1)  # ScratchのAPIへの優しさ（サーバー負荷を下げる）

    return network
def mainloop():
    
    scratch_fl = Scratch_flwer_5()["tomakare"]

    for i in range(len(scratch_fl)):
        print("USER:" + scratch_fl[i])
        save_to_wayback("https://scratch.mit.edu/users/"+scratch_fl[i])
for i in range(10000000000000000000000000000000000000):
    mainloop()
    time.sleep(60)
