import drs_api, pprint
from drs_api.rest import ApiException
from drs_api.drs_configuration import DrsConfiguration

configuration = DrsConfiguration()
configuration.host = "https://drs.test.cmgg.be"
configuration.username = "admin"
configuration.password = "password"



api = drs_api.DataRepositoryServiceApi(drs_api.ApiClient(configuration))

try:
    # Retrieve a DrsObject
    api_response = api.get_object_ga4gh_drs_v1_objects_object_id_get("fdjslfjdslkjflksdjf", True)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataRepositoryServiceApi->get_object_ga4gh_drs_v1_objects_object_id_get: %s\n" % e)

print(configuration.get_api_key_with_prefix("Authorization"))