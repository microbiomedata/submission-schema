import re
import click


def process_lines(lines, discard_line_pattern):
    # Find index of line to discard
    discard_line_index = None
    for i, line in enumerate(lines):
        if re.search(discard_line_pattern, line):
            discard_line_index = i
            break

    # Discard lines up to and including discard line
    if discard_line_index is not None:
        lines = lines[discard_line_index + 1:]

    # Remove initial "* [] ", "* [i] ", "* [p] " etc.
    lines = [re.sub('\*.*\] ', '', line) for line in lines]

    return lines


@click.command()
@click.option('--discard-line-pattern', '-d',
              default=r'\*\*ENVO:00000446 ! terrestrial biome\*\*',
              help='Pattern to match the line to discard and all preceding lines.')
@click.option('--input-file', '-i', type=click.Path(exists=True),
              help='Input file name.')
@click.option('--output-file', '-o', type=click.Path(),
              help='Output file name.')
def main(discard_line_pattern, input_file, output_file):
    with open(input_file) as f:
        lines = f.readlines()
        lines = [line.rstrip() for line in lines]

    processed_lines = process_lines(lines, discard_line_pattern)

    global_initial_whitespace_len = len(processed_lines[0]) - len(processed_lines[0].lstrip())

    assembled_lines = []
    for line in processed_lines:
        # remove initial whitespace equal to the initial whitespace on the first line
        line = line[global_initial_whitespace_len:].rstrip()
        match = re.match(r'^(\s*)', line)
        my_initial_whitespace = match.group(1)
        no_ws_line = line[len(my_initial_whitespace):]
        code, name = no_ws_line.split(" ! ")

        reassembled = f"{len(my_initial_whitespace) * '_'}{name} [{code}]"
        assembled_lines.append(reassembled)

    with open(output_file, 'w') as f:
        for line in assembled_lines:
            f.write(f"{line}\n")


if __name__ == '__main__':
    main()
