import numpy as np
import matplotlib.pyplot as plt


def demo_hist_with_labels_and_text():
    """直方图 + 轴标签/标题/文本 + 数学公式。"""
    mu, sigma = 115, 15
    x = mu + sigma * np.random.randn(10000)

    fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
    n, bins, patches = ax.hist(x, 50, density=True, facecolor='C0', alpha=0.75)

    ax.set_xlabel('Length [cm]')
    ax.set_ylabel('Probability')
    ax.set_title('Aardvark lengths\n (not really)')
    ax.text(75, .025, r'$\mu=115,\ \sigma=15$')
    ax.axis([55, 175, 0, 0.03])
    ax.grid(True)
    return fig


def demo_annotation_on_cosine():
    """注释：在余弦曲线上标出局部最大值。"""
    fig, ax = plt.subplots(figsize=(5, 2.7))
    t = np.arange(0.0, 5.0, 0.01)
    s = np.cos(2 * np.pi * t)
    line, = ax.plot(t, s, lw=2)

    ax.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
                arrowprops=dict(facecolor='black', shrink=0.05))

    ax.set_ylim(-2, 2)
    ax.set_title('Annotation example')
    return fig


def demo_legend_multilines():
    """图例：多曲线/标记 + legend。"""
    rng = np.random.default_rng(2024)
    data1, data2, data3 = rng.normal(size=(3, 50))

    fig, ax = plt.subplots(figsize=(5, 2.7))
    ax.plot(np.arange(len(data1)), data1, label='data1')
    ax.plot(np.arange(len(data2)), data2, label='data2')
    ax.plot(np.arange(len(data3)), data3, 'd', label='data3')
    ax.legend()
    ax.set_title('Legend example')
    return fig


def main():
    demo_hist_with_labels_and_text()
    demo_annotation_on_cosine()
    demo_legend_multilines()
    plt.show()


if __name__ == '__main__':
    main()


