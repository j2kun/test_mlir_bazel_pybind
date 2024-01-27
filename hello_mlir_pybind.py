"""Hello world example for MLIR python bindings."""
import numpy as np

import mlir.extras.types as T
from mlir.extras.ast.canonicalize import canonicalize
from mlir.extras.context import mlir_mod_ctx
from mlir.extras.dialects.ext.arith import constant
from mlir.extras.dialects.ext.func import func
from mlir.extras.dialects.ext.scf import canonicalizer as scf, range_ as range
from mlir.extras.runtime.passes import Pipeline, run_pipeline
from mlir.extras.runtime.refbackend import LLVMJITBackend

ctx_man = mlir_mod_ctx()
ctx = ctx_man.__enter__()
backend = LLVMJITBackend()

K = 10
memref_i64 = T.memref(K, K, T.i64())

@func(emit=True)
@canonicalize(using=scf)
def memfoo(A: memref_i64, B: memref_i64, C: memref_i64):
    one = constant(1)
    two = constant(2)
    if one > two:
        C[0, 0] = constant(3, T.i64())
    else:
        for i in range(0, K):
            for j in range(0, K):
                C[i, j] = A[i, j] * B[i, j]

run_pipeline(ctx.module, Pipeline().cse())
print(ctx.module)

module = backend.compile(
    ctx.module,
    kernel_name=memfoo.__name__,
    pipeline=Pipeline().bufferize().lower_to_llvm(),
)
print(module)

A = np.random.randint(0, 10, (K, K)).astype(np.int64)
B = np.random.randint(0, 10, (K, K)).astype(np.int64)
C = np.zeros((K, K), dtype=np.int64)
backend.load(module).memfoo(A, B, C)

print(C)
assert np.array_equal(A * B, C)

ctx_man.__exit__(None, None, None);
