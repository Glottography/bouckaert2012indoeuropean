from setuptools import setup
import json


with open('metadata.json', encoding='utf-8') as fp:
    metadata = json.load(fp)


setup(
    name='cldfbench_bouckaert2012indoeuropean',
    description=metadata['title'],
    license=metadata.get('license', ''),
    url=metadata.get('url', ''),
    py_modules=['cldfbench_bouckaert2012indoeuropean'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'cldfbench.dataset': [
            'bouckaert2012indoeuropean=cldfbench_bouckaert2012indoeuropean:Dataset',
        ]
    },
    install_requires=[
        'pyglottography>=2.0',
    ],
    extras_require={
        'test': [
            'pytest-cldf',
        ],
    },
)
