# University Student Data Analyzer

**Beginner portfolio project | Python, pandas, Matplotlib, CSV**

## Project overview
This project demonstrates a basic workflow for reviewing fictional university student data: load a CSV, inspect the records, check missing values, calculate summary statistics, compare departments and semesters, create charts, and export report files.

> **Data and policy note:** Every included record is fictional. The GPA value of 2.5 is a practice-only example threshold, not an official university rule. Do not use this project to make real student decisions. Never place private or identifiable student records in a public portfolio.

## Skills demonstrated
- Python scripting and file paths
- Reading CSV files with pandas
- Data quality checks with `isna()`
- Grouped summaries with `groupby()` and `agg()`
- Basic charting with Matplotlib
- Exporting results to CSV and PNG files

## Project files
- `student_data_analyzer.py` — main analysis script
- `sample_student_data.csv` — fictional sample dataset
- `requirements.txt` — Python dependencies
- `outputs/` — generated summaries and charts after running the script
- `PORTFOLIO_DESCRIPTION.md` — copy-ready portfolio summary
- `INTERVIEW_NOTES.md` — prompts to help explain the work honestly

## Run in Google Colab (no installation required)
1. Open https://colab.research.google.com/
2. Upload `sample_student_data.csv` using the folder icon, or create a code cell and upload it:
   ```python
   from google.colab import files
   uploaded = files.upload()
   ```
3. Upload `student_data_analyzer.py` the same way.
4. Run the script in a cell:
   ```python
   !pip -q install pandas matplotlib
   !python student_data_analyzer.py
   ```
5. View output files:
   ```python
   import os
   os.listdir("outputs")
   ```
6. Display a chart:
   ```python
   from IPython.display import Image, display
   display(Image("outputs/average_gpa_by_department.png"))
   ```

## Run on your own computer
Install Python 3.10+ and then run:
```bash
pip install -r requirements.txt
python student_data_analyzer.py
```
Keep the script and CSV file in the same folder.

## Questions this project answers
- How many student records are in the file?
- What is the overall average GPA and average number of completed credits?
- How do average GPA and credits compare by department?
- How do the summary values compare by semester?
- Are any fields missing?
- Which fictional records fall below the example GPA threshold?

## Limitations and responsible use
- The dataset is small and synthetic; findings do not represent any actual university.
- No conclusions about student success, causes, or institutional performance should be drawn from these data.
- Missing-value counts are reported; the script does not silently impute missing values.
- The example GPA threshold is not an official policy or recommendation.
- Real student information can be protected by privacy laws and university policy. Use only approved, de-identified data in authorized systems.

## Suggested next improvements
1. Add data validation for GPA range (0.0–4.0) and nonnegative credits.
2. Add a command-line option to select a CSV file.
3. Create a Power BI dashboard from the exported summaries.
4. Practice SQL by storing the fictional dataset in a local database.
5. Add tests for missing columns and invalid values.
