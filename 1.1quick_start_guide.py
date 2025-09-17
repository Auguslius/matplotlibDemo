import numpy as np
import matplotlib.pyplot as plt


def simple_example():
    """最小示例：subplots + Axes.plot + show。"""
    fig, ax = plt.subplots()  # 创建一个包含单个 Axes 的 Figure
    ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # 在 Axes 上绘制一些数据
    ax.set_title("Simple Example")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    return fig


def parts_of_a_figure():
    """Figure 组成：figure/subplots/2x2/subplot_mosaic 的基本用法。"""
    figures = []

    # 1) 空 Figure（无 Axes）
    fig1 = plt.figure(figsize=(4, 2.5))
    fig1.suptitle("figure(): empty Figure (no Axes)")
    figures.append(fig1)

    # 2) 单个 Axes 的 Figure
    fig2, ax2 = plt.subplots(figsize=(4, 2.5))
    x = np.linspace(0, 2 * np.pi, 200)
    ax2.plot(x, np.sin(x), label="sin(x)")
    ax2.set_title("subplots(): single Axes")
    ax2.set_xlabel("x")
    ax2.set_ylabel("sin(x)")
    ax2.legend()
    figures.append(fig2)

    # 3) 2x2 网格的 Axes
    fig3, axs = plt.subplots(2, 2, figsize=(6, 4))
    axs = axs.ravel()
    axs[0].plot(x, np.sin(x))
    axs[0].set_title("sin")
    axs[1].plot(x, np.cos(x))
    axs[1].set_title("cos")
    axs[2].plot(x, np.tan(x))
    axs[2].set_ylim(-5, 5)
    axs[2].set_title("tan (clipped)")
    axs[3].plot(x, np.sin(x) ** 2 + np.cos(x) ** 2)
    axs[3].set_title("sin^2 + cos^2")
    fig3.suptitle("subplots(2x2): grid of Axes")
    figures.append(fig3)

    # 4) mosaic：左侧一幅，右侧上下两幅
    layout = [["left", "right_top"], ["left", "right_bottom"]]
    fig4, axd = plt.subplot_mosaic(layout, figsize=(7, 4))
    axd["left"].plot(x, np.sin(x), color="C0")
    axd["left"].set_title("left: sin")
    axd["right_top"].plot(x, np.cos(x), color="C1")
    axd["right_top"].set_title("right_top: cos")
    axd["right_bottom"].plot(x, np.sin(x) * np.cos(x), color="C2")
    axd["right_bottom"].set_title("right_bottom: sin*cos")
    fig4.suptitle("subplot_mosaic(): named Axes layout")
    figures.append(fig4)

    return figures


def main():
    # quick start：在某些环境（如 Jupyter）可省略 plt.show()
    simple_example()
    parts_of_a_figure()
    plt.show()


if __name__ == "__main__":
    main()


