

class Alert(object):
    def __init__(self, user, price_limit, item):
        self.user = user
        self.price_limit = price_limit
        self.item = item

    #good practice to use the repr to define what the output will look like.
    def __repr__(self):
        return "<Alert for {} on item {} with price {}>".format(self.user.email, self.item.name, self.price_limit)
        pass