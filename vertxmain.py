#!/usr/bin/env python
# -*- coding: utf-8 -*-

import vertx

from frobnicate import handler

_log = vertx.logger()

_log.info("hello there")

server = vertx.create_http_server()
server.request_handler(handler)
server.listen(8080)
