from sample_web_interaction import *
import os

def test_it_should_download_a_file_from_the_web_with_a_url():
	url = "https://external-preview.redd.it/ETgaXY7lJOI8WhilZ8Qi0vfS_qRp7r1-idG0709VSYQ.jpg?auto=webp&s=369c06a081593206ecfb499c902d7a113a27f3ca"
	download_name = "cool_picture.jpg"
	download_link(url, download_name)
	assert os.path.exists(download_name)
