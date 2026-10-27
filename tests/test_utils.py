from utils import normalise_email,hash_password

def test_lowercase_email():
    assert normalise_email("DavId@example.com") == "david@example.com"
    
    
def test_remove_whitespaces():
    assert normalise_email(" david@example.com ") == "david@example.com"
    
def test_password_is_hashed():
   new_password = hash_password("password123")
   
   assert new_password != "passsword123"
    