import drs_api
from drs_api.rest import ApiException
from drs_api import Configuration

configuration = Configuration()
configuration.host = "https://drs.test.cmgg.be"
configuration.username = "admin"
configuration.password = "password"
## Uncomment and set expired token to test refresh
#expired_token = ""
#configuration.api_key = {"Authorization":expired_token}

import logging
logging.basicConfig(level=logging.DEBUG)

print(configuration.api_key_prefix)
print(configuration.host)

api = drs_api.DataRepositoryServiceApi(drs_api.ApiClient(configuration))

try:
    # Retrieve a DrsObject
    api_response = api.get_object_ga4gh_drs_v1_objects_object_id_get("fdjslfjdslkjflksdjf", True)
except ApiException as e:
    print("Exception when calling DataRepositoryServiceApi->get_object_ga4gh_drs_v1_objects_object_id_get: %s\n" % e)

print(configuration.get_api_key_with_prefix("Authorization"))