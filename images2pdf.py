from gooey import Gooey, GooeyParser
import img2pdf
from pathlib import Path

# From https://github.com/chriskiehl/Gooey/issues/207
# For disabling gooey, you can pass --ignore-gooey as a commandline arg when
# calling your file. For pre-filling items in Gooey, you can specify defaults
# in your argparse code:
# parser.add_argument("-f', '--foo', default="foobar")
# And they'll show in the form fields when Gooey loads.


@Gooey(program_name="Images2pdf",
       required_cols=1,
       header_height=60)
def parse_args():
    desc = "Konvertér en eller flere billedfiler til en enkelt flersidet PDF-fil."
    dir_input_msg = "Vælg en folder med billeder, der skal konverteres"
    save_file_msg = "Vælg placering og filnavn for pdf-filen"

    parser = GooeyParser(description=desc)
    parser.add_argument("in_folder",
                        metavar="Vælg mappe med billedfiler",
                        help=dir_input_msg,
                        widget="DirChooser")
    parser.add_argument("out_file",
                        metavar="Hvor skal pdf-filen skal gemmes",
                        help=save_file_msg,
                        widget="FileSaver")

    return parser.parse_args()


def generate_pdf(folder_object, out_file_object):
    # folder_object, out_file_object and obj are Path-objects
    files = []
    for obj in folder_object.rglob('*.*'):
        if obj.suffix in ['.png', '.jpg', '.jp2', '.jpeg']:
            files.append(str(obj))  # img2pdf.convert requirement

    with open(out_file_object, "wb") as f:
        f.write(img2pdf.convert(files))


if __name__ == '__main__':
    args = parse_args()
    print("Arguments parsed", flush=True)
    print("Generating pdf...", flush=True)
    generate_pdf(Path(args.in_folder), Path(args.out_file))
    print("Pdf-file generated", flush=True)
    print("Done", flush=True)
    print("", flush=True)
    print("Click the 'edit'-button to choose another folder to convert", flush=True)
