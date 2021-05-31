from django.urls import path
from .import views

urlpatterns = [
	path('', views.home, name="home"),
	path('score/', views.add_score, name='add_score'),
	path('score/<int:id>/', views.add_score_for, name='add_score_for'),
	path('profile/', views.profile, name='profile'),
	path('profile/view/<int:id>/', views.user_profile, name='user_profile'),
	path('profile/edit/', views.profile_update, name='edit_profile'),
	path('profile/edit1/', views.submit_update, name='submit_update'),

	path('staff/', views.staff_list, name="staff_list"),
	path('staff/add/new/', views.StaffAddView.as_view(), name="add_new_staff"),
	path('report/add/new/', views.RegAddView.as_view(), name="add_reg_report"),

	path('staff/edit/<int:pk>/', views.edit_staff, name="edit_staff"),
	path('staff/delete/<int:pk>/', views.delete_staff, name="delete_staff"),
	path('courses/', views.course_list, name="course_list"),
	path('reports/', views.report_list, name="report_list"),

	path('courses/add/new', views.CourseAddView.as_view(), name="add_new_course"),
	path('course/delete/<int:pk>/', views.delete_course, name="delete_course"),
	path('course/edit/<int:pk>/', views.course_edit, name="course_edit"),
	path('students/', views.student_list, name="student_list"),
	path('student/add/new/', views.StudentAddView.as_view(), name="add_new_student"),
	path('student/delete/<int:pk>/', views.delete_student, name="delete_student"),
	path('student/edit/<int:pk>/', views.edit_student, name="edit_student"),
	path('session/', views.session_list_view, name="manage_session"),
	path('session/add/new', views.session_add_view, name="create_new_session"),
	path('session/edit/<int:pk>/', views.session_update_view, name="edit_session"),
	path('session/delete/<int:pk>/', views.session_delete_view, name="delete_session"),
	path('semester/', views.semester_list_view, name="manage_semester"),
	path('semester/add/new', views.semester_add_view, name="create_new_semester"),
	path('semester/edit/<int:pk>/', views.semester_update_view, name="edit_semester"),
	path('semester/delete/<int:pk>/', views.semester_delete_view, name="delete_semester"),
	path('result/', views.view_result, name="view_results"),
	path('password/', views.change_password, name='change_password'),
	path('course/assign/', views.CourseAllocationView.as_view(), name='course_allocation'),
	path('course/registration/', views.course_registration, name='course_registration'),
	path('course/drop/', views.course_drop, name='course_drop'),
	path('course/allocated/', views.course_allocation_view, name='course_allocation_view'),
	path('course/deallocate/<int:pk>/', views.withheld_course, name='withheld_course'),
	path('students/carry-over-list/', views.carry_over, name='carry_over'),
	path('students/repeat-list/', views.repeat_list, name='repeat_list'),
	path('students/1st_class_list/', views.first_class_list, name='first_class_list'),
	path('result/print/<int:id>/', views.result_sheet_pdf_view, name='result_sheet_pdf_view'),
	path('registration/form/', views.course_registration_form, name='course_registration_form'),
	path('api/data/', views.get_chart, name='chart'),
]






