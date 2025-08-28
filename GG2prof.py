
import urllib.request
# GG = "70703823"
# count = 0
def GG2prof(GG, count):
    urllib.request.urlretrieve((f"https://avatars.gg.pl/user,{GG}/s,2048x2048?default=https://www.gg.pl/images/sr-avatar-blank-female-200.png&exist"), f"profilowe\\{count}.jpg")



