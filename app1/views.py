from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Recruitment_Season, Round, Section, Questions, Candidate, Candidate_Round, Candidate_Question, User, EvaluatorPanel
from .serializers import Recruitment_SeasonSerializer, RoundSerializer, SectionSerializer, QuestionsSerializer, CandidateSerializer, Candidate_RoundSerializer, Candidate_QuestionSerializer, UserSerializer, EvaluatorPanelSerializer

# Create your views here.
# views are python requests

class RecruitmentSeasonViewSet(viewsets.ModelViewSet):
    queryset = Recruitment_Season.objects.all()
    serializer_class =Recruitment_SeasonSerializer


class RoundViewSet(viewsets.ModelViewSet):
    queryset = Round.objects.all()
    serializer_class = RoundSerializer


class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer


class QuestionsViewSet(viewsets.ModelViewSet):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer


class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer


class EvaluatorPanelViewSet(viewsets.ModelViewSet):
    queryset = EvaluatorPanel.objects.all()
    serializer_class = EvaluatorPanelSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class Candidate_RoundViewSet(viewsets.ModelViewSet):
    queryset = Candidate_Round.objects.all()
    serializer_class = Candidate_RoundSerializer


class Candidate_QuestionViewSet(viewsets.ModelViewSet):
    queryset = Candidate_Question.objects.all()
    serializer_class = Candidate_QuestionSerializer


def index(request):
    return HttpResponse("<h1>App1 Homepage</h1>")

def login(request):
    return HttpResponse("<h1>Login Page</h1>")

def dashboard(request):
    return HttpResponse("<h1>Dashboard</h1>")

def round1(request):
    return HttpResponse("<h1>Round1</h1>")

def round2(request):
    return HttpResponse("<h1>Round2</h1>")

def round3(request):
    return HttpResponse("<h1>Round3</h1>")



