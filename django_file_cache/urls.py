from django.conf.urls import url
from django.contrib import admin

from upload import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url('upload/',views.UploadView.as_view()),
    # 配置测试环境下上传文件路径
]
