from .texout import render_expression
from ..elements import Explanation
from ..elements import Solution
import re


def render_explanation(expl: Explanation):
    if expl is None:
        return ''

    ptrn = r'!\[(?P<alt>.*?)\]\((?P<path>.*?)(?P<title> .*?)?\)'
    illustr = expl.illustration

    md = ''
    prev_end = 0
    for m in re.finditer(ptrn, expl.description):
        render = render_expression(illustr.get_at_path(m.group('path')))
        md += expl.description[prev_end:m.start()]
        md += f'${render}$'
        prev_end = m.end()

    # Make sure to append the last piece of the explanation
    md += expl.description[prev_end:]

    return md


def render_solution(solution: Solution) -> str:
    """Render the given `Solution` into markdown format."""
    md = ''
    for step in solution.steps:
        if step.purpose is not None:
            md += '# ' + render_explanation(step.purpose) + '\n\n'
        if step.execution is not None:
            if isinstance(step.execution, Solution):
                sub_md = render_solution(step.execution)
                md += re.sub('^#', '##', sub_md, flags=re.MULTILINE)
            else:
                md += render_explanation(step.execution)
            md += '\n\n'
        if step.result is not None:
            md += '-> ' + render_explanation(step.result)
            md += '\n\n'

    return md
