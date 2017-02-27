# -*- coding: utf-8 -*-
"""
Created on Mon Jun 06 11:20:01 2016

@author: t817682
"""
from afklortools.spark.submmiter import PexSubmitter
import configobj


def main():
    ps = PexSubmitter(package_name="helloworld")
    ps.add_file_argument('--test-app', metavar='TEST_APP', help="First customized app arg")
    ps.add_value_argument('--no-dataprocessing', help='run the model without the dataprocessing step',
                          action='store_true')
    return_value = ps.spark_submit()
    print("return Value is: " + str(return_value))


if __name__ == '__main__':
    main()
