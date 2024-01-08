from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

VERSION = '0.0.2'
DESCRIPTION = 'Wrapper for OpenWeather API.'
LONG_DESCRIPTION = (here / "README.md").read_text(encoding="utf-8")

# Setting up
setup(
    # the name must match the folder name 'verysimplemodule'
    name="openweathermap_api",
    version=VERSION,
    author="Bartlomiej Niemiec",
    author_email="<bniemiec11@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    url="https://github.com/bartlomiej-niemiec/py-open-weather-wrapper",
    packages=find_packages(where="src/openweathermap_api"),
    install_requires=['requests'],  # add any additional packages that
    # needs to be installed along with your package. Eg: 'caer'

    keywords=['python', 'open-weather-map'],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3.9",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    package_dir={"": "src/openweathermap_api"},
)
