
import numpy as np
import pandas as pd

from sklearn.base import BaseEstimator, TransformerMixin


class LoanFeatureEngineer(BaseEstimator, TransformerMixin):

    def fit(self, X, y=None):
        return self

    def transform(self, X):

        X = X.copy()

        # Convert loan issue date into datetime
        issue_date = pd.to_datetime(
            X["issue_d"].astype("string"),
            format="%b-%Y",
            errors="coerce"
        )

        # Convert earliest credit line into datetime
        credit_date = pd.to_datetime(
            X["earliest_cr_line"].astype("string"),
            format="%b-%Y",
            errors="coerce"
        )

        # Feature 1: Loan issue year
        X["issue_year"] = issue_date.dt.year

        # Feature 2: Loan issue month
        X["issue_month"] = issue_date.dt.month

        # Feature 3: Credit history duration in months
        X["credit_history_months"] = (
            (issue_date.dt.year - credit_date.dt.year) * 12
            + (issue_date.dt.month - credit_date.dt.month)
        )

        # Feature 4: Annual income to loan amount ratio
        X["income_to_loan_ratio"] = (
            X["annual_inc"] / X["loan_amnt"].replace(0, np.nan)
        )

        # Feature 5: Log transformation of annual income
        X["log_annual_inc"] = np.log1p(
            X["annual_inc"].clip(lower=0)
        )

        # Remove original date columns after extracting information
        X = X.drop(
            columns=["issue_d", "earliest_cr_line"]
        )

        return X
