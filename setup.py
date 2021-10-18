import setuptools


with open('README.md') as f:
    README = f.read()

setuptools.setup(
    author="Xephonine // Hylaxe",
    author_email="priyanshudeb3@gmail.com",
    name='XPHN_ezDiscord',
    license="MIT",
    description='Easily create and use Discord webhooks and bots with barely 2 lines of code!',
    version='v0.0.1',
    long_description=README,
    url='https://github.com/XephonineDeb/XPHN_ezDiscord/',
    packages=setuptools.find_packages(),
    python_requires=">=3.1",
    install_requires=['requests','discord'],
    classifiers=[
        # Trove classifiers
        # (https://pypi.python.org/pypi?%3Aaction=list_classifiers)
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
    ],
)