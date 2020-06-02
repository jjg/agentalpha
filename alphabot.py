from ananas import PineappleBot, ConfigurationError, hourly, reply

class AlphaBot(PineappleBot):

  def start(self):
    self.message = "yo"

  @hourly(minute=37)
  def say_something(self):
    self.mastodon.toot(self.message)

  @reply
  def respond(self, status, user):
    self.mastodon.toot(f"@{user['acct']}, {self.message}")
