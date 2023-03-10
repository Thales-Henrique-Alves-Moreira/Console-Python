import instaloader
import os

def getFollowers(commandLine):
    pass

def getUnfollowers(commandLine):
    pass

class Insta():
    def __init__(self, username, loginUsername, password):
        self.username = username        
        self.loginUsername = loginUsername
        self.password = password
        self.loader = instaloader.Instaloader(quiet=True)

        self.login()

        self.profile = instaloader.Profile.from_username(self.loader.context, self.username)

    def login(self):
        os.system(f'cmd /c "instaloader --login={self.loginUsername} --password={self.password} --q"')

        login = self.loader.load_session_from_file(self.loginUsername)

    def getFollowers(self):
        followersFile = []

        if(os.path.exists("console/plugins/insta/info/followers/" + self.username + "-followers.txt")):
            with open("console/plugins/insta/info/followers/" + self.username + "-followers.txt", "r") as file:
                for follower in file.readlines():
                    followersFile.append(follower.replace("\n", ""))

        followers = []

        for follower in self.profile.get_followers():
            if follower.username not in followersFile:
                with open("console/plugins/insta/info/followers/" + self.username +"-followers.txt", "a+") as f:
                    file = f.write(follower.username + '\n')
            
            followers.append(follower.username)

        return followers

    def getUnfollowers(self):
        followers = []

        if(os.path.exists("console/plugins/insta/info/followers/" + self.username + "-followers.txt")):
            with open("console/plugins/insta/info/followers/" + self.username + "-followers.txt", "r") as file:
                for follower in file.readlines():
                    followers.append(follower.replace("\n", ""))
        else:
            print("You still didnt check your followers")
            return

        unfollowersFile = []

        if(os.path.exists("console/plugins/insta/info/unfollowers/" + self.username + "-followers.txt")):
            with open("console/plugins/insta/info/unfollowers/" + self.username + "-followers.txt", "r") as file:
                for unfollower in file.readlines():
                    unfollowersFile.append(unfollower.replace("\n", ""))

        unfollowers = []

        for follower in self.profile.get_followers():
            if follower.username not in followers and follower.username not in unfollowersFile and follower not in self.profile.get_followers():
                with open("console/plugins/insta/info/unfollowers/" + self.username + "-unfollowers.txt", "a+") as file:
                    file.write(follower.username + '\n')

                unfollowers.append(follower.username)

        return unfollowers

insta = Insta("thales_thm", "testeconta123654", "picadura123")
insta.getFollowers()