
import pytest

from bigledger.akaun_sdk.skeleton import fib, main
from bigledger.akaun_sdk.hello_world import main as akn_main
from bigledger.google_lib.hello_world import main as g_main


__author__ = "Vincent Lee"
__copyright__ = "Vincent Lee"
__license__ = "MIT"


def test_google():
    """API Tests"""
    g_main

def test_akn():
    akn_main
