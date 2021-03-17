from django.http import HttpResponse


class mixed(object):
    def mix(self):
        return HttpResponse('this is my first mixin concept')