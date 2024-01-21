from .urlfetcher import grab_URL
import json

class SteamApp:
    # Initialize Class with app ID
    def __init__(self, appID, country='us'):
        self.__appID = appID
        parameters = {'appids':appID, 'cc':country} # Info for a game
        grab = urlfetcher.grab_URL(f"https://store.steampowered.com/api/appdetails", parameters)
        self.__json = json.loads(grab.text)

    def get_appID(self):
        return self.__appID
    def get_name(self):
        try:
            name = self.__json[f"{self.__appID}"]["data"]["name"]
        except KeyError:
            name = "NULL"
        return name
    # Steam has a seperate API for ratings
    def get_rating(self):
        parameters = {'json':1,'language':'all'}
        grab = urlfetcher.grab_URL(f"https://store.steampowered.com/appreviews/{self.__appID}", parameters)
        jsonArray = json.loads(grab.text)
        try: 
            positive = jsonArray["query_summary"]["total_positive"]
            total = jsonArray["query_summary"]["total_reviews"]
            rating = round(positive / total * 100, 0)
        except:
            rating = "NULL"
        return rating
    def get_developer(self):
        try:
            developer = str(self.__json[f"{self.__appID}"]["data"]["developers"][0]).lstrip("[\'").rstrip("\']")
        except KeyError:
            developer = "NOT FOUND"
        return developer
    def get_publisher(self):
        try:
            publisher = str(self.__json[f"{self.__appID}"]["data"]["publishers"][0]).lstrip("[\'").rstrip("\']")
        except KeyError:
            publisher = "NULL"
        return publisher
    def get_ogprice(self):
        try:
            ogprice = self.__json[f"{self.__appID}"]["data"]["price_overview"]["initial"]/100
        except KeyError:
            ogprice = "NULL"
        return ogprice
    def get_cprice(self):
        try:
            cprice = self.__json[f"{self.__appID}"]["data"]["price_overview"]["final"]/100
        except KeyError:
            cprice = "NULL"
        return cprice
    def get_discount(self):
        try:
            discount = f"{self.__json[f"{self.__appID}"]["data"]["price_overview"]["discount_percent"]}"
        except KeyError:
            discount = "NULL"
        return discount
    def get_metascore(self):
        try:
            score = f"{self.__json[f"{self.__appID}"]["data"]["metacritic"]["score"]}"
        except KeyError:
            score = "NULL"
        return score
    def get_releasedate(self):
        try:
            if (self.__json[f"{self.__appID}"]["data"]["release_date"]["coming_soon"]):
                release_date = "Coming Soon"
            else:
                release_date = f"{self.__json[f"{self.__appID}"]["data"]["release_date"]["date"]}"
        except:
            release_date = "NULL"
        return release_date
    
    
                   
