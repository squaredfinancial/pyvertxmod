Stupid example that uses setup.py (distutils) to build a (tiny, useless)
vertx module, rather than involving gradle or maven.

A proper vertx_mod Command implementation could do something cleaner and more
sophisticated than just subclassing sdist, this was just a proof-of-concept.

python setup.py vertx_mod
vertx runzip dist/pyvertxmod-1.0.0.zip


