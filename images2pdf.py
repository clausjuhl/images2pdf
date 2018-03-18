from gooey import Gooey, GooeyParser
from message import display_message


@Gooey(dump_build_config=True,
       program_name="Widget Demo")
def main():
    desc = "Example application to show Gooey's various widgets"
    file_help_msg = "Name of the file you want to process"

    parser = GooeyParser(description=desc)

    parser.add_argument("DirectoryChooser", help=file_help_msg, widget="DirChooser")
    parser.add_argument("FileSaver", help=file_help_msg, widget="FileSaver")
    parser.add_argument("MultiFileSaver", help=file_help_msg, widget="MultiFileChooser")
    parser.add_argument("directory", help="Directory to store output")

    parser.add_argument('-d', '--duration', default=2, type=int, help='Duration (in seconds) of the program output')
    parser.add_argument('-s', '--cron-schedule', type=int, help='datetime when the cron should begin', widget='DateChooser')
    parser.add_argument("-c", "--showtime", action="store_true", help="display the countdown timer")
    parser.add_argument("-p", "--pause", action="store_true", help="Pause execution")
    parser.add_argument('-v', '--verbose', action='count')
    parser.add_argument("-o", "--overwrite", action="store_true", help="Overwrite output file (if present)")
    parser.add_argument('-r', '--recursive', choices=['yes', 'no'], help='Recurse into subfolders')
    parser.add_argument("-w", "--writelog", default="writelogs", help="Dump output to local file")
    parser.add_argument("-e", "--error", action="store_true", help="Stop process on error (default: No)")
    verbosity = parser.add_mutually_exclusive_group()
    verbosity.add_argument('-t', '--verbozze', dest='verbose', action="store_true", help="Show more details")
    verbosity.add_argument('-q', '--quiet', dest='quiet', action="store_true", help="Only output on error")

    args = parser.parse_args()
    display_message()


def here_is_smore():
    pass


if __name__ == '__main__':
    main()
