# -*- coding: utf-8 -*-
import builtwith
import whois
import json


def get_website_info(url):
    info = builtwith.parse(url)
    json_dicts = json.dumps(info, indent=4)
    whois_info = whois.whois(url)
    print('builtwith_info：', json_dicts)
    print('whois_info：', whois_info)


if __name__ == '__main__':
    url0 = 'http://www.porn87.com'
    get_website_info(url0)
