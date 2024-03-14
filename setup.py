from distutils.core import setup


def readme():
  with open('README.md', 'r') as f:
    return f.read()

setup(
  name='eeronorg',
  version='1.0.0',
  author='Cypr',
  author_email='cyprcyrp@gmail.com',
  description='New organaizer module',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/Cyrp48/Eeron/tree/master',
  install_requires=['flask>=3.0.2'],
  classifiers=[
    'Programming Language :: Python :: 3.12',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='eeron python',
  project_urls={
    'Documentation': 'https://github.com/Cyrp48/Eeron/tree/master'
  },
  python_requires='>=3.12.0'
)