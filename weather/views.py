#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
---------------------------------------------
* Project Name : NPUPA_workbench
* File Name    : views.py
* Description  : Django views
* Create Time  : 2020-06-20 16:12:20
* Version      : 1.0
* Author       : Steve X
* GitHub       : https://github.com/Steve-Xyh
---------------------------------------------
'''

import beeprint
from django.shortcuts import render
from weather.api.get_info import get_info

# Create your views here.


def base(request):
    '''Render base template'''

    return render(request, 'weather/base.html')


def get_request_ip(request):
    '''Get IP address of request'''

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip_addr = x_forwarded_for.split(',')[0]  # 所以这里是真实的ip
    else:
        ip_addr = request.META.get('REMOTE_ADDR')  # 这里获得代理ip

    return ip_addr


def home(request):
    '''Render home page'''

    ip_addr = get_request_ip(request)
    req_location = '西安市' if ip_addr == '127.0.0.1' else ip_addr

    res = get_info(ip_addr=req_location)
    weather_dic = res[0]
    astro_dic = res[1]
    beeprint.pp(res)
    beeprint.pp(ip_addr)


    weather_now = weather_dic['res_dict']['now']
    weather_code = weather_now['cond_code']
    weather_icon = weather_code + '.png'

    content = {
        'ip': ip_addr,
        'location': weather_dic['city'],
        'admin_area': weather_dic['admin_area'],
        'latitude': weather_dic['lat_str'],
        'longitude': weather_dic['lon_str'],

        'weather_code': weather_code,
        'weather_icon': f'/static/weather/icons/weather_icon/{ weather_icon }',
        'weather_cond': weather_dic['res_dict']['now']['cond_txt'],
        'weather_temp':weather_now['tmp'],
    }

    beeprint.pp(content)
    return render(request, 'weather/home.html', content)
