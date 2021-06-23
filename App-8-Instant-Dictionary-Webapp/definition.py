import pandas


class Definition:

    def __init__(self, term):
        self.term = term

    def get(self):
        pd = pandas.read_csv('data.csv')
        return tuple(pd.loc[pd['word'] == self.term]['definition'])
