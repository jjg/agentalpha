from ananas import PineappleBot, ConfigurationError, hourly, reply

class AlphaBot(PineappleBot):

  def start(self):
    self.mastodon.toot("Online")

  @hourly(minute=5)
  def say_something(self):
    self.mastodon.toot("It's 5 after somewhere...")

  @reply
  def respond(self, mention, user):
    print(mention)
    print("---")
    print(user)
    self.mastodon.toot(f"@{user['acct']}, {mention['content']}")

  def stop(self):
    self.mastodon.toot("Offline")
