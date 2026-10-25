import csv
import sys
from pathlib import Path

#--------------------------------------------------------------------------------------------------------
#   The function opens the file with the given path+filename and generates the inner part if the asciidoc
# table. It raises an Exception if in any row there are not exactly 6 items.
# The first 3 columns contain the requirements, exacly one in each row, representing the hierarchy. The function
# generated an identifier for  each requirement, in the format of R#, R#.# or R#.#.# depending on which hierarchy-
# level holds the requirement.
# The generated cells of columns 1 (ID), 5 (priority) and 6 (implementation phase) are centre-aligned.
# There is no check for multiple entries in cells of the same row and no checks for valid priority values or
# implementation phase values.
#
# The result is written on the standard output.
# -------------------------------------------------------------------------------------------------------
def generate_req_table(filename : str) -> None:
    with open(filename, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        lvl1 : int = 0
        lvl2 : int = 0
        lvl3 : int = 0
        reqID : str
        row_num: int = 0

        for line in reader:
            row_num += 1
            if row_num == 1:
                continue                       # To skip the header line
            if len(line) != 6:
                raise Exception(f"Input file has not 6 items in row: {row_num}")
            asc_row = "|"
            phase_col : str
            if line[4] in {"1", "2", "3", "4"}:
                phase_col = f"^.^|[.phase-{line[4]}]##■  ## {line[4]}"            # Add a coloured square before the phase number
            else:
                phase_col = f"^|{line[4]}"

            if len(line[0]) > 0:
                lvl1 += 1
                lvl2 = 0
                lvl3 = 0
                reqID = f"R{lvl1}"
                asc_row = asc_row + reqID + f"\n3+.^|{line[0]}\n^.^|{line[3]}\n{phase_col}\n<|{line[5]}"          #for level 1 - merge cells 2, 3 and 4
            else:
                if len(line[1]) > 0:
                    lvl2 += 1
                    lvl3 = 0
                    reqID = f"R{lvl1}.{lvl2}"
                    asc_row = asc_row + reqID + f"\n|\n2+.^|{line[1]}\n^.^|{line[3]}\n{phase_col}\n<|{line[5]}"   #for level 2 - leave 2 as it is and merge cells 3 and 4
                else:
                    lvl3 += 1
                    reqID = f"R{lvl1}.{lvl2}.{lvl3}"
                    asc_row = asc_row + reqID + f"\n|\n|\n.^|{line[2]}\n^.^|{line[3]}\n{phase_col}\n<|{line[5]}"  # for level 3 - no merging of cells
            print(asc_row + "\n")


# The program should take one argument, which is a filename of CSV type and save it as an Asciidoc embedded table-rows definition.
# Currently instead of saving the result, it is produced on standard output and can be redirected into the desired file
# In later stages a colouring scheme will be added for columns 4 (priorities) and 5 (implementation phases).
# The input  CSV must have exactly 6 coloumns in each row. If not, then the program aborts. The first row is regarded as a header and is skipped.
#
def main():
    if len(sys.argv) == 2 and sys.argv[1] == "-h":
        print("Generates the inner part of an asciidoc table from a cvs file of requirements.")
        print("The csv file must have 6 columns, the first 3 can holds a hierarcy of requirements,")
        print("with exactly one non-empy value in the first 3 cells of each row")
        print("Coloumn 4 is the priority (low, med, high), coloumn 5 is the phase of implementation (1, 2, ... , ")
        print("and column 6 is a description - within \"\"-s is there is a comma in the text.")
        print("\nUsage: reqgen [-h | <FILE>]")
        print("\noptions:\n    -h    displays this help\n\nThe generated result is sent to stdout.")
        return

    if len(sys.argv) < 2:
        print("Usage: python3 reqgen.py <path_to_requirements_CSV> or use \"regen.py -h\" for detailed description")
        sys.exit(1)
    input_name : str = sys.argv[1]
    ext : str = Path(input_name).suffix
    if ext != ".csv":
        print("Input file must be a CSV file")
        sys.exit(1)
    try:
        generate_req_table(input_name)
    except Exception as e:
        print(str(e), file=sys.stderr)

main()
