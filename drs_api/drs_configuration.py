"""
    Data Repository Service
    OpenAPI spec version: 1.2.0
    Contact: ict@cmgg.be
"""

from jose import jwt, ExpiredSignatureError
from drs_api.configuration import Configuration
from drs_api import LoginApi, ApiClient
from drs_api.rest import ApiException

class DrsConfiguration(Configuration):
    """This class extends the auto generated Configuration class."""

    def __init__(self):
        """Constructor"""
        super().__init__()
        self.api_key_prefix = {"Authorization":"Bearer"}
        self.refresh_api_key_hook = self.refresh_api_key_hook_function.__func__


    def refresh_api_key_hook_function(self):
        """Refresh apiKey hook function

        If no api_key is set OR api_key is set but expired,
        request a new key/token using the LoginApi class
        """
        identifier = "Authorization"
        if self.api_key.get(identifier):
            token = self.api_key.get(identifier)
            try:
                _ = jwt.decode(token, None, options={'verify_signature': False})
                return
            except ExpiredSignatureError:
                pass

        login = LoginApi(ApiClient(self))
        try:
            login_response = login.login_token_post(
                username=self.username,
                password=self.password,
                grant_type="",
                scope="",
                client_id="",
                client_secret=""
                )
            assert login_response.token_type.lower() == "bearer"
            self.api_key[identifier] = login_response.access_token
        except ApiException as error:
            raise ApiException(
                status=0,
                reason="Failed to refresh apiKey"
            ) from error
