"""
Deis API exception classes.
"""

from __future__ import unicode_literals

from rest_framework.exceptions import APIException
from rest_framework import status


class AbstractDeisException(APIException):
    """
    Abstract class in which all Deis Exceptions and Errors should extend.

    This exception is subclassed from rest_framework's APIException so that
    subclasses can change the status code to something different than
    "500 SERVER ERROR."
    """

    def __init__(self, detail=None):
        self.detail = detail

    class Meta:
        abstract = True
