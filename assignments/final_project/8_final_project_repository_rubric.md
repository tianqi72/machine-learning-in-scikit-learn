<center><h2>Final Project Repository Rubric</h2></center>

Name: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_   

\_\_\_\_\_\_ of 70 points

1. Data (5 points)   
    - [ ] 5 points. Completely meets guidelines.
    - [ ] 4 points. 1 minor fault: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
    - [ ] 3 points. 2 minor faults or 1  major fault: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
    - [ ] 2 points. 3 major faults or 2 major faults: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
    - [ ] 1 point. Many minor faults or 3 major faults: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
    - [ ] 0 points. Many major faults: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  <br> <br> 
1. Feature Engineering (10 points)
    - [ ] 10 points. Completely meets guidelines.
    - [ ] \_\_  points. Faults: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
1. Algorithms & Search (10 points)
    - [ ] 10 points. Completely meets guidelines.
    - [ ] \_\_ points. Faults: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
1. Evaluation Metrics (5 points)   
    - [ ] 5 points. Completely meets guidelines.
    - [ ] 4 points. 1 minor fault: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
    - [ ] 3 points. 2 minor faults or 1  major fault: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
    - [ ] 2 points. 3 major faults or 2 major faults: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
    - [ ] 1 point. Many minor faults or 3 major faults: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
    - [ ] 0 points. Many major faults: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  <br> <br> 
1. Machine learning mechanics (10 points) 
    - [ ] 10 points. Completely meets guidelines.
    - [ ] \_\_ points. Faults: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
1. Results / Conclusion (10 points)
    - [ ] 10 points. Completely meets guidelines.
    - [ ] \_\_ points. Faults: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
1. Code Functionality (10 points)
    - [ ] 10 points. Completely meets guidelines.
    - [ ] \_\_ points. Faults: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
1. Code Appearance (10 points)
    - [ ] 10 points. Completely meets guidelines.
    - [ ] \_\_ points. Faults: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

-----------
Guidelines
-------
- Data 
    + Appropriate choice (not from 621 or 699 materials)
    + Single dataframe in [tidy format](https://en.wikipedia.org/wiki/Tidy_data)
    + Enough rows 
    + Enough columns
    - Primarily tabular data
    - Other: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
- Feature Engineering
    + No exploratory data analysis (EDA) code in notebook
    - All feature transformations in a Pipeline. Target transformations can be done outside of a Pipeline.
    - Appropriate feature engineering for data types and algorithms types
    - Appropriately handled missing values 
    - Each step has a comment on why it was done.
- Algorithms & Search
    - Fit at least 2 algorithms from 621 / 699
    - Automated hyperparameter search across features, algorithms, and algorithm-specific hyperparameters
    - Automated model selection with cross validation
    - Each hyperparameter has a comment on why is it important
- Evaluation Metrics
    - Evaluated multiple evaluation metrics
    - All evaluation metrics are appropriate for problem and algorithm
    - Clearly described reasoning for choosing metrics
    - Clearly describe what the evaluation metric says about the model results
    - Other: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
- Machine learning mechanics
    + Proper train-test splitting
    + Proper train-test split size
    + Call `.fit`` only on training dataset
    + Only looked at test data set once
    + Appropriate use of random seed
    - Other: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
- Results / Conclusion
    - Visually displayed single, best final model 
    - Display all pipelines steps and all non-default hyperparameters
    - Display final model parameters
    - Interpreted single, best final model 
    - Clear summary 
    - Explained why things worked (or didn't work)
    - Connection to business outcome. Answers "Why does this matter?"
    - List of next steps / future directions
    - Other: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
- Code Functionality 
    - Code ran on first try
    - Did not duplicate built-in Python, numpy, pandas, or scikit-learn functionality
    - Use scikit-learn appropriately
    - Only wrote user-defined functions if called more than once
    - Other: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
- Code Appearance 
    + Code follows all [coding guidelines](https://github.com/brianspiering/ml_lab/blob/main/resources/coding_guidelines.md), [coding review rubric](https://github.com/brianspiering/ml_lab/blob/main/resources/code_review_rubric.md), and course materials
    + All imports should be at the begining of the notebook.
    - Code is logical and easy to read
    - `README.md` provides overview of project and understandable to someone outside of course
        + The `README.md` is like an abstract Who are you? What is the project? Why is it important? What did you find?
    - No unnecessary code or commented out code
    - The expectation is a comment / markdown cell for each block of code (just like 699 course materials)
    - All external code sources are cited
    - Other: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
