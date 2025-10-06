__all__ = [
    'get_files',
]

def get_files(attachments: dict):
    if not attachments:
        return None
    files = dict()
    for k, v in attachments.items():
        if type(v) is str:
            files[k] = open(v, 'rb')
        elif type(v) is bytes:
            files[k] = v
        else:
            raise Exception(f'Invalid attachment {k}: Type {type(v)}')
    return files