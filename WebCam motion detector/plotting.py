from motion_detection import df
from bokeh.plotting import figure, show, output_file

plot = figure(x_axis_type = "datetime", height = 100, width = 500, responsive = True, title = "Motion Graph")

q = plot.quad(left = df["Start"], right = df["End"], bottom = 0 , top = 1, color = "green")

output_file("Graph.html")
show(plot)
