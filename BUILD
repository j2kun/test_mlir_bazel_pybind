load("@pybind11_bazel//:build_defs.bzl", "pybind_extension")
load("@llvm-project//mlir/python:symlink_inputs.bzl", "symlink_inputs")

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

py_library(
    name = "mlir",
    deps = [
      ":_mlir_libs",
    ],
)

symlink_inputs(
    name = "ir",
    rule = py_library,
    symlinked_inputs = {"srcs": {
        ".": ["@llvm-project//mlir/python:IRPyFiles"],
    }},
    deps = [
        ":mlir",
    ],
)

symlink_inputs(
    name = "core",
    rule = py_library,
    symlinked_inputs = {"srcs": {
        "dialects": ["@llvm-project//mlir/python:DialectCorePyFiles"],
    }},
)

symlink_inputs(
    name = "extras",
    rule = py_library,
    symlinked_inputs = {"srcs": {
        "extras": ["@llvm-project//mlir/python:ExtrasPyFiles"],
    }},
    deps = [
        ":ir",
        ":mlir",
    ],
)

symlink_inputs(
    name = "func_dialect",
    rule = py_library,
    symlinked_inputs = {"srcs": {
        "dialects": ["@llvm-project//mlir/python:FuncPyFiles"],
    }},
    deps = [
        ":core",
        ":ir",
        ":mlir",
    ],
)

symlink_inputs(
    name = "vector_dialect",
    rule = py_library,
    symlinked_inputs = {"srcs": {
        "dialects": ["@llvm-project//mlir/python:VectorOpsPyFiles"],
    }},
    deps = [
        ":core",
        ":ir",
        ":mlir",
    ],
)

symlink_inputs(
    name = "math_dialect",
    rule = py_library,
    symlinked_inputs = {"srcs": {
        "dialects": ["@llvm-project//mlir/python:MathOpsPyFiles"],
    }},
    deps = [
        ":core",
        ":ir",
        ":mlir",
    ],
)

symlink_inputs(
    name = "arithmetic_dialect",
    rule = py_library,
    symlinked_inputs = {"srcs": {
        "dialects": ["@llvm-project//mlir/python:ArithOpsPyFiles"],
    }},
    deps = [
        ":core",
        ":ir",
        ":mlir",
    ],
)

symlink_inputs(
    name = "memref_dialect",
    rule = py_library,
    symlinked_inputs = {"srcs": {
        "dialects": ["@llvm-project//mlir/python:MemRefOpsPyFiles"],
    }},
    deps = [
        ":core",
        ":ir",
        ":mlir",
    ],
)

symlink_inputs(
    name = "scf_dialect",
    rule = py_library,
    symlinked_inputs = {"srcs": {
        "dialects": ["@llvm-project//mlir/python:SCFPyFiles"],
    }},
    deps = [
        ":core",
        ":ir",
        ":mlir",
    ],
)

symlink_inputs(
    name = "builtin_dialect",
    rule = py_library,
    symlinked_inputs = {"srcs": {
        "dialects": ["@llvm-project//mlir/python:BuiltinOpsPyFiles"],
    }},
    deps = [
        ":core",
        ":extras",
        ":ir",
        ":mlir",
    ],
)

symlink_inputs(
    name = "pass_manager",
    rule = py_library,
    symlinked_inputs = {"srcs": {
        ".": ["@llvm-project//mlir/python:PassManagerPyFiles"],
    }},
    deps = [
        ":mlir",
    ],
)

py_library(
    name = "mlir_python_bindings",
    data = [
        ":_mlir.so",
    ],
    srcs_version = "PY3",
    deps = [
        ":arithmetic_dialect",
        ":builtin_dialect",
        ":core",
        ":extras",
        ":func_dialect",
        ":ir",
        ":math_dialect",
        ":memref_dialect",
        ":mlir",
        ":pass_manager",
        ":scf_dialect",
        ":vector_dialect",
    ],
)

py_binary(
    name = "hello_mlir",
    srcs = [
        "hello_mlir.py",
    ],
    python_version = "PY3",
    srcs_version = "PY3",
    deps = [
        ":mlir_python_bindings",
    ],
)
