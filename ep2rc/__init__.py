#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Scott Burns <scott.s.burns@gmail.com>'
__license__ = 'BSD 3-Clause'
__version__ = '0.5.2'

import os
from os import path

from core import parse_file
from rc import upload
from errors import BadDataError


def parse_and_upload(fname, database, do_upload=True):
    msg = ''
    try:
        to_redcap = {}
        with open(fname) as f:
            to_redcap = parse_file(fname, f)
    except BadDataError as e:
        msg = "(%s)" % e + " Failed with %s" % fname
    suc = False
    if to_redcap and do_upload:
        suc = upload(to_redcap, database)
    if suc:
        msg = "Success with %s" % fname
    print msg
    return to_redcap, suc


def switchboard_fxn(**kwargs):
    """For the time being, this is going to pull the file from
    "sentcomp_file" in the RCV redcap and upload it back there"""
    from redcap import Project
    from secret import TOKENS, URL
    project = Project(URL, TOKENS['RC'])
    record = kwargs['record']
    behav_id = record.split('_', 1)[0]
    dir_to_write = path.join('/',
                        'fs0',
                        'New_Server',
                        'RCV',
                        'Out_Behavioral',
                        'RC_%s' % behav_id,
                        'RC_%s_E-Prime' % behav_id)
    if not path.isdir(dir_to_write):
        os.makedirs(dir_to_write, mode=0770)
    content, headers = project.export_file(record=record, field='sentcomp_file')
    fullfile = path.join(dir_to_write, headers['name'])
    with open(fullfile, 'w') as f:
        f.write(content)
    print "ep2rc.switchboard_fxn: Running parse_and_upload on %s" % fullfile
    to_redcap, success = parse_and_upload(fullfile, 'rc')
    if not success:
        print "ep2rc.switchboard_fxn: Failed uploading results for %s" % record
