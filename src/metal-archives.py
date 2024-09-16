from typing import List, Final
import sys

try:
    import enmet
    from argparse import ArgumentParser
except ImportError as e:
    print(f'Import Error: {e}')
    sys.exit()


def print_genres(band : enmet.Band) -> None:
    print('\tGenres\t: ', end='')

    genres : List[str] = band.genres

    if len(genres) == 1:
        print(f'{genres[0]}')
    else:
        print(
            f'{', '.join(band.genres[:-1])}, {band.genres[-1]}')


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
        help='Get lyrical themes from searched band'
    )

    args = parser.parse_args()

    band_name : str = args.band
    genres_flag : bool = args.genre

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
    print(f'\tBand\t: {band_search_result.name}')

    if genres_flag == True:
        print_genres(band_search_result)
    
    print('')


if __name__ == '__main__':
    main()
