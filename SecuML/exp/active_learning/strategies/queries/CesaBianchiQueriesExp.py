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

from SecuML.core.active_learning.strategies.queries.CesaBianchiQueries \
        import CesaBianchiQueries
from SecuML.exp.active_learning.strategies.queries.QueryExp import QueryExp


class CesaBianchiQueriesExp(CesaBianchiQueries):

    def generateQuery(self, instance_id, predicted_proba,
                                suggested_label, suggested_family,
                                confidence=None):
        return QueryExp(instance_id, predicted_proba, suggested_label,
                        suggested_family, confidence=confidence)
