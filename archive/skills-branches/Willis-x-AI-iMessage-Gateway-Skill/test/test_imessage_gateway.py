import importlib.util
import pathlib
import unittest


SCRIPT = pathlib.Path(__file__).parents[1] / "imessage-gateway" / "scripts" / "imessage_gateway.py"
SPEC = importlib.util.spec_from_file_location("imessage_gateway", SCRIPT)
gateway = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(gateway)


class NormalizePhoneTests(unittest.TestCase):
    def test_accepts_e164(self):
        self.assertEqual(gateway.normalize_phone("+86 138-1234-5678"), "+8613812345678")

    def test_rejects_ambiguous_number(self):
        with self.assertRaises(ValueError):
            gateway.normalize_phone("13812345678")

    def test_attachment_limit(self):
        self.assertEqual(gateway.MAX_FILE_BYTES, 104857600)


if __name__ == "__main__":
    unittest.main()
