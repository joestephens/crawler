from remodel.models import Model

class Webpage(Model):
    has_and_belongs_to_many = ("Word",)
