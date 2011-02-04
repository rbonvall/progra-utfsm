from pygments.lexer import RegexLexer
from pygments.token import *
from sphinx.highlighting import lexers

class TestCaseLexer (RegexLexer):
    name = 'testcase'
    aliases = ['testcase']
    tokens = {
        'root': [
            (r'[^`]+', Text),
            (r'`[^`]*`\n', Comment),
        ],
    }

def setup(app):
    lexers['testcase'] = TestCaseLexer()
