from unittest.util import _MAX_LENGTH
from django.db import models
# from tkinter import CASCADE

# Create your models here.

class Recruitment_Season(models.Model):
    SeasonID = models.IntegerField(primary_key=True)
    Year = models.CharField(max_length=255)

class Round(models.Model):
    RoundID = models.IntegerField(primary_key=True)
    SeasonID = models.ForeignKey(Recruitment_Season, on_delete=models.CASCADE)
    Role = models.CharField
    Type = models.CharField

class Section(models.Model):
    SectionID = models.IntegerField(primary_key=True)
    RoundID = models.ForeignKey(Round, on_delete=models.CASCADE)
    SectionName = models.CharField(max_length=255)
    Role = models.CharField(max_length=255)
    TotalQuestions = models.IntegerField
    MaxMarks = models.IntegerField

class Questions(models.Model):
    QuestionID = models.IntegerField(primary_key=True)
    SectionID = models.ForeignKey(Section, on_delete=models.CASCADE)
    QuestionStatement = models.CharField(max_length=255)
    AnswerType = models.CharField(max_length=255)
    Answer = models.IntegerField

class Candidate(models.Model):
    CandidateID = models.IntegerField(primary_key=True)
    EnrollmentNumber = models.CharField(max_length=255)
    Name = models.CharField(max_length=255)
    EMail = models.CharField(max_length=255)
    Phone = models.CharField(max_length=255)
    Branch = models.CharField(max_length=255)
    Year = models.CharField(max_length=255)
    Role = models.CharField(max_length=255)
    CG = models.CharField(max_length=255)
    SeasonID = models.ForeignKey(Recruitment_Season, on_delete=models.CASCADE)
    RoundID = models.ForeignKey(Round, on_delete=models.CASCADE)


class Candidate_Round(models.Model):
    CandidateID = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    RoundID = models.ForeignKey(Round, on_delete=models.CASCADE)
    TimeSlot = models.CharField(max_length=255)
    EvaluationStatus = models.CharField(max_length=255)
    RoundStatus = models.CharField(max_length=255)
    

class Candidate_Question(models.Model):
    CandidateID = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    QuestionID = models.IntegerField
    QuestionScore = models.IntegerField
    QuestionResponse = models.IntegerField
    PanelistRemarks = models.IntegerField

class User(models.Model):
    UserID = models.IntegerField
    EnrollmentNumber = models.CharField(max_length=255)
    Name = models.CharField(max_length=255)
    Branch = models.CharField(max_length=255)
    Role = models.CharField(max_length=255)
    Year = models.CharField(max_length=255)
    EMail = models.CharField(max_length=255)
    PhoneNumber = models.CharField(max_length=255)
    UserName = models.CharField(max_length=255)
    Password = models.CharField(max_length=255)
    DOB = models.CharField(max_length=255)

class EvaluatorPanel(models.Model):
    PanelID = models.IntegerField
    EvaluatorID = models.IntegerField
    UserID = models.ForeignKey(User, on_delete=models.CASCADE)
    SeasonID = models.IntegerField
    # Field = models.IntegerField




