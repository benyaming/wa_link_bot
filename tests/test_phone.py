import unittest

from wa_link_bot.phone import extract_whatsapp_number, whatsapp_link


class PhoneParsingTest(unittest.TestCase):
    def test_local_israeli_number(self) -> None:
        self.assertEqual(extract_whatsapp_number("0544445811"), "+972544445811")

    def test_free_form_local_number(self) -> None:
        self.assertEqual(
            extract_whatsapp_number("please message 054-444-5811"),
            "+972544445811",
        )

    def test_plus_prefixed_number(self) -> None:
        self.assertEqual(
            extract_whatsapp_number("+972 54 444 5811"),
            "+972544445811",
        )

    def test_00_international_prefix(self) -> None:
        self.assertEqual(
            extract_whatsapp_number("00972 54 444 5811"),
            "+972544445811",
        )

    def test_configurable_country_code(self) -> None:
        self.assertEqual(
            extract_whatsapp_number("020 7946 0018", default_country_code="44"),
            "+442079460018",
        )

    def test_invalid_text(self) -> None:
        self.assertIsNone(extract_whatsapp_number("hello there"))

    def test_whatsapp_link(self) -> None:
        self.assertEqual(
            whatsapp_link("+972544445811"),
            "https://wa.me/+972544445811",
        )


if __name__ == "__main__":
    unittest.main()
