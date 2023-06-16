
import instaloader
import getpass

fi = open("followers.txt", "r")
old_followers =[]

for line in fi:
    old_followers.append(line)
fi.close

L = instaloader.Instaloader()
username = input("enter username")
password = getpass.getpass("enter password")
L.login(username, password)
profile = instaloader.Profile.from_username(L.context, "zahra")

new_followers =[]
for follower in profile.get_followees():
    new_followers.append(follower)

for new_folower in new_followers:
    if new_followers not in new_followers:
        print(new_followers)


fi = open("folower.txt", "w")

for folower in new_followers:
    fi.write(folower + "\n")
fi.close()    

