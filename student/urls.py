from django.urls import path
from .views import Lessons_List, Lesson_Detail, subject, contents, control_panel
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

                  path('subject', subject, name='subject'),
                  path('contents', contents, name='contents'),
                  path('control_panel', control_panel, name='control_panel'),
                  path('lesson_list.html/', Lessons_List.as_view(), name='lesson_list.html'),
                  path('lesson_detail/<int:pk>', Lesson_Detail.as_view(), name='lesson_detail'),


              ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

