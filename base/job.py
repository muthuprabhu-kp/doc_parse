from base.page import Page
from rules import get_rules


def job(page: Page):
    for rule in get_rules():
        rule.apply(page)
