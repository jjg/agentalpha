import random
from ananas import PineappleBot, hourly, reply

class AgentLyrics(PineappleBot):

    def get_lyric(self):
        # Read a random line from the lyric file
        return random.choice(list(open("./data/lyrics.txt")))

    def start(self):
        self.mastodon.toot(self.get_lyric())

    @hourly(minute=10)
    def hourly_lyric(self):
        self.mastodon.toot(self.get_lyric())

    @reply
    def reply_lyric(self, mention, user):
        self.mastodon.toot(f"@{user['acct']}, {self.get_lyric()}")

    def stop(self):
        self.mastodon.toot(self.get_lyric())
