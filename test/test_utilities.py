#!/usr/bin/env python
u"""
test_utilities.py (12/2020)
Verify file utility functions
"""
import io
import gzip
import pytest
import posixpath
import timescale.utilities

def test_urlsplit():
    HOST = ['https://cddis.nasa.gov','archive','products','iers','deltat.data']
    url = posixpath.join(*HOST)
    TEST = timescale.utilities.url_split(url)
    assert (HOST == list(TEST))

def test_roman():
    for s,i in zip(['MMXVIII','MCMXVI','DXCIV'],[2018,1916,594]):
        TEST = timescale.utilities.roman_to_int(s)
        assert (TEST == i)

def test_even():
    for s,i in zip([2015,1916,591,99,10,3],[2014,1916,590,98,10,2]):
        TEST = timescale.utilities.even(s)
        assert (TEST == i)

def test_ceil():
    for s,i in zip([-2.5, 0.0, 2.5], [-2, 0, 3]):
        TEST = timescale.utilities.ceil(s)
        assert (TEST == i)

def test_token(username, password):
    # attempt to login to NASA Earthdata
    urs = 'urs.earthdata.nasa.gov'
    opener = timescale.utilities.attempt_login(urs,
        username=username,
        password=password,
        password_manager=False,
        get_ca_certs=False,
        redirect=False,
        authorization_header=True)
    # get data access token
    token = timescale.utilities.get_token(build=False)
    # get list of tokens
    token_list = timescale.utilities.list_tokens(build=False)
    # assert that token is in list of tokens
    access_tokens = [t['access_token'] for t in token_list]
    assert (token['access_token'] in access_tokens)
    # revoke the access token
    timescale.utilities.revoke_token(token['access_token'], build=False)
