# json2cmake

`json2cmake` converts [JSON compilation database][] files into [CMake][] files.
The resulting `CMakeLists.txt` file can then be used to recompile the same object files with less overhead via [Ninja][], used as an IDE project file for [CLion][], or for integration into a larger CMake project.

The output files only include [object library][] definitions, as a `compile_commands.json` file typically doesn't contain any linker commands.

[JSON compilation database]: http://clang.llvm.org/docs/JSONCompilationDatabase.html
[CMake]: https://cmake.org/
[Ninja]: https://ninja-build.org/
[CLion]: https://www.jetbrains.com/clion/
[object library]: https://cmake.org/Wiki/CMake/Tutorials/Object_Library
