from rest_framework.permissions import DjangoModelPermissions


class AllModelPermission(DjangoModelPermissions):
    """By default DjangoModelPermissions does not check permission for GET requests, here the perms_map property is overridden to ensure that users are associated with a view permission to receive data from a GET request.

    Args:
        DjangoModelPermissions ([type]): [description]
    """
    

    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }