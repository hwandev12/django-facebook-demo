from django.core.exceptions import ValidationError
import os


def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path & filename
    # populate with the extensions that you allow / want
    valid_extensions = ['.pdf', '.doc', '.docx',
                        '.jpg', '.png', '.svg', '.xlsx', '.xls', '.mp4']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')
