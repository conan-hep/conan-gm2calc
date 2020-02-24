import os
from conans import ConanFile, CMake, tools


class Gm2calcConan(ConanFile):
    name = "GM2Calc"
    version = "1.6.0"
    license = "GPL-3.0"
    author = "Alexander Voigt"
    url = "https://github.com/GM2Calc/GM2Calc"
    description = "C++ library to calculate the anomalous magnetic moment of the muon in the MSSM"
    topics = ("HEP")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = ("shared=False", "fPIC=True")
    build_policy = "missing"
    exports = ["LICENSE", "FindGM2Calc.cmake"]
    generators = "cmake"
    requires = ("eigen/[>=3.1]@conan/stable", "boost/[>=1.37.0]@conan/stable")
    _source_subfolder = "GM2Calc"

    def source(self):
        self.run("git clone https://github.com/GM2Calc/GM2Calc")

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder=self._source_subfolder)
        cmake.build()

    def package(self):
        _header_dst     = "include{}gm2calc".format(os.sep)
        _pub_header_src = "{}{}include{}gm2calc".format(self._source_subfolder, os.sep, os.sep)

        self.copy("*.h", dst=_header_dst, src=_pub_header_src, keep_path=False)
        self.copy("*.hpp", dst=_header_dst, src=_pub_header_src, keep_path=False)
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)
        self.copy("LICENSE", src=self._source_subfolder, dst="licenses", keep_path=False)
        self.copy('FindGM2Calc.cmake', '.', '.')

    def package_info(self):
        self.cpp_info.libs = ["gm2calc"]
