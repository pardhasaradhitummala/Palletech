from django.urls import path


from student import views

# app_name = 'student'
urlpatterns = [
    path('traineeform',views.getTraineeForm,name='traineeform'),
    path('traineereg',views.maketraineintodatabase),
    path('taineesearch',views.traineesearch,name="traineesearch"),
    path('searchingTrainee',views.searchingtrainee)
]