import os
import pandas as pd
import click


@click.command()
@click.option(
    '--file', '-f',
    type=click.Path(exists=True),
    multiple=True,
    help="Paths to the input TSV files. This option can be used multiple times to specify multiple files."
)
@click.option(
    '--output', '-o',
    type=click.Path(),
    default="Combined_Environmental_Context_Data.tsv",
    help="Path to the output TSV file. Defaults to 'Combined_Environmental_Context_Data.tsv'."
)
def combine_context_files(file, output):
    """Combine environmental context files into a single TSV file with Extension, Context Field, ENVO Class CURIE, and Label columns."""
    combined_data = []

    for file_path in file:
        # Parse extension and context field from the filename
        filename = os.path.basename(file_path)
        parts = filename.split("_")
        extension = parts[3].capitalize()  # e.g., "soil" or "water"

        # Correctly map context fields to their full names
        if "broad" in filename:
            context_field = "env_broad_scale"
        elif "local" in filename:
            context_field = "env_local_scale"
        elif "medium" in filename:
            context_field = "env_medium"
        else:
            raise ValueError(f"Could not determine context field from filename: {filename}")

        # Load the file into a DataFrame
        df = pd.read_csv(file_path, sep="\t")

        # Extract CURIEs and labels from the "id" and "label" columns
        if "id" in df.columns and "label" in df.columns:
            for curie, label in zip(df["id"].dropna(), df["label"].dropna()):
                combined_data.append((extension, context_field, curie, label))

    # Convert the combined data into a DataFrame
    final_df = pd.DataFrame(combined_data, columns=["extension", "env_context_field", "class_curie", "label"])

    # Save the DataFrame to a TSV file
    final_df.to_csv(output, sep="\t", index=False)
    click.echo(f"Combined data saved to: {output}")


if __name__ == "__main__":
    combine_context_files()
