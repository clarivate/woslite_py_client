# coding: utf-8

"""
    Web of Science API Lite

    A responsive API that supports rich searching across the Web of Science Core Collection to retrieve core article metadata.  This service provides a great way to reuse Web of Science data both internally and externally to enhance  institutional repositories and research networking systems with best-in-class data. This API supports searching across the Web of Science to retrieve item-level metadata with limited fields:  - UT (Unique Identifier) - Authors - Author keywords - Document type - Title - Issue - Pages - Publication date - Source title - Volume - DOI - ISBN - ISSN   The API supports JSON and XML responses, and this documentation supports trying both response types.   # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from woslite_client.api_client import ApiClient


class SearchApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def query_query_id_get(self, query_id, count, first_record, **kwargs):  # noqa: E501
        """Fetch record(s) by query identifier  # noqa: E501

        This operation returns record(s) identified by a query identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.query_query_id_get(query_id, count, first_record, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int query_id: Retrieve records based on query identifier. (required)
        :param int count: Number of records to return, must be 0-100. (required)
        :param int first_record: Specific record, if any within the result set to return. Cannot be less than 1 and greater than 100000. (required)
        :param str sort_field: Order by field(s). Field name and order by clause separated by '+', use A for ASC and D for DESC, ex: PY+D. Multiple values are separated by comma. If sortField was set on the original query, this parameter should be set as sorting is not a property of the query.
        :return: WosLiteResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.query_query_id_get_with_http_info(query_id, count, first_record, **kwargs)  # noqa: E501
        else:
            (data) = self.query_query_id_get_with_http_info(query_id, count, first_record, **kwargs)  # noqa: E501
            return data

    def query_query_id_get_with_http_info(self, query_id, count, first_record, **kwargs):  # noqa: E501
        """Fetch record(s) by query identifier  # noqa: E501

        This operation returns record(s) identified by a query identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.query_query_id_get_with_http_info(query_id, count, first_record, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int query_id: Retrieve records based on query identifier. (required)
        :param int count: Number of records to return, must be 0-100. (required)
        :param int first_record: Specific record, if any within the result set to return. Cannot be less than 1 and greater than 100000. (required)
        :param str sort_field: Order by field(s). Field name and order by clause separated by '+', use A for ASC and D for DESC, ex: PY+D. Multiple values are separated by comma. If sortField was set on the original query, this parameter should be set as sorting is not a property of the query.
        :return: WosLiteResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['query_id', 'count', 'first_record', 'sort_field']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method query_query_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'query_id' is set
        if ('query_id' not in params or
                params['query_id'] is None):
            raise ValueError("Missing the required parameter `query_id` when calling `query_query_id_get`")  # noqa: E501
        # verify the required parameter 'count' is set
        if ('count' not in params or
                params['count'] is None):
            raise ValueError("Missing the required parameter `count` when calling `query_query_id_get`")  # noqa: E501
        # verify the required parameter 'first_record' is set
        if ('first_record' not in params or
                params['first_record'] is None):
            raise ValueError("Missing the required parameter `first_record` when calling `query_query_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'query_id' in params:
            path_params['queryId'] = params['query_id']  # noqa: E501

        query_params = []
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501
        if 'first_record' in params:
            query_params.append(('firstRecord', params['first_record']))  # noqa: E501
        if 'sort_field' in params:
            query_params.append(('sortField', params['sort_field']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['key']  # noqa: E501

        return self.api_client.call_api(
            '/query/{queryId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WosLiteResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def root_get(self, database_id, usr_query, count, first_record, **kwargs):  # noqa: E501
        """Submits a user query and returns results  # noqa: E501

        The search operation submits a search query to the specified database edition and retrieves data. This operation returns a query ID that can be used in subsequent operations to retrieve more records.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.root_get(database_id, usr_query, count, first_record, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str database_id: Database to search. Must be a valid database ID, one of the following: BCI/BIOABS/BIOSIS/CCC/DCI/DIIDW/MEDLINE/WOK/WOS/ZOOREC. WOK represents all databases. (required)
        :param str usr_query: User query for requesting data, ex: TS=(cadmium). The query parser will return errors for invalid queries. (required)
        :param int count: Number of records to return, must be 0-100. (required)
        :param int first_record: Specific record, if any within the result set to return. Cannot be less than 1 and greater than 100000. (required)
        :param str lang: Language of search. This element can take only one value: en for English. If no language is specified, English is passed by default.
        :param str edition: Edition(s) to be searched. If null, user permissions will be substituted. Must include the name of the collection and edition name separated by '+', ex: WOS+SCI. Multiple editions are separated by ','. Editions available for collection(WOS) - AHCI,CCR,IC,ISSHP,ISTP,SCI,SSCI,BHCI,BSCI and ESCI.
        :param str publish_time_span: This element specifies a range of publication dates. If publishTimeSpan is used, the loadTimeSpan parameter must be omitted. If publishTimeSpan and loadTimeSpan are both omitted, then the maximum time span will be inferred from the editions data. Beginning and end dates should be specified in the yyyy-mm-dd format separated by +, ex: 1993-01-01+2009-12-31.
        :param str load_time_span: Load time span (otherwise described as symbolic time span) defines a range of load dates. The load date is the date a record was added to the database. If load date is specified, the publishTimeSpan parameter must be omitted. If both publishTimeSpan and loadTimeSpan are omitted, the maximum publication date will be inferred from the editions data. Any of D/W/M/Y prefixed with a number where D-Day, M-Month, W-Week, Y-Year allowed. Acceptable value range for Day(0-6), Week(1-52), Month(1-12) and Year(0-10), ex: 5D,30W,10M,8Y.
        :param str sort_field: Order by field(s). Field name and order by clause separated by '+', use A for ASC and D for DESC, ex: PY+D. Multiple values are separated by comma.
        :return: WosLiteResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.root_get_with_http_info(database_id, usr_query, count, first_record, **kwargs)  # noqa: E501
        else:
            (data) = self.root_get_with_http_info(database_id, usr_query, count, first_record, **kwargs)  # noqa: E501
            return data

    def root_get_with_http_info(self, database_id, usr_query, count, first_record, **kwargs):  # noqa: E501
        """Submits a user query and returns results  # noqa: E501

        The search operation submits a search query to the specified database edition and retrieves data. This operation returns a query ID that can be used in subsequent operations to retrieve more records.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.root_get_with_http_info(database_id, usr_query, count, first_record, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str database_id: Database to search. Must be a valid database ID, one of the following: BCI/BIOABS/BIOSIS/CCC/DCI/DIIDW/MEDLINE/WOK/WOS/ZOOREC. WOK represents all databases. (required)
        :param str usr_query: User query for requesting data, ex: TS=(cadmium). The query parser will return errors for invalid queries. (required)
        :param int count: Number of records to return, must be 0-100. (required)
        :param int first_record: Specific record, if any within the result set to return. Cannot be less than 1 and greater than 100000. (required)
        :param str lang: Language of search. This element can take only one value: en for English. If no language is specified, English is passed by default.
        :param str edition: Edition(s) to be searched. If null, user permissions will be substituted. Must include the name of the collection and edition name separated by '+', ex: WOS+SCI. Multiple editions are separated by ','. Editions available for collection(WOS) - AHCI,CCR,IC,ISSHP,ISTP,SCI,SSCI,BHCI,BSCI and ESCI.
        :param str publish_time_span: This element specifies a range of publication dates. If publishTimeSpan is used, the loadTimeSpan parameter must be omitted. If publishTimeSpan and loadTimeSpan are both omitted, then the maximum time span will be inferred from the editions data. Beginning and end dates should be specified in the yyyy-mm-dd format separated by +, ex: 1993-01-01+2009-12-31.
        :param str load_time_span: Load time span (otherwise described as symbolic time span) defines a range of load dates. The load date is the date a record was added to the database. If load date is specified, the publishTimeSpan parameter must be omitted. If both publishTimeSpan and loadTimeSpan are omitted, the maximum publication date will be inferred from the editions data. Any of D/W/M/Y prefixed with a number where D-Day, M-Month, W-Week, Y-Year allowed. Acceptable value range for Day(0-6), Week(1-52), Month(1-12) and Year(0-10), ex: 5D,30W,10M,8Y.
        :param str sort_field: Order by field(s). Field name and order by clause separated by '+', use A for ASC and D for DESC, ex: PY+D. Multiple values are separated by comma.
        :return: WosLiteResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['database_id', 'usr_query', 'count', 'first_record', 'lang', 'edition', 'publish_time_span', 'load_time_span', 'sort_field']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method root_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'database_id' is set
        if ('database_id' not in params or
                params['database_id'] is None):
            raise ValueError("Missing the required parameter `database_id` when calling `root_get`")  # noqa: E501
        # verify the required parameter 'usr_query' is set
        if ('usr_query' not in params or
                params['usr_query'] is None):
            raise ValueError("Missing the required parameter `usr_query` when calling `root_get`")  # noqa: E501
        # verify the required parameter 'count' is set
        if ('count' not in params or
                params['count'] is None):
            raise ValueError("Missing the required parameter `count` when calling `root_get`")  # noqa: E501
        # verify the required parameter 'first_record' is set
        if ('first_record' not in params or
                params['first_record'] is None):
            raise ValueError("Missing the required parameter `first_record` when calling `root_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'database_id' in params:
            query_params.append(('databaseId', params['database_id']))  # noqa: E501
        if 'lang' in params:
            query_params.append(('lang', params['lang']))  # noqa: E501
        if 'usr_query' in params:
            query_params.append(('usrQuery', params['usr_query']))  # noqa: E501
        if 'edition' in params:
            query_params.append(('edition', params['edition']))  # noqa: E501
        if 'publish_time_span' in params:
            query_params.append(('publishTimeSpan', params['publish_time_span']))  # noqa: E501
        if 'load_time_span' in params:
            query_params.append(('loadTimeSpan', params['load_time_span']))  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501
        if 'first_record' in params:
            query_params.append(('firstRecord', params['first_record']))  # noqa: E501
        if 'sort_field' in params:
            query_params.append(('sortField', params['sort_field']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['key']  # noqa: E501

        return self.api_client.call_api(
            '/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WosLiteResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
