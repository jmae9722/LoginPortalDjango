from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.forms import AuthenticationForm
from .models import Course  # Ensure this is here to access Course model

User = get_user_model()

# Login View for All Roles
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        selected_role = request.POST.get('role', '').lower()

        user = authenticate(request, username=username, password=password)

        if user:
            if user.role.lower() == selected_role:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, "Role does not match user account.")
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, "index.html", {"form": AuthenticationForm()})

# Register View
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        role = request.POST.get('role')
        major = request.POST.get('major', '')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
        else:
            user = User.objects.create_user(
                username=username,
                password=password,
                role=role.lower(),
                major=major
            )
            login(request, user)
            return redirect('dashboard')

    return render(request, "register.html")

# Logout View
def logout_view(request):
    logout(request)
    return redirect('login')

# Role-based Dashboard View
@login_required
def dashboard_view(request):
    user = request.user
    context = {
        "username": user.username,
        "role": user.role,
        "major": user.major,
    }

    if user.role == "student":
        return render(request, "student_dashboard.html", context)

    elif user.role == "faculty":
        courses = Course.objects.filter(instructor=user)
        context["courses"] = courses
        return render(request, "faculty_dashboard.html", context)

    elif user.role == "admin":
        return render(request, "admin_dashboard.html", context)

    else:
        return render(request, "dashboard.html", context)

# Profile View
@login_required
def profile_view(request):
    user = request.user
    return render(request, "profile.html", {
        "username": user.username,
        "major": user.major,
        "role": user.role,
    })

# Grades View (Student Feature)
@login_required
def grades_view(request):
    grades = {
        "Math 101": "A",
        "History 201": "B+",
        "Biology 105": "A-",
    }
    return render(request, "grades.html", {"grades": grades})

# Admin-only User List View
@login_required
@staff_member_required
def user_list_view(request):
    students = User.objects.filter(role="student")
    faculty = User.objects.filter(role="faculty")
    admins = User.objects.filter(role="admin")
    return render(request, "user_list.html", {
        "students": students,
        "faculty": faculty,
        "admins": admins,
    })
