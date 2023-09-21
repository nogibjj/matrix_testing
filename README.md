# Continuous Integration using GitHub Actions of Python Data Science Project: Individual Project One
### by Rakeen Rouf

![install packages](https://img.shields.io/badge/install%20packages-success-green)
![Linting](https://img.shields.io/badge/lint-success-green) 
![Format](https://img.shields.io/badge/format-success-green) 
![Test](https://img.shields.io/badge/test-success-green)  

---
**Summary**

This prohject illustrates the use of matrix testing using Github workflows. Matrix testing is done to make sure your code works for multiple versions of your chosen programming lanugae and operating systems.
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
