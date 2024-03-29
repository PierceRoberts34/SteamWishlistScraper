import re # Regular expressions for matching Steam AppIDs
from .urlfetcher import grab_URL # Retry in case of timeout
from .SteamApp import SteamApp
from .options import options

def main():
    # Get command line arguments
    args = options()
    SteamID = args.id
    Country = args.country
    WishlistURL = f"https://store.steampowered.com/wishlist/id/{SteamID}"
    
    # Capture URLs from Wishlist
    grab = grab_URL(WishlistURL)
    regex = re.findall("(?<=\"appid\":)(\\d+)(?=,\"priority)",grab.text)
    
    # Check whether any games have been scraped
    try:
        regex[0]
    except IndexError:
        print("No games found, make sure your profile is set to public")
        return 1

    SteamCSV = open(f'{SteamID}\'s Wishlist.csv', 'a')
    csv_columns = ["App ID","Name","%Rating","Developer","Publisher","Original Price","Current Price","%Discount","Metascore"]

    for column in csv_columns:
        SteamCSV.write(f"{column},")
    SteamCSV.write("\n")
    print("Scraping wishlist, please wait...")
    for appID in regex:
        print(appID)
        game = SteamApp(appID, Country)
        SteamCSV.write(f"{game.get_appID()},\"{game.get_name()}\",{game.get_rating()},\"{game.get_developer()}\",\"{game.get_publisher()}\",{game.get_ogprice()},{game.get_cprice()},{game.get_discount()},{game.get_metascore()}\n")

if __name__ == '__main__':
    wishlist-scraper.main()
