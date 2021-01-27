# swagger_client.SearchApi

All URIs are relative to *https://api.clarivate.com/api/woslite*

Method | HTTP request | Description
------------- | ------------- | -------------
[**query_query_id_get**](SearchApi.md#query_query_id_get) | **GET** /query/{queryId} | Fetch record(s) by query identifier
[**root_get**](SearchApi.md#root_get) | **GET** / | Submits a user query and returns results

# **query_query_id_get**
> WosLiteResponse query_query_id_get(query_id, count, first_record, sort_field=sort_field)

Fetch record(s) by query identifier

This operation returns record(s) identified by a query identifier.

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
api_instance = woslite_client.SearchApi(woslite_client.ApiClient(configuration))
query_id = 56 # int | Retrieve records based on query identifier.
count = 56 # int | Number of records to return, must be 0-100.
first_record = 56 # int | Specific record, if any within the result set to return. Cannot be less than 1 and greater than 100000.
sort_field = 'sort_field_example' # str | Order by field(s). Field name and order by clause separated by '+', use A for ASC and D for DESC, ex: PY+D. Multiple values are separated by comma. If sortField was set on the original query, this parameter should be set as sorting is not a property of the query. (optional)

try:
    # Fetch record(s) by query identifier
    api_response = api_instance.query_query_id_get(query_id, count, first_record, sort_field=sort_field)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->query_query_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_id** | **int**| Retrieve records based on query identifier. | 
 **count** | **int**| Number of records to return, must be 0-100. | 
 **first_record** | **int**| Specific record, if any within the result set to return. Cannot be less than 1 and greater than 100000. | 
 **sort_field** | **str**| Order by field(s). Field name and order by clause separated by &#x27;+&#x27;, use A for ASC and D for DESC, ex: PY+D. Multiple values are separated by comma. If sortField was set on the original query, this parameter should be set as sorting is not a property of the query. | [optional] 

### Return type

[**WosLiteResponse**](WosLiteResponse.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **root_get**
> WosLiteResponse root_get(database_id, usr_query, count, first_record, lang=lang, edition=edition, publish_time_span=publish_time_span, load_time_span=load_time_span, sort_field=sort_field)

Submits a user query and returns results

The search operation submits a search query to the specified database edition and retrieves data. This operation returns a query ID that can be used in subsequent operations to retrieve more records.

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
api_instance = woslite_client.SearchApi(woslite_client.ApiClient(configuration))
database_id = 'database_id_example' # str | Database to search. Must be a valid database ID, one of the following: BCI/BIOABS/BIOSIS/CCC/DCI/DIIDW/MEDLINE/WOK/WOS/ZOOREC. WOK represents all databases.
usr_query = 'usr_query_example' # str | User query for requesting data, ex: TS=(cadmium). The query parser will return errors for invalid queries.
count = 56 # int | Number of records to return, must be 0-100.
first_record = 56 # int | Specific record, if any within the result set to return. Cannot be less than 1 and greater than 100000.
lang = 'lang_example' # str | Language of search. This element can take only one value: en for English. If no language is specified, English is passed by default. (optional)
edition = 'edition_example' # str | Edition(s) to be searched. If null, user permissions will be substituted. Must include the name of the collection and edition name separated by '+', ex: WOS+SCI. Multiple editions are separated by ','. Editions available for collection(WOS) - AHCI,CCR,IC,ISSHP,ISTP,SCI,SSCI,BHCI,BSCI and ESCI. (optional)
publish_time_span = 'publish_time_span_example' # str | This element specifies a range of publication dates. If publishTimeSpan is used, the loadTimeSpan parameter must be omitted. If publishTimeSpan and loadTimeSpan are both omitted, then the maximum time span will be inferred from the editions data. Beginning and end dates should be specified in the yyyy-mm-dd format separated by +, ex: 1993-01-01+2009-12-31. (optional)
load_time_span = 'load_time_span_example' # str | Load time span (otherwise described as symbolic time span) defines a range of load dates. The load date is the date a record was added to the database. If load date is specified, the publishTimeSpan parameter must be omitted. If both publishTimeSpan and loadTimeSpan are omitted, the maximum publication date will be inferred from the editions data. Any of D/W/M/Y prefixed with a number where D-Day, M-Month, W-Week, Y-Year allowed. Acceptable value range for Day(0-6), Week(1-52), Month(1-12) and Year(0-10), ex: 5D,30W,10M,8Y. (optional)
sort_field = 'sort_field_example' # str | Order by field(s). Field name and order by clause separated by '+', use A for ASC and D for DESC, ex: PY+D. Multiple values are separated by comma. (optional)

try:
    # Submits a user query and returns results
    api_response = api_instance.root_get(database_id, usr_query, count, first_record, lang=lang, edition=edition, publish_time_span=publish_time_span, load_time_span=load_time_span, sort_field=sort_field)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->root_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_id** | **str**| Database to search. Must be a valid database ID, one of the following: BCI/BIOABS/BIOSIS/CCC/DCI/DIIDW/MEDLINE/WOK/WOS/ZOOREC. WOK represents all databases. | 
 **usr_query** | **str**| User query for requesting data, ex: TS&#x3D;(cadmium). The query parser will return errors for invalid queries. | 
 **count** | **int**| Number of records to return, must be 0-100. | 
 **first_record** | **int**| Specific record, if any within the result set to return. Cannot be less than 1 and greater than 100000. | 
 **lang** | **str**| Language of search. This element can take only one value: en for English. If no language is specified, English is passed by default. | [optional] 
 **edition** | **str**| Edition(s) to be searched. If null, user permissions will be substituted. Must include the name of the collection and edition name separated by &#x27;+&#x27;, ex: WOS+SCI. Multiple editions are separated by &#x27;,&#x27;. Editions available for collection(WOS) - AHCI,CCR,IC,ISSHP,ISTP,SCI,SSCI,BHCI,BSCI and ESCI. | [optional] 
 **publish_time_span** | **str**| This element specifies a range of publication dates. If publishTimeSpan is used, the loadTimeSpan parameter must be omitted. If publishTimeSpan and loadTimeSpan are both omitted, then the maximum time span will be inferred from the editions data. Beginning and end dates should be specified in the yyyy-mm-dd format separated by +, ex: 1993-01-01+2009-12-31. | [optional] 
 **load_time_span** | **str**| Load time span (otherwise described as symbolic time span) defines a range of load dates. The load date is the date a record was added to the database. If load date is specified, the publishTimeSpan parameter must be omitted. If both publishTimeSpan and loadTimeSpan are omitted, the maximum publication date will be inferred from the editions data. Any of D/W/M/Y prefixed with a number where D-Day, M-Month, W-Week, Y-Year allowed. Acceptable value range for Day(0-6), Week(1-52), Month(1-12) and Year(0-10), ex: 5D,30W,10M,8Y. | [optional] 
 **sort_field** | **str**| Order by field(s). Field name and order by clause separated by &#x27;+&#x27;, use A for ASC and D for DESC, ex: PY+D. Multiple values are separated by comma. | [optional] 

### Return type

[**WosLiteResponse**](WosLiteResponse.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

