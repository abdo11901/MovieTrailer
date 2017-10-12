import webbrowser


class Movie():
    # the constructor of our class
    def __init__(self, title, story, image, youtube):
        self.title = title
        self.story = story
        self.image = image
        self.youtube = youtube

    # show trailer function of the movie
    def show_trailer(self):
        webbrowser.open(self.youtube)

    # show image functiom of the movie
    def show_image(self):
        webbrowser.open(self.image)
