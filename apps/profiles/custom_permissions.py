from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.mixins import LoginRequiredMixin

class UserIsPatientMixin(UserPassesTestMixin):
    
    def test_func(self):
        return self.request.user.is_patient
    
class UserIsEmployeeMixin(UserPassesTestMixin):
    
    def test_func(self):
        return self.request.user.is_employee 
    
class UserIsDoctorMixin(UserPassesTestMixin):
    
    def test_func(self):
        return self.request.user.is_employee  and self.request.user.employee.role == 'Doctor'
    

class UserIsStaffMixin(UserPassesTestMixin):
    
    def test_func(self):
        return self.request.user.is_staff


 