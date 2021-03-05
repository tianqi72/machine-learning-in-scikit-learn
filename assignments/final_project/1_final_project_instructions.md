Machine Learning Final Project
------

### Learning Outcomes:

- Formulate a meaningful and answerable Data Science research question.
- Munge real data.
- Create and tune a machine learning model.
- Communicate your process and findings to a technical audience.
- Write correct and readable code.

You should follow the Data Science Workflow:

1. Ask the right question.
2. Acquire the relevant data.
3. Process the data.
4. Model the data with machine learning.
5. Deliver: Create presentation and Jupyter Notebook.

These steps are iterative (do a little preprocessing, do a little modeling, redo the preprocessing, …).

This project will become a part of your public Data Science portfolio, thus all data must be public data.  

----

1. Ask.

	This is your project so it is up to you to develop the right question. I'm here to help guide you.

2. Acquire.
	
	It is best if you pick a single, unique dataset. The instructor will approve the data to make sure it is appropriate and within scope.

    The dataset should be primarily tabular. No image data is allowed. A small amount of text data is okay, but it should a minor set of features.

	Acquiring data should not take away from the other aspects of the project (i.e., no collecting or web scraping the data). 

3. Process.

	What specific munging issues do you have to address (e.g., encoding, missing data, or data to exclude)? What descriptive/summary statistics are useful for understanding your data? What visualizations provide insight into your data?

3. Model.

	You must fit at least 2 different types of algorithms from scikit-learn and compare results. For example, you could pick logistic regression and Random Forest™. Or pick k-means clustering and spectral clustering.

    Each algorithm's hyperparameters should be tuned.

