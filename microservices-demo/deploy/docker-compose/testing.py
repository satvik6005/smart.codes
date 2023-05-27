import requests
import base64
import unittest
class testing__(unittest.TestCase):
  def test_c(self):
    print('testing user_info') 
    url=self.BASE+'customers/'+str(self.user_id)
    response=requests.get(url)
    self.assertEqual(response.status_code,200,'customer failed')
  def setUp(self):
    self.BASE='http://edge-router/'
    self.data={
    "username": "satvik6005",
	"password": "password",
	"email": "email",
	"firstName": "firstName",
	"lastName": "lastName"
    }
    self.user_id=None
 
  def test_a(self):
    url=self.BASE+'register'
    
    print('testing register')
    response=requests.post(url,json=self.data)
    self.assertEqual(response.status_code,200,'register failed')
    self.user_id=response.json()['id']
    
  def test_b(self):
    print('testing login') 
    url=self.BASE+'login'
    userpass = self.data['username'] + ':' + self.data['password']
    encoded_u = base64.b64encode(userpass.encode()).decode()
    headers = {"Authorization" : "Basic %s" % encoded_u}
    response=requests.get(url,headers=headers)
    self.assertEqual(response.status_code,200,'login failed')




unittest.main()