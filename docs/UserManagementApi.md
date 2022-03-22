# drs_api.UserManagementApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_user_users_username_delete**](UserManagementApi.md#delete_user_users_username_delete) | **DELETE** /users/{username} | Delete a user
[**delete_user_users_username_get**](UserManagementApi.md#delete_user_users_username_get) | **GET** /users/{username} | Get user info
[**post_user_users_post**](UserManagementApi.md#post_user_users_post) | **POST** /users | Create a new user
[**put_user_users_username_put**](UserManagementApi.md#put_user_users_username_put) | **PUT** /users/{username} | Update a user

# **delete_user_users_username_delete**
> object delete_user_users_username_delete(username)

Delete a user

Delete an existing user

### Example
```python
from __future__ import print_function
import time
import drs_api
from drs_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2PasswordBearer
configuration = drs_api.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = drs_api.UserManagementApi(drs_api.ApiClient(configuration))
username = 'username_example' # str | The username of the user that needs to be deleted

try:
    # Delete a user
    api_response = api_instance.delete_user_users_username_delete(username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserManagementApi->delete_user_users_username_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username of the user that needs to be deleted | 

### Return type

**object**

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_users_username_get**
> object delete_user_users_username_get(username)

Get user info

Get an existing user

### Example
```python
from __future__ import print_function
import time
import drs_api
from drs_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2PasswordBearer
configuration = drs_api.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = drs_api.UserManagementApi(drs_api.ApiClient(configuration))
username = 'username_example' # str | The username of the user that needs to be fetched

try:
    # Get user info
    api_response = api_instance.delete_user_users_username_get(username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserManagementApi->delete_user_users_username_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username of the user that needs to be fetched | 

### Return type

**object**

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_user_users_post**
> object post_user_users_post(body)

Create a new user

Create a new user

### Example
```python
from __future__ import print_function
import time
import drs_api
from drs_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2PasswordBearer
configuration = drs_api.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = drs_api.UserManagementApi(drs_api.ApiClient(configuration))
body = drs_api.UserInputModel() # UserInputModel | 

try:
    # Create a new user
    api_response = api_instance.post_user_users_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserManagementApi->post_user_users_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserInputModel**](UserInputModel.md)|  | 

### Return type

**object**

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_user_users_username_put**
> object put_user_users_username_put(body, username)

Update a user

Update an existing user

### Example
```python
from __future__ import print_function
import time
import drs_api
from drs_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2PasswordBearer
configuration = drs_api.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = drs_api.UserManagementApi(drs_api.ApiClient(configuration))
body = drs_api.UserTemplate() # UserTemplate | 
username = 'username_example' # str | 

try:
    # Update a user
    api_response = api_instance.put_user_users_username_put(body, username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserManagementApi->put_user_users_username_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserTemplate**](UserTemplate.md)|  | 
 **username** | **str**|  | 

### Return type

**object**

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

