import unittest
from iomanager import *

class TestIOManager(unittest.TestCase):
	def test_extractPuzzleLines(self):
		extractedLines = extractPuzzleLines("test_input-file.txt")
		expectedLines = ["AAABCDFEEBCDF.RRC.GGH....IH.KK.IJJLL",
			"AAB...C.BHHHC.RRDF....DFEEGGG.......",
			"AAB...C.BHHHC.RRDF....DFEEGGG....... D0"]
		self.assertEqual(extractedLines, expectedLines)

	def test_getGrid(self):
		self.assertEqual(getGrid("AAABCDFEEBCDF.RRC.GGH....IH.KK.IJJLL"), "AAABCDFEEBCDF.RRC.GGH....IH.KK.IJJLL")
		self.assertEqual(getGrid("AAB...C.BHHHC.RRDF....DFEEGGG....... D0"), "AAB...C.BHHHC.RRDF....DFEEGGG.......")
		self.assertEqual(getGrid("AAB...C.BHHHC.RRDF....DFEEGGG....... D0 F12 A3"), "AAB...C.BHHHC.RRDF....DFEEGGG.......")

	def test_getFuel(self):
		self.assertEqual(getFuel("AAABCDFEEBCDF.RRC.GGH....IH.KK.IJJLL"), {})
		self.assertEqual(getFuel("AAB...C.BHHHC.RRDF....DFEEGGG....... D0"), {"D": 0})
		self.assertEqual(getFuel("AAB...C.BHHHC.RRDF....DFEEGGG....... D0 F12 A3"), {"D": 0, "F": 12, "A": 3})

if __name__ == '__main__':
    unittest.main()