# -*- coding: utf-8 -*-
"""
Created on Wed 20 09:40:01 2016

@author: t817682
"""

#  Imports & Definitions
from afklortools.spark.context import BaseHiveContext


class Reduce(BaseHiveContext):

    def rdd_reduce(self):
        # def test_pymongo(x):
        #     import pymongo
        #     return (x[1], 1)
        # start by creating a mockup dataset
        nb_airport = self.hc.sql("select * from crm_data.airport").count()

        l = [(1, 'hello'), (2, 'world'), (3, 'world')]
        self.logger.info("Inside the reduce !!!!!!!!!!!!!!!!!!!  :" + str(self.sc.master))
        self.logger.info("Number of airports !!!!!!!!!!!!!!!!!!!  :" + str(nb_airport))
        # and create a RDD out of it
        hellordd = self.sc.parallelize(l)
        return hellordd.map(lambda x: (x[1], 1)).reduceByKey(lambda a, b: a + b).collect()