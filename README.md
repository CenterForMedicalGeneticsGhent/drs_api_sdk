# drs-api
 GET request: Fetch a DrsObject from the database by sending a unique ID through the request  POST request: Create a non-existing DrsObject in the database by giving an identifier  DELETE request: Delete a DrsObject from the database by unique identifier  PUT request: Update an existing DrsObject by unique identifier and the changes in the body 

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.2.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.ugent.be/cmgg/drs_api_sdk.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/CenterForMedicalGeneticsGhent/drs_api_sdk.git`)

Then import the package:
```python
import drs_api 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import drs_api
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import drs_api
from drs_api.rest import ApiException

# Configure OAuth2 access token for authorization: OAuth2PasswordBearer
configuration = drs_api.Configuration()
configuration.host = ""
configuration.username = ""
configuration.password = ""

# Get the access token
login_instance = drs_api.LoginApi(drs_api.ApiClient(configuration))

try:
    login_response = login_instance.login_token_post(username=configuration.username, password=configuration.password, grant_type="", scope="", client_id="", client_secret="")
    assert login_response.token_type.lower() == "bearer"
    configuration.access_token = login_response.access_token
except ApiException as e:
    print("Exception when calling LoginApi->login_token_post: %s\n" % e)

# Do a health check 
api_instance = drs_api.HealthApi(drs_api.ApiClient(configuration))

try:
    api_response = api_instance.get_health_health_get()
    assert api_response == "Okay"
    print("Health check is okay!")
except ApiException as e:
    print("Exception when calling DataRepositoryServiceApi->get_health_ga4gh_drs_v1_health_get: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to */*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DataRepositoryServiceApi* | [**delete_object_ga4gh_drs_v1_objects_object_id_delete**](docs/DataRepositoryServiceApi.md#delete_object_ga4gh_drs_v1_objects_object_id_delete) | **DELETE** /ga4gh/drs/v1/objects/{object_id} | Delete a DrsObject
*DataRepositoryServiceApi* | [**get_health_ga4gh_drs_v1_health_get**](docs/DataRepositoryServiceApi.md#get_health_ga4gh_drs_v1_health_get) | **GET** /ga4gh/drs/v1/health | Check if the API is running correctly
*DataRepositoryServiceApi* | [**get_object_alias_ga4gh_drs_v1_objects_get**](docs/DataRepositoryServiceApi.md#get_object_alias_ga4gh_drs_v1_objects_get) | **GET** /ga4gh/drs/v1/objects | Query DrsObjects on alias
*DataRepositoryServiceApi* | [**get_object_ga4gh_drs_v1_objects_object_id_access_access_id_get**](docs/DataRepositoryServiceApi.md#get_object_ga4gh_drs_v1_objects_object_id_access_access_id_get) | **GET** /ga4gh/drs/v1/objects/{object_id}/access/{access_id} | Get a URL for fetching bytes
*DataRepositoryServiceApi* | [**get_object_ga4gh_drs_v1_objects_object_id_get**](docs/DataRepositoryServiceApi.md#get_object_ga4gh_drs_v1_objects_object_id_get) | **GET** /ga4gh/drs/v1/objects/{object_id} | Retrieve a DrsObject
*DataRepositoryServiceApi* | [**post_object_ga4gh_drs_v1_objects_post**](docs/DataRepositoryServiceApi.md#post_object_ga4gh_drs_v1_objects_post) | **POST** /ga4gh/drs/v1/objects | Create a new DrsObject
*DataRepositoryServiceApi* | [**put_object_ga4gh_drs_v1_objects_object_id_put**](docs/DataRepositoryServiceApi.md#put_object_ga4gh_drs_v1_objects_object_id_put) | **PUT** /ga4gh/drs/v1/objects/{object_id} | Update a DrsObject
*LoginApi* | [**login_token_post**](docs/LoginApi.md#login_token_post) | **POST** /token | Login
*UserManagementApi* | [**delete_user_users_username_delete**](docs/UserManagementApi.md#delete_user_users_username_delete) | **DELETE** /users/{username} | Delete a user
*UserManagementApi* | [**delete_user_users_username_get**](docs/UserManagementApi.md#delete_user_users_username_get) | **GET** /users/{username} | Get user info
*UserManagementApi* | [**post_user_users_post**](docs/UserManagementApi.md#post_user_users_post) | **POST** /users | Create a new user
*UserManagementApi* | [**put_user_users_username_put**](docs/UserManagementApi.md#put_user_users_username_put) | **PUT** /users/{username} | Update a user

## Documentation For Models

 - [AccessMethods](docs/AccessMethods.md)
 - [AccessURL](docs/AccessURL.md)
 - [AllOfDrsObjectAccessMethods](docs/AllOfDrsObjectAccessMethods.md)
 - [AllOfDrsObjectChecksums](docs/AllOfDrsObjectChecksums.md)
 - [AllOfDrsObjectContents](docs/AllOfDrsObjectContents.md)
 - [BasicResponse](docs/BasicResponse.md)
 - [BodyLoginTokenPost](docs/BodyLoginTokenPost.md)
 - [Checksums](docs/Checksums.md)
 - [ContentsExpanded](docs/ContentsExpanded.md)
 - [DrsObject](docs/DrsObject.md)
 - [Error](docs/Error.md)
 - [HTTPValidationError](docs/HTTPValidationError.md)
 - [Token](docs/Token.md)
 - [UserInputModel](docs/UserInputModel.md)
 - [UserTemplate](docs/UserTemplate.md)
 - [ValidationError](docs/ValidationError.md)

## Documentation For Authorization


## OAuth2PasswordBearer

- **Type**: OAuth
- **Flow**: password
- **Authorization URL**: 
- **Scopes**: 


## Author

ga4gh-cloud@ga4gh.org
