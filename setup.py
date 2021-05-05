import sys
from setuptools import setup, find_packages

sys.path[0:0] = ['Deep-Flow-Prediction']
#from version import __version__

setup(
  name = 'Deep-Flow-Prediction',
  packages = find_packages(),
  #version = __version__,
  license='NO LICENSE',
  description = 'A framework for fluid flow (Reynolds-averaged Navier Stokes) predictions with deep learning'

  author = 'Shauray Singh',
  author_email = 'shauray9@gmail.com',
  url = 'https://github.com/shauray8/Deep-Flow-Prediction',
  keywords = ['Machine learning',"physics","fluid dynamics", 'machine learning'],
  install_requires=[
      'numpy',
      'tqdm',
      'torch',
      'torchvision',
      'pillow',
  ],
)
