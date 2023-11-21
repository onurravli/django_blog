from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.TextField(max_length=50)
    is_blocked = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(
        "blog.Author",
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField("date published")

    def __str__(self) -> str:
        # return f"Title: {self.title}\nContent: {self.content}\nCreated At: {self.created_at}"
        return f"{self.title} (#{self.pk})"

    def get_as_json(self):
        return dict(
            title=self.title,
            author=self.author,
            content=self.content,
            created_at=self.created_at,
        )
