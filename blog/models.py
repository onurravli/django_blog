from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField("date published")

    def __str__(self) -> str:
        # return f"Title: {self.title}\nContent: {self.content}\nCreated At: {self.created_at}"
        return f"{self.title} (#{self.pk})"

    def get_as_json(self):
        return dict(
            title=self.title,
            content=self.content,
            created_at=self.created_at,
        )
