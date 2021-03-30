from sqlalchemy.orm import relationship
from sql_data.db import Base
import sqlalchemy as sa
from .movies import Movie, Character


class Conversation(Base):
    __tablename__ = 'conversations'

    conversation_id = sa.Column(sa.Integer, primary_key=True)
    characters_character1_id = sa.Column(sa.String(6), sa.ForeignKey('characters.character_id'), nullable=False)
    characters_character2_id = sa.Column(sa.String(6), sa.ForeignKey('characters.character_id'), nullable=False)
    movies_movie_id = sa.Column(sa.String(5), sa.ForeignKey('movies.movie_id'), nullable=False)


class ConversationLine(Base):
    __tablename__ = 'conversion_lines'

    conversation_line_id = sa.Column(sa.Integer, primary_key=True)
    conversation_line_pos = sa.Column(sa.Integer, nullable=False)
    conversations_conversation_id = sa.Column(sa.Integer, sa.ForeignKey('conversations.conversation_id'))
    movie_lines_line_id = sa.Column(sa.String(8), sa.ForeignKey('movie_lines.line_id'), nullable=False)

    text_line = relationship('MovieLine', uselist=False)


class MovieLine(Base):
    __tablename__ = 'movie_lines'

    line_id = sa.Column(sa.String(8), primary_key=True)
    line_text = sa.Column(sa.Text, nullable=False)
    characters_character_id = sa.Column(sa.String(6), sa.ForeignKey('characters.character_id'), nullable=False)
    movies_movie_id = sa.Column(sa.String(5), sa.ForeignKey('movies.movie_id'), nullable=False)
