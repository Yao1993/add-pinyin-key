from setuptools import setup

setup(
    name='add_pinyin_key',
    version='0.0.1',
    description='Add pinyin keys to Chinese bib entries',
    license='MIT',
    packages=['add_pinyin_key'],
    author='Yao Xu',
    author_email='yaoxu@mail.ustc.edu.cn',
    keywords=['Bib'],
    install_requires=[
        'pypinyin',
        'bibtexparser'
    ],
    entry_points={
        'console_scripts': [
            'add_pinyin_key = add_pinyin_key.__main__:main',
        ],
    },
    long_description_content_type='text/markdown',
    url='https://github.com/Yao1993/add-pinyin-key'
)