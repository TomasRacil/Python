#secret	Ckx7FHfiy6s6ZRDvNu3iw_Y2yFTbLA
#web app  gUHWjSK1j1LsR9XH3dPX7w

import praw

reddit = praw.Reddit(
    client_id="my client id",
    client_secret="my client secret",
    user_agent="my user agent",
    username="my username",
    password="my password",
)

print(reddit.read_only)