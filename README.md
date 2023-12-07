# KMA Machine Learning

## Homework #4

Machine Learning project homework #4

### Kaggle Competition

Link - <https://www.kaggle.com/competitions/kmaml223>

### Team

- Polinchuk Kyrylo
- Halaida Mykhailo
- Barsuk Oleksandr

### Folder structure

- .github/worflows - CI workflow with GitHub Actions;
- EDA - notebooks with data analysis, statistics etc;
- configs - configs for model training;
- src - project code;
- tests - unit-tests for the code.

### CI Workflow

#### Trigger

- **On Push**: The workflow is triggered on every push to the repository.

#### Jobs

- **Explore-GitHub-Actions**: This is the main job of the workflow.

#### Environment

- **Runs-On**: The job runs on the latest Ubuntu runner provided by GitHub Actions.

#### Steps

1. **Trigger Information**:
   - Echoes the event that triggered the job.
   - Shows the operating system of the runner.

2. **Repository Setup**:
   - Checks out the repository code to the runner, allowing the workflow to access it.

3. **Environment Setup**:
   - **Python Environment**: Sets up the Python environment, specifically Python 3.10.
   - **Dependency Installation**: Installs all the necessary dependencies from `requirements.txt` using pip.

4. **NLTK Data Download**:
   - Downloads necessary NLTK datasets (words, wordnet, punkt) which are essential for certain Python operations involving natural language processing.

5. **Testing and Quality Checks**:
   - **Run Tests with Coverage**: Executes Pytest tests with coverage analysis.
   - **Generate Coverage Report**: Produces a report detailing the test coverage.
   - **Run Pylint**: Conducts a linting check on the source code in the `./src/` directory using Pylint.
   - **Run Ruff**: Additional linting with Ruff, focusing on style and errors.

6. **Job Completion Status**:
   - Displays the final status of the job.

### Running project

First of all project dependencies should be installed with command:

````sh
pip install -r requirements.txt
````

#### Exploratory Data Analysis

For EDA three Jupyter notebooks should be run:

- `./EDA/DataAnalyze.ipynb` - analysis and statistics visualization from train and test datasets, including preprocessing steps like lemmatization, calculating various textual statistics, generating histograms and bar charts for data distribution;
- `./EDA/DataPreparing.ipynb` - data preprocessing on train and test datasets, including text cleaning and processing (lemmatizing, filtering, and tokenizing). Results are saved to CSV files `train_processed.csv` and `test_processed.csv` accordingly;
- `./EDA/DataVector.ipynb` - dimensionality reduction and visualization on processed text data: TF-IDF vectorization, SVD dimensionality reduction and vizualization. Results are saved to CSV files `train_ml.csv` and `test_ml.csv` for machine learning purposes.

#### Training model

For training model `./src/trining.ipynb` notebook should be used. For classification **MultiOutputClassifier** model is used. Trained model get stored to `./src/models/MOC_LR.pkl` file.

#### Making predictions

For making predictions put input text to `./data/input.txt` and run this script:

````sh
py ./src/prediction.py
````

#### Unit tests

For running unit-tests on your local machine use these commands:

````sh
pytest .
````

To see code coverage use these commands:

````sh
coverage run -m pytest
coverage report
````

#### Running linters

For running linters on your local machine use these commands:

````sh
pylint ./src/
ruff check .
````

### Running Jupyter Notebook in Docker

To start container with Jupyter Notebook:

````sh
docker build -t jupyter-notebook .
docker-compose up
````

**IMPORTANT**: to login find token in container output logs

To stop container:

````sh
docker-compose down
````
