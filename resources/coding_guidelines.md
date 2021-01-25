Coding Guidelines
--------

1. Do __not__ reimplement any function or class. 
    
    If possible, call existing code. If possible, call scikit-learn code. Only use Pandas, NumPy, or SciPy if scikit-learn does not have the functionality you require. 

    Write your own custom code only if it is not available in any commonly used package.

    Often times Pandas has similar functionality as scikit-learn. Here are the reasons we are using scikit-learn:

    - Can cross validate the entire workflow.
    - Can grid search model and preprocessing hyperparameters.
    - Avoids adding new columns to the source DataFrame.
    - Pandas lacks separate fit/transform steps to prevent data leakage.

    Source: dataquest.io

1. Prefer keywords arguments. 

    For clarity and practice using the scikit-learn API, almost all arguments should be keyword arguments. 

    The most common exception is when the variable name is the same as the keyword argument. Here is an example:

    ```python
    import numpy as np
    from sklearn.linear_model import LinearRegression
    
    X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
    y = np.dot(X, np.array([1, 2])) + 3
    reg = LinearRegression().fit(X, y)
    ```

1. Prefer inline code. 

    Only write functions if you call the code more than once or if creating functions makes testing easier.

1. Display only 2 significant digits and add commas.

    By default numerical values have many digits and no separators. This slows down visually comparisons between models. 

    Use this code snippet when presenting numbers for humans:

    ```python
    print(f"{number:,.2f}")
    ```

1. Hide plot hashes.

    By default figures in Jupyter Notebook often have an ugly hash like:

    `[<matplotlib.lines.Line2D at 0x1288b7fd0>]`

    Suppress that hash with `;` at the end

    `plt.scatter(diabetes_X_test, diabetes_y_test,  color='black');`
