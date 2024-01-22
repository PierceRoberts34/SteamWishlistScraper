# Define program launch arguments
import argparse

def options():
    parser = argparse.ArgumentParser(description='Download info about your Steam wishlist')
    # Set options for scraper
    parser.add_argument(
        'id',
        metavar='ID',
        help='Your Steam ID.'
    )
    parser.add_argument('--country',
        default='us',
        help="Set ISO 3166-1 country code for regional pricing. Default is us"
    )
    scraper=parser.add_argument_group('Scraper Options')
    scraper.add_argument('--include_absolute_discount',
        action='store_true',
        help='Add a column for absolute discount'
    )
    scraper.add_argument('--include_steampage',
        action='store_true',
        help='Include a link to the app\'s Steam Store page'
    )
    scraper.add_argument('--include_steamdblink',
       action='store_true',
       help='Include a link to the app\'s SteamDB page'
    )
    args = parser.parse_args()
    return args
