#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Scott Burns <scott.s.burns@gmail.com>'
__license__ = 'BSD 3-Clause'


import os

from pdb import set_trace
import projects

#  This maps grants/tasks to the correct parser
TASKS = ('MI', 'SWR', 'PIC', 'REP', 'MR', 'FIG', 'MI', 'OLSON', 'SENT')
PROJECT_CLASS = {'NF': projects.NF, 'NFB': projects.NFB}

#  Fully implemented grants: THESE MUST BE IN THE ABOVE TWO DICTS PROJECT_CLASS
GRANTS = ('NF', 'NFB')


def upload_key(info):
    fields = ('grant', 'task', 'id', 'visit', 'list')
    good_fields = [f for f in fields if f in info]
    fname = '_'.join([info.get(f) for f in good_fields]) + '.txt'
    proj = class_from_projstr(info['grant'])(fname, None, database=info['database'])
    return proj.upload_key()

def class_from_projstr(proj_str):
    return PROJECT_CLASS[proj_str]

def parse_file(fname, fobj):
    bname = os.path.basename(fname)
    name, ext = os.path.splitext(bname)
    #  PROJECT_BLAHBLAHBLAH
    project = name.split('_')[0]
    proj_class = class_from_projstr(project)
    parser_object = proj_class(fname, fobj)

    #  Parse the file and write out a copy
    to_redcap = parser_object.parse()

    return to_redcap

