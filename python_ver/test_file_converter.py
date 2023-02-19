import unittest

import file_converter

class TestFileManipulator(unittest.TestCase):

    def test_verify_file_extend(self):
        html_path = 'output.html'
        md_path = 'README.md'
        self.assertEqual(True, file_converter.verify_file_extend(html_path, len(html_path) - 5 ,'.html'))
        self.assertEqual(True, file_converter.verify_file_extend(md_path, len(md_path) - 3 ,'.md'))
        self.assertEqual(False, file_converter.verify_file_extend(html_path, len(html_path) - 5 ,'.jpeg'))
        self.assertEqual(False, file_converter.verify_file_extend(md_path, len(md_path) - 3 ,'.sh'))



    def test_verify_arguments(self):
        with self.assertRaises(SystemExit):
            file_converter.verify_arguments(2, ['README.md'])


if __name__ == '__main__':
    unittest.main()