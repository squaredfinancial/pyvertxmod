#!/usr/bin/env python
# -*- coding: utf-8 -*-

def handler(request):
    request.response.put_header('Content-Type', 'text/plain')
    request.response.end("Hello, World!")
