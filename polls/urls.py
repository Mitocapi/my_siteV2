from django.urls import path

from .views import *

app_name = "polls"

urlpatterns = [
    path('', IndexViewList.as_view(), name='index'),
    path('<pk>/detail', DetailQuestion.as_view(), name='detail'),
    #path("vote/<pk>", vote, name="search"),
    path('<int:question_id>/results/', results, name='results'),
    path('recent/<int:n_polls>', recent, name='recent'),
    path("search", search, name="search"),
    path("searchresults/<str:sstring>/<str:where>/", SearchResultsList.as_view(), name="searchresults"),
    path("vote/<pk>", vote, name="vote"),
    path("votecasted/<pk>/<str:answer>", VoteCastedDetail.as_view(), name="votecasted"),
    path("createquestion/", CreateQuestionView.as_view(), name= "createquestion"),
    path ("createchoice/", CreateChoiceView.as_view(), name="createchoice"),


]

