import argparse

def get_config():
    parser = argparse.ArgumentParser()

    parser.add_argument('--main_url', type=str, default="'https://mangaqq.com/'")
    parser.add_argument('--manga_id', type=str, default='none')
    parser.add_argument('--manga_name', type=str, default='MiraiSan')
    parser.add_argument('--mode', type=str, default='one')
    parser.add_argument('--cs', type=int, default=0)
    parser.add_argument('--ce', type=int, default=20)
    parser.add_argument('--lang', type=str, default='vie')
    parser.add_argument('--fold', type=str, default='Hanayome')
    parser.add_argument('--train', type=float, default=0.7)
    parser.add_argument('--val', type=float, default=0.2)
    parser.add_argument('--test', type=float, default=0.1)

    args = parser.parse_args()

    return args
