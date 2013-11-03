# -*- coding: utf-8 -*-

import upyun

# ------------------ CONFIG ---------------------
BUCKETNAME = 'herockpost'
USERNAME = 'herockpost'
PASSWORD = '7Ne-Qwg-NtU-5Uw'
# -----------------------------------------------

up = upyun.UpYun(BUCKETNAME, USERNAME, PASSWORD, timeout=30,
                     endpoint=upyun.ED_AUTO)

def upload(img_name):
    # up = upyun.UpYun(BUCKETNAME, USERNAME, PASSWORD, timeout=30,
    #                  endpoint=upyun.ED_AUTO)
    print "=================================================="
    print "Getting Started with UpYun Storage Service"
    print "==================================================\n"
    with open(img_name, 'rb') as f:
        up.put(img_name, f)
    print 'done.'
    print 'http://herockpost.b0.upaiyun.com/%s' %img_name


def list():
    res = up.getlist()
    print res


def delete(img_name):
    res = up.delete(img_name)
    print res
