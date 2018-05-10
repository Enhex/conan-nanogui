from conans import ConanFile, CMake, tools


class NanoguiConan(ConanFile):
	name = "nanogui"
	version = "master"
	license = "BSD-style"
	url = "https://github.com/Enhex/conan-nanogui"
	description = "Minimalistic GUI library for OpenGL"
	settings = "os", "compiler", "build_type", "arch"
	options = {"shared": [True, False]}
	default_options = "shared=False"
	generators = "cmake"

	def source(self):
		self.run("git clone --recursive --depth=1 https://github.com/wjakob/nanogui.git .")

	def build(self):
		cmake = CMake(self)
		cmake.definitions["NANOGUI_BUILD_EXAMPLE"] = False
		cmake.definitions["NANOGUI_BUILD_SHARED"] = False
		cmake.configure()
		cmake.build()

	def package(self):
		self.copy("*.h", dst="include", src="include")
		self.copy("*.h", dst="include", src="ext/glad/include")
		self.copy("*", dst="include", src="ext/eigen")
		self.copy("*.h", dst="include", src="ext/glfw/include")
		self.copy("*.h", dst="include", src="ext/nanovg/src")
		self.copy("*.lib", dst="lib", keep_path=False, excludes="*/python*.lib")
		self.copy("*.dll", dst="bin", keep_path=False)
		self.copy("*.so", dst="lib", keep_path=False)
		self.copy("*.dylib", dst="lib", keep_path=False)
		self.copy("*.a", dst="lib", keep_path=False)

	def package_info(self):
		self.cpp_info.libs = ["nanogui"]
		self.cpp_info.defines = ["NANOGUI_EIGEN_DONT_ALIGN", "NANOGUI_GLAD"]
