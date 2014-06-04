#!/usr/bin/python

import pygal

line_chart = pygal.Line()
line_chart.title = 'Browser usage evolution (in %)'
line_chart.x_labels = map(str, range(2002, 2013))
line_chart.add('Firefox', [None, None, 0, {'value': 16.6, 'href':'https://pbs.twimg.com/profile_images/2605985080/gs0lbe62xbadoozj698t_bigger.jpeg'},   25,   31, {'value':36.4,'href':'https://pbs.twimg.com/profile_images/2605985080/gs0lbe62xbadoozj698t_bigger.jpeg'}, 45.5, 46.3, 42.8, 37.1])
line_chart.render_to_png('a.png')
