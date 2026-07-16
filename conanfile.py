from conan import ConanFile
from conan.tools.cmake import CMake, cmake_layout


class SteamControllerConan(ConanFile):
    name = "steam_controller"
    version = "1.1"
    license = "MIT"
    author = "Marius Elvert marius.elvert@googlemail.com"
    url = "https://github.com/ltjax/steam_controller"
    description = "Access the Steam Controller without Steam"
    topics = ("hardware", "gamepad")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    generators = "CMakeDeps", "CMakeToolchain"
    exports_sources = "source/*", "externals/*",\
                      "!externals/hidapi/LICENSE-*.txt",\
                      "include/*", "CMakeLists.txt",\
                      "demo/*"

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC
    
    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def layout(self):
        cmake_layout(self)

    def package_info(self):
        self.cpp_info.libs = ["steam_controller"]
        if self.settings.os == "Windows":
            self.cpp_info.system_libs.append("Setupapi")
        if self.settings.os == "Linux":
            self.cpp_info.system_libs.append("udev")
        if self.settings.os == "Macos":
            self.cpp_info.frameworks.extend(["CoreFoundation", "IOKit"])


