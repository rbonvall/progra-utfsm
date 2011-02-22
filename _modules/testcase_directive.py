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


def visit_testcase(self, node):
    text = node.astext()
    lines = [
        re.sub('`(.*)`', r'<b>\1</b>', line)
        for line in text.splitlines()
    ]
    return u'\n'.join(lines)


def depart_testcase(*args):
    pass


def setup(app):
    app.add_node(TestcaseNode,
            html=(visit_testcase, depart_testcase))

    app.add_directive('testcase', TestcaseDirective)

