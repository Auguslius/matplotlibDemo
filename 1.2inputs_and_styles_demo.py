import numpy as np
import matplotlib.pyplot as plt


def demo_inputs_matrix_to_array():
    """输入类型示例 1：将 numpy.matrix 转为 numpy.array 再绘图。"""
    b = np.matrix([[1, 2], [3, 4]])
    b_asarray = np.asarray(b)

    fig, ax = plt.subplots(figsize=(4.2, 3))
    ax.plot(b_asarray[0, :], b_asarray[1, :], marker="o")
    ax.set_title("matrix -> array for plotting")
    ax.set_xlabel("col 1")
    ax.set_ylabel("col 2")
    return fig


def demo_inputs_data_keyword_scatter():
    """输入类型示例 2：使用 data 关键字与字符串字段名的散点图。"""
    np.random.seed(19680801)
    data = {
        "a": np.arange(50),
        "c": np.random.randint(0, 50, 50),
        "d": np.random.randn(50),
    }
    data["b"] = data["a"] + 10 * np.random.randn(50)
    data["d"] = np.abs(data["d"]) * 100

    fig, ax = plt.subplots(figsize=(5, 2.7), layout="constrained")
    ax.scatter("a", "b", c="c", s="d", data=data)
    ax.set_xlabel("entry a")
    ax.set_ylabel("entry b")
    ax.set_title("scatter with data keyword")
    return fig


def demo_styles_oo():
    """编程风格示例：OO 风格。"""
    x = np.linspace(0, 2, 100)
    fig, ax = plt.subplots(figsize=(5, 2.7), layout="constrained")
    ax.plot(x, x, label="linear")
    ax.plot(x, x ** 2, label="quadratic")
    ax.plot(x, x ** 3, label="cubic")
    ax.set_xlabel("x label")
    ax.set_ylabel("y label")
    ax.set_title("Simple Plot (OO)")
    ax.legend()
    return fig


def demo_styles_pyplot():
    """编程风格示例：pyplot 风格。"""
    x = np.linspace(0, 2, 100)
    plt.figure(figsize=(5, 2.7), layout="constrained")
    plt.plot(x, x, label="linear")
    plt.plot(x, x ** 2, label="quadratic")
    plt.plot(x, x ** 3, label="cubic")
    plt.xlabel("x label")
    plt.ylabel("y label")
    plt.title("Simple Plot (pyplot)")
    plt.legend()


def main():
    # 输入类型
    demo_inputs_matrix_to_array()
    demo_inputs_data_keyword_scatter()

    # 编程风格
    demo_styles_oo()
    demo_styles_pyplot()

    # 统一展示
    plt.show()


if __name__ == "__main__":
    main()


