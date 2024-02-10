"""Provides the repository macro to import LLVM."""

def import_llvm(name):
    """Imports LLVM."""
    native.new_local_repository(
        name = name,
        build_file_content = "# empty",
        path = "/home/j2kun/fhe/llvm-project",
    )

# load(
#     "@bazel_tools//tools/build_defs/repo:git.bzl",
#     "new_git_repository",
# )
#
# def import_llvm(name):
#     """Imports LLVM."""
#     LLVM_COMMIT = "5585ddd90b08ecc287e1fb7f765056dc13ccbfe1"
#
#     new_git_repository(
#         name = name,
#         build_file_content = "# empty",
#         commit = LLVM_COMMIT,
#         init_submodules = False,
#         remote = "https://github.com/llvm/llvm-project.git",
#     )
