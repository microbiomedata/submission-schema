# Introduction: This Dockerfile can be used to build a container image that can, in turn, be used
#               to "build" (hence, its name, "builder") the submission schema release artifacts.

# Use Python 3.10 because that's the Python version listed in `pyproject.toml`.
FROM python:3.10

WORKDIR /submission-schema

# Install uv, which manages both environments and package operations.
RUN pip install uv

# Copy the entire repository into the container image.
#
# Note: Copying _only_ the dependency lists (i.e. `pyproject.toml` and `uv.lock`) and then
#       mounting the entire repository as a volume in the container image at `docker run` time
#       results in `make all` failing due to the absence of an `nmdc_submission_schema` package.
#       I haven't yet figured out why that happens, but it doesn't happen if I have copied the
#       entire repository into the container image here at build time—so, I do the latter.
#
ADD . /submission-schema

# Install the project's Python dependencies.
RUN uv sync --locked

# Run the command that builds the submission schema release artifacts.
CMD ["make", "clean", "all"]
