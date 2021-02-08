import os

from conans import ConanFile, CMake, tools


class Gm2calcTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        if not tools.cross_building(self.settings):
            self.run(os.path.join("bin", "example-c"), run_environment=True)
            self.run(os.path.join("bin", "example-cpp"), run_environment=True)
