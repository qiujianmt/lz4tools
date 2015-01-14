#!/usr/bin/env python


from setuptools import setup, Extension

VERSION = (1, 2, 1, 2)
VERSION_STR = ".".join([str(x) for x in VERSION])

setup(
    name='lz4tools',
    version=VERSION_STR,
    description="LZ4Frame Bindings and tools for Python",
    license = 'BSD',
    long_description=open('README.rst', 'r').read(),
    author='Christopher Jackson',
    author_email='darkdragn.cj@gmail.com',
    url='https://github.com/darkdragn/lz4file',
    packages=['lz4tools'],
    scripts=['lz4toolsCli'],
    ext_modules=[
        Extension('lz4f', [
            'src/python-lz4f.c',
        ], extra_compile_args=[
            "-std=c99",
            "-O3",
            "-Wall",
            "-W",
            "-Wundef",
            "-DVERSION=\"%s\"" % VERSION_STR,
            "-DLZ4_VERSION=\"r123\"",
        ], libraries=[
            "lz4",
        ])],
    setup_requires=["nose>=1.0"],
    test_suite = "nose.collector",
    keywords = ['lz4', 'lz4frame', 'lz4file', 'lz4tar'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: BSD License',
        'Intended Audience :: Developers',
        'Programming Language :: C',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
