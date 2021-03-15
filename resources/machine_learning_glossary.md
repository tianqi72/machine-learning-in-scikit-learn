Machine Learning Glossary
-----

| Acronym | Definition | 
|:---|:---|
| AI  | Artificial Intelligence |
| CV  | Cross Validation |
| CV  | Computer Vision |
| DT  | Decision Tree |
| DL  | Deep Learning |
| EM  | Expectation-maximization algorithm |
| k-NN| k Nearest Neighbors |
| GD  | Gradient Descent |
| LM  | Linear Model |
| LR  | Linear Regression |
| ML  | Machine Learning |
| RF™ | Random Forest™ |
| SVM | Support Vector Machine |

Term: Definition
--------

- Accuracy: Percentage of correct predictions made by a model.

- Algorithm: An unambiguous specification of how to solve a particular problem. In Machine Learning, an algorithm is a list of explicit steps that include: data ingest -> feature extraction -> train model -> predict -> evaluation metrics. Examples: linear regression and SVM

- Data Leakage: Data leakage is when there is meaningful information present during training that will not be present during pure prediction later. And that meaningful information increases performance on the the training data but can not generalize to a pure prediction phase. One common example is encoding the target variable information by mistake in an id variable. Another example is looking at your test data set more than once. You are using additional information (test set performance) which will not be present during a pure-prediction phase.

- Epoch: A complete pass through the training d ataset.

- Example: An instance (with its features) and a label.

- Feature: A property of an instance used in a prediction task. Should be columns in dataframe. For example, a cat may be "black" in color.

- Feature Column: A set of related features, such as the set of all possible countries in which users might live. An example may have one or more features present in a feature column. A feature column is referred to as a “namespace” in the VW system (at Yahoo/Microsoft), or a field.

- Instance: The thing about which you want to make a prediction. For example, the instance might be a web page that you want to classify as either "about cats" or "not about cats".

- Label: An answer for a prediction task ­­either the answer produced by a machine learning system, or the right answer supplied in training data. For example, the label for a web page might be "about cats".

- Metric: A number that you care about. May or may not be directly optimized.

- Model: The result of applying a machine learning algorithm. After training a dataset, you have a specific model that then can be used to make predictions.

- Objective: A metric that your algorithm is trying to optimize.

- Optimization: The process of finding the best parameters for a specific model on a specific dataset. Common Examples: ordinary least squares (OLS) and Stochastic gradient descent (SGD)
    - Constrained Optimization: Willing to accept a worse estimate of the model parameters to satisfy other external conditions, typically regularization. Common Examples: Lasso, Ridge, and Elastic Net regression

- Parameters:  
    - Model-parameters: 
        - Properties of specific model for a specific dataset.
        - Learned during training.
    - Hyper-parameters:
        - Properties of the algorithm that control how the model is fit.
        - Either learned or chosen before training.

- Pipeline: The infrastructure surrounding a machine learning algorithm. Includes gathering the data, putting it into tabular form, training models, and exporting the models to be used in other systems.

- Supervised learning: This is the most common kind of (commercial) ML algorithm today where the system is presented with labeled examples to explicitly learn from.

- Target - Labels for training dataset. The most common labels are numeric values for regression and set of discrete categories for classification.

- Unsupervised learning: In contrast to supervised learning, the ML algorithm has to infer the inherent structure of the data that is not annotated with labels.
 
-------
Other resources & references
-------

- Acronyms
    - [ML acronyms / abbreviations](https://docs.google.com/spreadsheets/d/1EijyTxc7OKrr2bIRJXitIr_7p0BJNHD8tgRDH8Pruk4/edit?usp=sharing)
    - [Acronyms](https://machinelearning.wtf/acronyms/)

- Glossaries
    - [Josh's glossary](https://semanti.ca/blog/?glossary-of-machine-learning-terms)
    - [Analytics Vidhya's glossary](https://www.analyticsvidhya.com/glossary-of-common-statistics-and-machine-learning-terms/)
    - [scikit-learn's glossary](http://scikit-learn.org/stable/glossary.html#glossary)
    - [Terms & Definitions](https://github.com/bfortuner/ml-cheatsheet/blob/master/docs/glossary.rst)
    - [TensorFlow & general terms](https://medium.com/google-cloud/a-tensorflow-glossary-cheat-sheet-382583b22932)

-Other
    - [Rules of Machine Learning: Best Practices for ML Engineering Martin Zinkevich](http://martin.zinkevich.org/rules_of_ml/rules_of_ml.pdf)
