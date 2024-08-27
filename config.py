import argparse

def get_config():
    parser = argparse.ArgumentParser()

    parser.add_argument('--main_url', type=str, default="'https://mangaqq.com/'")
    parser.add_argument('--manga_id', type=str, default='none')
    parser.add_argument('--cs', type=int, default=0)
    parser.add_argument('--ce', type=int, default=20)
    parser.add_argument('--lang', type=str, default='vie')
    parser.add_argument('--fold', type=str, default='Hanayome')

    args = parser.parse_args()

    return args
