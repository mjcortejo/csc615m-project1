import sys
import json
from utils import create_case, simulator

if __name__ == "__main__":
    prog_input = sys.argv[1]
    case_input = sys.argv[2]
    cases = [
        create_case(f"#{case_input}#")
    ]

    f = open(prog_input, "r")
    program_json = f.read()
    program = json.loads(program_json)

    simulator(cases, program)
