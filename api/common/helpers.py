from flask_restful import abort
from api.models import User, BucketList, BucketListItem
from api import db

def abucketlistitem(bucketitem):
    """
    It returns the output for a single bucketlist item
    in a json format.
    """
    return {
        'id': bucketitem.id_no,
        'name': bucketitem.name,
        'date_created': bucketitem.date_created,
        'date_modified': bucketitem.date_modified,
        'done': bucketitem.done
    }


def getallbucketlistitem(bucketlist_id):
    """
    It returns all bucketlist items for a particular bucketlist id.
    """
    list_items = BucketListItem.query.filter_by(id_no=bucketlist_id).all()
    return [abucketlistitem(bucketitem)
            for bucketitem in list_items]


def getbucketlist(bucketlist):
    """
    It returns a single bucketlist.
    """
    return {
        'id': bucketlist.id_no,
        'name': bucketlist.name,
        'items': getallbucketlistitem(bucketlist.id_no),
        'date_created': bucketlist.date_created,
        'date_modified': bucketlist.date_modified,
        'created_by': bucketlist.created_by
    }


def delete_bucketlist(bucketlist):
    # It deletes a single bucketlist

    if bucketlist:
        db.session.delete(bucketlist)
        db.session.commit()
    else:
        abort(404)


def update_database():
    # It updates the content of the database.
    if db.session.commit():
        return True
    else:
        return False


def save_into_database(bucketlist):
    if bucketlist:
        db.session.add(bucketlist)
        db.session.commit()
        return True
    else:
        abort(400)
