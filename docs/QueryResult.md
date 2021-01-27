# QueryResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query_id** | **int** | The ID of the query that can be used for pagination.  Note: The id will expire after four hours (session duration) and during a session you can have maximum 2,500 Queries.  The QueryIDs will be reused (starting from 1) if more than 2,500 queries are requested within a session.  The session will expire after four hours inactivity,  i.e. no requests with the token.  Use always &#x60;x-paginate-by-query-id&#x60; Header to paginate through records. The response time will be faster by using QueryID.  | [optional] 
**records_searched** | **int** | The overrall number of records available in Web of Science. | [optional] 
**records_found** | **int** | The number of records of your request that are filtered through usrQuery but as well other query parameters. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

