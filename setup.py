import setuptools
import os

# Load dependency. Credit goes to https://stackoverflow.com/a/53069528
install_requires = []
lib_folder = os.path.dirname(os.path.realpath(__file__))
requirement_path = lib_folder + "/requirements.txt"
if os.path.isfile(requirement_path):
    with open(requirement_path) as f:
        install_requires = f.read().splitlines()

setuptools.setup(
    name="yolov3",
    install_requires=install_requires,
    version="0.0.1",
    description="YOLOv3 in PyTorch with training and inference module implemented.",
    url="https://github.com/mzweilin/YOLOv3-in-PyTorch",
    packages=["yolov3", "yolov3/datasets"],
)
