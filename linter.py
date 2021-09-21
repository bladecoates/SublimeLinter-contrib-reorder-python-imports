from SublimeLinter.lint import (
    PythonLinter,
)  # or NodeLinter, PythonLinter, ComposerLinter, RubyLinter


class ReorderPythonImports(PythonLinter):
    cmd = ('reorder_python_imports', '--py36-plus')
    multiline = False
    defaults = {'selector': 'source.python'}
    regex = r''
    tempfile_suffix = '-'
