from django.urls import path
import careapp.views


urlpatterns = [
    path("",careapp.views.index, name="index"),
    path("index",careapp.views.index, name="index"),
    path("login",careapp.views.login1,name="login"),
    path("checklogin",careapp.views.checklogin,name="checklogin"),
    path("admin_home",careapp.views.admin_home,name="admin_home"),
    path("add_category", careapp.views.add_category,name="add_category"),
    path("logout",careapp.views.logout1,name="logout"),
    path("surgical/<str:group_name>/",careapp.views.surgical,name="surgical"),
    path("add_surgical",careapp.views.add_surgical,name="add_surgical"),
    path("adminaddcategory",careapp.views.adminaddcategory,name="adminaddcategory"),
    path("portfolio",careapp.views.portfolio,name="portfolio"),
    path('submit_admin_portfolio', careapp.views.submit_admin_portfolio,name="submit_admin_portfolio"),
    path('viewportfolio', careapp.views.viewportfolio,name="viewportfolio"),
    path('admin_profile_list', careapp.views.admin_profile_list,name="admin_profile_list"),
    path('edit_admin_profile/<pk>', careapp.views.edit_admin_profile,name="edit_admin_profile"),
    path('surgical_list',careapp.views.surgical_list,name="surgical_list"),
    path('syringes',careapp.views.syringes,name="syringes"),
    path('belts',careapp.views.belts,name="belts"),
    path('support',careapp.views.support,name="support"),
    path('gloves',careapp.views.gloves,name="gloves"),
    path('dressing',careapp.views.dressing,name="dressing"),
    path('hotwaterbag',careapp.views.hotwaterbag,name="hotwaterbag"),
    path('thermo',careapp.views.thermo,name="thermo"),
    path('sthe',careapp.views.sthe,name="sthe"),
    path('neb',careapp.views.neb,name="neb"),
    path('bp',careapp.views.bp,name="bp"),
    path('dipers',careapp.views.dipers,name="dipers"),
    path('hyg',careapp.views.hyg,name="hyg"),
    path('baby',careapp.views.baby,name="baby"),
    path('mask',careapp.views.mask,name="mask"),
    path('vapor',careapp.views.vapor,name="vapor"),
    path('cot',careapp.views.cot,name="cot"),
    path('other',careapp.views.other,name="other"),
    path('admin_profile/delete/<int:pk>/', careapp.views.delete_admin_profile, name='delete_admin_profile'),
    path('delete/<int:id>/', careapp.views.delete_surgical, name='delete_surgical'),
    path('category/delete/<int:id>/', careapp.views.delete_category, name='delete_category'),




]