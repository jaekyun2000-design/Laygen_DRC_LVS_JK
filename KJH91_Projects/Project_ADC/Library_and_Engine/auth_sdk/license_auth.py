# from KJH91_Projects.Project_ADC.Library_and_Engine.netaddr import EUI
# import KJH91_Projects.Project_ADC.Library_and_Engine.requests


JSON_ERRCODE_SUCCESS_SDK = 0

def write_client_license(context_auth, license_path='license.txt'):
    #write config
    from configparser import ConfigParser

    #Get the configparser object
    config_object = ConfigParser()

    config_object["LICENSE"] = {
        'VALIDATION_SERVER_URL' : context_auth['validation_server_url'],
        'LICENSE_SERVER_IP'     : context_auth['license_server_ip'],
        'LICENSE_SERVER_PORT'   : context_auth['license_server_port'],

        'LICENSE_NAME'          : context_auth['license_name'],
        'MAC_ADDRESS'           : context_auth['client_mac'],
    }

    #Write the above sections to config.ini file
    with open(license_path, 'w') as conf:
        config_object.write(conf)

def get_context_auth_from_client_license(client_license_path):
    if client_license_path == None:
        raise Exception

    from configparser import ConfigParser

    #Read config.ini file
    config_object = ConfigParser()
    config_object.read(client_license_path)
    licenseinfo = config_object["LICENSE"]

    context_auth = {
        'path'                  : client_license_path,

        'validation_server_url' : licenseinfo['VALIDATION_SERVER_URL'],
        'license_server_ip'     : licenseinfo['LICENSE_SERVER_IP'],
        'license_server_port'   : licenseinfo['LICENSE_SERVER_PORT'],

        'license_name'          : licenseinfo['LICENSE_NAME'],
        #'client_mac_file'       : licenseinfo['MAC_ADDRESS'],
    }
    _mac_license = licenseinfo['MAC_ADDRESS']
    #_mac_license = None

    mac_picked, ip_picked = get_mac_address_and_ip(_mac_license)
    
    #mac_picked = 'AA:BB:CC:99:88:77'
    context_auth.update({
        'client_mac'            : mac_picked,
        'client_ip'             : ip_picked,
    })


    #TODO: check, licenseinfo['MAC_ADDRESS] == client_mac?

    return context_auth
def update_context_auth_from_response(context_auth, _response):
    if context_auth == None:
        raise Exception

    if _response != None and \
        'errCode' in _response and _response['errCode'] ==  JSON_ERRCODE_SUCCESS_SDK and \
            'data' in _response:
        if 'access_token' in _response['data']:
            dict_token = {
                'access_token'      : _response['data']['access_token'],
                'refresh_token'     : _response['data']['refresh_token'],
            }
            context_auth.update(**dict_token)
    return context_auth
def fill_dict_request_from_context_auth(context_auth):
    dict_request = {}
    for _key in ['license_name', 'license_server_ip', 'client_mac', 'client_ip']: #TODO: check, 'license_server_ip' required? (use get_client_ip, @server)
        dict_request[_key] = context_auth[_key]
    return dict_request



