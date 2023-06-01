import locale
from pathlib import Path
from typing import Any
from datetime import date
from gooey import Gooey, GooeyParser
import img2pdf


def parse_args(cli: GooeyParser) -> Any:
    desc = "Konvertér mappe med billedfiler (jpg, png, jp2, jpeg, gif, tif) til en enkelt flersidet PDF-fil."
    dir_input_msg = "Vælg en mappe med billeder, der skal konverteres"
    save_file_msg = "Vælg placering og fulde filnavn for pdf-filen"

    cli.add_argument("in_folder",
                        metavar="Vælg mappe med billedfiler",
                        help=dir_input_msg,
                        widget="DirChooser")
    cli.add_argument("out_file",
                        metavar="Hvor skal pdf-filen skal gemmes",
                        help=save_file_msg,
                        widget="FileSaver")

    args = cli.parse_args()
    return args


def generate_pdf(folder_object, out_file_object):
    # folder_object, out_file_object and obj are Path-objects
    files = []
    for obj in folder_object.rglob('*.*'):
        if obj.suffix.lower() in ['.png', '.jpg', '.jp2', '.jpeg', '.gif', '.tif', '.tiff']:
            files.append(str(obj))  # img2pdf.convert requirement

    with open(out_file_object, "wb") as f:
        f.write(img2pdf.convert(files))


@Gooey(
    program_name=f"Images2pdf, version {date.today().strftime('%Y-%m-%d')}",
    # program_name="Smartarkivering",
    program_description="Generér en pdf udfra en mappe med billedfiler",
    default_size=(600, 700),
    # https://github.com/chriskiehl/Gooey/issues/520#issuecomment-576155188
    # necessary for pyinstaller to work in --windowed mode (no console)
    encoding=locale.getpreferredencoding(),
    show_restart_button=False,
    show_failure_modal=False,
    show_success_modal=False,
)
def cli() -> None:
    cli: GooeyParser = GooeyParser(description="Images2pdf")
    args = parse_args(cli)
    print("Arguments parsed", flush=True)
    print("Generating pdf...", flush=True)
    generate_pdf(Path(args.in_folder), Path(args.out_file))
    print("Done", flush=True)
    print("", flush=True)
    print("Click the 'edit'-button to choose another folder to convert", flush=True)


if __name__ == '__main__':
    SystemExit(cli())
