from docutils.parsers import rst
from docutils import nodes
import re

class TestcaseDirective(rst.Directive):
    required_arguments = 0
    optional_arguments = 0
    has_content = True

    def run(self):
        code = u'\n'.join(self.content)
        return [nodes.literal_block(code, code)]

def setup(app):
    app.add_directive('testcase', TestcaseDirective)

