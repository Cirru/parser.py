
import unittest
import cirru_parser
import json

class ParserTest(unittest.TestCase):

  def test_parser(self):
    sourceFile = open('cirru/unfolding.cirru', 'r')
    source = sourceFile.read()
    sourceFile.close()
    tree = cirru_parser.pare(source, '')
    generated = json.dumps(tree, indent=2, separators=(',', ':'))

    jsonFile = open('ast/unfolding.json', 'r')
    jsonData = jsonFile.read().strip()

    self.assertEqual(generated, jsonData)
