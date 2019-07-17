from config import db
from models import User, BlogPost

# create database and table create
db.create_all()

# insert data
# db.session.add(User("michael", "michael@realpython.com", "i'll-never-tell"))
# db.session.add(User("admin", "ad@min.com", "admin"))
# db.session.add(User("mike", "mike@herman.com", "tell"))
#
# db.session.add(BlogPost("Good", "I\'m good."))
# db.session.add(BlogPost("Well", "I\'m well."))
# db.session.add(BlogPost("Excellent", "I\'m excellent."))
# db.session.add(BlogPost("Okay", "I\'m okay."))
# db.session.add(BlogPost("postgres", "we setup a local postgres instance"))

michael = User("michael", "michael@realpython.com", "i'll-never-tell")
admin = User("admin", "ad@min.com", "admin")
mike = User("mike", "mike@herman.com", "tell")

michael.posts.append(BlogPost("Good", "I\'m good."))
mike.posts.append(BlogPost("Well", "I\'m well."))

michael.posts.append(BlogPost("Excellent", "I\'m excellent."))
mike.posts.append(BlogPost("Okay", "I\'m okay."))

admin.posts.append(BlogPost("postgres", "we setup a local postgres instance"))

db.session.add(michael)
db.session.add(admin)
db.session.add(mike)

db.session.commit()