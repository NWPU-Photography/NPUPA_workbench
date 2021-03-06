#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
* Project Name : NPUPA_workbench
* File Name    : format_string.py
* Description  : String formatter
* Create Time  : 2020-05-14 11:45:00
* Version      : 1.0
* Author       : Steve X
* GitHub       : https://github.com/Steve-Xyh
'''


import datetime
import colorama

colorama.init(autoreset=True)


def format_dict_en(dic):
    '''
    格式化英文key多行dict

    Parameters::
        dic: dict - log dict(e.g. {name: value})
    Returns::
        res: str - formatted string
    '''
    form_len = 40

    res = '-' * form_len + '\n'
    for key in dic:
        flg = dic[key] is not None
        res += str(key).ljust(20)
        res += (str(dic[key]) if flg else '').ljust(20) + '\n'
    res += '-' * form_len
    return res


def format_dict_cn(dic: dict):
    '''
    格式化中文key多行dict

    Parameters::
        dic: dict - log dict(e.g. {name: value})

    Returns::
        res: str - formatted string
    '''
    form_len = 40

    res = '-' * form_len + '\n'
    for key in dic:
        flg = dic[key] is not None
        res += str(key).ljust(12, chr(12288))
        res += (str(dic[key]) if flg else '').ljust(20, chr(12288)) + '\n'
    res += '-' * form_len
    return res


def log_line_cn(dic: dict):
    '''
    中文key单行log

    Parameters::
        dic: dict - log dict(e.g. {name: value})

    Returns::
        res: str - formatted string
    '''

    for key in dic:
        flg = dic[key] is not None
        res = str(key).ljust(12, chr(12288))
        res += (set_color(dic[key], color='yellowFore')
                if flg else '').ljust(20, chr(12288)) + '\n'
    print(res)
    return res


def log_line_en(dic: dict):
    '''
    英文key单行log

    Parameters::
        dic: dict - log dict(e.g. {name: value})

    Returns::
        res: str - formatted string
    '''

    for key in dic:
        flg = dic[key] is not None
        res = str(key).ljust(12, chr(12288))
        res += (set_color(dic[key], color='yellowFore')
                if flg else '').ljust(20) + '\n'
    print(res)
    return res


def log_cn(dic: dict):
    '''
    中文key多行log

    Parameters::
        dic: dict - log dict(e.g. {name: value})

    Returns::
        res: str - formatted string
    '''
    form_len = 40

    res = '-' * form_len + '\n'
    res += '[' + set_color(datetime.datetime.now().strftime(
        '%Y-%m-%d %H:%M:%S'), color='greenFore') + ']\n'
    for key in dic:
        flg = dic[key] is not None
        res += str(key).ljust(12, chr(12288))
        res += (set_color(dic[key], color='yellowFore')
                if flg else '').ljust(20, chr(12288)) + '\n'
    res += '-' * form_len
    print(res)
    return res


def log_en(dic):
    '''
    英文key多行log

    Parameters::
        dic: dict - log dict(e.g. {name: value})
    Returns::
        res: str - formatted string
    '''
    form_len = 40

    res = '-' * form_len + '\n'
    res += '[' + set_color(datetime.datetime.now().strftime(
        '%Y-%m-%d %H:%M:%S'), color='greenFore') + ']\n'
    for key in dic:
        flg = dic[key] is not None
        res += str(key).ljust(20)
        res += (set_color(dic[key], color='yellowFore')
                if flg else '').ljust(20) + '\n'
    res += '-' * form_len
    print(res)
    return res


def err_en(dic: dict):
    '''
    英文key单行err

    Parameters::
        dic: dict - log dict(e.g. {name: value})

    Returns::
        res: str - formatted string
    '''

    for key in dic:
        flg = dic[key] is not None
        res = set_color(str(key), color='redBack').ljust(40)
        res += (set_color(dic[key], color='redFore')if flg else '').ljust(20)
    print(res)
    return res


def err_cn(dic: dict):
    '''
    中文key单行err

    Parameters::
        dic: dict - log dict(e.g. {name: value})

    Returns::
        res: str - formatted string
    '''

    for key in dic:
        flg = dic[key] is not None
        res = set_color(str(key), color='redBack').ljust(40, chr(12288))
        res += (set_color(dic[key], color='redFore')
                if flg else '').ljust(20, chr(12288))
    print(res)
    return res


def set_color(string, color):
    '''设置颜色'''
    convert_color = {
        'redFore': colorama.Fore.RED + colorama.Back.RESET,
        'redBack': colorama.Fore.WHITE + colorama.Back.RED,

        'greenFore': colorama.Fore.GREEN + colorama.Back.RESET,
        'greenBack': colorama.Fore.BLACK + colorama.Back.GREEN,

        'yellowFore': colorama.Fore.YELLOW + colorama.Back.RESET,
    }

    return colorama.Style.BRIGHT + convert_color[color] + string + colorama.Style.RESET_ALL


if __name__ == "__main__":
    str_a = set_color('This is red.', 'redFore')
    print(str_a)
