def draw_vector(v0: float, v1:float, ax=None) -> None:
    "Draw a single vector arrow that has both direction and magnitude."
    ax = ax or plt.gca()
    arrowprops=dict(arrowstyle='->',
                    linewidth=2,
                    shrinkA=0, shrinkB=0)
    ax.annotate('', v1, v0, arrowprops=arrowprops)