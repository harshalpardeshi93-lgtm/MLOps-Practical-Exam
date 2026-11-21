# Wine Classification – Dataset Versioning Using DVC

## 1. Project Title
**Dataset Versioning and Collaboration Using DVC**

## 2. Aim
To implement dataset versioning using Data Version Control (DVC) and Git for managing changes in a Wine Classification dataset.

## 3. Introduction
DVC (Data Version Control) is an open-source tool used to track and manage datasets and machine learning models. It works with Git to maintain different versions of data and ensure reproducibility.

## 4. Tools and Technologies
- Python
- DVC
- Git
- GitHub
- Pandas
- VS Code

## 5. Dataset Description
The Wine Classification dataset contains:
- 178 rows
- 14 columns
- 13 input features
- 1 target column

## 6. Implementation Steps
1. Created a Wine Classification dataset.
2. Initialized Git and DVC repositories.
3. Tracked the dataset using `dvc add`.
4. Checked dataset status using `dvc status`.
5. Modified the dataset to create a new version.
6. Detected changes using MD5 hash comparison.
7. Updated DVC metadata.
8. Committed changes using Git.
9. Pushed the repository to GitHub.

## 7. Important DVC Commands

| Command | Purpose |
|---|---|
| `dvc init` | Initialize DVC |
| `dvc add` | Track dataset |
| `dvc status` | Check dataset status |
| `dvc diff` | Compare data versions |
| `dvc dag` | Display pipeline graph |
| `dvc root` | Show DVC root directory |
| `dvc version` | Check DVC version |

## 8. Versioning Result

**Original MD5 Hash:**
`2925c4a8cd201c79d97d3d283429ef23`

**Updated MD5 Hash:**
`4f8cfa72761bfe60458b59a933e5601c`

The dataset was modified by changing the first row's alcohol value from 14.23 to 14.24. DVC detected the modification and generated a new MD5 hash.

## 9. Conclusion
Successfully implemented dataset versioning using DVC and Git. Changes in the dataset were detected, tracked, and maintained through Git commits and GitHub.