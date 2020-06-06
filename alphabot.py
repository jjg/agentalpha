from ananas import PineappleBot, ConfigurationError, hourly, reply
import markovify
from bs4 import BeautifulSoup

class AlphaBot(PineappleBot):

  def start(self):
    self.mastodon.toot("Online")

  @hourly(minute=5)
  def say_something(self):
    self.mastodon.toot("It's 5 after somewhere...")

  @reply
  def respond(self, mention, user):

    # Extract the text of the mention
    soup = BeautifulSoup(mention["content"])
    mention_string = soup.get_text()
    print(mention_string)

    # Load the corpus
    corpus = open("./uni.txt","r")

    # generate markov model
    markov_model = markovify.Text(corpus.read() + " " + mention_string)

    # Reply with a generated sentence
    self.mastodon.toot(f"@{user['acct']}, {markov_model.make_sentence()}")
    corpus.close()

  def stop(self):
    self.mastodon.toot("Offline")
