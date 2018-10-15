import sys
import os
import re
from setuptools import setup, find_packages

# 'setup.py publish-test' shortcut
if sys.argv[-1] == 'publish-test':
    os.system('rm -r dist/*')
    os.system('python setup.py sdist')
    os.system('twine upload -r pypitest dist/*')
    sys.exit()
# 'setup.py publish' shortcut
if sys.argv[-1] == 'publish':
    os.system('rm -r dist/*')
    os.system('python setup.py sdist')
    os.system('twine upload dist/*')
    sys.exit()

# read the version number from source
version = re.search("^__version__\s*=\s*'(.*)'", open('fuzzy_swagger/fuzzy_swagger.py').read(), re.M).group(1)

# Get the long description from the relevant file
try:
    # in addition to pip install pypandoc, might have to: apt install -y pandoc
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError, OSError) as e:
    print("Error converting READMD.md to rst:", str(e))
    long_description = open('README.md').read()

setup(name='fuzzy-swagger',
      version=version,
      description='Generates and run API fuzz tests against endpoints defined in swagger document.',
      long_description=long_description,
      keywords=['swagger', 'apis', 'fuzz', 'testing'],
      author='Nauman Leghari',
      author_email='nauman@docker-files.com',
      url='https://github.com/namuan/fuzzy-swagger',
      install_requires=[],
      packages=find_packages(exclude=['pypandoc']),
      entry_points={
        "console_scripts": [
            'fuzzy-swagger = fuzzy_swagger.fuzzy_swagger:main'
        ]
        },
      license='MIT',
      classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        ]
     )
