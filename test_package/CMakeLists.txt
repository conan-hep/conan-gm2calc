cmake_minimum_required(VERSION 2.8.12)
project(PackageTest C CXX)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(example-cpp example.cpp)
target_link_libraries(example-cpp ${CONAN_LIBS})

add_executable(example-c example.cpp)
target_link_libraries(example-c ${CONAN_LIBS})
