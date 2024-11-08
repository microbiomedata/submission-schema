import click
import pandas as pd

@click.command()
@click.option('--input-file', type=click.Path(exists=True), default="gold-soils-by-semsql.tsv",
              help="Path to the input TSV file containing the data.")
@click.option('--output-file', type=click.Path(), default="gold-soils-by-semsql-wide.tsv",
              help="Path to the output TSV file for the transformed data.")
def transform_data(input_file: str, output_file: str) -> None:
    """
    Reads a TSV file, performs grouping and transformation on columns,
    extracts specific patterns from text data, and saves the output to a new TSV file.

    Args:
        input_file (str): Path to the input TSV file.
        output_file (str): Path to the output TSV file.
    """
    # Read input TSV file
    df = pd.read_csv(input_file, sep="\t")

    # Group by 'sub' and 'pred' columns and concatenate 'object_or_value' values
    df = df.groupby(["sub", "pred"])["object_or_value"].apply(lambda x: ', '.join(x.astype(str))).reset_index()

    # Pivot to wide format with 'sub' as index and 'pred' as columns
    df_wide = df.pivot(index="sub", columns="pred", values="object_or_value")

    # Define the regex pattern for extracting 'env_broad', 'env_local', and 'env_medium' labels
    pattern = (
        r'env_broad:\s*([^;]+);.*?'  # capture 'env_broad' value
        r'env_local:\s*([^;]+);.*?'  # capture 'env_local' value
        r'env_medium:\s*([^;]+);.*?'  # capture 'env_medium' value
    )

    # Apply str.extract to create new columns based on the refined regex groups
    df_wide[['env_broad_label', 'env_local_label', 'env_medium_label']] = \
        df_wide['rdfs:comment'].str.extract(pattern)

    # Save the transformed dataframe to the specified output file
    df_wide.to_csv(output_file, sep="\t")

if __name__ == "__main__":
    transform_data()
