from django.db import models

# Create your models here.
class main_cat(models.Model):
    Type = models.CharField(max_length=50)

    def __str__(self):
        return str(self.Type)
    class Meta:
        db_table = "main_cat"

class category(models.Model):
    Type =models.CharField(max_length=50)
    main_cat=models.ForeignKey(main_cat,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.Type)
    class Meta:
        db_table = "category"

class author(models.Model):
    Name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.Name)

    class Meta:
        db_table = "author"

class book(models.Model):
    Name = models.CharField(max_length=30)
    Desc = models.CharField(max_length=80)
    Publisher = models.CharField(max_length=50)
    Url = models.FileField(upload_to='static/')
    status = models.CharField(max_length=50)
    Image = models.ImageField(upload_to='static/')
    main_cat = models.ForeignKey(main_cat, on_delete=models.CASCADE)
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    author = models.ForeignKey(author,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.Name)
    class Meta:
        db_table = "book"

class status(models.Model):
    Name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.Name)

    class Meta:
        db_table = "status"


class details(models.Model):
    Email = models.CharField(max_length=100)
    book = models.CharField(max_length=50)
    Url = models.FileField(upload_to='static/')
    Img = models.ImageField(upload_to='static/')
    Des = models.CharField(max_length=80)
    status = models.ForeignKey(status,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.status)

    class Meta:
        db_table = "details"

class contact(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=100)
    Msg = models.CharField(max_length=255)

    def __str__(self):
        return str(self.Email)

    class Meta:
        db_table = "contact"


class slider(models.Model):
    title = models.CharField(max_length=255)
    des = models.CharField(max_length=255)
    img = models.ImageField(upload_to='static/images/header-slider/')

    def __str__(self):
        return str(self.title)

    class Meta:
        db_table = "slider"

class testimonials(models.Model):
    name = models.CharField(max_length=50)
    ig = models.ImageField(upload_to='static/')
    com = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)

    class Meta:
        db_table = "testimonials"


