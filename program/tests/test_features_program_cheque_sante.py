"""
Tests for backend/features/program-cheque-sante.feature, program module part.
"""
from django.test import TestCase

from program.models import Program
from program.test_helpers import create_test_program


class ProgramCodeTest(TestCase):
    # Scenario: A program has a code used to build claim codes (@redmine-27173)
    def test_program_code_persists(self):
        program = create_test_program(code="CCS", name="Chèque Santé feature")
        self.assertEqual(Program.objects.get(idProgram=program.idProgram).code, "CCS")
