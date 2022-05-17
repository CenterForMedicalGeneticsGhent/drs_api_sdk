from drs_api.configuration import Configuration
from drs_api import LoginApi, ApiClient
from drs_api.rest import ApiException
from jose import jwt, ExpiredSignatureError
# from drs_api import rest

class DrsConfiguration(Configuration):

    def __init__(self):
        super().__init__()
        self.api_key_prefix = {"Authorization":"Bearer"}
        self.refresh_api_key_hook = self.refresh_api_key_hook_function()

    def refresh_api_key_hook_function(self):
        auth_setting = self.auth_settings().get("OAuth2PasswordBearer")
        identifier = auth_setting['key']

        if self.api_key.get(identifier):
            token = self.api_key.get(identifier)
            try: 
                payload = jwt.decode(token, None, options={'verify_signature': False})
                return
            except ExpiredSignatureError:
                pass

        
        # client = rest.RESTClientObject(self)
        # client.POST(f'{self.host}/token',

        #         )
        # self.username
        # self.password
        # Renew token here

        login = LoginApi(ApiClient(self))
        try:
            login_response = login.login_token_post(username=self.username, password=self.password, grant_type="", scope="", client_id="", client_secret="")
            assert login_response.token_type.lower() == "bearer"
            self.api_key[identifier] = login_response.access_token
        except ApiException as e:
            print("Exception when calling LoginApi->login_token_post: %s\n" % e) 
