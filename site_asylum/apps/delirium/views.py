# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.views.generic.list import ListView
from .models import Post

class PostList(ListView):
    template_name = 'delirium/index.html'
    model = Post
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context['paginator']
        page = context['page_obj']
        page_range = [i for i in range(page.number-5, page.number+5) if i>0 and i<=paginator.num_pages]
        context.update({
            'page_range': page_range
        })
        return context

post_list = PostList.as_view()
