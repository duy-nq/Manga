import os
import shutil
from config import get_config
from random import shuffle

BASE_PATH_IMG = r"D:\Project\Manga109\Manga109_released_2023_12_07\images_all"
BASE_PATH_LABEL = r"D:\Project\Manga109\Manga109_released_2023_12_07\labels_all"
BASE_PATH_YOLO = r"D:\Project\Manga109\dataset"

def create_folder(path):
    try:
        os.makedirs(path, exist_ok=True)
    except Exception as e:
        print(e)

def split(type, data):
    type_path = f'{BASE_PATH_YOLO}\\{type}'
    img_path = f'{type_path}\\images'
    label_path = f'{type_path}\\labels'

    create_folder(type_path)
    create_folder(img_path)
    create_folder(label_path)

    for page in data:
        shutil.copy(f'{BASE_PATH_IMG}\\{page}', f'{img_path}\\{page}')
        shutil.copy(f'{BASE_PATH_LABEL}\\{page[:-4]}.txt', f'{label_path}\\{page[:-4]}.txt')
    
def main():
    config = get_config()
    manga_list = os.listdir(BASE_PATH_IMG)
    shuffle(manga_list)

    num = [int(config.train*len(manga_list)), int(config.val*len(manga_list)), int(config.test*len(manga_list))]

    train = manga_list[:num[0]]
    val = manga_list[num[0]:num[0]+num[1]]
    test = manga_list[num[0]+num[1]:]

    create_folder(BASE_PATH_YOLO)

    split('train', train)
    split('val', val)
    split('test', test)

if __name__ == '__main__':
    main()