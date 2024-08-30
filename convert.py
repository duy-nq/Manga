import xml.etree.ElementTree as ET
import os
import shutil
from config import get_config

BASE_PATH_ANNOTATION = r"D:\Project\Manga109\Manga109_released_2023_12_07\annotations.v2020.12.18"
BASE_PATH = r"D:\Project\Manga109\Manga109_released_2023_12_07"

def create_folder(manga_name, base_path, folder_type):
    folder_path = f"{base_path}\\{folder_type}\\{manga_name}"
    
    try:
        os.makedirs(folder_path, exist_ok=True)
    except Exception as e:
        print(e)

    return folder_path

def read_xml(manga_name):
    file_path = f"{BASE_PATH_ANNOTATION}\\{manga_name}.xml"

    with open(file_path, encoding='utf-8') as f:
        xml_data = f.read()

    return xml_data

def save_annotation(manga_name, page, annotation):
    folder_path = create_folder(manga_name, BASE_PATH, 'labels')

    file_path = f"{folder_path}\\{format_page(page)}.txt"
    with open(file_path, "w") as f:
        f.write("\n".join(annotation))

def annotation(data, img_width, img_height, class_id, class_name):
    annotations = []
    
    for obj in data.findall(class_name):
        xmin = float(obj.attrib['xmin'])
        ymin = float(obj.attrib['ymin'])
        xmax = float(obj.attrib['xmax'])
        ymax = float(obj.attrib['ymax'])

        x_center = (xmin + xmax) / 2 / img_width
        y_center = (ymin + ymax) / 2 / img_height
        box_width = (xmax - xmin) / img_width
        box_height = (ymax - ymin) / img_height

        row = f"{class_id} {x_center:.6f} {y_center:.6f} {box_width:.6f} {box_height:.6f}"
        annotations.append(row)

    return annotations

def format_page(page):
    if len(page) == 1:
        return f'00{str(page)}'
    elif len(page) == 2:
        return f'0{str(page)}'
    else:
        return str(page)

def remove_no_labels(manga_name, no_label: list[int]):
    if len(no_label) == 0:
        return
    
    folder_path = f"{BASE_PATH}\\images\\{manga_name}"
    folder_path_dest = create_folder(manga_name, BASE_PATH,'images_no_labels')
    
    for page in no_label:
        try:
            shutil.move(f"{folder_path}\\{format_page(page)}.jpg", f"{folder_path_dest}\\{format_page(page)}.jpg")
        except:
            continue
        
def process(xml_data, manga_name):
    root = ET.fromstring(xml_data)
    pages = root.find('pages')

    nothing = []

    for page in pages:
        img_width = float(page.attrib['width'])
        img_height = float(page.attrib['height'])
        page_number = page.attrib['index']

        yolo_annotations = []

        text = annotation(page, img_width, img_height, 0, 'text')
        frame = annotation(page, img_width, img_height, 1, 'frame')

        yolo_annotations += text
        yolo_annotations += frame

        if (len(yolo_annotations) == 0):
            nothing.append(page_number)
        else:
            save_annotation(manga_name, page_number, yolo_annotations)

    remove_no_labels(manga_name, nothing)  

def all_in_one():
    manga_list = os.listdir(f'{BASE_PATH}\\images')
    for manga in manga_list:
        xml_data = read_xml(manga)
        process(xml_data, manga)

def main():
    config = get_config()

    if config.mode == 'all':
        all_in_one()
    else:
        xml_data = read_xml(config.manga_name)
        process(xml_data, config.manga_name)

if __name__ == '__main__':
    main()
