import pandas as pd

df = pd.read_csv("gold-soils.tsv", sep="\t")

df = df.groupby(["sub", "pred"])["object_or_value"].apply(lambda x: ', '.join(x.astype(str))).reset_index()
df_wide = df.pivot(index="sub", columns="pred", values="object_or_value")

pattern = (
    r'env_broad:\s*([^;]+);.*?'  # capture 'env_broad' value
    r'env_local:\s*([^;]+);.*?'  # capture 'env_local' value
    r'env_medium:\s*([^;]+);.*?'  # capture 'env_medium' value
)

# Apply str.extract to create new columns based on the refined regex groups
df_wide[['env_broad_label', 'env_local_label', 'env_medium_label']] = \
    df_wide['rdfs:comment'].str.extract(pattern)

df_wide.to_csv("wide_gold_soils.tsv", sep="\t")
