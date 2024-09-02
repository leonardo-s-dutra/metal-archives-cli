from typing import Final
import sys

try:
    from bs4 import BeautifulSoup
    import requests
    from requests import Response
    from argparse import ArgumentParser
    import json
except ImportError as e:
    print(f'Import Error: {e}')
    sys.exit()


BASE_URL : Final[str] = 'https://www.metal-archives.com'


def main() -> None:
    parser : ArgumentParser = ArgumentParser(
        description='Metal Archives CLI',
    )
    parser.add_argument(
        '--band',
        required=True,
        help='Name of the band to be searched'
    )

    args = parser.parse_args()

    band : str = args.band
    url : str = f'{BASE_URL}/bands/{band.lower().replace(' ', '_')}'
    request : Response = requests.get(
        url=url,
        headers={'User-Agent': 'Mozilla/5.0'}
    )

    if not request.ok:
        print(f'Request Error: status code {request.status_code}')
        sys.exit()

    soup : BeautifulSoup = BeautifulSoup(request.text, 'html.parser')


if __name__ == '__main__':
    main()
