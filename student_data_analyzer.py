"""
University Student Data Analyzer
A beginner-friendly practice project using pandas and matplotlib.

IMPORTANT:
- All included student records are fictional.
- This script is for learning and portfolio demonstration only.
- The GPA threshold is a practice example, not an official university policy.
"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

PROJECT_DIR = Path(__file__).resolve().parent
DATA_FILE = PROJECT_DIR / "sample_student_data.csv"
OUTPUT_DIR = PROJECT_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

GPA_SUPPORT_THRESHOLD = 2.5  # Practice-only threshold; not an official policy.


def main():
    print("\nUNIVERSITY STUDENT DATA ANALYZER")
    print("=" * 36)

    if not DATA_FILE.exists():
        raise FileNotFoundError(
            f"Could not find {DATA_FILE.name}. Keep it in the same folder as this script."
        )

    students = pd.read_csv(DATA_FILE)

    required_columns = {
        "Student_ID", "Semester", "Department",
        "Credits_Completed", "GPA", "Enrollment_Status"
    }
    missing_columns = required_columns - set(students.columns)
    if missing_columns:
        raise ValueError(f"Dataset is missing required columns: {sorted(missing_columns)}")

    print(f"\nRows loaded: {len(students)}")
    print("\nFirst five records:")
    print(students.head().to_string(index=False))

    print("\nMissing values by column:")
    print(students.isna().sum().to_string())

    # Numeric overview
    overall_summary = pd.DataFrame({
        "Metric": ["Student records", "Average GPA", "Average credits completed"],
        "Value": [
            len(students),
            round(students["GPA"].mean(), 2),
            round(students["Credits_Completed"].mean(), 2),
        ],
    })
    overall_summary.to_csv(OUTPUT_DIR / "overall_summary.csv", index=False)

    # Department summary
    department_summary = (
        students.groupby("Department", dropna=False)
        .agg(
            Student_Count=("Student_ID", "count"),
            Average_GPA=("GPA", "mean"),
            Average_Credits=("Credits_Completed", "mean"),
        )
        .round(2)
        .reset_index()
    )
    department_summary.to_csv(OUTPUT_DIR / "department_summary.csv", index=False)

    # Semester summary
    semester_summary = (
        students.groupby("Semester", dropna=False)
        .agg(
            Student_Count=("Student_ID", "count"),
            Average_GPA=("GPA", "mean"),
            Average_Credits=("Credits_Completed", "mean"),
        )
        .round(2)
        .reset_index()
    )
    semester_summary.to_csv(OUTPUT_DIR / "semester_summary.csv", index=False)

    # Practice-only review list; do not interpret as official academic standing.
    support_review = students.loc[
        students["GPA"].notna() & (students["GPA"] < GPA_SUPPORT_THRESHOLD),
        ["Student_ID", "Semester", "Department", "GPA"]
    ].copy()
    support_review.to_csv(OUTPUT_DIR / "practice_gpa_review_list.csv", index=False)

    # Charts
    if not department_summary.empty:
        chart_data = department_summary.dropna(subset=["Average_GPA"])
        if not chart_data.empty:
            ax = chart_data.plot(
                x="Department", y="Average_GPA", kind="bar",
                legend=False, title="Average GPA by Department"
            )
            ax.set_xlabel("Department")
            ax.set_ylabel("Average GPA")
            ax.set_ylim(0, 4)
            plt.xticks(rotation=20, ha="right")
            plt.tight_layout()
            plt.savefig(OUTPUT_DIR / "average_gpa_by_department.png", dpi=160)
            plt.close()

    if not semester_summary.empty:
        chart_data = semester_summary.dropna(subset=["Average_GPA"])
        if not chart_data.empty:
            ax = chart_data.plot(
                x="Semester", y="Average_GPA", kind="bar",
                legend=False, title="Average GPA by Semester"
            )
            ax.set_xlabel("Semester")
            ax.set_ylabel("Average GPA")
            ax.set_ylim(0, 4)
            plt.xticks(rotation=20, ha="right")
            plt.tight_layout()
            plt.savefig(OUTPUT_DIR / "average_gpa_by_semester.png", dpi=160)
            plt.close()

    print("\nOverall summary:")
    print(overall_summary.to_string(index=False))
    print("\nDepartment summary:")
    print(department_summary.to_string(index=False))
    print(f"\nReports and charts saved in: {OUTPUT_DIR}")
    print("Finished successfully.")


if __name__ == "__main__":
    main()
