import matplotlib.pyplot as plt

def plot_correlation_circle(PCA_model, features, pc1=0, pc2=1):
    """
    Plots a correlation circle for the specified principal components.

    Parameters
    ----------
    PCA_model : Fitted PCA model from sklearn
    features : List of feature names corresponding to the PCA input data
    pc1 : Index of the first principal component (0-based)
    pc2 : Index of the second principal component (0-based)
    """
    # extract loadings for the specified principal components
    loadings = PCA_model.components_.T[:, [pc1, pc2]]  # shape: (n_features, 2)

    # plot unit circle
    plt.axhline(0, color='grey', lw=1)
    plt.axvline(0, color='grey', lw=1)
    circle = plt.Circle((0, 0), 1, color='lightgrey', fill=False, linestyle='--')
    plt.gca().add_artist(circle)

    # plot arrows and feature names
    for i, feature in enumerate(features):
        plt.arrow(0, 0, loadings[i,0], loadings[i,1], color='b', alpha=0.7, head_width=0.04, length_includes_head=True)
        plt.text(loadings[i,0]*1.1, loadings[i,1]*1.1, feature, color='black', ha='center', va='center')

    # set labels and title
    plt.xlabel(f'PC{pc1+1}')
    plt.ylabel(f'PC{pc2+1}')
    plt.title(f'PCA Correlation Circle (Biplot PC{pc1+1} vs PC{pc2+1})')
    plt.xlim(-1.1, 1.1)
    plt.ylim(-1.1, 1.1)
    plt.grid(True)
    plt.show()