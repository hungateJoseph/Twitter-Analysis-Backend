import graphlib as plt


def multiple_line_plots(x_values, y_values):
    """
    :param x_values: a list of lists with each element corresponding to the x_values for a dataset. Note that
    x_values[0] corresponds to y_values[0].
    :param y_values: a list of lists with each element corresponding to the y_values for a dataset.
    :return: N/A. Plots line graph(s) corresponding to the given data.
    """
    i = 0
    for x, y in zip(x_values, y_values):
       i += 1
       plt.plot(x, y, label="line " + str(i))
        
    plt.legend()
    plt.show()

def multiple_bar_plots(data):
    """
    :param x_values: a list of lists with each element corresponding to the x_values for a dataset. Note that
    x_values[0] corresponds to y_values[0].
    :param y_values: a list of lists with each element corresponding to the y_values for a dataset.
    :return: N/A. Plots bar graph(s) corresponding to the given data.
    """

    x_axis_vals = []
    y_axis_vals = []

    for pair in data:
        x_axis_vals.append(pair[0])
        y_axis_vals.append(pair[1])
