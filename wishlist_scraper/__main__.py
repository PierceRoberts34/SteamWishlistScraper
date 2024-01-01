#!/usr/bin/env python
from __future__ import unicode_literals

# Execute with
# $ python wishlist_scraper/__main__.py (2.6+)
# $ python -m wishlist_scraper          (2.7+)

import sys

if __package__ is None and not hasattr(sys, 'frozen'):
    # direct call of __main__.py
    import os.path
    path = os.path.realpath(os.path.abspath(__file__))
    sys.path.insert(0, os.path.dirname(os.path.dirname(path)))

import wishlist_scraper

if __name__ == '__main__':
    wishlist_scraper.main()