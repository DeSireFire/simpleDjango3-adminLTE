from django.shortcuts import render
from django.views import View


class index(View):
    '''
    首页视图
    '''

    def get(self, request, tempurl=None):
        renderfile = request.path.replace('/', '')
        print(renderfile)
        print(request._current_scheme_host)
        if renderfile:
            return render(request, renderfile)
        else:
            return render(request, 'index.html')
