# -*- coding: iso-8859-15 -*-
"""Simple FunkLoad test

$Id$
"""
import unittest
from random import random
from funkload.FunkLoadTestCase import FunkLoadTestCase
from funkload.utils import extract_token
from funkload.Lipsum import Lipsum


class Critical(FunkLoadTestCase):
    """This test use a configuration file Simple.conf."""

    def setUp(self):
      """Setting up test."""
      self.server_url = self.conf_get('main', 'url')

    def test_critical_path(self):
	server_url = self.server_url
	self.get(server_url, description='Get root URL')
	self.get(server_url + "/users/sign_up", description="View the user signup page")

	auth_token = extract_token(self.getBody(), 'name="authenticity_token" type="hidden" value="', '"')
	email = Lipsum().getUniqWord() + "@" + Lipsum().getWord() + ".com"

	self.post(self.server_url + "/users",
	    params=[['user[email]', email],
	      ['user[password]', 'alphabet'],
	      ['user[password_confirmation]', 'alphabet'],
	      ['authenticity_token', auth_token],
	      ['commit', 'Sign up']],
	    description="Create New User")

	self.get(server_url + "/cabins/new", description="View the new cabins page")
	auth_token = extract_token(self.getBody(), 'name="authenticity_token" type="hidden" value="', '"')

	cabin_name = Lipsum().getSentence()
	self.post(self.server_url + "/cabins",
	    params=[['cabin[name]', cabin_name],
	      ['authenticity_token', auth_token],
	      ['commit', 'Create Cabin']],
	    description="Create New Cabin")
	last_url = self.getLastUrl()

	created_cabin_id = last_url.split('/')[-1]
	self.get(server_url + "/cabins/"+created_cabiny_id, description="View the created cabin page")

	self.get(server_url + "/post/new", description="View the new post page")
	auth_token = extract_token(self.getBody(), 'name="authenticity_token" type="hidden" value="', '"')

	post_title = Lipsum().getSentence()
	#post_url = "http://www."+Lipsum().getWord() + Lipsum().getUniqWord() + ".com/"
	self.post(self.server_url + "/posts",
	    params=[['submission[title]', post_title],
	      ['post[cabin_id]', created_cabin_id],
	      ['authenticity_token', auth_token],
	      ['commit', 'Create Post']],
	    description="Create New Post")
	last_url = self.getLastUrl()
	created_post_id = last_url.split('/')[-1]

	self.get(server_url + "/comments/new", description="View the new comments page")
	auth_token = extract_token(self.getBody(), 'name="authenticity_token" type="hidden" value="', '"')

	comment_message = Lipsum().getSentence()
	comment_parent = ''
	post_id = created_post_id
	self.post(self.server_url + "/comments",
	    params=[['comment[message]', comment_message],
	      ['comment[post_id]', post_id],
	      ['comment[parent_id]', comment_parent],
	      ['authenticity_token', auth_token],
	      ['commit', 'Create Comment']
	      ],
	    description="Create New Comment")


    def test_critical_path_readonly(self):
	server_url = self.server_url
	self.get(server_url, description='View root URL')
	self.get(server_url + "/users/sign_up", description="View the user signup page")
	self.get(server_url + "/cabins/", description="View the cabins page")
	self.get(server_url + "/comments/", description="View the new comments page")




if __name__ in ('main', '__main__'):
  unittest.main()
