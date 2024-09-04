import matplotlib.pyplot as plt
    # Sample data for the x-axis (horizontal axis) and y-axis (vertical axis)
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create a new figure and axis
plt.figure()

# Plot the data using a line plot
plt.plot(x, y, marker='o', linestyle='-')

# Add labels to the axes and a title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Plot')

# Display the plot
plt.show()
import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Simple Graph')
plt.show()


#Customization of Plots:
import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')

#The axis() function is used to customize the axis range. 
#The arguments provided [0, 6, 0, 20] represent [xmin, xmax, ymin, ymax], 
#setting the minimum and maximum values for the x-axis and y-axis, respectively.
plt.axis([0, 6, 0, 20]) 
plt.show()



import matplotlib.pyplot as plt 
  
# x axis values 
x = [1,2,3,4,5,6] 
# corresponding y axis values 
y = [2,4,1,5,2,6] 
  
# plotting the points  
plt.plot(x, y, color='green', linestyle='dashed', linewidth = 3, 
         marker='o', markerfacecolor='blue', markersize=12) 
  
# setting x and y axis range 
plt.ylim(1,8) 
plt.xlim(1,8) 
  
# naming the x axis 
plt.xlabel('x - axis')
# naming the y axis 
plt.ylabel('y - axis') 
  
# giving a title to my graph 
plt.title('Some cool customizations!') 
  
# function to show the plot 
plt.show() 


#Creating Scatter Plots
import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

plt.scatter(x, y)
plt.show()


#Comparing Plots
import matplotlib.pyplot as plt
import numpy as np

x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])
plt.scatter(x, y)

x = np.array([2, 2, 8, 1, 15, 8, 12, 9, 7, 3, 11, 4, 7, 14, 12])
y = np.array([100, 105, 84, 105, 90, 99, 90, 95, 94, 100, 79, 112, 91, 80, 85])
plt.scatter(x, y)

plt.show()

#Scatter Plot
import matplotlib.pyplot as plt
  
# x-axis values 
x = [1,2,3,4,5,6,7,8,9,10] 
# y-axis values 
y = [2,4,5,7,6,8,9,11,12,12] 
  
# plotting points as a scatter plot 
plt.scatter(x, y, label= "stars", color="green", marker="*", s=30) 
  
# x-axis label 
plt.xlabel('x - axis') 
# frequency label 
plt.ylabel('y - axis') 
# plot title 
plt.title('My scatter plot!') 
# showing legend 
plt.legend() 
  
# function to show the plot 
plt.show() 


#Pie Chart
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])

plt.pie(y)
plt.show() 

#As you can see the pie chart draws one piece (called a wedge) for each 
#value in the array (in this case [35, 25, 25, 15]).
#By default the plotting of the first wedge starts from the x-axis and move counterclockwise:


'''Labels

Add labels to the pie chart with the label parameter.
The label parameter must be an array with one label for each wedge:
            
Start Angle
            
The default start angle is at the x-axis, but you can change the start angle by 
specifying a startangle parameter.
The startangle parameter is defined with an angle in degrees, default angle is 0

Explode

The explode parameter, if specified, and not None, must be an array with one value for each wedge.
Each value represents how far from the center each wedge is displayed

Shadow
Add a shadow to the pie chart by setting the shadows parameter to True 

Colors
You can set the color of each wedge with the colors parameter.
The colors parameter, if specified, must be an array with one value for each wedge


You can use Hexadecimal color values, any of the 140 supported color names, or one of these shortcuts:
'r' - Red
'g' - Green
'b' - Blue
'c' - Cyan
'm' - Magenta
'y' - Yellow
'k' - Black
'w' - White

Legend
To add a list of explanation for each wedge, use the legend() function 


Legend With Header
To add a header to the legend, add the title parameter to the legend function. 
'''
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Eat", "Sleep", "Work", "Play"]
mycolors = ["black", "hotpink", "b", "#4CAF50"]

plt.pie(y, labels = mylabels, startangle = 90,colors=mycolors)
#plt.legend()
plt.legend(title = "Activities:")
plt.show() 


#Box Plot
'''# Box Plot 

A Box Plot is also known as Whisker plot is created to display the summary of the set of data values having properties like minimum, first quartile, median, third quartile and maximum. In the box plot, a box is created from the first quartile to the third quartile, a vertical line is also there which goes through the box at the median. Here x-axis denotes the data to be plotted while the y-axis shows the frequency distribution.

Syntax: 
matplotlib.pyplot.boxplot(data, notch=None, vert=None, patch_artist=None, widths=None)
'''
import matplotlib.pyplot as plt

