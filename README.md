# Project 1 – Stack Overflow Developer Survey Analysis

## Motivation
This project analyzes data from the Stack Overflow Developer Survey to explore
factors that influence developers' yearly compensation and to build a simple
baseline model for prediction.

## Blog Post
Read the blog here: BLOG.md

## Dataset
The dataset is **not included** in the repository due to GitHub file size limits (>100MB).
GitHub blocks files larger than 100 MiB.  
Download the Stack Overflow Developer Survey CSV and place it in:

data/survey_results_public.csv

## Libraries Used
- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn

## Repository Structure
- analysis.ipynb: Data analysis, model training, evaluation, and predictions
- BLOG.md: Blog post with findings and visualization
- img/: Images used in the blog (e.g., workexp_vs_comp.png)
- .gitignore: Excludes large dataset file and other non-tracked items

## Summary of Results
A linear regression model was trained to predict yearly compensation based on
experience and job satisfaction. The results suggest compensation is influenced by
many factors beyond these baseline features.

## Acknowledgments
Dataset provided by Stack Overflow Developer Survey.