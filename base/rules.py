import re


class Rules(object):
    def re_parser(self, pattern, text):
        exceptions = re.findall(pattern, text)
        return exceptions

    def text_range(self, exception, para):
        range = para.Range
        range.Find.MatchCase = True
        range.Find.MatchWholeWord = True
        range.Find.ClearFormatting = True
        range.Find.Execute(FindText=exception)
        return range

    def apply(self, para):
        pass
