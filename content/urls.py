from django.urls import path
from content.views import ContentListView, ContentDetailView, management_page, delete_content

app_name = 'content'
urlpatterns = [
    path('', ContentListView.as_view(), name='home'),
    path('content/<pk>', ContentDetailView.as_view(), name='content-view'),
    path('management/', management_page, name='management'),
    path('delete/<pk>', delete_content, name='delete')
]
