cmake_minimum_required(VERSION 3.23)
project(steam_controller)

set(CMAKE_CXX_STANDARD 14)

# Canonize platform selection
set(steam_controller_PLATFORM Undefined)
if(WIN32)
  set(steam_controller_PLATFORM PLATFORM_WIN32)
elseif(APPLE)
  set(steam_controller_PLATFORM PLATFORM_MACOS)
elseif(UNIX AND NOT APPLE)
  set(steam_controller_PLATFORM PLATFORM_LINUX)
else()
  message(FATAL_ERROR "Unsupported platform")
endif()

add_subdirectory(source)
add_subdirectory(demo)
