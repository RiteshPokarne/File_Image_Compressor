import numpy
from PIL import Image



class image:

    def __init__(self,path):
        self.path = path
        
    def openImage(self,imagePath):
        imOrig = Image.open(imagePath)
        im = numpy.array(imOrig)

        aRed = im[:, :, 0]
        aGreen = im[:, :, 1]
        aBlue = im[:, :, 2]

        return [aRed, aGreen, aBlue, imOrig]



    def compressSingleChannel(self, channelDataMatrix, singularValuesLimit):
        uChannel, sChannel, vhChannel = numpy.linalg.svd(channelDataMatrix)
        aChannelCompressed = numpy.zeros((channelDataMatrix.shape[0], channelDataMatrix.shape[1]))
        k = singularValuesLimit

        leftSide = numpy.matmul(uChannel[:, 0:k], numpy.diag(sChannel)[0:k, 0:k])
        aChannelCompressedInner = numpy.matmul(leftSide, vhChannel[0:k, :])
        aChannelCompressed = aChannelCompressedInner.astype('uint8')
        return aChannelCompressed


    def compress_img(self):
        print('* Image Compression using SVD - a demo')
        aRed, aGreen, aBlue, originalImage = self.openImage(self.path)


        imageWidth = 512
        imageHeight = 512


        singularValuesLimit = 160

        aRedCompressed = self.compressSingleChannel(aRed, singularValuesLimit)
        aGreenCompressed = self.compressSingleChannel(aGreen, singularValuesLimit)
        aBlueCompressed = self.compressSingleChannel(aBlue, singularValuesLimit)

        imr = Image.fromarray(aRedCompressed, mode=None)
        img = Image.fromarray(aGreenCompressed, mode=None)
        imb = Image.fromarray(aBlueCompressed, mode=None)

        newImage = Image.merge("RGB", (imr, img, imb))

        originalImage.show()
        newImage.show()


        mr = imageHeight
        mc = imageWidth

        originalSize = mr * mc * 3
        compressedSize = singularValuesLimit * (1 + mr + mc) * 3

        print('original size:')
        print(originalSize)

        print('compressed size:')
        print(compressedSize)

        print('Ratio compressed size / original size:')
        ratio = compressedSize * 1.0 / originalSize
        print(ratio)

        print('Compressed image size is ' + str(round(ratio * 100, 2)) + '% of the original image ')
        print('DONE - Compressed the image! Over and out!')