from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

setup(
    name='neterr',
    description='Useful groupings of exceptions for working with network requests.',
    long_description=readme,
    packages=find_packages(exclude=['tests']),
    use_scm_version=True,
    author='Matt Wisniewski',
    author_email='hello@mattw.life',
    url='https://github.com/polishmatt/neterr',
    keywords=[
        'network',
        'api',
        'http',
        'request'
    ],
    license='Apache License 2.0',
    setup_requires=[
        'pytest-runner',
        'setuptools_scm',
    ],
    tests_require=[
        'pytest',
        'pytest-flake8',
        'pytest-cov',
        'requests',
    ],
    include_package_data=True,
    zip_safe=False,
    python_requires='>=3.6.0',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
