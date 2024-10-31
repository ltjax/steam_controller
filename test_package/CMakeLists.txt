cmake_minimum_required(VERSION 3.25)
project(PackageTest CXX)

set(CMAKE_CXX_STANDARD 14)

find_package(steam_controller CONFIG REQUIRED)

add_executable(example example.cpp)
target_link_libraries(example steam_controller::steam_controller)

