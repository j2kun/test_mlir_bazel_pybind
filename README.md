# Repro steps

```
# update bazel/import_llvm.bzl to load any upstream commit before
# 75952873036fc9989fcf12c526d1a2deaeef596a

bazel build @llvm-project//mlir:MLIRBindingsPythonCore
```

Error:

```
no such package '@python_runtime//': The repository '@python_runtime'
could not be resolved: Repository '@python_runtime' is not defined and
referenced by '@llvm-project//mlir:MLIRBindingsPythonCore'
```

Set the local path `bazel/import_llvm.bzl` to point to a local copy of
https://github.com/llvm/llvm-project/pull/79676, and the build should succeed.
