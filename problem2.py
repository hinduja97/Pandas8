import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:

    teacher=teacher.groupby('teacher_id')['subject_id'].value_counts().reset_index()
    teacher=teacher.rename(columns={'subject_id':'cnt'})
    return teacher
