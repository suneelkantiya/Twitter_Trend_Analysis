import twint

c = twint.Config()
c.Search = "T20WorldCup"

twint.run.Search(c)