# Sample data for the box plot
data = [10, 20, 25, 30, 35, 40, 45, 50, 55, 60, 70, 75]
# Create the box plot
plt.boxplot(data)
plt.show()



# Import libraries
import matplotlib.pyplot as plt
import numpy as np
# Creating dataset
np.random.seed(10)
data = np.random.normal(100, 20, 200)
fig = plt.figure(figsize =(10, 7))
# Creating plot
plt.boxplot(data)
# show plot
plt.show()


#Matplot Grid
import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)

plt.grid()

plt.show()


#Display only grid lines for the x-axis:
import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)

plt.grid(axis='x')  # Only show gridlines along the x-axis

plt.show()



import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)

plt.grid(color='green', linestyle='--', linewidth=0.5)

plt.show()


## Display images using matplotlib

'''The image module in matplotlib library is used for working with images in Python.
The image module also includes two useful methods which are imread which is used to 
read images and imshow which is used to display the image.'''

# importing required libraries
import matplotlib.pyplot as plt
import matplotlib.image as img
  
# reading the image
testImage = img.imread('KMIT Logo.png')
  
# displaying the image
plt.imshow(testImage)


# Create a Table with Matplotlib
'''Matplotlib Table in Python is a particular function that allows you to plot a table.
By using matplotlib.pyplot.table(), we can add a table to Axes. 
This table is then plotted with columns as an x-axis and values as the y-axis. 

Syntax of Matplotlib Table:

matplotlib.pyplot.table(cellText=None, cellColours=None, cellLoc='right', colWidths=None, rowLabels=None, rowColours=None, rowLoc='left', colLabels=None, colColours=None, colLoc='center', loc='bottom', bbox=None, edges='closed', **kwargs) 

Parameters:

cellText: The texts to place into the table cells.
cellColours: The background colors of the cells.
cellLoc: The alignment of the text within the cells. (default: ‘right’)
colWidths (optional): The column widths in units of the axes.
rowLabels (optional): The text of the row header cells.
rowColours (optional): The colors of the row header cells.
rowLoc (optional): The text alignment of the row header cells. (default: ‘left’)
colLabels (optional): The text of the column header cells.
colColours (optional): The colors of the column header cells.
colLoc (optional): The text alignment of the column header cells.(default: ‘left’)
Loc (optional): This parameter is the position of the cell with respect to ax.
bbox (optional): This parameter is the bounding box to draw the table into.
edges (optional): This parameter is the cell edges to be drawn with a line.
**kwargs: Used to control table properties.
'''


import matplotlib.pyplot as plt

val1 = ["{:X}".format(i) for i in range(10)]
val2 = ["{:02X}".format(10 * i) for i in range(10)]
val3 = [["" for c in range(10)] for r in range(10)]

fig, ax = plt.subplots()
ax.set_axis_off()
table = ax.table(
    cellText=val3,
    rowLabels=val2,
    colLabels=val1,
    rowColours=["palegreen"] * 10,
    colColours=["palegreen"] * 10,
    cellLoc='center',
    loc='upper left'
)

ax.set_title('matplotlib.axes.Axes.table() function Example', fontweight="bold")

plt.show()


## Matplotlib Table Example As Line Graph
import numpy as np
import matplotlib.pyplot as plt
 
data = [[ 100, 100,  99, 95],
        [ 66, 71,  76,  82],
        [ 73,  75, 79, 81],
        [ 17,  23, 42, 55],
        [ 12, 18, 26, 20]]
 
columns = ('2010', '2012', '2014', '2016')
rows = ("Make Calls", "Take Photos", "Texting", "Internet", "Playing games")[::-1]
 
values = np.arange(0, 10, 1)
value_increment = 10
 
# Get some pastel shades for the colors
colors = plt.cm.BuPu(np.linspace(0, 0.5, len(rows)))
colors = colors[::-1]
index = np.arange(len(columns)) + 0.3
bar_width = 0.4
n_rows = len(data)
 
for row in range(n_rows):
    plt.bar(index, data[row], bar_width, color=colors[row], label=rows[row])
    index += bar_width
    
    #plt.plot(index, data[row], bar_width, color=colors[row], label=rows[row])
    #index += bar_width
 
plt.table(cellText=data, rowLabels=rows, rowColours=colors, colLabels=columns, loc='bottom')
 
