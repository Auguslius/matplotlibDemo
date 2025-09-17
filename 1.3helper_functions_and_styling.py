import numpy as np
import matplotlib.pyplot as plt


def my_plotter(ax, data1, data2, param_dict):
    """
    A helper function to make a graph.
    """
    out = ax.plot(data1, data2, **param_dict)
    return out


def demo_helper_on_two_subplots():
    """在两个子图上重复使用 my_plotter。"""
    data1, data2, data3, data4 = np.random.randn(4, 100)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(5, 2.7))
    my_plotter(ax1, data1, data2, {'marker': 'x'})
    my_plotter(ax2, data3, data4, {'marker': 'o'})
    fig.suptitle('my_plotter on two subplots')
    return fig


def demo_styling_artists():
    """样式设置：颜色、线宽、线型，及通过 setter 修改。"""
    rng = np.random.default_rng(0)
    data1, data2 = rng.normal(size=(2, 100))
    x = np.arange(len(data1))

    fig, ax = plt.subplots(figsize=(5, 2.7))
    ax.plot(x, np.cumsum(data1), color='blue', linewidth=3, linestyle='--')
    l, = ax.plot(x, np.cumsum(data2), color='orange', linewidth=2)
    l.set_linestyle(':')
    ax.set_title('Styling Artists')
    ax.grid(True, alpha=0.3)
    return fig


def demo_colors_scatter():
    """颜色散点：面色与边色。"""
    rng = np.random.default_rng(42)
    data1 = rng.normal(size=50)
    data2 = data1 + rng.normal(scale=0.5, size=50)

    fig, ax = plt.subplots(figsize=(5, 2.7))
    ax.scatter(data1, data2, s=50, facecolor='C0', edgecolor='k')
    ax.set_title('Scatter colors (face & edge)')
    ax.set_xlabel('data1')
    ax.set_ylabel('data2')
    return fig


def demo_linewidth_linestyle_markersizes():
    """线宽/线型/标记大小与图例。"""
    rng = np.random.default_rng(1)
    data1, data2, data3, data4 = rng.normal(size=(4, 50))

    fig, ax = plt.subplots(figsize=(5, 2.7))
    ax.plot(data1, 'o', label='data1')
    ax.plot(data2, 'd', label='data2')
    ax.plot(data3, 'v', label='data3')
    ax.plot(data4, 's', label='data4')
    ax.legend()
    ax.set_title('Markers and legend')
    return fig


def main():
    demo_helper_on_two_subplots()
    demo_styling_artists()
    demo_colors_scatter()
    demo_linewidth_linestyle_markersizes()
    plt.show()


if __name__ == '__main__':
    main()


