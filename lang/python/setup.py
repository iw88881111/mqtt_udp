#!/bin/python

from setuptools import setup, find_packages

setup(
    name='mqttudp',
    version='0.1',
    description='An MQTT/UDP implementation in Python',
    long_description="MQTT/UDP is a simplest brokerless variation of MQTT protocol based on UDP broadcast. See https://github.com/dzavalishin/mqtt_udp for more prog. languages and info.",
    author='Dmitry Zavalishin',
    author_email='dz@dz.ru',
    url='https://github.com/dzavalishin/mqtt_udp',
    packages=find_packages(),
    #platforms='any',
    #zip_safe=False,
    include_package_data=True,
    #install_requires=['admintools==0.1'],
    classifiers=[
        #'Development Status :: 5 - Production/Stable',
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: MQTT',
        'Topic :: Internet :: IoT',
    ],
    #data_files=[(
    #      '/path/to/icons', ['myApp/icons/a.ico', 'myApp/icons/e.ico']
    #)],
)