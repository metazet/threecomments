# coding: utf-8
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Comment(models.Model):
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey("self", null=True, blank=True, related_name="children")
    lft = models.PositiveIntegerField("Left", default=1, editable=False)
    rght = models.PositiveIntegerField("Right", default=2, editable=False)
    tree_id = models.PositiveIntegerField("Tree", null=True, editable=False)
    level = models.PositiveIntegerField("Level", default=0, editable=False)

    def save(self, *args, **kwargs):
        if not self.pk:
            if not self.parent:
                super(Comment, self).save(*args, **kwargs)
                self.__class__.objects.filter(id=self.id).update(tree_id=self.id)
            else:
                self.tree_id = self.parent.tree_id
                self.lft = self.parent.rght
                self.rght = self.parent.rght + 1
                self.level = self.parent.level + 1
                self.__class__.objects.filter(tree_id=self.parent.tree_id, lft__gt=self.lft).update(lft=models.F('lft')+2)
                self.__class__.objects.filter(tree_id=self.parent.tree_id, rght__gte=self.rght).update(rght=models.F('rght')+2)
                self.__class__.objects.filter(id = self.parent.id).update(rght=models.F('rght')+2)
                super(Comment, self).save(*args, **kwargs)
        else:
            super(Comment, self).save(*args, **kwargs)

    class Meta:
        ordering = ['tree_id', 'lft']
        abstract = True

    def __str__(self):
        return unicode(self.id)
