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

    def test_critical(self): 
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

        self.get(server_url + "/cabins/new", description = "View the new cabin page")
        auth_token = extract_token(self.getBody(), 'name="authenticity_token" type="hidden" value="', '"')

        cabin_name = Lipsum().getWord()
        cabin_Adr = Lipsum().getSentence()
        cabin_desc = Lipsum().getSentence() 

        self.post(self.server_url + "/cabins",
            params=[["cabin[navn]", cabin_name],
            ["cabin[address]", cabin_Adr],
            ["cabin[descritpion]", cabin_desc],
            ["authenticity_token", auth_token],
            ["commit", "Create Cabin"]],
            description = "Create new cabin")
        last_url = self.getLastUrl()
        created_cabin_id = last_url.split("/")[-1]

        self.get(server_url + "/cabins", description= "View the all cabin page")
        self.get(server_url + "/cabins/" + created_cabin_id, description="View cabin page")
    
            
        self.get(server_url + "/posts/new?cabin_id=" + str(1), description="View the new post page pr cabin")
        auth_token = extract_token(self.getBody(), 'name="authenticity_token" type="hidden" value="', '"')

        cabin_post_title = Lipsum().getSentence()
        cabin_post_mess = Lipsum().getSentence()

        self.post(self.server_url + "/posts",
            params=[["post[title]", cabin_post_title],
            ["post[message]", cabin_post_mess],
            ["post[cabin_id]", str(1)],
            ["authenticity_token", auth_token],
            ["commit", "Create Post"]],
            description="Create comment on cabin")

        self.get(server_url + "/cabins/" + str(1), description="View cabin page")

    def test_readOnly(self): 

        server_url = self.server_url
        
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

        self.get(server_url + "/cabins", description="view cabins page")
        self.get(server_url + "/cabins/1", description="view cabin 1 page")

    def test_writeOnly(self):
        server_url = self.server_url
        
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

        self.get(server_url + "/cabins/new", description = "View the new cabin page")
        auth_token = extract_token(self.getBody(), 'name="authenticity_token" type="hidden" value="', '"')

        cabin_name = Lipsum().getWord()
        cabin_Adr = Lipsum().getSentence()
        cabin_desc = Lipsum().getSentence() 

        self.post(self.server_url + "/cabins",
            params=[["cabin[navn]", cabin_name],
            ["cabin[address]", cabin_Adr],
            ["cabin[descritpion]", cabin_desc],
            ["authenticity_token", auth_token],
            ["commit", "Create Cabin"]],
            description = "Create new cabin")
        last_url = self.getLastUrl()
        created_cabin_id = last_url.split("/")[-1]
            
        self.get(server_url + "/posts/new?cabin_id=" + str(1), description="View the new post page pr cabin")
        auth_token = extract_token(self.getBody(), 'name="authenticity_token" type="hidden" value="', '"')

        cabin_post_title = Lipsum().getSentence()
        cabin_post_mess = Lipsum().getSentence()

        self.post(self.server_url + "/posts",
            params=[["post[title]", cabin_post_title],
            ["post[message]", cabin_post_mess],
            ["post[cabin_id]", str(1)],
            ["authenticity_token", auth_token],
            ["commit", "Create Post"]],
            description="Create comment on cabin")

    def test_creatUser(self):
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

    def test_createCabin(self):
        server_url = self.server_url

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

        self.get(server_url + "/cabins", description= "View the all-cabin page")
        auth_token = extract_token(self.getBody(), 'name="authenticity_token" type="hidden" value="', '"')

        self.get(server_url + "/cabins/new", description = "View the new cabin page")
        auth_token = extract_token(self.getBody(), 'name="authenticity_token" type="hidden" value="', '"')

        cabin_name = Lipsum().getWord()
        cabin_Adr = Lipsum().getSentence()
        cabin_desc = Lipsum().getSentence() 

        self.post(self.server_url + "/cabins",
            params=[["cabin[navn]", cabin_name],
            ["cabin[address]", cabin_Adr],
            ["cabin[descritpion]", cabin_desc],
            ["authenticity_token", auth_token],
            ["commit", "Create Cabin"]],
            description = "Create new cabin")

    def test_createPostOnCabin(self):
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

        self.get(server_url + "/cabins/new", description = "View the new cabin page")
        auth_token = extract_token(self.getBody(), 'name="authenticity_token" type="hidden" value="', '"')

        cabin_name = Lipsum().getWord()
        cabin_Adr = Lipsum().getSentence()
        cabin_desc = Lipsum().getSentence() 

        self.post(self.server_url + "/cabins",
            params=[["cabin[navn]", cabin_name],
            ["cabin[address]", cabin_Adr],
            ["cabin[descritpion]", cabin_desc],
            ["authenticity_token", auth_token],
            ["commit", "Create Cabin"]],
            description = "Create new cabin")
        last_url = self.getLastUrl()
        created_cabin_id = last_url.split("/")[-1]

        self.get(server_url + "/cabins/" + "1", description="View cabin page")
        auth_token = extract_token(self.getBody(), 'name="authenticity_token" type="hidden" value="', '"')

        self.get(server_url + "/posts/new?cabin_id=" + created_cabin_id, description="View the new post page pr cabin")
        auth_token = extract_token(self.getBody(), 'name="authenticity_token" type="hidden" value="', '"')

        cabin_post_titile = Lipsum().getWord()
        cabin_post_mess = Lipsum().getSentence()

        for i in range (1, int(created_cabin_id)):
            self.post(self.server_url + "/posts",
                params=[["post[titile]", cabin_post_titile],
                ["post[message]", cabin_post_mess],
                ["post[cabin_id]", "1"],
                ["authenticity_token", auth_token],
                ["commit", "Create Post"]],
                description="Create comment on cabin")

    def test_createToDoListOnCabin(self): 
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

        self.get(server_url + "/cabins/new", description = "View the new cabin page")
        auth_token = extract_token(self.getBody(), 'name="authenticity_token" type="hidden" value="', '"')

        cabin_name = Lipsum().getWord()
        cabin_Adr = Lipsum().getSentence()
        cabin_desc = Lipsum().getSentence() 

        self.post(self.server_url + "/cabins",
            params=[["cabin[navn]", cabin_name],
            ["cabin[address]", cabin_Adr],
            ["cabin[descritpion]", cabin_desc],
            ["authenticity_token", auth_token],
            ["commit", "Create Cabin"]],
            description = "Create new cabin")
        last_url = self.getLastUrl()
        created_cabin_id = last_url.split("/")[-1]

        self.get(server_url + "/todolists?cabin_id=" + created_cabin_id, description="View the todolist page")
        self.get(server_url + "/todolists/new?cabin_id=" + created_cabin_id, description="View upload new todolist page")
        auth_token = extract_token(self.getBody(), 'name="authenticity_token" type="hidden" value="', '"')
        todolist_title = Lipsum().getWord()

        self.post(self.server_url + "/todolists", 
            params=[["todolist[name]", todolist_title],
            ["todolist[cabin_id]", created_cabin_id],
            ["authenticity_token", auth_token],
            ["commit", "Create Todolist"]],
            description="Create new Todolist")

        self.get(server_url + "/todolists?cabin_id=" + created_cabin_id, description="Vies to the todlist page")

    def test_createPhotoalbumOnCabin(self): #not finished
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

        self.get(server_url + "/cabins/new", description = "View the new cabin page")
        auth_token = extract_token(self.getBody(), 'name="authenticity_token" type="hidden" value="', '"')

        cabin_name = Lipsum().getWord()
        cabin_Adr = Lipsum().getSentence()
        cabin_desc = Lipsum().getSentence() 

        self.post(self.server_url + "/cabins",
            params=[["cabin[navn]", cabin_name],
            ["cabin[address]", cabin_Adr],
            ["cabin[descritpion]", cabin_desc],
            ["authenticity_token", auth_token],
            ["commit", "Create Cabin"]],
            description = "Create new cabin")
        last_url = self.getLastUrl()
        created_cabin_id = last_url.split("/")[-1]

        self.get(server_url + "/photoalbums?cabin_id=" + created_cabin_id, description="View the photoalbumpage page")
        self.get(server_url + "/photoalbums/new?cabin_id=" + created_cabin_id, description="View upload new photo page")
        auth_token = extract_token(self.getBody(), 'name="authenticity_token" type="hidden" value="', '"')
        photoalbum_title = Lipsum().getWord()
        photoalbum_desc = Lipsum().getSentence() 
        
        self.post(self.server_url + "/photoalbums", 
            params=[["photoalbum[name]", photoalbum_title],
            ["photoalbum[description]", photoalbum_desc],
            ["photoalbum[cabin_id]", created_cabin_id],
            ["photoalbum[picture]", ""], # fix this 
            ["authenticity_token", auth_token],
            ["commit", "Create Photoalbum"]],
            description="Create a new picture in photoalbum")

    def tearDown(self):
        """Setting up test."""
        self.logd("tearDown.\n")



if __name__ in ('main', '__main__'):
    unittest.main()
