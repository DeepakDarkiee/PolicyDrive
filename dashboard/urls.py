from django.urls import path
from dashboard import views
from django.conf import settings
from django.conf.urls.static import static
from dashboard.views import export_data, import_data


urlpatterns = [
    
    path('index/',views.index, name='index'),
    path('add_record/', views.add_record, name='add_record'),
    path('performance/', views.performance, name='performance'),
    path('show_record/', views.show_record, name='show_record'),
    path('edit_policy/<int:id>', views.edit_policy,name='edit_policy'),
    path('view_policy/<int:id>', views.view_policy,name='view_policy'),
    path('update_policy/<int:id>', views.update_policy,name='update_policy'),
    #path("delete_policy",views.delete_policy, name="delete_policy"),
    path('delete_policy/<int:id>', views.delete_policy,name='delete_policy'),      
    path('search_record/', views.SearchResultsView.as_view(),name='search_record'),
    path('sort_record/', views.sort_record, name='sort_record'),
    #path('csv/',views.getfile),
    #path('excel_import/',views.excel_import, name="excel_import"), 
    path('export/', export_data, name="export_data"),
    path('import/', import_data, name="import_data"),

    


    
]
