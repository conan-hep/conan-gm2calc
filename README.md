[![Build Status Travis](https://travis-ci.org/conan-hep/conan-gm2calc.svg)](https://travis-ci.org/conan-hep/conan-gm2calc)

## Conan package recipe for [*GM2Calc*](https://github.com/GM2Calc/GM2Calc)

References:

* Peter Athron, Markus Bach, Helvecio G. Fargnoli, Christoph
  Gnendiger, Robert Greifenhagen, Jae-hyeon Park, Sebastian Paßehr,
  Dominik Stöckinger, Hyejung Stöckinger-Kim, Alexander Voigt,
  *GM2Calc: Precise MSSM prediction for (g-2) of the muon*,
  [*Eur.Phys.J.* **C76** (2016) no.2, 62](https://inspirehep.net/record/1401235)
  [arXiv:1510.08071](https://arxiv.org/abs/1510.08071)


## For users

### Installation of dependencies

GM2Calc can be installed with conan by running:

    conan install GM2Calc/1.7.2@conan/stable

Alternatively a `conanfile.txt` file can be created in your project
directory with the following content:

    [requires]
    GM2Calc/1.7.2@conan/stable

    [generators]
    cmake
    make
    pkg_config

The dependencies of your project are then installed by running:

    mkdir build
    cd build
    conan install ..

### Building your project

Afterwards the project can be configured via CMake and build with
`make` by running:

    cmake ..
    make

Alternatively the project can be configured with Meson and build with
`ninja` by running:

    export PKG_CONFIG_PATH=.
    meson ..
    ninja

Alternatively the project can be build with `make` by running:

    make -f ../Makefile

A complete example can be found in the `examples/` directory.


## Build and package

The following command both runs all the steps of the conan file, and
publishes the package to the local system cache.  This includes
downloading dependencies from "build_requires" and "requires" , and
then running the build() method.

    $ conan create . conan/stable


### Available Options

| Option        | Default          | Possible Values                          |
| ------------- |------------------|------------------------------------------|
| shared        | False            |  [True, False]                           |
| fPIC          | True             |  [True, False]                           |


## Conan Recipe License

NOTE: The conan recipe license applies only to the files of this
recipe, which can be used to build and package GM2Calc.  It does *not* in
any way apply or is related to the actual software being packaged.

[MIT](LICENSE)
