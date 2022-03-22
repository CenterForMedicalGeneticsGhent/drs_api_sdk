# coding: utf-8

"""
    Data Repository Service

     GET request:  - Fetch a DrsObject from the database by sending a unique ID through the request - Fetch an access url to the data which the object refers to - Fetch DrsObjects by doing a search on the aliases  POST request:  - Create a non-existing DrsObject in the database by giving an identifier  DELETE request:  - Delete a DrsObject from the database by unique identifier  PUT request:  - Update an existing DrsObject by unique identifier and the changes in the body   # noqa: E501

    OpenAPI spec version: 1.2.0
    Contact: ict@cmgg.be
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import drs_api
from drs_api.models.error import Error  # noqa: E501
from drs_api.rest import ApiException


class TestError(unittest.TestCase):
    """Error unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testError(self):
        """Test Error"""
        # FIXME: construct object with mandatory attributes with example values
        # model = drs_api.models.error.Error()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
