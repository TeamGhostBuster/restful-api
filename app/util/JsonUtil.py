import importlib


def serialize(obj, only=tuple(), exclude=tuple()):
    """
    Python object serializer
    :param obj: The object to parse into json string
    :return: A dictionary
    """

    # Read from type name
    type_name = type(obj).__name__
    try:
        # Convert string into actual class object
        TypeSchema = getattr(importlib.import_module('app.api.{}.model'.format
                                                     (type_name.lower())), '{}Schema'.format(type_name))
    except ImportError:
        return None

    # Init the TypeSchema
    schema = TypeSchema(only=only, exclude=exclude)

    # Convert into JSON-dict
    return dict(schema.dump(obj).data)
