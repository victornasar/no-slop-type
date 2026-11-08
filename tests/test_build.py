"""The validator must reject broken catalogs. Run: python3 -m unittest discover tests"""
import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from build import validate  # noqa: E402

GOOD = json.loads((ROOT / "fonts.json").read_text())


def broken(mutate):
    data = copy.deepcopy(GOOD)
    mutate(data)
    return validate(data)


class ValidatorTest(unittest.TestCase):
    def test_real_catalog_is_valid(self):
        self.assertEqual(validate(GOOD), [])

    def test_tag_outside_vocab(self):
        errors = broken(lambda d: d["fonts"][0].update(feel=["cozy"]))
        self.assertTrue(any("'cozy' not in vocab" in e for e in errors), errors)

    def test_too_many_tags(self):
        errors = broken(lambda d: d["fonts"][0].update(use=["body", "ui", "headlines", "logos"]))
        self.assertTrue(any("needs 1-3 tags" in e for e in errors), errors)

    def test_missing_field_does_not_hide_other_fonts_errors(self):
        def mutate(d):
            del d["fonts"][0]["note"]
            d["fonts"][1]["feel"] = ["cozy"]
        errors = broken(mutate)
        self.assertTrue(any("missing 'note'" in e for e in errors), errors)
        self.assertTrue(any("'cozy' not in vocab" in e for e in errors), errors)
        # The font with the missing field must still count as a known id.
        self.assertFalse(any("unknown font id" in e for e in errors), errors)

    def test_cdn_url(self):
        errors = broken(lambda d: d["fonts"][0].update(url="https://fonts.googleapis.com/css2?family=X"))
        self.assertTrue(any("not a CDN" in e for e in errors), errors)

    def test_avoid_points_at_unknown_font(self):
        errors = broken(lambda d: d["avoid"][0]["instead"].append("nope"))
        self.assertTrue(any("unknown font id 'nope'" in e for e in errors), errors)

    def test_duplicate_id(self):
        errors = broken(lambda d: d["fonts"].append(copy.deepcopy(d["fonts"][0])))
        self.assertTrue(any("duplicate id" in e for e in errors), errors)


if __name__ == "__main__":
    unittest.main()
