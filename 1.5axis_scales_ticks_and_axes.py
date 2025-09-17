import numpy as np
import matplotlib.pyplot as plt
from matplotlib.dates import ConciseDateFormatter


def demo_scales():
    """比例尺：线性与对数。"""
    rng = np.random.default_rng(0)
    data1 = rng.normal(size=100)
    xdata = np.arange(len(data1))
    data = 10 ** data1

    fig, axs = plt.subplots(1, 2, figsize=(7, 2.7), layout='constrained')
    axs[0].plot(xdata, data)
    axs[0].set_title('Linear scale')

    axs[1].set_yscale('log')
    axs[1].plot(xdata, data)
    axs[1].set_title('Log scale (y)')
    return fig


def demo_ticks():
    """刻度：自动与手动。"""
    rng = np.random.default_rng(1)
    data1 = rng.normal(size=100)
    xdata = np.arange(len(data1))

    fig, axs = plt.subplots(2, 1, figsize=(5, 4.5), layout='constrained')
    axs[0].plot(xdata, data1)
    axs[0].set_title('Automatic ticks')

    axs[1].plot(xdata, data1)
    axs[1].set_xticks(np.arange(0, 100, 30), ['zero', '30', 'sixty', '90'])
    axs[1].set_yticks([-1.5, 0, 1.5])
    axs[1].set_title('Manual ticks')
    return fig


def demo_dates_and_categorical():
    """日期与分类：ConciseDateFormatter 与字符串分类条形图。"""
    rng = np.random.default_rng(2)

    # 日期
    fig1, ax1 = plt.subplots(figsize=(6, 2.7), layout='constrained')
    dates = np.arange(np.datetime64('2021-11-15'), np.datetime64('2021-12-25'),
                      np.timedelta64(1, 'h'))
    data = np.cumsum(rng.normal(size=len(dates)))
    ax1.plot(dates, data)
    ax1.xaxis.set_major_formatter(ConciseDateFormatter(ax1.xaxis.get_major_locator()))
    ax1.set_title('Dates with ConciseDateFormatter')

    # 分类
    fig2, ax2 = plt.subplots(figsize=(5, 2.7), layout='constrained')
    categories = ['turnips', 'rutabaga', 'cucumber', 'pumpkins']
    ax2.bar(categories, rng.random(len(categories)))
    ax2.set_title('Categorical bar')
    return [fig1, fig2]


def demo_additional_axes():
    """附加坐标轴：twinx 与 secondary_xaxis。"""
    t = np.linspace(0, 2 * np.pi, 200)
    s = np.sin(t)

    fig, (ax1, ax3) = plt.subplots(1, 2, figsize=(7, 2.7), layout='constrained')
    l1, = ax1.plot(t, s)
    ax2 = ax1.twinx()  # 右侧 y 轴
    l2, = ax2.plot(t, np.arange(len(t)), 'C1')
    ax2.legend([l1, l2], ['Sine (left)', 'Straight (right)'])

    ax3.plot(t, s)
    ax3.set_xlabel('Angle [rad]')
    ax4 = ax3.secondary_xaxis('top', functions=(np.rad2deg, np.deg2rad))
    ax4.set_xlabel('Angle [°]')
    return fig


def main():
    demo_scales()
    demo_ticks()
    demo_dates_and_categorical()
    demo_additional_axes()
    plt.show()


if __name__ == '__main__':
    main()


