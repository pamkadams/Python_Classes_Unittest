import unittest

#CLASS ART
class Art:
    """ Art object contains information about the artwork.
    :param
        artist - str
        title -str
        medium str
        year - int
       owner - object (client class)
        """

    def __init__(self, artist, title, medium, year, owner):
        self.artist = artist
        self.title = title
        self.medium = medium
        self.year = year
        self.owner = owner

    def __repr__(self):
        """
                String representation of the object
                :param
                    self
                    :return: (string)
                """
        return f'{self.artist}. "{self.title}". {self.year}, {self.medium}. {self.owner}'


#CLASS MARKETPLACE
class Marketplace:
    """ Marketplace object contains information about the place where art can be bought/sold.
        param:
            Listings - list
            """

    def __init__(self):
        self.listings = []

    def add_listing(self, new_listing):
        """
            Inserts the new listing for an art object that is for sale into the listings list
            :param
                self
                new_listings - list element of art (object, price which is a str, and seller which is a str)
            """

        self.listings.append(new_listing)

    def remove_listing(self, expired_listing):
        """
            Removes the listing for an art object that is from the listings list
            :param
                self
                expired_listings - list element of art (object, price which is a str, and seller which is a str)
            :return
                listing - list
            """


        self.listings.remove(expired_listing)
        return self.listings

    def show_listings(self):
        """
            Removes the listing for an art object that is from the listings list
            :param
                self
                expired_listings - list element of art (object, price which is a str, and seller which is a str)
            """

        for listing in self.listings:
            print(listing)


#CLASS CLIENT
class Client:
    """ Client object contains information about organizations and people who own art.
        :param
            name - str
            location -str
            is_museum - boolean describing if it is an organization (true)
            """

    def __init__(self, name, location, is_museum):
        self.name = name
        self.location = location
        self.is_museum = is_museum

    def __repr__(self):
        """
            String representation of the object
            :param
                self
                :return: (string)
            """

        return f"{self.name}. {self.location}"

    def sell_artwork(self, artwork, price):
        """
          This method adds a for-sale listing for an artwork in the marketplace instance's listing instance
           :param
               self
               artwork - art object
               price - str
           """
        if self == artwork.owner:
            new_listing = Listing(artwork, price, self.name)
            veneer.add_listing(new_listing)


    def buy_artwork(self, artwork):
        """
          This method validates buyers, changes ownership, and removes the listing from the marketplace instance's listing.
            :param
               self
               artwork - art object
           """

        if self != artwork.owner:
            art_listing = None
            for listing in veneer.listings:
                if listing.art.title == artwork.title:
                    art_listing = listing
                    break
            if art_listing != None:
                listing.art.owner = self
                veneer.remove_listing(art_listing)

# CLASS TO LIST ART TO BUY?SELL
class Listing:
    """ Listing object contains information about the artwork that is on sale in a marketplace instance.
        :param
            art - Art object (remember this is a nested object that includes the client object (who is the owner of the object)
            price -str
            """

    def __init__(self, art, price, seller):
        self.art = art
        self.price = price
        self.seller = seller

    def __repr__(self):
        """
            String representation of the object
            :param
                self
                :return: (string)
            """
        return f'{self.art.title}  {self.price}, {self.seller}'

if __name__ == '__main__':
	unittest.main()

# TEST CODE
veneer = Marketplace()

# test Client
edytta = Client("Edytta Halpirt", "Private Collection", False)
moma = Client("The MOMA", "New York", True)
lucky_dude = Client("Lucky Person", "CT", False)

# test Art class
girl_with_mandolin = Art("Picasso, Pablo", 'Girl with a Mandolin (Fanny Tellier)', 'oil on canvas', 1910, edytta)
girl_with_pearl_earring = Art("Veemer, Jan ", 'Girl with a Pearl Earring', 'oil on canvas', 1665, moma)
the_scream = Art("Munch, Edvard", "The Scream", "oil tempera, pastel and crayon", 1883, moma)
sunflowers = Art("Van Gogh, Vincent", "Sunflowers", 'oil on canvas', 1888, moma)
pipe = Art("Magritte, Rene", "Ceci N'est pas une Pipe", 'oil on canvas', 1929, lucky_dude)

print("Veneer listings available for sale", veneer.listings)

# test purchase of from one client to another
edytta.sell_artwork(girl_with_mandolin, '$6M (USD)')
moma.sell_artwork(the_scream, '$200M (USD)')


# MOMA buys girl with mandolin
moma.buy_artwork(girl_with_mandolin)
veneer.show_listings()
