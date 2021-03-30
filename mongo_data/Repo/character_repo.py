from mongo_data.Models.characters import Character


def store_characters(lines):
    for line in lines:
        line['_id'] = line['character_id']
        del line['character_id']
        if line['gender'] == '?':
            del line['gender']
        character = Character(**line)
        character.save()