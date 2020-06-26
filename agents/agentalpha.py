from ananas import PineappleBot, ConfigurationError, hourly, reply
import markovify
from bs4 import BeautifulSoup

class AgentAlpha(PineappleBot):

  def start(self):
    self.mastodon.toot("Online")

  @hourly(minute=40)
  def say_something(self):
    # Load the corpus
    corpus = open("./a.txt","r")

    # generate markov model
    markov_model = markovify.Text(corpus.read())
    self.mastodon.toot(markov_model.make_sentence())

    corpus.close()

  @reply
  def respond(self, mention, user):

    # Extract the text of the mention
    soup = BeautifulSoup(mention["content"], features="html.parser")
    mention_string = soup.get_text()
    print(mention_string)

    # Load the corpus
    corpus = open("./data/a.txt","r")

    # generate markov model
    markov_model = markovify.Text(corpus.read() + " " + mention_string)
    
    # Generate a reply
    reply_string = markov_model.make_sentence()
    print(reply_string)

    # Reply with a generated sentence
    self.mastodon.toot(f"@{user['acct']}, {reply_string}")

    corpus.close()

  def stop(self):
    self.mastodon.toot("Offline")