plt.subplots_adjust(left=0.2, bottom=0.25)
plt.ylabel("Usage of mobile phones in ${0}'s".format(value_increment))
plt.yticks(values * value_increment, ['%d' % val for val in values])
plt.xticks([])
plt.title('Using Mobile Phones')
 
plt.legend()
plt.show()


# Matplotlib.pyplot.plot_date ()

'''The `matplotlib.pyplot.plot_date()` function is used to create a line plot with dates on the x-axis. This function is particularly useful when you have time series data and you want to visualize it as a line plot.

Syntax:
matplotlib.pyplot.plot_date(x, y, fmt=’o’, tz=None, xdate=True, ydate=False,  data=None, **kwargs)

parameters

Here's an explanation of each parameter in the function signature:

- `x`: This parameter represents the data for the x-axis, which are typically dates. It should be an array-like sequence of dates or datetimes.

- `y`: This parameter represents the data for the y-axis, which are the corresponding values associated with the dates in the `x` parameter. It should be an array-like sequence of numerical values.

- `fmt`: This is an optional parameter that specifies the format of the markers or lines used in the plot. It uses the same format strings as the `matplotlib.pyplot.plot()` function. The default value is `'o'`, which means circles as markers.

- `tz`: This optional parameter is used to specify the time zone for the x-axis data. It's useful when working with time zones.

- `xdate`: This optional boolean parameter specifies whether the x-axis should display dates. If set to `True`, the x-axis will display dates, and if set to `False`, it will display numerical values.

- `ydate`: This optional boolean parameter specifies whether the y-axis should display dates. If set to `True`, the y-axis will display dates, and if set to `False`, it will display numerical values. It's typically used when you have both x and y axes as dates.

- `data`: This optional parameter is used to provide a data source, typically a pandas DataFrame or a structured numpy array. This allows you to specify the data using column names rather than individual arrays for `x` and `y`.

- `**kwargs`: This parameter allows you to pass additional keyword arguments that are passed to the underlying `Line2D` objects created by the plot. You can use this to customize various aspects of the plot, such as colors, linewidths, and labels.

In summary, `matplotlib.pyplot.plot_date()` is a function for creating date-oriented line plots. You provide dates for the x-axis, associated numerical values for the y-axis, and you can customize the appearance of the plot using optional parameters and keyword arguments.
'''

# importing libraries
import matplotlib.pyplot as plt
from datetime import datetime

# creating array of dates for x axis
dates = [
    datetime(2020, 6, 30),
    datetime(2020, 7, 22),
    datetime(2020, 8, 3),
    datetime(2020, 9, 14)
]

# for y axis
x = [0, 1, 2, 3]

plt.plot_date(dates, x, 'g')
plt.xticks(rotation=70)
plt.show()


## Plotting polar curves
'''Plotting polar curves involves creating plots using polar coordinates instead of Cartesian coordinates. Matplotlib provides a way to create polar plots using the polar() function. Here's the syntax and an example code for plotting polar curves:

Syntax :
matplotlib.pyplot.polar(theta, r, **kwargs)

This function allows you to create a plot using polar coordinates instead of the usual Cartesian coordinates. Here's an explanation of the parameters in this syntax:

- `theta`: This parameter represents an array of angles in radians. It specifies the angular positions at which the data points should be plotted. The angles are measured in a counterclockwise direction from the reference direction (usually the positive x-axis).

- `r`: This parameter represents an array of corresponding radial distances. It specifies how far each data point should be from the origin (center) of the polar plot.

- `**kwargs`: This parameter allows you to pass additional keyword arguments that customize the appearance of the polar plot. These keyword arguments are similar to the ones used in regular Matplotlib plot functions.

Here are some common keyword arguments that you can use with `plt.polar()`:

- `color`: Specifies the color of the plotted data points or lines.
- `linestyle`: Specifies the line style used for connecting data points.
- `marker`: Specifies the marker style for the data points.
- `label`: Specifies the label for the plot, which can be used in legends.
- `linewidth`: Specifies the width of the lines connecting the data points.
- `markersize`: Specifies the size of the markers.
- `alpha`: Specifies the transparency of the plot (between 0 and 1).

Here's an example of using `plt.polar()` to create a simple polar plot:
'''
import matplotlib.pyplot as plt
import numpy as np

theta = np.linspace(0, 2 * np.pi, 100)  # Array of angles
r = 2 + 3 * theta  # Array of radial distances

plt.polar(theta, r, color='blue', linestyle='-', linewidth=2, label='Polar Curve')
plt.legend()  # Show legend
plt.title('Polar Plot Example')
plt.show()