5. Deliver(ables).

    There are two deliverables:

    1. A video presentation. 
    2. A GitHub repository.

    The presentation will be 6-7 minute public video on YouTube. If you have an issue with a public video on YouTube, please discuss it with me.

    The GitHub repo for this assignment should be public with a __single__ Jupyter Notebook (.ipynb) notebook and no subfolders. You can include other files (e.g., custom modules or code to deploy your model). 

    I except the code to be reproducible (i.e., it will run on other people's computers). I will try run your notebook. So it transparant and testable for you, there are 2 options:

    1. You include a colab link in the README that I will click on. 
    2. If there is no clear colab link, I will attempt run it on DeepNote using the import from GitHub.

    Thus, I suggest creating a conda environment for your project to manage dependencies. Feel free to use a copy of the conda environment from the class.

    Regarding data management, that Jupyter Notebook should read in a single dataframe or numpy-like array. If that single object is less than 40 MB, it can committed to the GitHub repo. If that single object is too large for GitHub, store the data on a public file sharing service (e.g., AWS S3) and code within the Jupyter Notebook should fetch it. The total size is limited to 100 MB.

    All other work, such as exploratory data analysis, should not be in the repo and will not be graded. I suggest you have a second repo that contains the other work that might be of interest to other people (e.g., potential employers).

----
Hints
----

- Make it run, make it right, make it fast. (in that order)
- Go end-to-end as quickly possible. From raw data -> basic features -> simple model -> evaluation. Then explore options for each stage.
- Follow along with course content. After each session, apply the same concepts to your projects.
- Use this [Machine Learning Project Checklist](https://docs.google.com/spreadsheets/d/1d7xTL8DgUpbbHuHZp5LTqvIwo7gc96NG4IJhCej7IpI/edit?usp=sharing)

----
FAQs
-----

1. Can I pick a dataset that is commonly analyzed or the same dataset as someone else in the class?

    Yes & Yes. 

    Well-temper dataset (e.g., UCIML) are easier to analyze, thus will work well for the Final Project. However, I suggest you pick something unique.

    Real-world, applied, contemporary datasets are more difficult to analyze. Choosing the more difficult path will increase your skill level and give you more to talk about during your future job search.

    If you choose common dataset, it will be easier for me to compare your work to other work. You might have to work harder to make it stand out.

1. Can I use a dataset from practicum?

    Yes - If it is can be public and you get permission from your manager at the practicum organization.

    Most practicum data is not public, thus can not be used for this project.

1. Can I use \_\_\_\_\_\_\_\_ algorithm?

    The goal of this project to review the course materials. After you have hyperparameter tuned at __least two different algorithms__ from 621 and/or 699, you can try other algorithms. 

1. Can I use \_\_\_\_\_\_\_\_ software package?

    The goal of this project to review the course materials, this course has been in Python and primarily using scikit-learn package. __All code must be Python code__. The majority of your code should be in scikit-learn.

    There should be __no__ shell scripting, Spark, TensorFlow, or PyTorch code anywhere. 

    Do __not__ reimplement any algorithm or function. If possible, call existing code. If possible, call scikit-learn code. Only use Pandas, NumPy, or SciPy if scikit-learn does not have the functionality you require. Write your own custom code only if it is not available in any package.

    Visualizations are important for understanding your system and communicating to your audience. Visualizations should be clear; They do not need to be beautiful. You can use any Python visualization package, suggestions are scikit-plot, Matplotlib, and Seaborn.

    You can use any third party Python packages. Try to use packages that are related to scikit-learn, see list [here](https://scikit-learn.org/stable/related_projects.html).


1. For the Final Project, how will model performance on my chosen evaluation metric effect my grade?

    Absolute model performance on evaluation metrics will have __no__ impact the grade. There are many different datasets, each one will perform differently. This is different from the assignments where absolute model performance on evaluation metrics was important because everyone use the same datasets.

    What will impact your grade is relative model performance on the evaluation metrics. I except you to try different combinations of features, algorithms, and hyperparameters. You should find a combination that does better as measured by evaluation metrics.

    Selecting the evaluation metric will impact your grade. You should select metric(s) that are relevant for the research question, not just something that you can easily optimize.

1. Can I use some random piece of code I found on the Internet in my Final Project?

    Yes.

    Any ideas or code that are not your own have to be documented. The only exceptions are ideas or code from this course since I know where they come from. 

    There should only be a handful of citations. The expectation is that you'll do most of the thinking and code writing on your own. If there is an excessive amount of work that is not your own (even if properly cited), you'll receive a reduced score. The Final Project's goal is to practice the ideas and code from this course on another dataset. See examples from last year.

    Anything you to fail to cite will be considered plagiarism. Plagiarism will result in a zero score on this assignment and may result in other plagiarism related penalties.

    Any concerns should be run by me before you turn the project in.
    
1. What do you mean by visualization?

    I think visualizations are important at every stage of data science. Visualizations are especially under-utilized in the interpretation of machine learning models. I would like to see at least one figure that tries to understand a trained model.

    This project is about the entire machine learning process. Exploratory data analysis (EDA) is vital but should only be a brief section. You should not present a complete coverage of what you did for EDA, just the highlights that the tell the story of your model. 

    Here are examples to get you going:  

    - https://explained.ai/decision-tree-viz/  
    - https://github.com/parrt/random-forest-importances  
    - https://zhiyzuo.github.io/Python-Plot-Regression-Coefficient/  

1. Can I get other classmates help for a code review or give feedback on my presentation?
    
    Yes - Please help your fellow colleagues out. Feel to check out each other's project and offer constructive criticism. You should add people that helped in a acknowledgments section.

1. How do I get a "A"? 

    First, follow the directions as written and intended.

    Second, add an "X" factor:
    - Do something groundbreaking (seriously). Either ground-breaking for the field or for the class.
    - Create new, meaningful insight. Currently, we are dealing vaccine distribution and effectiveness. It would be meaningful make a prediction about that topic.
    - Implement a new, meaningful algorithm that works with scikit-learn.
    - Find multiple datasets to put together. As always - "Data is the world's best regularizer." Being able to find and join multiple datasets will make you stand out in this project and as a data scientist.
    - Fit models and use methodologies from outside class materials.
    - "Deploy" to production. Make website for your model. Suggestions include [FastAPI](https://fastapi.tiangolo.com/) and [Streamlit](https://www.streamlit.io/)