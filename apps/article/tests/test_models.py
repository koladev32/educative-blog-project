import pytest
from apps.user.models import User
from apps.article.models import Article

@pytest.fixture
def user():
    return User.objects.create_user(
        username='test',
        first_name="John",
        last_name="Doe",
        password="12345",
        email="johndoe@yopmail"
    )
    
    
@pytest.mark.django_db
def test_article_create(user):
    data_article = {
        "author": user,
        "body": "This is a test article",
        "title": "Test Article"
    }
    
    article = Article.objects.create(**data_article)
    
    assert article.author == user
    assert article.title == data_article.get("title")
    assert article.body == data_article.get("body")