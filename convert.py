import xml.etree.ElementTree as ET

def read_xml(manga_name):
    base_path = r"D:\Project\Manga109\Manga109_released_2023_12_07\annotations.v2020.12.18"
    file_path = f"{base_path}\\{manga_name}.xml"

    with open(file_path, encoding='utf-8') as f:
        xml_data = f.read()

    return xml_data

xml_data = '''<page index="79" width="1654" height="1170">
<text id="0007c82d" xmin="1153" ymin="761" xmax="1223" ymax="814">俺はひとりなんだ</text>
<frame id="0007c82e" xmin="10" ymin="762" xmax="814" ymax="1163"/>
<!-- More elements... -->
</page>'''

# Parse the XML data
root = ET.fromstring(xml_data)

# Get image width and height
image_width = float(root.attrib['width'])
image_height = float(root.attrib['height'])

# Prepare list to store YOLO format annotations
yolo_annotations = []

# Iterate over all 'text' elements
for text in root.findall('text'):
    class_id = 0  # Class ID for text boxes
    xmin = float(text.attrib['xmin'])
    ymin = float(text.attrib['ymin'])
    xmax = float(text.attrib['xmax'])
    ymax = float(text.attrib['ymax'])

    # Convert to YOLO format
    x_center = (xmin + xmax) / 2 / image_width
    y_center = (ymin + ymax) / 2 / image_height
    box_width = (xmax - xmin) / image_width
    box_height = (ymax - ymin) / image_height

    # Create a YOLO annotation line
    annotation = f"{class_id} {x_center:.6f} {y_center:.6f} {box_width:.6f} {box_height:.6f}"
    yolo_annotations.append(annotation)

# Save annotations to a .txt file
output_file = "image_79.txt"
with open(output_file, "w") as f:
    f.write("\n".join(yolo_annotations))

print(f"YOLO annotations saved to {output_file}")

def process(xml):
    pass

def main():
    pass

if __name__ == '__main__':
    main()
