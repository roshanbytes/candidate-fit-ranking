import pandas as pd

from candidate_fit_ranking.config import RAW_DATA_PATH

EXPECTED_COLUMNS = ["id", "job_title", "location", "connection", "fit"]


def load_raw_data(path=RAW_DATA_PATH):
    """Load the raw candidate CSV and check its columns.

    Parameters
    ----------
    path : str or Path, optional
        Location of the CSV file. Defaults to RAW_DATA_PATH.

    Returns
    -------
    pandas.DataFrame
        The raw data, unchanged.

    Raises
    ------
    ValueError
        If any expected column is missing.
    """
    df = pd.read_csv(path)

    missing = set(EXPECTED_COLUMNS) - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {sorted(missing)}")

    return df
