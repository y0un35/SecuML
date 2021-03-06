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

from .Iteration import Iteration
from .Iteration import NoAnnotationAdded
from .Iteration import NoUnlabeledDataLeft


class ActiveLearning(object):

    def __init__(self, conf, datasets):
        self.conf = conf
        self.datasets = datasets
        self.budget = self.conf.budget
        self.iteration_number = 1
        self.current_budget = self.budget
        self.prev_iter = None
        self.curr_iter = None

    def runIterations(self, output_dir=None):
        while True:
            try:
                self.runNextIteration(output_dir)
            except (NoAnnotationAdded, NoUnlabeledDataLeft) as e:
                self.conf.logger.info(e)
                break

    def runNextIteration(self, output_dir=None):
        self.curr_iter = Iteration(self.conf,
                                   self.iteration_number,
                                   datasets=self.datasets,
                                   prev_iter=self.prev_iter,
                                   budget=self.current_budget)
        self.current_budget = self.curr_iter.runIteration()
        self.iteration_number += 1
        self.curr_iter.prev_iter = None
        self.prev_iter = self.curr_iter
