import argparse

def options():
    # Create parser
    parser = argparse.ArgumentParser(
        description='Download info about your Steam wishlist',
        prog='wishlist_scraper',
        usage='py -m wishlist_scraper [OPTIONS] [ID]')
    
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
    args = parser.parse_args()
    return args
