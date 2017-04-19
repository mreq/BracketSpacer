import sublime
import sublime_plugin
import re

opposite_brackets = {
    '(': ')',
    '[': ']',
    '{': '}',
    ')': '(',
    ']': '[',
    '}': '{'
}

def find_next_bracket(view, line, bracket, start):
    found = None
    same_count = 0
    opposite = opposite_brackets[bracket]

    while start < line.b and start < 999999:
        region = sublime.Region(start, start + 1)
        if view.substr(region) == bracket:
            same_count += 1
        elif view.substr(region) == opposite:
            if same_count == 0:
                found = start
                break
            else:
                same_count -= 1
        start += 1

    return found


class AddSpacesInBraces(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        sel = view.sel()[0]
        line = view.line(sel)
        line_text = view.substr(line)
        bracket = view.substr(sublime.Region(sel.a - 1, sel.a))

        if bracket not in opposite_brackets:
            return view.insert(edit, sel.a, '  ')

        matching_bracket_pos = find_next_bracket(view, line, bracket, sel.b)

        if matching_bracket_pos:
            view.insert(edit, sel.a, ' ')
            view.insert(edit, matching_bracket_pos + 1, ' ')

            # maintain cursor position if we're in an empty bracket
            # with | being the cursor:
            # (|) -> ( | )
            if (sel.a == matching_bracket_pos):
                view.sel().clear()
                view.sel().add(sublime.Region(sel.a + 1, sel.a + 1))


class RemoveSpacesInBraces(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        sel = view.sel()[0]
        line = view.line(sel)
        line_text = view.substr(line)
        bracket = view.substr(sublime.Region(sel.a - 2, sel.a - 1))

        view.run_command('left_delete')

        if bracket not in opposite_brackets:
            return

        matching_bracket_pos = find_next_bracket(view, line, bracket, sel.b)

        if matching_bracket_pos:
            view.erase(edit, sublime.Region(matching_bracket_pos - 1,
                                            matching_bracket_pos))
