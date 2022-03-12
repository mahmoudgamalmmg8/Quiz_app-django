from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('score/', include('results.urls',namespace="results"),name="results_page"),
    path('', include('quizz.urls', namespace='quizes'),name= 'home'),
    path('accounts/',include('django.contrib.auth.urls'),name='login'),


]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)