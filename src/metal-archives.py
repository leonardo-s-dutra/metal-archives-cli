from typing import List, Final
import sys

try:
    import enmet
    from argparse import ArgumentParser
except ImportError as e:
    print(f'Import Error: {e}')
    sys.exit()


def print_genres(band : enmet.Band) -> None:
    print('\tGenres\t\t: ', end='')

    genres : List[str] = band.genres

    if len(genres) == 1:
        print(f'{genres[0]}')
    else:
        print(
            f'{', '.join(genres[:-1])}, {genres[-1]}')

def print_lyrical_themes(band : enmet.Band) -> None:
    print('\tLyrical Themes\t: ', end='')

    lyrical_themes : List[str] = band.lyrical_themes

    if len(lyrical_themes) == 1:
        print(f'{lyrical_themes[0]}')
    else:
        print(
            f'{', '.join(lyrical_themes[:-1])}, {lyrical_themes[-1]}')


def main() -> None:
    parser : ArgumentParser = ArgumentParser(
        description='Metal Archives CLI',
    )
    parser.add_argument(
        '--band',
        required=True,
        help='Name of the band to be searched'
    )
    parser.add_argument(
        '--genre',
        required=False,
        action='store_true',
        help='Get genres from searched band'
    )
    parser.add_argument(
        '--lyrical_themes',
        required=False,
        action='store_true',
        help='Get lyrical themes from searched band'
    )

    args = parser.parse_args()

    band_name : str = args.band
    genres_flag : bool = args.genre
    lyrical_themes_flag : bool = args.lyrical_themes

    if band_name == None:
        return
    
    try:
        band_search_result : enmet.Band = enmet.search_bands(
            name=band_name,
            strict=True
        )[0]
    except IndexError:
        print('\n\tBand not found\n')
        return

    print('')
    print(f'\tBand\t\t: {band_search_result.name}')

    if genres_flag == True:
        print_genres(band_search_result)
    
    if lyrical_themes_flag == True:
        print_lyrical_themes(band_search_result)

    print('')


if __name__ == '__main__':
    main()
