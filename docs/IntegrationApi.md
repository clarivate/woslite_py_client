# swagger_client.IntegrationApi

All URIs are relative to *https://api.clarivate.com/api/woslite*

Method | HTTP request | Description
------------- | ------------- | -------------
[**id_unique_id_get**](IntegrationApi.md#id_unique_id_get) | **GET** /id/{uniqueId} | Find record(s) by specific id

# **id_unique_id_get**
> WosLiteResponse id_unique_id_get(database_id, unique_id, count, first_record, lang=lang, sort_field=sort_field)

Find record(s) by specific id

This operation returns a record identified by a unique identifier. You may specify multiple identifiers in a single request.

### Example

```python
from __future__ import print_function
import time
import woslite_client
from woslite_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: key
configuration = woslite_client.Configuration()
configuration.api_key['X-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-ApiKey'] = 'Bearer'

# create an instance of the API class
api_instance = woslite_client.IntegrationApi(woslite_client.ApiClient(configuration))
database_id = 'database_id_example' # str | Database to search. Must be a valid database ID, one of the following: BCI/BIOABS/BIOSIS/CCC/DCI/DIIDW/MEDLINE/WOK/WOS/ZOOREC. WOK represents all databases.
unique_id = 'unique_id_example' # str | Primary item(s) id to be searched, ex: WOS:000270372400005. Cannot be null or an empty string. Multiple values are separated by comma.
count = 56 # int | Number of records returned in the request
first_record = 56 # int | Specific record, if any within the result set to return. Cannot be less than 1 and greater than 100000.
lang = 'lang_example' # str | Language of search. This element can take only one value: en for English. If no language is specified, English is passed by default. (optional)
sort_field = 'sort_field_example' # str | Order by field(s). Field name and order by clause separated by '+', use A for ASC and D for DESC, ex: PY+D. Multiple values are separated by comma. (optional)

try:
    # Find record(s) by specific id
    api_response = api_instance.id_unique_id_get(database_id, unique_id, count, first_record, lang=lang, sort_field=sort_field)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationApi->id_unique_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_id** | **str**| Database to search. Must be a valid database ID, one of the following: BCI/BIOABS/BIOSIS/CCC/DCI/DIIDW/MEDLINE/WOK/WOS/ZOOREC. WOK represents all databases. | 
 **unique_id** | **str**| Primary item(s) id to be searched, ex: WOS:000270372400005. Cannot be null or an empty string. Multiple values are separated by comma. | 
 **count** | **int**| Number of records returned in the request | 
 **first_record** | **int**| Specific record, if any within the result set to return. Cannot be less than 1 and greater than 100000. | 
 **lang** | **str**| Language of search. This element can take only one value: en for English. If no language is specified, English is passed by default. | [optional] 
 **sort_field** | **str**| Order by field(s). Field name and order by clause separated by &#x27;+&#x27;, use A for ASC and D for DESC, ex: PY+D. Multiple values are separated by comma. | [optional] 

### Return type

[**WosLiteResponse**](WosLiteResponse.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

