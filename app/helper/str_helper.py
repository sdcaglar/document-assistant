from bson import ObjectId


def convert_objectid_to_str(data):
    if isinstance(data, list):
        return [convert_objectid_to_str(item) for item in data]
    elif isinstance(data, dict):
        return {
            k: str(v) if isinstance(v, ObjectId) else convert_objectid_to_str(v)
            for k, v in data.items()
        }
    return data
