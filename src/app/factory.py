from app.models import School, OtherSchool


def SchoolFactory(data):
    # if the school is not secondary, skip it
    if 'mainlevel_code' in data and data['mainlevel_code'] != 'SECONDARY' and data['mainlevel_code'] != 'MIXED LEVEL':
        return OtherSchool(**data)
    else:
        return School(**data)
