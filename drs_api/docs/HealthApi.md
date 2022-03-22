# drs_api.HealthApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_health_health_get**](HealthApi.md#get_health_health_get) | **GET** /health | Check if the API is running correctly

# **get_health_health_get**
> object get_health_health_get()

Check if the API is running correctly

Health check for the API

### Example
```python
from __future__ import print_function
import time
import drs_api
from drs_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = drs_api.HealthApi()

try:
    # Check if the API is running correctly
    api_response = api_instance.get_health_health_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HealthApi->get_health_health_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

