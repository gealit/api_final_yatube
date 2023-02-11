from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Group(models.Model):
    """Model for groups in database.
    Any Post is able to relate to one group.
    """

    title = models.CharField(max_length=200, verbose_name='Название')
    slug = models.SlugField(unique=True, verbose_name='Слаг')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class Post(models.Model):
    """Post model, contains all information about post."""

    text = models.TextField(
        verbose_name='текст',
        help_text='Введите текст поста'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата публикации'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор',
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        related_name="posts",
        blank=True,
        null=True,
        verbose_name='Группа',
        help_text='Группа к которой будет относиться пост'
    )
    image = models.ImageField(
        'Картинка',
        upload_to='posts/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.text[:15]

    class Meta:
        ordering = ('pub_date',)
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Comment(models.Model):
    """Comment model, contains all information about comment.
    it's text, author, and related post."""

    text = models.TextField(
        verbose_name='текст',
        help_text='Введите текст комментария'
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Пост'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор'
    )
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата публикации'
    )

    def __str__(self):
        return f'{self.post} - {self.text[:15]}'

    class Meta:
        ordering = ('created',)
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Follow(models.Model):
    """Model allow us to make a subscriptions on the favorite authors.
    I cannot get a subscription to yourself. Also unique_together constraint
    check unique entries at the database and provides the same check to the
    ModelSerializer.(Anyway, you may improve it by using ManyToMany in the
    User model, but it is a whole different story)."""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="follower",
        verbose_name="Сталкер",
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="following",
        verbose_name="Тот кого сталкерят",
    )

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        unique_together = ('user', 'following')

    def __str__(self):
        return f'Подписка на автора {self.following}'
