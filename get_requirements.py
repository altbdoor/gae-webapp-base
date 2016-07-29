#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals

from os import listdir, remove, walk
from os.path import abspath, dirname, isdir, isfile, join, normpath, relpath

import shlex
import shutil
import subprocess
import zipfile

# prep paths
current_dir = dirname(abspath(__file__))
libs_dir = join(current_dir, 'libs')

print('> Build libs starting')

# clearing libs
print("> Clearing old libs")
for item in listdir(libs_dir):
    item_dir = join(libs_dir, item)

    if isdir(item_dir):
        shutil.rmtree(item_dir)

compiled_zip_path = join(libs_dir, 'compiled.zip')
if isfile(compiled_zip_path):
    remove(compiled_zip_path)

# pip install
print("> Installing new libs")
subprocess.call(shlex.split(
    'pip install -q -r requirements.txt -t ./libs/ --disable-pip-version-check'
))

# clear pyc
print("> Clearing .pyc files")
for root, dirnames, filenames in walk(libs_dir):
    for filename in filenames:
        if filename.endswith('.pyc'):
            remove(join(root, filename))

# zip zap
print("> Zipping dependencies")
zip_path = join(libs_dir, 'compiled.zip')
zip_handler = zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED)

for root, dirs, files in walk(libs_dir):
    if normpath(root) != normpath(libs_dir) and not root.endswith('.dist-info'):
        for file in files:
            zip_handler.write(
                join(root, file),
                relpath(join(root, file), libs_dir)
            )

zip_handler.close()

print("> Done")
