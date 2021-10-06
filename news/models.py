from django.db import models
import datetime as dt 

# Create your models here.
class Editor(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField() 
    phone_number = models.CharField(max_length = 10,blank =True) 
    # blank =True this allows us to add NULL values to our database.
    class Meta:
        ordering = ['first_name']
    def save_editor(self):
        self.save()         
    def __str__(self):
        return self.first_name    

class tags(models.Model):
  name = models.CharField(max_length=30)
  def __str__(self):
      return self.name

class Article(models.Model):
    title = models.CharField(max_length =60)
    post = models.TextField()
    editor = models.ForeignKey(
      'Editor',
      on_delete=models.CASCADE,
      )
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True)
    article_image = models.ImageField(upload_to = 'articles/', default='SOME STRING')    

    @classmethod    
    def todays_news(cls,):
        today = dt.date.today()
        news = cls.objects.filter(pub_date__date = today)
        return news   

    @classmethod
    def days_news(cls,date):
        news = cls.objects.filter(pub_date__date = date)
        return news       
    @classmethod
    def search_by_title(cls,search_term):
        news = cls.objects.filter(title__icontains=search_term)
        return news             
        
    def __str__(self):
         return self.title
   
    
# Article model has a One to many relationship with the Editor model in that, an Article can have a single editor. While an Editor can write multiple articles.    
#  we create the Article model and we define three fields. A title that is a CharField that will contain the title of the article. post which is a TextField that will contain the Article content. This will be represented using a textArea tag in HTML. We then create a models.ForeignKey field. This will create a foreign key column that will store the ID of the Editor from the Editor table.

#  Many to Many field tells Django to create a separate join table. This new table handles mapping between articles to tags.

# . We pass in the argument auto_now_add and equate it to True. This will automatically save the exact time and date to the database as soon as we save that model.

# __date is a query filter that allows us to convert the datetimefield to a date.
# __icontains query filter will check if any word in the titlefield of our articles matches the search_term