#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os


class LibltcConan(ConanFile):
	name = "libltc"
	version = "1.3.0"
	url = "https://github.com/impsnldavid/conan-libltc"
	description = "Linear/longitudinal time code (LTC) library"
	license = "LGPL-3.0"

	exports = ["LICENSE.md"]

	exports_sources = ["CMakeLists.txt"]
	generators = "cmake"

	settings = "os", "arch", "compiler", "build_type"
	options = {"shared": [True, False]}
	default_options = "shared=False"

	source_subfolder = "source_subfolder"
	build_subfolder = "build_subfolder"

	def source(self):
		source_url = "https://github.com/impsnldavid/libltc"
		tools.get("{0}/archive/v{1}.tar.gz".format(source_url, self.version))
		extracted_dir = self.name + "-" + self.version
		os.rename(extracted_dir, self.source_subfolder)

	def build(self):
		cmake = CMake(self)
		cmake.definitions["LIBLTC_USE_STATIC_MSVC_RUNTIME"] = self.settings.compiler == "Visual Studio" and self.settings.compiler.runtime == "MT"
		cmake.configure(build_folder=self.build_subfolder)
		cmake.build()

	def package(self):
		include_folder = os.path.join(self.source_subfolder, "src")
		self.copy(pattern="LICENSE", dst="license", src=self.source_subfolder)
		self.copy(pattern="*.h", dst="include", src=include_folder)
		self.copy(pattern="*.dll", dst="bin", keep_path=False)
		self.copy(pattern="*.lib", dst="lib", keep_path=False)
		self.copy(pattern="*.a", dst="lib", keep_path=False)
		self.copy(pattern="*.so*", dst="lib", keep_path=False)
		self.copy(pattern="*.dylib", dst="lib", keep_path=False)


	def package_info(self):
		self.cpp_info.libs = tools.collect_libs(self)
