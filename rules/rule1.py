from base.rules import Rules


class Rule1(Rules):
    def apply(self, para):
        text = para.Range.Text
        pattern = r'(?<!\.\s|\:\s)(?<!\.|\\|\/|\-|\"|\(|\")(?<!^)(?<!n)\b(?:Email)\b(?! of America\b)'.format('|'.join(
            [
                'And',
                'Or'
            ]
        ))
        exceptions = self.re_parser(pattern, text)
        for exception in exceptions:
            found_range = self.text_range(exception, para)
            word = found_range.Text
            reference = f'Suggestion | Validate capitalization of {word}' \
                        f' | Grammar |\n Capitalization | Do not Capitalize'
        #  insert_comments(found_range, reference)
        pass
