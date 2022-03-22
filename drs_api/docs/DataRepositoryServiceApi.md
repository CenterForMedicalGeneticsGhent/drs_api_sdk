# drs_api.DataRepositoryServiceApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_object_ga4gh_drs_v1_objects_object_id_delete**](DataRepositoryServiceApi.md#delete_object_ga4gh_drs_v1_objects_object_id_delete) | **DELETE** /ga4gh/drs/v1/objects/{object_id} | Delete a DrsObject
[**get_object_alias_ga4gh_drs_v1_objects_get**](DataRepositoryServiceApi.md#get_object_alias_ga4gh_drs_v1_objects_get) | **GET** /ga4gh/drs/v1/objects | Query DrsObjects on alias
[**get_object_ga4gh_drs_v1_objects_object_id_access_access_id_get**](DataRepositoryServiceApi.md#get_object_ga4gh_drs_v1_objects_object_id_access_access_id_get) | **GET** /ga4gh/drs/v1/objects/{object_id}/access/{access_id} | Get a URL for fetching bytes
[**get_object_ga4gh_drs_v1_objects_object_id_get**](DataRepositoryServiceApi.md#get_object_ga4gh_drs_v1_objects_object_id_get) | **GET** /ga4gh/drs/v1/objects/{object_id} | Retrieve a DrsObject
[**post_object_ga4gh_drs_v1_objects_post**](DataRepositoryServiceApi.md#post_object_ga4gh_drs_v1_objects_post) | **POST** /ga4gh/drs/v1/objects | Create a new DrsObject
[**put_object_ga4gh_drs_v1_objects_object_id_put**](DataRepositoryServiceApi.md#put_object_ga4gh_drs_v1_objects_object_id_put) | **PUT** /ga4gh/drs/v1/objects/{object_id} | Update a DrsObject

# **delete_object_ga4gh_drs_v1_objects_object_id_delete**
> BasicResponse delete_object_ga4gh_drs_v1_objects_object_id_delete(object_id)

Delete a DrsObject

Delete a ```DrsObject``` index entry

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
api_instance = drs_api.DataRepositoryServiceApi(drs_api.ApiClient(configuration))
object_id = 'object_id_example' # str | 

try:
    # Delete a DrsObject
    api_response = api_instance.delete_object_ga4gh_drs_v1_objects_object_id_delete(object_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataRepositoryServiceApi->delete_object_ga4gh_drs_v1_objects_object_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**|  | 

### Return type

[**BasicResponse**](BasicResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_object_alias_ga4gh_drs_v1_objects_get**
> list[DrsObject] get_object_alias_ga4gh_drs_v1_objects_get(alias)

Query DrsObjects on alias

Returns all objects that correspond to the list of aliases passed through         the request. The query is regex compatible.

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
api_instance = drs_api.DataRepositoryServiceApi(drs_api.ApiClient(configuration))
alias = ['alias_example'] # list[str] | The alias(ses) on which to query DrsObjects (regex compatible)

try:
    # Query DrsObjects on alias
    api_response = api_instance.get_object_alias_ga4gh_drs_v1_objects_get(alias)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataRepositoryServiceApi->get_object_alias_ga4gh_drs_v1_objects_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | [**list[str]**](str.md)| The alias(ses) on which to query DrsObjects (regex compatible) | 

### Return type

[**list[DrsObject]**](DrsObject.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_object_ga4gh_drs_v1_objects_object_id_access_access_id_get**
> AccessURL get_object_ga4gh_drs_v1_objects_object_id_access_access_id_get(object_id, access_id)

Get a URL for fetching bytes

Returns a URL that can be used to fetch the bytes of a `DrsObject`.                     This method only needs to be called when using an `AccessMethod` that contains an `access_id`                     (e.g., for servers that use signed URLs for fetching object bytes).

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
api_instance = drs_api.DataRepositoryServiceApi(drs_api.ApiClient(configuration))
object_id = 'object_id_example' # str | ```DrsObject``` identifier
access_id = 'access_id_example' # str | An `access_id` from the `access_methods` list of a `DrsObject`

try:
    # Get a URL for fetching bytes
    api_response = api_instance.get_object_ga4gh_drs_v1_objects_object_id_access_access_id_get(object_id, access_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataRepositoryServiceApi->get_object_ga4gh_drs_v1_objects_object_id_access_access_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| &#x60;&#x60;&#x60;DrsObject&#x60;&#x60;&#x60; identifier | 
 **access_id** | **str**| An &#x60;access_id&#x60; from the &#x60;access_methods&#x60; list of a &#x60;DrsObject&#x60; | 

### Return type

[**AccessURL**](AccessURL.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_object_ga4gh_drs_v1_objects_object_id_get**
> DrsObject get_object_ga4gh_drs_v1_objects_object_id_get(object_id, expand)

Retrieve a DrsObject

Returns object metadata, and a list of access methods that can be used to fetch object bytes.

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
api_instance = drs_api.DataRepositoryServiceApi(drs_api.ApiClient(configuration))
object_id = 'object_id_example' # str | ```DrsObject``` identifier
expand = true # bool | If false and the object_id refers to a bundle, then the ContentsObject array contains only         those objects directly contained in the bundle. That is, if the bundle contains other bundles,         those other bundles are not recursively included in the result. If true and the object_id refers to a bundle,         then the entire set of objects in the bundle is expanded. That is, if the bundle contains aother bundles,         then those other bundles are recursively expanded and included in the result.         Recursion continues through the entire sub-tree of the bundle.         If the object_id refers to a blob, then the query parameter is ignored.

try:
    # Retrieve a DrsObject
    api_response = api_instance.get_object_ga4gh_drs_v1_objects_object_id_get(object_id, expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataRepositoryServiceApi->get_object_ga4gh_drs_v1_objects_object_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| &#x60;&#x60;&#x60;DrsObject&#x60;&#x60;&#x60; identifier | 
 **expand** | **bool**| If false and the object_id refers to a bundle, then the ContentsObject array contains only         those objects directly contained in the bundle. That is, if the bundle contains other bundles,         those other bundles are not recursively included in the result. If true and the object_id refers to a bundle,         then the entire set of objects in the bundle is expanded. That is, if the bundle contains aother bundles,         then those other bundles are recursively expanded and included in the result.         Recursion continues through the entire sub-tree of the bundle.         If the object_id refers to a blob, then the query parameter is ignored. | 

### Return type

[**DrsObject**](DrsObject.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_object_ga4gh_drs_v1_objects_post**
> BasicResponse post_object_ga4gh_drs_v1_objects_post(body)

Create a new DrsObject

POST a requested ID to create an object that corresponds to this ID

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
api_instance = drs_api.DataRepositoryServiceApi(drs_api.ApiClient(configuration))
body = drs_api.DrsObject() # DrsObject | 

try:
    # Create a new DrsObject
    api_response = api_instance.post_object_ga4gh_drs_v1_objects_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataRepositoryServiceApi->post_object_ga4gh_drs_v1_objects_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DrsObject**](DrsObject.md)|  | 

### Return type

[**BasicResponse**](BasicResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_object_ga4gh_drs_v1_objects_object_id_put**
> BasicResponse put_object_ga4gh_drs_v1_objects_object_id_put(body, object_id)

Update a DrsObject

Update the ```DrsObject```

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
api_instance = drs_api.DataRepositoryServiceApi(drs_api.ApiClient(configuration))
body = drs_api.DrsObject() # DrsObject | 
object_id = 'object_id_example' # str | 

try:
    # Update a DrsObject
    api_response = api_instance.put_object_ga4gh_drs_v1_objects_object_id_put(body, object_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataRepositoryServiceApi->put_object_ga4gh_drs_v1_objects_object_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DrsObject**](DrsObject.md)|  | 
 **object_id** | **str**|  | 

### Return type

[**BasicResponse**](BasicResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

