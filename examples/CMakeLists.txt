cmake_minimum_required(VERSION 2.8.12)
project(PackageTest CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

add_executable(test_gm2calc test_gm2calc.cpp)
target_link_libraries(test_gm2calc CONAN_PKG::GM2Calc)
