load("@pybind11_bazel//:build_defs.bzl", "pybind_extension")
load("@llvm-project//mlir/python:symlink_inputs.bzl", "symlink_inputs")


package(
    default_visibility = [
        "//visibility:public",
    ],
)

pybind_extension(
    name = "_mlir",
    srcs = [
        "@llvm-project//mlir:lib/Bindings/Python/MainModule.cpp",
    ],
    deps = [
        "@llvm-project//llvm:Support",
        "@llvm-project//mlir:MLIRBindingsPythonCore",
        "@llvm-project//mlir:MLIRBindingsPythonHeaders",
        "@llvm-project//mlir:Support",
    ],
)

symlink_inputs(
    name = "_mlir_libs",
    rule = py_library,
    symlinked_inputs = {"srcs": {
        ".": [
            "@llvm-project//mlir/python:MlirLibsPyFiles",
        ],
    }},
    deps = [
        ":_mlir.so",
    ],
)


