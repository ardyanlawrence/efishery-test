# Base Activity
class BaseActivity:
    context = None

    def __init__(self, context):
        self.context = context
        pass

    def render(self, *args):
        pass

    def update(self, *args):
        pass
