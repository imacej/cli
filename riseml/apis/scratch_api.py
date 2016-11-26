# coding: utf-8

"""
    RiseML API


    OpenAPI spec version: 1.1.0
    Contact: support@riseml.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class ScratchApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def create_scratch(self, scratch_id, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_scratch(scratch_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str scratch_id:  (required)
        :return: list[ScratchEntry]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_scratch_with_http_info(scratch_id, **kwargs)
        else:
            (data) = self.create_scratch_with_http_info(scratch_id, **kwargs)
            return data

    def create_scratch_with_http_info(self, scratch_id, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_scratch_with_http_info(scratch_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str scratch_id:  (required)
        :return: list[ScratchEntry]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['scratch_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_scratch" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'scratch_id' is set
        if ('scratch_id' not in params) or (params['scratch_id'] is None):
            raise ValueError("Missing the required parameter `scratch_id` when calling `create_scratch`")


        collection_formats = {}

        resource_path = '/scratches/{scratch_id}'.replace('{format}', 'json')
        path_params = {}
        if 'scratch_id' in params:
            path_params['scratch_id'] = params['scratch_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['api_key']

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='list[ScratchEntry]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'),
                                            _preload_content=params.get('_preload_content', True),
                                            collection_formats=collection_formats)

    def delete_scratch_object(self, scratch_id, path, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_scratch_object(scratch_id, path, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str scratch_id:  (required)
        :param str path:  (required)
        :return: list[ScratchEntry]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_scratch_object_with_http_info(scratch_id, path, **kwargs)
        else:
            (data) = self.delete_scratch_object_with_http_info(scratch_id, path, **kwargs)
            return data

    def delete_scratch_object_with_http_info(self, scratch_id, path, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_scratch_object_with_http_info(scratch_id, path, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str scratch_id:  (required)
        :param str path:  (required)
        :return: list[ScratchEntry]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['scratch_id', 'path']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_scratch_object" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'scratch_id' is set
        if ('scratch_id' not in params) or (params['scratch_id'] is None):
            raise ValueError("Missing the required parameter `scratch_id` when calling `delete_scratch_object`")
        # verify the required parameter 'path' is set
        if ('path' not in params) or (params['path'] is None):
            raise ValueError("Missing the required parameter `path` when calling `delete_scratch_object`")


        collection_formats = {}

        resource_path = '/scratches/{scratch_id}/{path}'.replace('{format}', 'json')
        path_params = {}
        if 'scratch_id' in params:
            path_params['scratch_id'] = params['scratch_id']
        if 'path' in params:
            path_params['path'] = params['path']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['api_key']

        return self.api_client.call_api(resource_path, 'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='list[ScratchEntry]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'),
                                            _preload_content=params.get('_preload_content', True),
                                            collection_formats=collection_formats)

    def get_scratch_meta(self, scratch_id, path, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_scratch_meta(scratch_id, path, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str scratch_id:  (required)
        :param str path:  (required)
        :return: list[ScratchEntry]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_scratch_meta_with_http_info(scratch_id, path, **kwargs)
        else:
            (data) = self.get_scratch_meta_with_http_info(scratch_id, path, **kwargs)
            return data

    def get_scratch_meta_with_http_info(self, scratch_id, path, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_scratch_meta_with_http_info(scratch_id, path, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str scratch_id:  (required)
        :param str path:  (required)
        :return: list[ScratchEntry]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['scratch_id', 'path']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_scratch_meta" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'scratch_id' is set
        if ('scratch_id' not in params) or (params['scratch_id'] is None):
            raise ValueError("Missing the required parameter `scratch_id` when calling `get_scratch_meta`")
        # verify the required parameter 'path' is set
        if ('path' not in params) or (params['path'] is None):
            raise ValueError("Missing the required parameter `path` when calling `get_scratch_meta`")


        collection_formats = {}

        resource_path = '/scratches/{scratch_id}/{path}'.replace('{format}', 'json')
        path_params = {}
        if 'scratch_id' in params:
            path_params['scratch_id'] = params['scratch_id']
        if 'path' in params:
            path_params['path'] = params['path']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['api_key']

        return self.api_client.call_api(resource_path, 'PATCH',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='list[ScratchEntry]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'),
                                            _preload_content=params.get('_preload_content', True),
                                            collection_formats=collection_formats)

    def get_scratch_object(self, scratch_id, path, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_scratch_object(scratch_id, path, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str scratch_id:  (required)
        :param str path:  (required)
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_scratch_object_with_http_info(scratch_id, path, **kwargs)
        else:
            (data) = self.get_scratch_object_with_http_info(scratch_id, path, **kwargs)
            return data

    def get_scratch_object_with_http_info(self, scratch_id, path, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_scratch_object_with_http_info(scratch_id, path, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str scratch_id:  (required)
        :param str path:  (required)
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['scratch_id', 'path']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_scratch_object" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'scratch_id' is set
        if ('scratch_id' not in params) or (params['scratch_id'] is None):
            raise ValueError("Missing the required parameter `scratch_id` when calling `get_scratch_object`")
        # verify the required parameter 'path' is set
        if ('path' not in params) or (params['path'] is None):
            raise ValueError("Missing the required parameter `path` when calling `get_scratch_object`")


        collection_formats = {}

        resource_path = '/scratches/{scratch_id}/{path}'.replace('{format}', 'json')
        path_params = {}
        if 'scratch_id' in params:
            path_params['scratch_id'] = params['scratch_id']
        if 'path' in params:
            path_params['path'] = params['path']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['api_key']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='file',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'),
                                            _preload_content=params.get('_preload_content', True),
                                            collection_formats=collection_formats)

    def put_scratch_object(self, scratch_id, path, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.put_scratch_object(scratch_id, path, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str scratch_id:  (required)
        :param str path:  (required)
        :return: ScratchEntry
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.put_scratch_object_with_http_info(scratch_id, path, **kwargs)
        else:
            (data) = self.put_scratch_object_with_http_info(scratch_id, path, **kwargs)
            return data

    def put_scratch_object_with_http_info(self, scratch_id, path, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.put_scratch_object_with_http_info(scratch_id, path, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str scratch_id:  (required)
        :param str path:  (required)
        :return: ScratchEntry
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['scratch_id', 'path']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_scratch_object" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'scratch_id' is set
        if ('scratch_id' not in params) or (params['scratch_id'] is None):
            raise ValueError("Missing the required parameter `scratch_id` when calling `put_scratch_object`")
        # verify the required parameter 'path' is set
        if ('path' not in params) or (params['path'] is None):
            raise ValueError("Missing the required parameter `path` when calling `put_scratch_object`")


        collection_formats = {}

        resource_path = '/scratches/{scratch_id}/{path}'.replace('{format}', 'json')
        path_params = {}
        if 'scratch_id' in params:
            path_params['scratch_id'] = params['scratch_id']
        if 'path' in params:
            path_params['path'] = params['path']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['api_key']

        return self.api_client.call_api(resource_path, 'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='ScratchEntry',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'),
                                            _preload_content=params.get('_preload_content', True),
                                            collection_formats=collection_formats)
