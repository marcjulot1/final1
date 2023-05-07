from api import url
import pytest
import requests


def test_api_can_connect():
    res = requests.get(url)
    assert res != None


def test_api_index():
    res = requests.get(url)
    assert res != None
