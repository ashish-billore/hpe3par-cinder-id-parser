#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#

"""
Cinder Volume ID to HPE3PAR Virtual Volume Name converter utility. Can be used
used as standalone tool for debugging between Cinder and HPE3PAR Volume Driver.
"""

import uuid
import base64
from sys import version_info

py3 = version_info[0] > 2

usage_msg = 'This tool converts Cinder Volume ID (#cinder list) to HPE3PAR' \
            'Virtual Volume Name (#showvv).'
prompt_msg = 'Enter Cinder Volume ID: '

result_msg = 'Mapping HPE3PAR Virtual Volume Name: '

print usage_msg

if py3:
    usr_input = input(prompt_msg)
else:
    usr_input = raw_input(prompt_msg)


def convert_cinder2hpe3par_vvol(name):

    """
    Utility to convert Cinder volume ID to corresponding mapping HPE3PAR
    Virtual Volume Name.

    :param name: Cinder volume ID (as seen on executing #cinder list command
    under "ID" column.

    :return: Corresponding Virtual Volume Name as seen in HPE3PAR Backend (as
    seen on executing #showvv command under "Name" column.
    """
    try:
        uuid_str = name.replace("-", "")
        vol_uuid = uuid.UUID('urn:uuid:%s' % uuid_str)
        vol_uuid = vol_uuid.bytes
        encoded = base64.b64encode(vol_uuid)
        vol_encoded = encoded.decode('ascii')

        # 3par doesn't allow +, nor /
        vol_encoded = vol_encoded.replace('+', '.')
        vol_encoded = vol_encoded.replace('/', '-')
        # strip off the == as 3par doesn't like those.
        vol_encoded = vol_encoded.replace('=', '')

        print result_msg + "osv-" + vol_encoded
    except Exception:
        print 'Please check the input: ' + usr_input + ' and try again!'

convert_cinder2hpe3par_vvol(usr_input)