def _response_requests_wrapper(context_auth, api, dict_request = None, dict_exception = None, use_post = False, use_json = True, _debug = False, **kwargs_response):
    #header


    #TODO: check, move to common?
    import requests
    _url = '%s/%s'%(context_auth['validation_server_url'],api)
    proxies = {
        'http': 'http://%s:%s'%(context_auth['license_server_ip'],context_auth['license_server_port']),
        'https': 'http://%s:%s'%(context_auth['license_server_ip'],context_auth['license_server_port']),
    }


    #TODO: check, context_auth is not set
    if context_auth and 'access_token' in context_auth:
        dict_bearer = {
            'Authorization': 'Bearer %s'%(context_auth['access_token']),
        }
        if 'headers' not in kwargs_response or kwargs_response['headers'] == None:
            kwargs_response.update({'headers' : dict_bearer})
        elif 'headers' in kwargs_response and 'Authorization' not in kwargs_response['headers']:
            kwargs_response['headers'].update(dict_bearer)
            
            
    count_try = 0
    while count_try < 3:
        if use_post:
            if use_json:
                _response = requests.post(_url, proxies=proxies, json=dict_request, **kwargs_response)
            else:
                _response = requests.post(_url, proxies=proxies, data=dict_request, **kwargs_response)
        else:
            _response = requests.get(_url, params=dict_request, **kwargs_response)
        if _debug:
            print(_response.url)
        if _response.status_code in [504,]:
            _json = { 'status' : _response.status_code }
            break            
        try:
            _json = _response.json()
            if False and dict_request != None:
                dict_request['cookies'] = _response.cookies
            break
        except ValueError as e:        
            try:
                str_title = u'exp_json:%s'%(_response.text)
            except UnicodeDecodeError:
                str_title = u'exp_json:%s'%_response.text.decode('utf-8','replace')
            if dict_exception == None:
                #log_exception(e, desc=str_title)
                pass
            elif str(e) not in dict_exception:
                dict_exception[str(e)] = str_title
        _json = None
        count_try += 1
    if _debug:
        print(_json)
    return _json
    


def bevil_client_authentication_base(_api, context_auth, client_license_path=None, mac_address_optional=None, _debug=False):
    if context_auth == None and client_license_path == None:
        raise Exception
    if context_auth != None and client_license_path != None:
        raise Exception

    if context_auth == None:
        context_auth = get_context_auth_from_client_license(client_license_path)    
    dict_request = fill_dict_request_from_context_auth(context_auth)
    
    _response = _response_requests_wrapper(context_auth, _api, dict_request=dict_request, _debug=_debug, use_post = True, use_json=False)

    return update_context_auth_from_response(context_auth, _response), _response


#TODO: check, return status_code?
def bevil_client_authentication_start(client_license_path, mac_address_optional, _debug=False):
    _api = 'api/v1/auth/start'
    context_auth_updated, _response = bevil_client_authentication_base(_api, None, client_license_path=client_license_path, mac_address_optional=mac_address_optional, _debug=_debug)
    return context_auth_updated

def bevil_client_authentication_status(context_auth, _debug=False):
    _api = 'api/v1/auth/status'
    context_auth_updated, _response = bevil_client_authentication_base(_api, context_auth, _debug=_debug)
    if _response != None and 'errCode' in _response and _response['errCode'] != JSON_ERRCODE_SUCCESS_SDK:
        context_auth_updated = None #TODO: check, refresh token case
        '''
        if 'access_token' in context_auth_updated:
            context_auth_updated.pop('access_token', None)
        if 'refresh_token' in context_auth_updated:
            context_auth_updated.pop('refresh_token', None)
        '''
    return context_auth_updated, _response

#TODO: check, return status_code?
def bevil_client_authentication_end(context_auth, _debug=False):
    _api = 'api/v1/auth/end'
    context_auth_updated, _response = bevil_client_authentication_base(_api, context_auth, _debug=_debug)
    return context_auth_updated, _response


#### COMMON ####
def file_out(t1, file_prefix, str_fileout, file_ext='csv'):
    str_fileout += u'\n'
    path_file_exception = u'%s_%s%s'%(t1.strftime('%Y%m%d%H%M%S'),file_prefix, '.%s'%(file_ext) if file_ext != None else '' )
    with open(path_file_exception,'a', encoding='utf-8') as f_except:
        f_except.write(str_fileout)
