# -*- coding:utf-8 -*-


from __future__ import absolute_import

from celery1 import app


@app.task
def add(x, y):
    return x + y