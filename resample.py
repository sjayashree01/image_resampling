'''
Resample one of the images using a sum aggregator to 500m resolution.

Note: ROI, Raster and Aggregator are specified as inputs in the master config.yaml file

Reference:
https://gdal.org/
'''

import sys
import yaml
from osgeo import gdal
import matplotlib.pyplot as plt

def main():
    # load configuration parameters from file
    cfg = None
    try:
        with open("../config.yaml", "r") as ymlfile:
            cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)
    except Exception as e:
        print('Configuration file not found: %s',e)
        sys.exit()

    #resample input raster to specifications in the config.yaml file
    resample(cfg)

def resample(cfg):
    # Assign input vector and raster from config.yaml
    input_raster = cfg["input_raster"]
    output_raster = cfg["output_raster"]
    resample_algorithm = cfg["resample_algo"]
    xRes = cfg["xResolution"]
    yRes = cfg["yResolution"]

    #open input raster
    ds = gdal.Open(input_raster)

    # resample
    dsRes = gdal.Warp(output_raster, ds, xRes = xRes, yRes = yRes, resampleAlg = resample_algorithm)

    # visualize (optional)
    array = dsRes.GetRasterBand(1).ReadAsArray()
    plt.figure()
    plt.imshow(array)
    plt.colorbar()
    plt.show()

    # release gdal datasets
    ds = dsRes = None

if __name__ == '__main__':
    main()