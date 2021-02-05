import os
from conans import ConanFile, CMake, tools


class Gm2calcConan(ConanFile):
    name = "GM2Calc"
    license = "GPL-3.0"
    author = "Alexander Voigt"
    url = "https://github.com/GM2Calc/GM2Calc"
    description = "C++ library to calculate the anomalous magnetic moment of the muon in the MSSM"
    topics = ("HEP")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True, "boost:header_only": True}
    build_policy = "missing"
    exports = ["LICENSE"]
    exports_sources = ["CMakeLists.txt"]
    generators = "cmake"
    requires = ("eigen/[>=3.1]@conan/stable")
    build_requires = ("boost/[>=1.37.0]@conan/stable", "libuuid/[>=1.0.0]")
    _cmake = None

    @property
    def _source_subfolder(self):
        return "source_subfolder"

    @property
    def _build_subfolder(self):
        return "build_subfolder"

    def source(self):
        tools.get(**self.conan_data["sources"][self.version])
        os.rename("{}-{}".format(self.name, self.version), self._source_subfolder)

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def _configure_cmake(self):
        if self._cmake:
            return self._cmake
        self._cmake = CMake(self)
        self._cmake.configure(build_folder=self._build_subfolder)
        return self._cmake

    def package(self):
        self.copy("LICENSE", src=self._source_subfolder, dst="licenses", keep_path=False)
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
