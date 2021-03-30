from sql_data.Models.conversations import Conversation, ConversationLine, MovieLine
from sql_data.db import session


def store_conversations(convers, lines):
    for conv_no, conversation in enumerate(convers):
        print(f'Processing converstaion {conv_no} of total {len(convers)}')
        line_list = conversation['line_list'].copy()
        del conversation['line_list']
        conversation_obj = Conversation(**conversation)
        session.add(conversation_obj)
        session.commit()
        for i, line_id in enumerate(line_list):
            conversation_line= ConversationLine(conversation_line_pos=i+1,
                                                conversations_conversation_id=conversation_obj.conversation_id,
                                                movie_lines_line_id=line_id)
            session.add(conversation_line)

            for line in lines:
                if line['line_id'] == line_id:
                    movie_line = MovieLine(**line)
                    session.add(movie_line)
                    break
            session.commit()