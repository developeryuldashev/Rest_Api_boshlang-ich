from rest_framework import routers   #  rootlarni boshqarib turish uchun
from blog_profile import views

router=routers.DefaultRouter()

router.register(r'user', views.UserView, basename='user')
router.register(r'autor', views.AutorView, basename='autor')
router.register(r'linked_files', views.FileView, basename='liked_files')
router.register(r'article', views.ArticleView, basename='article')
router.register(r'article_by_tag', views.ArticleByTagView, basename='article_by_tag')

