from setuptools import find_packages, setup
import os
from glob import glob
package_name = 'mypkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Shuhei Yanagihori',
    maintainer_email='shuhei.daigaku@gmail.com',
    description='a package for practice',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = mypkg.talker:main',
            'listener = mypkg.listener:main',
            'talker1 = mypkg.talker1:main',
            'listener1 = mypkg.listener1:main',
            'listener2 = mypkg.listener2:main',
            'listener3 = mypkg.listener3:main',
        ],
    },
)
