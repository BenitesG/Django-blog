def validate_png(image):
    if not image.name.lower().endswith('.png'):
        raise ValueError('Image need to be .png!')