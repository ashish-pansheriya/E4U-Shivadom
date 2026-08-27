import re
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.


class recruiter(models.Model):
    industrys = (
        ('Feature Film', 'Feature Film'),
        ('Short Film', 'Short Film'),
        ('Web Series', 'Web Series'),
        ('Commercial', 'Commercial'),
        ('Music Video', 'Music Video'),
        ('Reality Show', 'Reality Show'),
        ('TV Serial', 'TV Serial'),
        ('Documentary', 'Documentary'),
        ('Fashion / Modeling', 'Fashion / Modeling'),
        ('Theatre', 'Theatre'),
        ('Ad Films', 'Ad Films'),
        ('Casting Agency', 'Casting Agency'),
        ('Production House', 'Production House'),
        ('Studio', 'Studio'),
        ('Content Creator', 'Content Creator'),
        ('Other', 'Other'),
    )
    experience = (
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
        ('13', '13'),
        ('14', '14'),
        ('15', '15'),
        ('16', '16'),
        ('17', '17'),
        ('18', '18'),
        ('19', '19'),
        ('20', '20'),
        ('Fresher', 'Fresher'),
        ('Any', 'Any'),
    )
    name = models.CharField(verbose_name='Casting director / producer', max_length=25)
    designation = models.CharField(verbose_name='Role / department', null=True, max_length=25)
    starts = models.CharField(verbose_name='Audition date',  null=True, max_length=25)
    ends = models.CharField(verbose_name='Audition end date', null=True, max_length=25)
    company = models.CharField(verbose_name='Production house / brand', max_length=50)
    project_title = models.CharField(verbose_name='Project title', max_length=100, blank=True, null=True)
    image = models.ImageField(verbose_name='Project / profile image', upload_to='media')
    industry = models.CharField(verbose_name='Production category', choices=industrys, max_length=50)
    role_type = models.CharField(verbose_name='Role type', choices=(
        ('Actor', 'Actor'),
        ('Model', 'Model'),
        ('Extra', 'Extra'),
        ('Dancer', 'Dancer'),
        ('Singer', 'Singer'),
        ('Voiceover', 'Voiceover'),
        ('Director', 'Director'),
        ('Assistant', 'Assistant'),
        ('Crew', 'Crew'),
        ('Other', 'Other'),
    ), max_length=30, blank=True, null=True)
    gender = models.CharField(verbose_name='Gender preference', choices=(
        ('Any', 'Any'),
        ('Female', 'Female'),
        ('Male', 'Male'),
        ('Transgender', 'Transgender'),
        ('Non-binary', 'Non-binary'),
    ), max_length=20, blank=True, null=True)
    age_min = models.IntegerField(verbose_name='Minimum age', blank=True, null=True)
    age_max = models.IntegerField(verbose_name='Maximum age', blank=True, null=True)
    payment_status = models.CharField(verbose_name='Payment status', choices=(
        ('Paid', 'Paid'),
        ('Paid + expenses', 'Paid + expenses'),
        ('Unpaid', 'Unpaid'),
        ('Negotiable', 'Negotiable'),
    ), max_length=25, blank=True, null=True)
    location = models.CharField(verbose_name='City / location', max_length=100)
    job_title = models.CharField(verbose_name='Role title', max_length=50)
    job_details = models.CharField(verbose_name='Project brief', null=True,  max_length=200)
    job_exp = models.CharField(verbose_name='Experience required', choices=experience, max_length=50)
    skill = models.CharField(verbose_name='Required skills / traits', null=True, max_length=100)
    audition_type = models.CharField(verbose_name='Audition format', choices=(
        ('In-person', 'In-person'),
        ('Self-tape', 'Self-tape'),
        ('Online audition', 'Online audition'),
        ('Callback', 'Callback'),
    ), max_length=25, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='User', max_length=40)
    date_posted = models.DateTimeField(default=timezone.now, verbose_name='Posted')
    contact = models.IntegerField(null=True, verbose_name='Phone Number')
    email = models.EmailField(max_length=50, null=True, verbose_name='Email id')

    @property
    def skill_tags(self):
        if not self.skill:
            return []
        tags = re.split(r'[;,|/]+', self.skill)
        return [tag.strip() for tag in tags if tag.strip()]

    def __str__(self):
        return self.job_title or self.company

    def get_absolute_url(self):
        return reverse('recruiter-post-detail', kwargs={'pk': self.pk})
