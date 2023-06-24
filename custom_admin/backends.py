# # In backends.py
# from django.contrib.auth.backends import ModelBackend
# from django.shortcuts import redirect

# class CustomAdminBackend(ModelBackend):
#     def get_user(self, user_id):
#         user = super().get_user(user_id)
#         print('HEY',user,'HEY')
#         if user and user.is_superuser:
#             return redirect('/custom_admin')  # Redirect to your custom admin page
#         return user
