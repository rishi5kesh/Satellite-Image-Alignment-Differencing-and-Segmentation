# exampleM9.py
# IN snake.png
# OUT snake_contrast.png

## TITLE #######################################################################
# Contrast enhancement using top hat operators

## DESCRIPTION #################################################################
# This example presents a contrast enhancement technique based on the
# black top hat and white top hat operators.

## SCRIPT ######################################################################
# Importing mamba
import mamba

def contrastEnhancer(imIn, imOut, n=1, se=mamba.DEFAULT_SE):
    """
    Increase the contrast of image 'imIn' and put the result in
    image 'imOut'. Parameter 'n' will control the size and 'se' the
    structuring element used by the top hat operators.
    """

    imWrk = mamba.imageMb(imIn)
    mamba.whiteTopHat(imIn, imWrk, n, se=se)
    mamba.add(imIn, imWrk, imOut)
    mamba.blackTopHat(imIn, imWrk, n, se=se)
    mamba.sub(imOut, imWrk, imOut) 
 
def contrast():
    im = mamba.imageMb("before.jpg")
    imContrast = mamba.imageMb(im)
    contrastEnhancer(im, imContrast, 10)
    imContrast.save("contrast_A.jpg")

    im = mamba.imageMb("after.jpg")
    imContrast = mamba.imageMb(im)
    contrastEnhancer(im, imContrast, 10)
    imContrast.save("contrast_B.jpg")
