# -*- coding: utf-8 -*-

import upyun

# ------------------ CONFIG ---------------------
BUCKETNAME = 'herockpost'
USERNAME = 'herockpost'
PASSWORD = '7Ne-Qwg-NtU-5Uw'
# -----------------------------------------------

up = upyun.UpYun(BUCKETNAME, USERNAME, PASSWORD, timeout=30,
                     endpoint=upyun.ED_AUTO)

def upload(filename):
    # up = upyun.UpYun(BUCKETNAME, USERNAME, PASSWORD, timeout=30,
    #                  endpoint=upyun.ED_AUTO)
    print "=================================================="
    print "Getting Started with UpYun Storage Service"
    print "==================================================\n"
    with open(filename, 'rb') as f:
        up.put(filename, f)
    print 'done.'
    print 'http://herockpost.b0.upaiyun.com/%s' %filename


def list():
    res = up.getlist()
    print res


def delete(filename):
    res = up.delete(filename)
    print res
