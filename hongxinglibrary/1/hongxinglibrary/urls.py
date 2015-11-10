from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'library.views.index',name='index'),

    url(r'^addbook.html/', 'library.views.addbook0',name='addbook'),
    url(r'^addbook$', 'library.views.addbook',name='addbook'),

    url(r'^addwriter.html/', 'library.views.addwriter0',name='addwriter'),
    url(r'^addwriter$', 'library.views.addwriter',name='addwriter'),

    url(r'^serchbook.html/', 'library.views.serchbook0',name='serchbook'),
    url(r'^serchbook$', 'library.views.serchbook',name='serchbook'),

    url(r'^serchwriter.html/', 'library.views.serchwriter0',name='serchwriter'),
    url(r'^serchwriter$', 'library.views.serchwriter',name='serchwriter'),

    url(r'^booklist.html/', 'library.views.booklist',name='booklist'),
    url(r'^booklist$', 'library.views.booklist',name='booklist'),
    
    url(r'^library$', 'library.views.library',name='library'),

    url(r'^information$','library.views.information',name='information'),

    url(r'^DelBook/(?P<key>[0-9]*)/$','library.views.DelBook',name='DelBook'),
]
