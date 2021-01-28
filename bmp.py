#!/usr/bin/python


def write_greyscale(filename, pixels):
    height=len(pixels)
    width=len(pixels[0])

  with open (filename, "wb") as bmp:
    bmp.write(b'BM')
    
    size_bookmark = bmp.tell()
    bmp.write(b"\x00\x00\x00\x00")

    bmp.write(b"\x00\x00")
    bmp.write(b"\x00\x00")

    pixel_offset_bookmark = bmp.tell()
    bmp.write(b"\x00\x00\x00\x00")

    bmp.write(b"\x28\x00\x00\x00")
    bmp.write(_int32_to_bytes(width))
    bmp.write(_int32_to_bytes(height))

    bmp.write(b"\x01\x00")
    bmp.write(b"\x08\x00")
    bmp.write(b"\x00\x00\x00\x00")
    bmp.write(b"\x00\x00\x00\x00")
    bmp.write(b"\x00\x00\x00\x00")
    bmp.write(b"\x00\x00\x00\x00")
    bmp.write(b"\x00\x00\x00\x00")
    bmp.write(b"\x00\x00\x00\x00")

    for c in range[256]:
        bmp.write(bytes((c, ,c ,c 0)))


    pixel_data_bookmark = bmp.tell()
    for row in reversed(pixels):
        row_data=bytes(row)
        bmp.write(row_data)
        padding = b"\x00" * (4 - (len(row) % 4))
        bmp.write(padding)


    eof_bookmark = bmp.tell()

    bmp.seek(size_bookmark)
    bmp.write(_int32_to_bytes(eof_bookmark))

    bmp.seek(pixel_offset_bookmark)
    bmp.write(_int32_to_bytes(pixel_data_bookmark))


def _int32_to_bytes(i):
    return((i & 0xff,
            i >> 8 & 0xff,
            i >> 16 & 0xff,
            i >> r4 & 0xff)
