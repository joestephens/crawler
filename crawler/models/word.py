from remodel.models import Model

class Word(Model):
    has_and_belongs_to_many = ("Webpage",)
