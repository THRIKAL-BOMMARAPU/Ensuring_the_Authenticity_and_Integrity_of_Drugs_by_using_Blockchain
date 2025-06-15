from django.urls import path

from . import views

urlpatterns = [path("index.html", views.index, name="index"),
	       path('AdminLogin.html', views.AdminLogin, name="AdminLogin"), 
	       path('AdminLoginAction', views.AdminLoginAction, name="AdminLoginAction"),
	       path('StakeLogin.html', views.StakeLogin, name="StakeLogin"), 
	       path('StakeLoginAction', views.StakeLoginAction, name="StakeLoginAction"),
	       path('AddStake.html', views.AddStake, name="AddStake"),
	       path('AddStakeAction', views.AddStakeAction, name="AddStakeAction"),
	       path('GenerateOrders', views.GenerateOrders, name="GenerateOrders"),
	       path('ViewStake', views.ViewStake, name="ViewStake"),
	       path('GenerateOrdersAction', views.GenerateOrdersAction, name="GenerateOrdersAction"),
	       path('AdminTracing.html', views.AdminTracing, name="AdminTracing"),
	       path('ViewAdminTracingAction', views.ViewAdminTracingAction, name="ViewAdminTracingAction"),
	       path('UpdateTracing', views.UpdateTracing, name="UpdateTracing"),
	       path('UpdateTracingAction', views.UpdateTracingAction, name="UpdateTracingAction"),	  
	       path('AddTracingAction', views.AddTracingAction, name="AddTracingAction"),	
	       path('ConsumerTracing.html', views.ConsumerTracing, name="ConsumerTracing"), 
	       path('ConsumerTracingAction', views.ConsumerTracingAction, name="ConsumerTracingAction"),
	       path('AdminMap', views.AdminMap, name="AdminMap"),
	       path('UserMap', views.UserMap, name="UserMap"),
]