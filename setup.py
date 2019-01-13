from setuptools import setup
from setuptools.command.install import install

class InstallGeckodriver(install):
    def run(self):
        install.run(self)
        from webdriverdownloader import GeckoDriverDownloader
        gdd = GeckoDriverDownloader()
        gdd.download_and_install()
        print("geckodriver installed")

setup (
    name="RedditOverwrite",
    version="1.1.0",
    install_requires=[
        "selenium",
        "requests",
        "tqdm",
        "webdriverdownloader"
    ],
    cmdclass={'install': InstallGeckodriver},

    author="Kixiron",
    author_email="kixiron.contact@gmail.com",
    description="Overwrite Reddit comments for safety and privacy",
    license="Apache 2.0",
    keywords="reddit overwrite privacy safety doxx comment",
    url="https://github.com/Kixiron/Reddit-Overwrite"
)
