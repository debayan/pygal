# -*- coding: utf-8 -*-
# This file is part of pygal
#
# A python svg graph plotting library
# Copyright © 2012-2014 Kozea
#
# This library is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# This library is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with pygal. If not, see <http://www.gnu.org/licenses/>.
from pygal import Bar

class ChangeBarsXMLFilter(object):
    def __init__(self, a, b):
        self.data = [b[i] - a[i] for i in range(len(a))]

    def __call__(self, T):
        subplot = Bar(legend_at_bottom=True, explicit_size=True, width=800, height=150)
        subplot.add("Difference", self.data)
        subplot = subplot.render_tree()
        subplot = subplot.xpath("g")[0]
        T.insert(2, subplot)
        T.xpath("g")[1].set('transform', 'translate(0,150), scale(1,0.75)')
        return T

def test_xml_filters_round_trip():
    plot = Bar()
    plot.add("A", [60, 75, 80, 78, 83, 90])
    plot.add("B", [92, 87, 81, 73, 68, 55])
    before = plot.render()
    plot.add_xml_filter(lambda T: T)
    after = plot.render()
    assert before == after

def test_xml_filters_change_bars():
    plot = Bar(legend_at_bottom=True, explicit_size=True, width=800, height=600)
    A = [60, 75, 80, 78, 83, 90]
    B = [92, 87, 81, 73, 68, 55]
    plot.add("A", A)
    plot.add("B", B)
    plot.add_xml_filter(ChangeBarsXMLFilter(A,B))
    q = plot.render_tree()
    assert len(q.xpath("g")) == 2
    assert q.xpath("g")[1].attrib["transform"] == "translate(0,150), scale(1,0.75)"
