import setuptools


try:
    with open('README.md') as f:
        readme = f.read()
except IOError:
    readme = ''


def _requires_from_file(filename):
    return open(filename).read().splitlines()


setuptools.setup(
    long_description=readme,
    packages=setuptools.find_packages(),
    install_requires=_requires_from_file('requirements.txt'),
    setup_requires=['pbr>=5.4.3'],
    pbr=True
)
