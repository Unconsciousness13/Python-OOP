import math

class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for i in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count):
        return cls(math.ceil(photos_count/4))

    def add_photo(self, label):
        for page in self.photos:
            if len(page) < 4:
                page.append(label)
                return f"{label} photo added successfully on page {self.photos.index(page) + 1} slot {page.index(label) + 1}"
        return "No more free slots"

    def display(self):
        result = ""
        for i in range(len(self.photos)):
            result += "-" * 11 + "\n"
            if len(self.photos[i]) == 0:
                result += "\n"
            else:
                result += "[] " * len(self.photos[i])
                result = result.rstrip()
                result += "\n"
        result += "-" * 11 + "\n"
        return result