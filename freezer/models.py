from django.db import models

#################################
#   Hierarchy of dependence     #
#################################
#
#   NOTES:
#           - TOP:          Highly dependent models (basal nodes)
#           - BOTTOM:       Least dependent models (terminal nodes)
#
#           - THEREFORE:    If the database needs to be reconstructed, we start by populating
#                           the least dependent fields first
#
# lvl.1          lesson_________________tutor
#                |           __|__
#                |          |     |
# lvl.2    student   location    subject
#

#################################
#          Core models          #
#################################
# Andrew
#jeffddddd


class location(models.Model):
        postcode = models.CharField(max_length=150,unique=True)


class subject(models.Model):
        subject         = models.CharField(max_length=150,unique=True)      # e.g. "math, biology, chemistry, physics"
        examboard       = models.CharField(max_length=150,unique=True)      # e.g. "aqa, wjec, ocr"
        keystage        = models.CharField(max_length=150,unique=True)      # e.g. "ks1, ks2, ks3, gcse, alevel"


class student(models.Model):
        name            = models.CharField(max_length=150,unique=True)      # e.g. Hyuk-Jin
        school          = models.CharField(max_length=150,unique=True)      # e.g. St. Mary
        expired         = models.CharField(max_length=150,unique=True)      # e.g. TRUE // FALSE

        location_key    = models.ForeignKey(location)
        subject_key     = models.ForeignKey(subject)


class tutor(models.Model):
        university      = models.CharField(max_length=150,unique=True)      # Imperial College
        degree          = models.CharField(max_length=150,unique=True)      # BSc Biology
        name            = models.CharField(max_length=150,unique=True)      # Andrew
        expired         = models.CharField(max_length=150,unique=True)      # TRUE
#        willing_zone    =

        location_key    = models.ForeignKey(location)
        subject_key     = models.ForeignKey(subject)

class lesson(models.Model):
        vacancy         = models.CharField(max_length=150,unique=True)      # 'open', 'occupied', 'expired'
        date            = models.CharField(max_length=150)                  #
        starttime       = models.CharField(max_length=150,unique=True)      # e.g. "taxid:9606" } in particular "9606" (?) // Header: "Taxid Interactor A:"&"Taxid Interactor B:"
        endtime         = models.CharField(max_length=150,unique=True)      # e.g. "taxid:9606" } in particular "9606" (?) // Header: "Taxid Interactor A:"&"Taxid Interactor B:"

        location_key    = models.ForeignKey(location)
        subject_key     = models.ForeignKey(subject)
        student_key     = models.ForeignKey(student)
        tutor_key       = models.ForeignKey(tutor)
