from django.conf.urls import url

from quizsys.apps.quizzes.views import QuizListCreateAPIView, QuizRetrieveUpdateDestroyAPIView, \
    QuizSubmissionListCreateAPIView, QuizSubmissionRetrieveAPIView, ScoreDistributionListCreateAPIView, \
    ScoreDistributionDestroyAPIView, QuizQuestionsListAPIView, QuizSubmissionAllListAPIView, QuizFilteredListAPIView, \
    QuizSendEmailAPIView

app_name = 'quizzes'

urlpatterns = [
    url(r'^quizzes/?$', QuizListCreateAPIView.as_view()),
    url(r'^quiz/(?P<quiz_pk>\d+)/?$', QuizRetrieveUpdateDestroyAPIView.as_view()),
    url(r'^quiz/(?P<quiz_pk>\d+)/score-distributions/?$', ScoreDistributionListCreateAPIView.as_view()),
    url(r'^quiz/(?P<quiz_pk>\d+)/score-distributions/(?P<score_pk>\d+)/?$', ScoreDistributionDestroyAPIView.as_view()),
    url(r'^quiz/(?P<quiz_pk>\d+)/questions/?$', QuizQuestionsListAPIView.as_view()),

    url(r'^quiz/(?P<quiz_pk>\d+)/quiz-submissions/?$', QuizSubmissionListCreateAPIView.as_view()),
    url(r'^quiz-submissions/(?P<quiz_submission_pk>\d+)/?$', QuizSubmissionRetrieveAPIView.as_view()),
    url(r'^quiz-submissions/?$', QuizSubmissionAllListAPIView.as_view()),
    url(r'^quiz-submissions-filtered/?$', QuizFilteredListAPIView.as_view()),

    url(r'send-email/?', QuizSendEmailAPIView.as_view()),
    url(r'quiz-send-email/(?P<quiz_pk>\d+)/?', QuizSendEmailAPIView.as_view())
]