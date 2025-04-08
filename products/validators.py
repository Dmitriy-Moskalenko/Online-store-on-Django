from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions, ImageFile


def image_resolution_validator(image):
    """Валидатор, который проверяет разрешение изображений"""
    width, height = get_image_dimensions(image)
    max_width, min_width = 1900, 900
    max_height, min_height = 2400, 1200

    if width > max_width or height > max_height:
        raise ValidationError(f'Максимальное разрешение Обложки {max_width}х{max_height}')

    if width < min_width or height < min_height:
        raise ValidationError(f'Минимальное разрешение изображения {min_width}х{min_height}')


def image_size_validator(image):
    """Валидатор, который проверяет размер изображения"""
    img = ImageFile(image)
    max_size = 50 * 1024 * 1024

    if img.size > max_size:
        raise ValidationError(f'Максимальный размер изображения {max_size / 1024 / 1024:.1f} МБ')

