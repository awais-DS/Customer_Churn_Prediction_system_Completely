from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,OrdinalEncoder
from sklearn.linear_model import LogisticRegression

def build_pipeline():
    encoders=ColumnTransformer(
        transformers=[
            ("gender", OneHotEncoder(drop="first",handle_unknown="ignore"),["gender"]),
            ("dependents",OneHotEncoder(drop="first",handle_unknown="ignore"),["Dependents"]),
            ("contract",OrdinalEncoder(
                categories=[["Month-to-month","One Year","Two Year"]]
            ),["Contract"]),
        ],
        remainder="passthrough"
    )
    pipeline=Pipeline([
        ("encoders",encoders),
        ("model", LogisticRegression(class_weight="balanced",max_iter=1000,random_state=0))
    ])
    return pipeline


