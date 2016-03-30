#!/usr/bin/env python

import unittest
import xml.dom.minidom
import xpath

# Goal: "ceiling(avg(//day/temperature/number(translate(.,' Mins',''))))"


class TestXPath2(unittest.TestCase):
    """Test ability to handle XPath2 syntax"""
    def test_para_children(self):
        doc = xml.dom.minidom.parseString("""
            <doc>
                <para id="1" />
                <div id="2" />
                <para id="3" />
            </doc>
        """).documentElement
        result = xpath.find('child::para', doc)
        self.failUnlessEqual([x.getAttribute("id") for x in result],
                             ["1", "3"])

    def test_translate_node(self):
        print 'look for hi'
        doc = xml.dom.minidom.parseString("""
            <days>
                <day><temperature>40 F</temperature></day>
                <day><temperature>45 F</temperature></day>
                <day><temperature>50 F</temperature></day>
            </days>""").documentElement
        result = xpath.find("//day/temperature/translate(.,' Mins','')", doc)
        print result
if __name__ == '__main__':
    unittest.main()
