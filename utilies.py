"""FamilyTree Utilities submodule"""

def paginate_person(request, persons, person_number):
    page = request.args.get('page', 1, type=int)
    start =  (page - 1) * person_number
    end = start + person_number
    persons  = [person.format() for person in persons]
    current_person  = persons [start:end]
    return current_person
