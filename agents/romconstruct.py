from ananas import PineappleBot, ConfigurationError, reply
import markovify

class ROMConstruct(PineappleBot):

  def model_text(self):

    # Load the corpus
    with open(self.config.rom_file,"r") as corpus:

        # generate markov model
        markov_model = markovify.Text(corpus.read(), state_size=3)
    
        return markov_model.make_sentence()

  def start(self):
    self.mastodon.toot(f"{self.config.name} coming online")

    # Say a little somthing to test things out
    self.mastodon.toot(self.model_text())

  @reply
  def respond(self, mention, user):

        # Reply with a generated sentence
        # TODO: Figure out how to call the API so that this is
        # a properly-threaded reply
        self.mastodon.toot(f"@{user['acct']}, {self.model_text()}")

  def stop(self):
    self.mastodon.toot(f"{self.config.name} going offline")
