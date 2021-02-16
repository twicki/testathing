import gt4py
from gt4py import gtscript
from gt4py.gtscript import FORWARD, Field, computation, interval


@gtscript.stencil(backend="gtx86")
def copy_stencil(
    in_storage: Field[float],
    out_storage: Field[float],
):

    with computation(FORWARD), interval(...):
        out_storage = in_storage[0, 1, 0]


def test_compile_and_run():
    shape = (1, 10, 10)
    in_storage = gt4py.storage.zeros(
        shape=shape, default_origin=(0, 0, 0), dtype=float, backend="gtx86"
    )
    in_storage.data[:, :, :] = 2
    out_storage = gt4py.storage.zeros(
        shape=shape, default_origin=(0, 0, 0), dtype=float, backend="gtx86"
    )

    # otuput printing
    print("input")
    print(in_storage)
    print("after stencil:")
    copy_stencil(
        in_storage,
        out_storage,
        origin=(0, 0, 0),
        domain=(1, 9, 10),
    )
    print("in:")
    print(in_storage)
    print("out:")
    print(out_storage)


if __name__ == "__main__":
    test_compile_and_run()
