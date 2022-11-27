from django.urls import path

from measurement.views import SmartHomeView, SensorView, MeasurementCreate

urlpatterns = [
    path('sensors/', SmartHomeView.as_view()),
    path('sensors/<pk>/', SensorView.as_view()),
    path('measurements/', MeasurementCreate.as_view()),
]
