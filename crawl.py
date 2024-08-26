from config import get_config
import requests
import os

URL = 'https://mangaqq.com/'

def construct_url(manga_id, chapter, img):
    img_url = f'{URL}/{manga_id}/{chapter}/{img}.jpg'
    return img_url

def download_image(manga_id, chapter, img, out_folder):
    img_url = construct_url(manga_id, chapter, img)

    response = requests.get(img_url)
    
    if response.status_code == 200:
        out_path = f'./{out_folder}/chap_{chapter}/{img}.jpg'
        
        with open(out_path, 'wb') as file:
            file.write(response.content)
        file.close()
        return 0
    else:
        print("Please check out manga_id or chapter! {response.status_code}")
        return 1

def main():
    config = get_config()

    cs, ce = config.cs, config.ce
    manga_id = config.manga_id
    OUT_FOLDER = f'{config.fold}/{config.lang}'

    for chapter in range(cs, ce):
        s = 0
        try:
            os.makedirs(f'./{OUT_FOLDER}/chap_{chapter}')
        except Exception as e:
            print(e)
            
        for img in range(2, 50):
            s += download_image(manga_id, chapter, img, OUT_FOLDER)
            if s == 3:
                break        

if __name__ == '__main__':
    main()


    

