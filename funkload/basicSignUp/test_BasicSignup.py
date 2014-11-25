# -*- coding: iso-8859-15 -*-
"""basic_signUp FunkLoad test

$Id: $
"""
import unittest
from funkload.FunkLoadTestCase import FunkLoadTestCase
from webunit.utility import Upload
from funkload.utils import Data
#from funkload.utils import xmlrpc_get_credential

class BasicSignup(FunkLoadTestCase):
    """XXX

    This test use a configuration file BasicSignup.conf.
    """

    def setUp(self):
        """Setting up test."""
        self.logd("setUp")
        self.server_url = self.conf_get('main', 'url')
        # XXX here you can setup the credential access like this
        # credential_host = self.conf_get('credential', 'host')
        # credential_port = self.conf_getInt('credential', 'port')
        # self.login, self.password = xmlrpc_get_credential(credential_host,
        #                                                   credential_port,
        # XXX replace with a valid group
        #                                                   'members')

    def test_basic_signUp(self):
        # The description should be set in the configuration file
        server_url = self.server_url
        # begin of test ---------------------------------------------

        # /tmp/tmpgDnqJf_funkload/watch0001.request
        self.get(server_url + "/data/images/full/4061/bill-gates-wealthiest-person.jpg?w=600",
            description="Get /data/images/full/4...althiest-person.jpg")

        # end of test -----------------------------------------------

    def tearDown(self):
        """Setting up test."""
        self.logd("tearDown.\n")



if __name__ in ('main', '__main__'):
    unittest.main()
