# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import re, ast

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in waroeng_bebek_selamet/__init__.py
_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('waroeng_bebek_selamet/__init__.py', 'rb') as f:
	version = str(ast.literal_eval(_version_re.search(
		f.read().decode('utf-8')).group(1)))

setup(
	name='waroeng_bebek_selamet',
	version=version,
	description='Aplikasi dengan kearifan lokal yang menyediakan berbagai macam makanan olahan ayam pilihan. Tidak ada bebek, karna bebeknya selamet semua. tinggal ayam',
	author='Kelompok 6',
	author_email='warungbebek@mail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
