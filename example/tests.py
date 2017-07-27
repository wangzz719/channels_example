# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.

from example.models import IntegerValue

if __name__ == '__main__':
    integer_value = IntegerValue(name='int_1', value=1)
    integer_value.save()
