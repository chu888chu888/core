#!/usr/local/bin/python2.7

"""
    Copyright (c) 2015 Deciso B.V. - Ad Schellevis
    All rights reserved.

    Redistribution and use in source and binary forms, with or without
    modification, are permitted provided that the following conditions are met:

    1. Redistributions of source code must retain the above copyright notice,
     this list of conditions and the following disclaimer.

    2. Redistributions in binary form must reproduce the above copyright
     notice, this list of conditions and the following disclaimer in the
     documentation and/or other materials provided with the distribution.

    THIS SOFTWARE IS PROVIDED ``AS IS'' AND ANY EXPRESS OR IMPLIED WARRANTIES,
    INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY
    AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
    AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY,
    OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
    SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
    INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
    CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
    ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
    POSSIBILITY OF SUCH DAMAGE.

    --------------------------------------------------------------------------------------
    update captive portal statistics
"""
import sys
import ujson
from lib.db import DB
from lib.arp import ARP
from lib.ipfw import IPFW

db = DB()
cur = db._connection.cursor();

# update accounting
ipfw = IPFW()
#print ipfw.list_accounting_info()
db.update_accounting_info(ipfw.list_accounting_info())

# tmp = """
# create table session_info (
#       zoneid int
# ,     sessionid varchar
# ,     prev_packets_in integer
# ,     prev_bytes_in   integer
# ,     prev_packets_out integer
# ,     prev_bytes_out   integer
# ,     packets_in integer default (0)
# ,     packets_out integer default (0)
# ,     bytes_in integer default (0)
# ,     bytes_out integer default (0)
# ,     last_accessed integer
# ,     primary key (zoneid, sessionid)
# );
#  """

# cur.execute("drop table session_info");
# cur.execute(tmp);