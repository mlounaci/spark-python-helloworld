# -*- coding: utf-8 -*-
"""
Created on Mon Jun 06 11:20:01 2016

@author: t817682
"""

#  Imports & Definitions
from afklortools.spark.submmiter import BaseDriver
from helloworld.wordcount.reduce import Reduce


class HelloWorld(BaseDriver):
    reduce = None

    def __init__(self):
        BaseDriver.__init__(self)
        self.reduce = Reduce()
        self.logger.info("Initializing the "
                         "hello world with "
                         "arguments :"
                         + self.print_args())

    def main(self):
        self.logger.info("Starting the "
                         "Word count process")
        result = self.reduce.rdd_reduce()
        self.logger.info("Checkout the Word "
                         "count Result " + str(result))


if __name__ == '__main__':
    HelloWorld().main()
