from motion_detection import df #from cv2 import
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource
df["Start_string"]=df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S") # Formatting the Start datetime as a string to a new column
df["End_string"]=df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")  # Formatting the end datetime as a string to a new column
cds=ColumnDataSource(df)
p=figure(x_axis_type='datetime', height=100, width=500, sizing_mode="scale_both", title="Motion Graph")#create the fig obj
p.yaxis.minor_tick_line_color=None
p.yaxis[0].ticker.desired_num_ticks=1
hover=HoverTool(tooltips=[("Start","@Start_string"),("End","@End_string")])
p.add_tools(hover)
q=p.quad(left="Start", right="End",bottom=0, top=1, color="green",source=cds)#visualize date and time along xaxis to left,right,bottom,top
output_file("Graph.html")
show(p)