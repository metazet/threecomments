# coding: utf-8
from django import forms
from django.utils.text import get_text_list
from django.utils.translation import ungettext, ugettext, ugettext_lazy as _

from threecomments.models import Comment
from threecomments.app_settings import THREECOMMENTS_ALLOW_PROFANITIES, THREECOMMENTS_PROFANITIES_LIST


class CommentForm(forms.ModelForm):
    class Meta:
        models = Comment

    def clean_comment(self):
        """
        If COMMENTS_ALLOW_PROFANITIES is False, check that the comment doesn't
        contain anything in PROFANITIES_LIST.
        """
        comment = self.cleaned_data["comment"]
        if not THREECOMMENTS_ALLOW_PROFANITIES:
            bad_words = [w for w in THREECOMMENTS_PROFANITIES_LIST if w in comment.lower()]
            if bad_words:
                raise forms.ValidationError(ungettext(
                    "Watch your mouth! The word %s is not allowed here.",
                    "Watch your mouth! The words %s are not allowed here.",
                    len(bad_words)) % get_text_list(
                        ['"%s%s%s"' % (i[0], '-'*(len(i)-2), i[-1])
                         for i in bad_words], ugettext('and')))
        return comment
