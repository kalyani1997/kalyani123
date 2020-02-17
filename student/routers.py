
from rest_framework.routers import SimpleRouter
from student.views import stu_op
app_routes = SimpleRouter()
app_routes.register('student',stu_op)
urlpatterns = app_routes.urls