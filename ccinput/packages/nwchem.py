import basis_set_exchange
import numpy as np

from ccinput.utilities import (
    get_method,
    get_solvent,
    get_basis_set,
    clean_xyz,
    get_distance,
    get_angle,
    get_dihedral,
    get_npxyz,
)
from ccinput.constants import CalcType, ATOMIC_NUMBER, LOWERCASE_ATOMIC_SYMBOLS
from ccinput.exceptions import InvalidParameter, ImpossibleCalculation


class NWChemCalculation:
    TEMPLATE = """start {}
    geometry units angstroms
    {}
    end
    task {}
    """

    CALC_TYPES = [
        # CalcType.SP,
        # CalcType.OPT,
        # CalcType.CONSTR_OPT,
        # CalcType.FREQ,
        # CalcType.TS,
        # CalcType.OPTFREQ,
    ]

    def __init__(self, calc):
        self.calc = calc
        self.has_scan = False
        self.appendix = []
        self.command_line = ""

        self.commands = {}
        self.solvation_radii = {}

        self.confirmed_specifications = ""
        self.xyz_structure = ""
        self.input_file = ""

        if self.calc.type not in self.KEYWORDS:
            raise ImpossibleCalculation(
                f"NWChem does not support calculations of type {self.calc.type}"
            )

        self.handle_specifications()
        self.handle_command()
        self.handle_xyz()

        self.handle_solvation()

        self.create_input_file()

    def clean(self, s):
        WHITELIST = set(
            "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ/()=-,. "
        )
        return "".join([c for c in s if c in WHITELIST])

    def add_option(self, key, option):
        _option = option.strip()
        if key in self.commands:
            if _option not in self.commands[key]:
                self.commands[key].append(_option)
        else:
            self.commands[key] = [_option]

    def add_options(self, key, options):
        for option in options:
            self.add_option(key, option)

    def handle_specifications(self):
        return

    def handle_command(self):
        return

    def handle_xyz(self):
        lines = [i + "\n" for i in clean_xyz(self.calc.xyz).split("\n") if i != ""]
        self.xyz_structure = "".join(lines)

    def handle_solvation(self):
        return

    def create_input_file(self):
        return

    @property
    def output(self):
        return self.input_file
