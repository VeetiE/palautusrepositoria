from urllib import request
from project import Project
<<<<<<< HEAD
import tomli
=======
import toml

print(toml.load('pyproject.toml'))
>>>>>>> 00a73d2da94e4a393868618ff6065bbe894e3093

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        print(content)
<<<<<<< HEAD
        dict = dict(tomli.loads(content))

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(dict["tool"]["poetry"]["name"], dict["tool"]["poetry"]["description"], dict["tool"]["poetry"]["dependencies"], dict["tool"]["poetry"]["dev-dependencies"])
=======

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project("Test name", "Test description", [], [])
>>>>>>> 00a73d2da94e4a393868618ff6065bbe894e3093
