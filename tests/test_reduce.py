from afklortools.spark.testing import BaseTestSparkContext
from helloworld.driver import Reduce


class TestReduce(BaseTestSparkContext):

    def test_reduce(self):
        r = Reduce()
        output = r.rdd_reduce()
        self.logger.info("My test Case logger")
        # since it's unit test let's make an assertion
        self.assertEqual(output[0][1], 2)
