import os
import sys

from kivy.core.image import Image as CoreImage
from kivy.uix.image import Image as kiImage
from io import BytesIO
from PIL import Image


if getattr(sys, 'frozen', False):
    # noinspection PyProtectedMember,PyUnresolvedReferences
    base_path = sys._MEIPASS  # PyInstaller's base directory
else:
    # The app is run as a script
    base_path = os.path.dirname(os.path.abspath(__file__))

images_folder_path = os.path.join(base_path, 'images')
doc_folder_path = os.path.join(base_path, 'documents')

class ResourceProvider:
    # -------------------------------------------
    # images

    @staticmethod
    def get_blended_logo_path() -> str:
        return os.path.join(images_folder_path, 'blended_logo.png')

    @staticmethod
    def get_logo_path() -> str:
        return os.path.join(images_folder_path, 'logo.png')

    @staticmethod
    def get_foldericon_path() -> str:
        return os.path.join(images_folder_path, 'folder.png')

    @staticmethod
    def get_fileicon_path() -> str:
        return os.path.join(images_folder_path, 'file.png')

    @staticmethod
    def get_collapsed_icon_path() -> str:
        return os.path.join(images_folder_path, 'collapsed.png')

    @staticmethod
    def get_expanded_icon_path() -> str:
        return os.path.join(images_folder_path, 'expanded.png')

    @staticmethod
    def get_loading_icon_path() -> str:
        return os.path.join(images_folder_path, 'loading.png')

    @staticmethod
    def get_checked_box_path() -> str:
        return os.path.join(images_folder_path, 'checked_box.png')

    @staticmethod
    def get_unchecked_box_path() -> str:
        return os.path.join(images_folder_path, 'unchecked_box.png')

    @staticmethod
    def get_kivy_image(width, imgPath, **kwargs):
        pil_image = Image.open(imgPath)
        aspect_ratio = pil_image.height / pil_image.width
        new_height = int(width * aspect_ratio)
        resized_image = pil_image.resize((int(width), new_height), Image.LANCZOS)
        return pil_to_kivy_image(resized_image, **kwargs)

    # -------------------------------------------
    # documents

    @staticmethod
    def get_template_csv() -> str:
        return os.path.join(doc_folder_path, 'template.csv')

    @staticmethod
    def get_empty_path() -> str:
        return os.path.join(images_folder_path, 'empty.png')


# -------------------------------------------
# resizing with PIL instead of kivy

def pil_to_kivy_image(pil_image, **kwargs):
    data = BytesIO()
    pil_image.save(data, format='png')
    data.seek(0)
    core_image = CoreImage(BytesIO(data.read()), ext='png')
    kivy_image = kiImage(**kwargs)
    kivy_image.texture = core_image.texture
    return kivy_image
