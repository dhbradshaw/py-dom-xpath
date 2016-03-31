# py-xpath2: Parsing xpath 2.0 in Python

lxml is the standard third party xpath parser for Python.  It is fully xpath 1.0 capable, but does not work for xpath 2.0 syntax.

In fact, as of March 31 2016, I have been unable to find an xpath 2.0 parser for python.  
The idea of this fork of (via Greg Haskin's copy) of Niel Damien's xpath 1.0  parser is to remedy that, at least to some extent.

This is a lazy endeavor--that is, I'm not committing to implementing a full parser.  
Rather, I'll start with specific xpath 2.0 xpaths, create tests for them, and see if I can get them to pass.  
The particular tests chosen are driven by commercial demands.
