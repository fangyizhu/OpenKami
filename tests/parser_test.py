import unittest
import parser
import os


class TestParser(unittest.TestCase):
    def test_parse_color_map(self):
        root_dir = os.path.abspath(__file__ + "/../../")
        file_path = os.path.join(root_dir, "TestFiles/SAL1_TwoSides.xml")
        print(parser.parse_color_map(file_path))
        file_path = os.path.join(root_dir, "TestFiles/SAL8_LadderLines.xml")
        print(parser.parse_color_map(file_path))


if __name__ == '__main__':
    unittest.main()