def dump_serializer(_serializer_data,_fields_out,file_prefix=None,_delimiter='\t'):
    import datetime
    t1 = datetime.datetime.utcnow()
    
    from collections import defaultdict
    dict_length = defaultdict(list)
    for _key in _fields_out:
        _str_key = str(_key)
        dict_length[_str_key].append(len(_str_key))
    for _log in _serializer_data:
        for _key in _fields_out:
            _str_val = ' '
            if _key in _log:
                _str_val = str(_log[_key])
            dict_length[str(_key)].append(len(_str_val))
    dict_fixed = {}
    for _key, _list in dict_length.items():
        dict_fixed[_key] = max(dict_length[_key])


    _str_out = ''
    _str_out_fixed = ''
    for _key in _fields_out:
        if bool(_str_out):
            _str_out += _delimiter
            _str_out_fixed += ' '
        _str_out += str(_key)
        _width = dict_fixed[_key]
        _str_out_fixed += f'{str(_key):<{_width}}'
    print(_str_out_fixed)
    if file_prefix != None:
        file_out(t1, file_prefix, _str_out)
    for _log in _serializer_data:
        _str_out = ''
        _str_out_fixed = ''
        for _key in _fields_out:
            if bool(_str_out):
                _str_out += _delimiter
                _str_out_fixed += ' '
            _str_val = ' '
            if _key in _log:
                _str_val = str(_log[_key])
            _str_out += _str_val
            
            _width = dict_fixed[_key]
            _str_out_fixed += f'{_str_val:<{_width}}'

        print(_str_out_fixed)    
        if file_prefix != None:
            file_out(t1, file_prefix, _str_out)

from netaddr import EUI
def str2eui(_mac):
    return EUI(_mac)
def eui2str(_eui):
    return str(_eui)
def pick_ip_linked(_mac_license, dict_address_to_af_inet_x):
    _mac_license_nomalized = eui2str(str2eui(_mac_license))
    list_ips = None
    for _mac, _list in dict_address_to_af_inet_x.items():
        _mac_normalized = eui2str(str2eui(_mac))
        if _mac_normalized != None and _mac_normalized.lower() == _mac_license_nomalized.lower():
            list_ips = _list
            break
    return list_ips
def get_mac_address_and_ip(_mac_license=None):
    import psutil
    from socket import AddressFamily
    from collections import defaultdict

    dict_address_to_af_inet = {}
    dict_address_to_af_inet6 = {}    
    # Iterate over all the keys in the dictionary

    for _interface in psutil.net_if_addrs():
        # Check if the interface has a valid MAC address

        dict_type_to_address = defaultdict(list)
        for _address in psutil.net_if_addrs()[_interface]:
            if _address.address:
                dict_type_to_address[_address.family].append(_address.address)
        if psutil.AF_LINK in dict_type_to_address:
            list_mac = dict_type_to_address[psutil.AF_LINK]
            for _mac in list_mac:
                for _key, _list in dict_type_to_address.items():
                    if _key == AddressFamily.AF_INET:
                        dict_address_to_af_inet.update({
                            _mac : _list
                        })
                    elif _key == AddressFamily.AF_INET6:
                        dict_address_to_af_inet6.update({
                            _mac : _list
                        })
    list_ips = None
    if _mac_license != None:
        if bool(dict_address_to_af_inet):
            list_ips = pick_ip_linked(_mac_license, dict_address_to_af_inet)
        if list_ips == None and bool(dict_address_to_af_inet6):
            list_ips = pick_ip_linked(_mac_license, dict_address_to_af_inet6)
        if list_ips == None:
            raise Exception("Matched MAC ADDRESS NOT FOUND")
    else:
        if bool(dict_address_to_af_inet):
            _mac_license = next(iter(dict_address_to_af_inet.keys()))
            list_ips = dict_address_to_af_inet[_mac_license]
        elif bool(dict_address_to_af_inet6):
            _mac_license = next(iter(dict_address_to_af_inet6.keys()))
            list_ips = dict_address_to_af_inet6[_mac_license]
        if list_ips == None:
            raise Exception("MAC ADDRESS NOT FOUND")
        
    return eui2str(str2eui(_mac_license)), list_ips[0]

