import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm


def main():
    # 生成网格与函数值
    X, Y = np.meshgrid(np.linspace(-3, 3, 128), np.linspace(-3, 3, 128))
    Z = (1 - X/2 + X**5 + Y**3) * np.exp(-X**2 - Y**2)

    # 生成散点数据
    rng = np.random.default_rng(0)
    data1 = rng.normal(size=200)
    data2 = rng.normal(size=200)
    data3 = rng.normal(size=200)

    fig, axs = plt.subplots(2, 2, figsize=(8, 6), layout='constrained')

    # pcolormesh
    pc = axs[0, 0].pcolormesh(X, Y, Z, vmin=-1, vmax=1, cmap='RdBu_r')
    fig.colorbar(pc, ax=axs[0, 0])
    axs[0, 0].set_title('pcolormesh()')

    # contourf
    co = axs[0, 1].contourf(X, Y, Z, levels=np.linspace(-1.25, 1.25, 11))
    fig.colorbar(co, ax=axs[0, 1])
    axs[0, 1].set_title('contourf()')

    # imshow + LogNorm
    im = axs[1, 0].imshow(Z**2 * 100, cmap='plasma', norm=LogNorm(vmin=0.01, vmax=100),
                          origin='lower', extent=[X.min(), X.max(), Y.min(), Y.max()])
    fig.colorbar(im, ax=axs[1, 0], extend='both')
    axs[1, 0].set_title('imshow() with LogNorm()')

    # scatter with colormap
    sc = axs[1, 1].scatter(data1, data2, c=data3, cmap='RdBu_r')
    fig.colorbar(sc, ax=axs[1, 1], extend='both')
    axs[1, 1].set_title('scatter()')

    plt.show()


if __name__ == '__main__':
    main()


