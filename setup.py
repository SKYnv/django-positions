from setuptools import setup, find_packages
 
setup(
    name='django-positions-2',
    version='0.6.0rc0',
    description='A Django field for custom model ordering',
    author='Joel Watts',
    author_email='joel@joelwatts.com',
    maintainer='NyanKiyoshi',
    maintainer_email='hello@vanille.bid',
    url='https://github.com/NyanKiyoshi/django-positions',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
        'Framework :: Django :: 1.7',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 2.0',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3 :: Only',
    ],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Django>=1.11,<2.1'
    ],
)
