# SecuML
# Copyright (C) 2016-2018  ANSSI
#
# SecuML is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# SecuML is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with SecuML. If not, see <http://www.gnu.org/licenses/>.

MALICIOUS = 'malicious'
BENIGN = 'benign'


def labelBooleanToString(label):
    if label is None:
        return None
    elif label:
        return MALICIOUS
    else:
        return BENIGN


def labelStringToBoolean(label):
    if label is None:
        return None
    return label == MALICIOUS
