#from database import db
from app import db
from process import encdode
class Event(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)  # Using user_id as the primary key
    user_id = db.Column(db.Integer)
    name = db.Column(db.String)
    age = db.Column(db.Integer)
    region = db.Column(db.String)
    orphanage = db.Column(db.String)
    alumni = db.Column(db.Boolean)
    problem = db.Column(db.String)
    
#register_route

def register_route(user_id,name, age, region, orphanage, alumni,problem):
    
    event = Event(user_id = user_id,name=name, age=age, region=region, orphanage=orphanage,
                    alumni=alumni, problem=problem)
    try:
        db.session.add(event)
    except Exception as e:
        print(f'str1{e}')
    try:    
        db.session.commit()
     
    except Exception as e:
        print(f'str2{e}')


















def create_event(title, start, end, instructorName, room, course, group):
    event = Event(title=title, start_time=start, end_time=end, instructor=instructorName,
                  room=room, target_course=course, target_group=group)
    db.session.add(event)
    db.session.commit()
    event_dict = encdode(event)
  

    return event_dict

def get_event(event_id):
    return Event.query.get(event_id)

def update_event(id,title, start, end, instructorName, room, course, group):
    event = Event.query.get(id)
    event.title = title
    event.start_time = start
    event.end_time = end
    event.instructor = instructorName
    event.room = room
    event.target_course = course
    event.target_group = group
    db.session.commit()

def delete_event(event_id):
    event = Event.query.get(event_id)
    db.session.delete(event)
    db.session.commit()

def get_all_events():
    events_json = []
    events = Event.query.all()

    # Serialize each Event object into a dictionary representation
    for event in events:
        event_dict = encdode(event)
        # event_dict = {
        #     'id': event.id,
        #     'title': event.title,
        #     'start': event.start_time,
        #     'end': event.end_time,

        #     "extendedProps": {
        #         "room": event.room,
        #         "course": event.target_course,
        #         "group":  event.target_group,
        #         "instructorName":  event.instructor
        #     }
            
        # }
        events_json.append(event_dict)

    # jsonify the list of dictionaries
    return events_json
    #eturn Event.query.all()
# {
#   "title": "string",
#   "start": "string",
#   "end": "string",
#   "extendedProps": {
#     "room": "",
#     "course": "",
#     "group": "",
#     "instructorName": ""
#   }
# }




