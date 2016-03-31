#!/usr/bin/env python

import unittest
import xml.dom.minidom
import xpath


class TestXPath2(unittest.TestCase):
    """Test ability to handle XPath2 syntax"""
    def test_average_from_dirty_nodes(self):
        doc = xml.dom.minidom.parseString("""
            <days>
                <day><temperature>40 F</temperature></day>
                <day><temperature>45 F</temperature></day>
                <day><temperature>50 F</temperature></day>
            </days>""").documentElement
        result = xpath.find("ceiling(avg(//day/temperature/number(translate(.,' F',''))))", doc)
        self.assertEqual(result, 45)
if __name__ == '__main__':
    unittest.main()
