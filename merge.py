import uuid
import os
import shutil

BASE_PATH = r"D:\Project\Manga109\Manga109_released_2023_12_07"
BASE_PATH_LABEL = r"D:\Project\Manga109\Manga109_released_2023_12_07\\labels"
BASE_PATH_IMG = r"D:\Project\Manga109\Manga109_released_2023_12_07\\images"

def merge():
    manga_list = os.listdir(BASE_PATH_IMG)

    for manga in manga_list:
        for img in os.listdir(f'{BASE_PATH_IMG}\\{manga}'):
            uid = str(uuid.uuid4())
            shutil.copy(f'{BASE_PATH_IMG}\\{manga}\\{img}', f'{BASE_PATH}\\images_all\\{uid}.jpg')
            shutil.copy(f'{BASE_PATH_LABEL}\\{manga}\\{img[:-4]}.txt', f'{BASE_PATH}\\labels_all\\{uid}.txt')

def main():
    merge()

if __name__ == '__main__':
    main()
