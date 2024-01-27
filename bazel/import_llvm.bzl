"""Provides the repository macro to import LLVM."""

def import_llvm(name):
    """Imports LLVM."""
    native.new_local_repository(
        name = name,
        build_file_content = "# empty",
        path = "/home/j2kun/fhe/llvm-project",
    )

# To try with an upstream commit, use the code below
#
# load(
#     "@bazel_tools//tools/build_defs/repo:git.bzl",
#     "new_git_repository",
# )
#
# def import_llvm(name):
#     """Imports LLVM."""
#     LLVM_COMMIT = "659a217b91a93869b6399fb85e24722a524c9d95"
#
#     new_git_repository(
#         name = name,
#         build_file_content = "# empty",
#         commit = LLVM_COMMIT,
#         init_submodules = False,
#         remote = "https://github.com/llvm/llvm-project.git",
#     )
