from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean, DateTime, ForeignKey, ARRAY, Text

from user import User


class Developer(User):
    id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    programming_languages = Column(ARRAY(String))
    experience_levels = Column(ARRAY(Integer))
    minimum_salary = Column(Integer)
    biography = Column(Text)
    avatar = Column(String(255))
    location = Column(String(255))
    is_profile_public = Column(Boolean, default=True)

    __mapper_args__ = {
        'polymorphic_identity': 'developer',
    }

    def show_profile(self):
        return {
            "name": self.name,
            "email": self.email,
            "skills": self.programming_languages,
            "experience": self.experience_levels
        }
