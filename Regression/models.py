from django.db import models

# Create your models here.

# Creating models
class Data(models.Model):
    name = models.CharField(max_length=100)
    qty = models.IntegerField()
    price = models.DecimalField(max_digits= 20, decimal_places= 2)

    def __str__(self):
        return f"{self.name}"

class Classes(models.Model):
    Class_name = models.CharField(max_length=50)
    Class_size = models.IntegerField()
    Class_Teacher = models.CharField(max_length=40)
    
    def __str__(self):
        return f'{self.Class_Teacher}'

class Students(models.Model):
    Student_name = models.CharField(max_length=40)
    Student_details = models.CharField(max_length=20)
    # Adding relationship between models Others include ForeignKey(many to one), OneToOne, ManyToMany
    student_class = models.ForeignKey(Classes, on_delete= models.CASCADE)

    def __str__(self):
        return f'{self.Student_name}'



# double underscores are like dots(.)
#  Students.objects.filter(student_class__Class_Teacher__icontains='Mr').all()

# Updating
# First, capture what to update
    # update = Students.objects.filter(student_class__Class_Teacher__icontains='Mr').first() 
# Modufy as desired
    #  update.Student_name = "John"
# Then save
    # update.save()

