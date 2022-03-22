# drs_api.LoginApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**login_token_post**](LoginApi.md#login_token_post) | **POST** /token | Login

# **login_token_post**
> Token login_token_post(grant_type, username, password, scope, client_id, client_secret)

Login

### Example
```python
from __future__ import print_function
import time
import drs_api
from drs_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = drs_api.LoginApi()
grant_type = 'grant_type_example' # str | 
username = 'username_example' # str | 
password = 'password_example' # str | 
scope = 'scope_example' # str | 
client_id = 'client_id_example' # str | 
client_secret = 'client_secret_example' # str | 

try:
    # Login
    api_response = api_instance.login_token_post(grant_type, username, password, scope, client_id, client_secret)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoginApi->login_token_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grant_type** | **str**|  | 
 **username** | **str**|  | 
 **password** | **str**|  | 
 **scope** | **str**|  | 
 **client_id** | **str**|  | 
 **client_secret** | **str**|  | 

### Return type

[**Token**](Token.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

