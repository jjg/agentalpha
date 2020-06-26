from ananas import PineappleBot, ConfigurationError, reply
import markovify

class ROMConstruct(PineappleBot):

  def start(self):
    self.mastodon.toot(f"{self.config.name} coming online")

  @reply
  def respond(self, mention, user):

    # Load the corpus
    with open(self.config.rom_file,"r") as corpus:

        # generate markov model
        markov_model = markovify.Text(corpus.read(), state_size=3)
    
        # Generate a reply
        reply_string = markov_model.make_sentence()

        # Reply with a generated sentence
        self.mastodon.toot(f"@{user['acct']}, {reply_string}")

  def stop(self):
    self.mastodon.toot(f"{self.config.name} going offline")
