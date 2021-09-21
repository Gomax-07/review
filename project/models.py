import uuid

from django.db import models
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns


class Technology(models.Model):
    """Model representing a project technology."""
    name = models.CharField(max_length=100, help_text='Enter a project framework/technology used (e.g. Django)')

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    image = models.OneToOneField('Image', on_delete=models.SET_NULL, blank=True, null=True)
    technologies = models.ManyToManyField(Technology, help_text="Select framework/technologies used for the project")

    def __str__(self):
        """String for representing the Model object."""
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('project-detail', args=[str(self.id)])

    def display_technology(self):
        """Create a string for the Technology used. This is required to display technology in Admin."""
        return ', '.join(technology.name for technology in self.technologies.all()[:3])

    display_technology.short_description = 'Technology'


class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.title

    @classmethod
    def search_by_title(cls, search_term):
        images = cls.objects.filter(title__icontains=search_term)
        return Image


class Detail(models.Model):
    """Model representing a specific copy of the repository ."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text='Unique ID for this particular book across whole library')
    project = models.ForeignKey('Project', on_delete=models.RESTRICT, null=True)
    location_url = models.CharField(max_length=150)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the repository')
    deployment_date = models.DateField(null=True, blank=True)
    RATING_STATUS = (
        (1, 'Too poor'),
        (2, 'Poor'),
        (3, 'Try'),
        (4, 'Somewhat good'),
        (5, 'Neutral'),
        (6, 'Somewhat good'),
        (7, 'Good'),
        (8, 'Too good'),
        (9, 'Near perfect'),
        (10, 'Excellent'),

    )

    status = models.IntegerField(
        choices=RATING_STATUS,
        blank=True,
        default='5',
        help_text='Project Ratings(Out of 10)',
    )

    class Meta:
        ordering = ['deployment_date']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.project.title})'


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'

    class Meta:
        ordering = ['last_name']
