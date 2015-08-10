
import unittest
import cirru_parser
import json

def generateByName(name):
  sourceFile = open('cirru/' + name  +'.cirru', 'r')
  source = sourceFile.read()
  sourceFile.close()
  tree = cirru_parser.pare(source, '')
  generated = json.dumps(tree, indent=2, separators=(',', ':'))
  return generated

def readByName(name):
  jsonFile = open('ast/' + name + '.json', 'r')
  jsonData = jsonFile.read().strip()
  return jsonData

class ParserTest(unittest.TestCase):

  def test_comma(self):
    generated = generateByName('comma')
    jsonData = readByName('comma')
    self.assertEqual(generated, jsonData)

  def test_demo(self):
    generated = generateByName('demo')
    jsonData = readByName('demo')
    self.assertEqual(generated, jsonData)

  def test_folding(self):
    generated = generateByName('folding')
    jsonData = readByName('folding')
    self.assertEqual(generated, jsonData)

  def test_html(self):
    generated = generateByName('html')
    jsonData = readByName('html')
    self.assertEqual(generated, jsonData)

  def test_indent(self):
    generated = generateByName('indent')
    jsonData = readByName('indent')
    self.assertEqual(generated, jsonData)

  def test_line(self):
    generated = generateByName('line')
    jsonData = readByName('line')
    self.assertEqual(generated, jsonData)

  def test_parentheses(self):
    generated = generateByName('parentheses')
    jsonData = readByName('parentheses')
    self.assertEqual(generated, jsonData)

  def test_quote(self):
    generated = generateByName('quote')
    jsonData = readByName('quote')
    self.assertEqual(generated, jsonData)

  def test_spaces(self):
    generated = generateByName('spaces')
    jsonData = readByName('spaces')
    self.assertEqual(generated, jsonData)

  def test_unfolding(self):
    generated = generateByName('unfolding')
    jsonData = readByName('unfolding')
    self.assertEqual(generated, jsonData)
