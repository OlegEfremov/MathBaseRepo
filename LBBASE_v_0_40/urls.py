from django.contrib import admin
from django.http import HttpResponse
from django.urls import re_path, path, include

from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url
from django.contrib.auth import views as auth_views

#from django.contrib.staticfiles.urls import static

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from registration.backends.hmac.views import RegistrationView
from registration.forms import RegistrationFormUniqueEmail

from apps.Export.views import export_folder_to_tex, export_folder_to_pdf
from apps.Main.views import count_checkboxes, try_page, count_squares, read_checkbox_values, write_checkbox_values, \
    export_as_file
from apps.Solution_Catalog.views import download_dynamic_text


class RegistrationViewUniqueEmail(RegistrationView):
    form_class = RegistrationFormUniqueEmail



urlpatterns = [
    path('admin/', admin.site.urls),
    # path(r'accounts/', include('django.contrib.auth.urls')),
#

    url(r'^accounts/password/reset/auth_password_reset_done$',
             auth_views.password_reset_done, name='auth_password_reset_done'),
    url(r'^accounts/password/change/auth_password_change_done$',
        auth_views.password_change_done,
        name='auth_password_change_done'),
    url(r'auth_password_reset_complete$',
          auth_views.password_reset_complete,
          name='auth_password_reset_complete'),
    url(r'^accounts/password/reset/$',
        auth_views.password_reset,
        {'post_reset_redirect': 'auth_password_reset_done',
         'email_template_name': 'registration/password_reset_email.txt'},
        name='auth_password_reset'),

    re_path(r'^accounts/register/$', RegistrationViewUniqueEmail.as_view(),
                      name='registration_register'),
    # url(r'^accounts/register/$',
    #                   RegistrationView.as_view(form_class=RegistrationFormUniqueEmail),
    #                   name='registration_register'),

    path(r'accounts/', include('registration.backends.hmac.urls')),
    path(r'main/', include('apps.Main.urls')),
    path(r'solution_catalog/', include('apps.Solution_Catalog.urls')),
    path(r'edit_mathattribute_catalog/', include('apps.Edit_MathAttribute_Catalog.urls')),
    path(r'full_search/', include('apps.Full_Search.urls')),
    re_path(r'edit_solution/', include('apps.Edit_Solution.urls')),
    path(r'edit_task/', include('apps.Edit_Task.urls')),
    path(r'edit_source_catalog/', include('apps.Edit_Source_Catalog.urls')),
    re_path(r'^$', include('apps.Main.urls')),
    re_path(r'export', include('apps.Export.urls')),
    re_path(r'beloved_cat', include('apps.BelovedCat.urls')),
    re_path(r'test_generated/', include('apps.Test_Generated.urls')),
    re_path(r'download_dynamic_text', download_dynamic_text),

    re_path(r'count_checkboxes', count_checkboxes),
    re_path(r'read_checkbox_values', read_checkbox_values),
    re_path(r'write_checkbox_values', write_checkbox_values),

    re_path(r'count_squares', count_squares),

    re_path(r'search', include('apps.All_Search.urls')),
    re_path(r'test_folder', include('apps.Main.py.Test_Folder.urls')),

    re_path(r'try', try_page),
    re_path(r'export_as_file', export_as_file),
    re_path(r'export_folder_to_tex', export_folder_to_tex),
    re_path(r'export_folder_to_pdf', export_folder_to_pdf),

    re_path(r'crm_actions', include('apps.crm_actions.urls')),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

# url(r'^password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/'
#     r'(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
#     auth_views.password_reset_confirm,
#     {'post_reset_redirect': 'auth_password_reset_complete'},
#     name='auth_password_reset_confirm'),
# url(r'^password/reset/complete/$',
#     auth_views.password_reset_complete,
#     name='auth_password_reset_complete'),
# url(r'^password/reset/done/$',
#     auth_views.password_reset_done,
#     name='auth_password_reset_done'),