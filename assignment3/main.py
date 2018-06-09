import dct
import util

# Original
name = "lena256.jpg"
img = util.read_image(name)

# DCT
dct_img = dct.transform_2d(img)
util.write_image("dct_" + name, dct_img)

# IDCT
idct_img = dct.i_transform_2d(dct_img)
util.write_image("idct_" + name, idct_img)
