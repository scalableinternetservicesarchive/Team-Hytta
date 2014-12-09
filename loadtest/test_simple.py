# -*- coding: iso-8859-15 -*-
"""test_simple FunkLoad test

$Id: $
"""
import unittest
from funkload.FunkLoadTestCase import FunkLoadTestCase
from webunit.utility import Upload
from funkload.utils import Data
from funkload.Lipsum import Lipsum
from funkload.utils import extract_token


class Simple(FunkLoadTestCase):
    """
    This test use a configuration file simple.conf.
    """

    def setUp(self):
        """Setting up test."""
        self.logd("setUp")
        self.server_url = self.conf_get('main', 'url') 

    def test_simple(self):
        server_url = self.server_url
        self.get(server_url, description="View the root URL")
        self.get(server_url + "/users/sign_up", description="View the sign in page")

        auth_token = extract_token(self.getBody(), 'name="authenticity_token" type="hidden" value="', '"')
        email = Lipsum().getUniqWord() + "@" + Lipsum().getWord() + ".com"
        name = Lipsum().getUniqWord()

        self.post(server_url + "/users",
            params=[["user[first_name]", name],
            ["user[last_name]", name],
            ["user[email]", email],
            ["user[password]", "alphabet"],
            ["user[password_confirmation]", "alphabet"],
            ["authenticity_token", auth_token],
            ["commit", "Sign up"]],
            description = "Create New User")

    def tearDown(self):
        """Setting up test."""
        self.logd("tearDown.\n")



if __name__ in ('main', '__main__'):
    unittest.main()
