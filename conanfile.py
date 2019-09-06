from conans import ConanFile, CMake, tools

import os


class MsgpackConan(ConanFile):
    name = "h264bitstream"
    version = "0.2"
    license = "https://github.com/ulricheck/h264bitstream/blob/master/LICENSE"
    url = "https://github.com/ulricheck/conan-h264bitstream"
    description = "library to parse h264 bitstreams"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=True"
    generators = "cmake"

    scm = {
        "type": "git",
        "subfolder": "sources",
        "url": "https://github.com/ulricheck/h264bitstream.git",
        "revision": "master"
     }

        
    def build(self):
        cmake = CMake(self)
        cmake.definitions["BUILD_SHARED_LIBS"] = self.options.shared
        cmake.configure(source_dir="sources")
        cmake.build()

    def package(self):
        self.copy("*.h", src="sources", dst="include")
        self.copy("*.so", dst="lib")
        self.copy("*.lib", dst="lib")
        self.copy("*.dll", dst="bin")

    def package_info(self):
        self.cpp_info.includedirs.append(os.path.join(self.package_folder, "include"))
        
        self.cpp_info.libs = list(set(tools.collect_libs(self))) # Remove duplicates from list
        self.output.info("LIBRARIES: %s" % ",".join(self.cpp_info.libs))


