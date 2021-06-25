#!/usr/bin/env python

import argparse
import cdsapi
import datetime
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

area = "90/-180/-90/180"
times = '00/to/23/by/1'

def downsfcdat(day,ofile):
    server = cdsapi.Client()
    server.retrieve(
        'reanalysis-era5-single-levels',
        {
             'variable' : ["165","166","167","168","172","134","151","235",
                           "31","34","33","141","139","170","183","236","39",
                           "40","41","42"],
            'product_type': "reanalysis",
            'year'        : day.strftime("%Y")+"",
            'month'       : day.strftime("%m")+"",
            'day'         : day.strftime("%d")+"",
            'area'        : area,
            'time'        : times,
            'format'      : 'grib'
        },
        ofile)
    return("Done")

def downpldat(day,ofile):
    server = cdsapi.Client()
    server.retrieve(
        'reanalysis-era5-pressure-levels',
        {
            'variable' : ["129","130","131","132","157"],
            'levelist' : "all",
            'product_type': "reanalysis",
            'year'        : day.strftime("%Y")+"",
            'month'       : day.strftime("%m")+"",
            'day'         : day.strftime("%d")+"",
            'area'        : area,
            'time'     : times,
            'format'   : "grib",
        },
        ofile)
    return("Done")

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('--dates',
                        type=lambda s: datetime.datetime.strptime(s, '%Y-%m-%d'),
                        nargs='+')
    args = parser.parse_args()

    for day in args.dates:
        ofile_sfc = "ERA5_sfc_" + day.strftime("%Y-%m-%d")
        ofile_pl = "ERA5_pl_" + day.strftime("%Y-%m-%d")

        downsfcdat(day, ofile_sfc)
        downpldat(day, ofile_pl)

if __name__ == '__main__':
    main()
