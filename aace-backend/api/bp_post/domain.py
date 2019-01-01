from . import backend


def create_post(post_data):
    """Create post.
    :param post_data: post information
    :type post_data: dict
    :returns: serialized post object
    :rtype: dict
    """
    post = backend.create_post(post_data)

    return post.to_dict()


def get_post_by_id(post_id):
    """Get Post by id.
    :param post_id: id of the post to be retrived
    :type post_id: integer
    :returns: serialized Post object
    :rtype: dict
    """
    post = backend.get_post_by_id(post_id)

    return post.to_dict()


def get_all_posts():
    """Get all Posts.
    :returns: serialized Post objects
    :rtype: list
    """
    posts = backend.get_all_posts()
    return [
        post.to_dict() for post in posts
    ]


def update_post(post_data, post_id):
    """Update Post.
    :param post_data: Post information
    :type post_data: dict
    :param post_id: id of the Post to be updated
    :type post_id: integer
    :returns: serialized Post object
    :rtype: dict
    """
    post = backend.update_post(post_data, post_id)

    return post.to_dict()


def delete_post(post_id):
    """Delete Post.
    :param post_id: id of the Post to be deleted
    :type post_id: integer
    """
    backend.delete_post(post_id)
