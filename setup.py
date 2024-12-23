from setuptools import setup, find_packages

setup(
    name='OpenBrowser',
    version='0.1.1',
    author='woopy',
    author_email='woopygit@icloud.com',
    description='OpenBrowser Help you to open selenium browser in one function',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/trimoon056/TrimoonCam2Telegram',
    packages=find_packages(),
    package_data={
            'WoopyCE': ['content/fonts/DynaPuff/DynaPuff-Regular.ttf'],  # Include il font nel pacchetto
        },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7, <3.13',
    install_requires=[
        'selenium',
        'webdriver-manager'
    ],
)