from rest_framework import serializers
from .models import Recruitment_Season, Round, Section, Questions, Candidate, Candidate_Round, Candidate_Question, User, EvaluatorPanel

class Recruitment_SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruitment_Season
        fields = ['SeasonID', 'Year']


class RoundSerializer(serializers.ModelSerializer):
    SeasonID = Recruitment_SeasonSerializer()
    class Meta:
        model = Round
        fields = ['RoundID', 'Role', 'Type']


class SectionSerializer(serializers.ModelSerializer):
    RoundID = RoundSerializer()
    class Meta:
        model = Section
        fields = ['SectionID', 'SectionName', 'Role', 'TotalQuestions', 'MaxMarks']


class QuestionsSerializer(serializers.ModelSerializer):
    SectionID = SectionSerializer()
    class Meta:
        model = Questions
        fields = ['QuestionID', 'QuestionStatement', 'Answertype', 'Answer']


class CandidateSerializer(serializers.ModelSerializer):
    SeasonID = Recruitment_SeasonSerializer()
    RoundID = RoundSerializer()
    class Meta:
        model = Candidate
        fields = ['CandidateID','EnrollmentNumber', 'Name', 'EMail', 'Phone', 'Branch', 'Year', 'Role', 'CG', 'CurrentStatus']


class EvaluatorPanelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EvaluatorPanel
        fields = ['PanelID', 'EvaluatorID', 'UserID', 'SeasonID']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['UserID', 'EnrollmentNumber', 'Name', 'Branch', 'Role', 'Year', 'EMail', 'PhoneNumber', 'UserName', 'Password', 'DOB']


class Candidate_RoundSerializer(serializers.ModelSerializer):
    CandidateID = CandidateSerializer()
    RoundID = RoundSerializer()
    class Meta:
        model = Candidate_Round
        fields = ['TimeSlot', 'EvaluationStatus', 'RoundStatus']


class Candidate_QuestionSerializer(serializers.ModelSerializer):
    CandidateID = CandidateSerializer()
    QuestionID = QuestionsSerializer()
    class Meta:
        model = Candidate_Question
        fields = ['QuestionScore', 'QuestionResponse', 'PanelistRemarks']  

