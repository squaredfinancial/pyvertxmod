#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup, Command
from distutils.command.sdist import sdist
from zipfile import ZipFile, ZIP_STORED


class vertx_mod(sdist):
    description = "build a vertx-platform module archive",

    def zip_dir_munge(self, old, new):
        "add some directory/ entries that vertx's unzipper prefers"
        o = ZipFile(old, 'r')
        orig_contents = o.namelist()
        dirs = {}
        for entry in orig_contents:
            components = entry.split("/")[:-1]
            for i in range(0, len(components)):
                path = "/".join(components[0:i+1]) + "/"
                dirs[path] = path

        n = ZipFile(new, 'w')
        # order them, even
        for d in sorted(dirs.keys()):
                n.writestr(d, '', ZIP_STORED)
        for entry in orig_contents:
            n.writestr(o.getinfo(entry), o.read(entry)) # sluurp

        o.close()
        n.close()

    # bodge: just skip the normal leading directory.
    def make_archive(self, base_name, format,
                     root_dir=None, base_dir=None,
                     owner=None, group=None):
        root_dir = base_dir
        base_dir = None
        sdist.make_archive(self, base_name + "-orig", "zip",
                           root_dir=root_dir, base_dir=base_dir,
                           owner=owner, group=group)
        # bodge^2: add vertx-expected directory entries.
        self.zip_dir_munge(base_name + "-orig.zip", base_name + "-mod.zip")

    # alternative manifest
    def finalize_options(self):
        if self.manifest is None:
            self.manifest = "MANIFEST.vertx"
        if self.template is None:
            self.template = "MANIFEST.in.vertx"

        self.ensure_string_list('formats')
        if self.formats is None:
            self.format = ["zip"]

        return sdist.finalize_options(self)


setup(
    name="pyvertxmod",
    version="1.0.0",
    description="example of python distutils building a vertx module",
    packages=['frobnicate'],
    author='Squared Financial',
    author_email='it@squaredfinancial.com',
    url="http://squaredfinancial.com",
    classifiers = [
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: Public Domain",
        "Programming Language :: Python",
        "Natural Language :: English",
        ],
    cmdclass= {
        'vertx_mod': vertx_mod,
    }
)
