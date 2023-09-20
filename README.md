# Continuous Integration using GitHub Actions of Python Data Science Project: Individual Project One
### by Rakeen Rouf

[![Format](https://github.com/nogibjj/ContinuousIntegrationusingGitHubActionsofPythonDataScienceProject/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/ContinuousIntegrationusingGitHubActionsofPythonDataScienceProject/actions/workflows/format.yml) [![Lint](https://github.com/nogibjj/ContinuousIntegrationusingGitHubActionsofPythonDataScienceProject/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/ContinuousIntegrationusingGitHubActionsofPythonDataScienceProject/actions/workflows/lint.yml) [![OnInstall](https://github.com/nogibjj/ContinuousIntegrationusingGitHubActionsofPythonDataScienceProject/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/ContinuousIntegrationusingGitHubActionsofPythonDataScienceProject/actions/workflows/install.yml) [![Test](https://github.com/nogibjj/ContinuousIntegrationusingGitHubActionsofPythonDataScienceProject/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/ContinuousIntegrationusingGitHubActionsofPythonDataScienceProject/actions/workflows/test.yml)

---

**Walk Through Youtube Video**
[Youtube](https://youtu.be/YduYJFkaXa0)

---
**Summary**

This project serves as an illustrative guide for implementing Continuous Integration (CI) using GitHub Actions in Python-based Data Science projects. By adopting CI, it helps maintain code quality and consistency throughout the development process. The workflows include linting, formatting, installing dependencies, and running tests, ensuring that these critical steps are automatically executed with every push and pull request to the repository.

---
**Project Structure**

- **`Jupyter Notebook(src/DescriptiveStats.ipynb)`**:
  - Contains cells that perform descriptive statistics using Pandas.
  - Validated using the nbval plugin for pytest.

- **`Python Script(src/script_descriptive_stats.py)`**:
  - Executes the same descriptive statistics using Pandas.

- **`lib.py(src/lib.py)`**:
  - Holds shared code used by both the script and the notebook.

- **`Makefile`**:
  - Contains four commands (Run by GitHub Workflows on each Push and Pull):
    - `Test`: Run all tests (notebook, script, and lib)
    - `Format`: Format code with Python black
    - `Lint`: Lint code with Ruff
    - `OnInstall`: Install dependencies via `pip install -r requirements.txt`

- **`test_script.py(tests/test_script_descriptive_stats.py)`**:
  - Contains tests for the Python script.

- **`test_lib.py(tests/test_lib.py)`**:
  - Includes tests for the library.

- **`Pinned requirements.txt`**:
  - Specifies exact versions of dependencies.

---

**Getting Started**

To get started with this template, follow these steps:

1. **Create a New Repository:** 
   - Click the "Use this template" button or manually create a new repository using this template as a starting point.

2. **Set Up CI/CD:** 
   - Define your CI/CD workflows by configuring the `.github/workflows/` directory. Modify the workflows to suit your project's specific needs. 

3. **Start Code Space (Optional):**
   - If you want to develop entirely in the cloud, click the "Code" button on the GitHub repository page and select "Open with Code Spaces". This will launch a cloud-based development environment where you can start coding without any local setup.

4. **Customize Automation:** 
   - Customize the automation scripts and rules in the `.github/workflows/` directory. Configure issue management, release automation, and code quality checks according to your project requirements.

5. **Documentation:** 
   - Update the project's documentation to reflect your project's specific setup, workflows, and guidelines.

6. **Requirement.txt:**
   - Update the `requirements.txt` file to ensure all necessary Python packages have been included.
