def image_path_generator(instance, filename):
    name = filename.split('.')
    return f"content_{instance.id}/{hash(name[0])}.{name[-1]}"
