from django.contrib.auth.models import User
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import os
from django.conf import settings
from django.http import JsonResponse
import json

from .forms import (
    StudentFrom,
    DocumentsFrom,
    AdditionalDetailsFrom,
    ParentDetailsFrom,
    ContactDetailsFrom
)

from .models import (
    Student,
    ContactDetails,
    AdditionalDetails,
    ParentDetails,
    Documents
)


@login_required(login_url='login')
def products(request):
    return render(request, 'student\products.html')


@login_required(login_url='login')
def home(request):
    student = Student.objects.filter(user=request.user).exists()
    if not student:
        return redirect('RegisterStudent')
    else:
        return render(request, 'student\index.html')

# <<<<<<<<<< JsonCall view >>>>>>>>>>
def jsoncall(request):
    json_data = open(os.path.join(settings.BASE_DIR, 'states\states-and-districts.json'))   
    data = json.load(json_data)
    print('json is colled')
    return JsonResponse(data)


@login_required(login_url='login')
def RegisterStudent(request):
    error = []
    studentform = StudentFrom()
    contactform = ContactDetailsFrom()
    parentform = ParentDetailsFrom()
    additionalform = AdditionalDetailsFrom()
    documentsform = DocumentsFrom()
    if request.method == 'POST':
        studentform = StudentFrom(request.POST or None)
        contactform = ContactDetailsFrom(
            request.POST or None)
        parentform = ParentDetailsFrom(
            request.POST or None)
        additionalform = AdditionalDetailsFrom(
            request.POST or None)
        documentsform = DocumentsFrom(
            request.POST or None, request.FILES)

        if studentform.is_valid():
            firstname = studentform.cleaned_data['firstname']
            lastname = studentform.cleaned_data['lastname']
            gender = studentform.cleaned_data['gender']
            DOB = studentform.cleaned_data['DOB']
            admission_Number = studentform.cleaned_data['admission_Number']
            religion = studentform.cleaned_data['religion']
            caste = studentform.cleaned_data['caste']
            aadhar = studentform.cleaned_data['aadhar']
            student = Student(
                user=request.user,
                firstname=firstname,
                lastname=lastname,
                gender=gender,
                DOB=DOB,
                admission_Number=admission_Number,
                religion=religion,
                caste=caste,
                aadhar=aadhar)
            student.save()
        if contactform.is_valid():
            current_addr = contactform.cleaned_data['current_addr']
            current_addr2 = contactform.cleaned_data['current_addr2']
            state = contactform.cleaned_data['state']
            city = contactform.cleaned_data['city']
            pincode = contactform.cleaned_data['pincode']
            permanent_addr = contactform.cleaned_data['permanent_addr']
            permanent_addr2 = contactform.cleaned_data['permanent_addr2']
            permanent_state = contactform.cleaned_data['permanent_state']
            permanent_city = contactform.cleaned_data['permanent_city']
            permanent_pincode = contactform.cleaned_data['permanent_pincode']
            contact = ContactDetails(
                user=request.user,
                current_addr=current_addr,
                current_addr2=current_addr2,
                state=state,
                city=city,
                pincode=pincode,
                permanent_addr=permanent_addr,
                permanent_addr2=permanent_addr2,
                permanent_state=permanent_state,
                permanent_city=permanent_city,
                permanent_pincode=permanent_pincode,
            )
            contact.save()
        if parentform.is_valid():
            father_name = parentform.cleaned_data['father_name']
            mother_name = parentform.cleaned_data['mother_name']
            father_dob = parentform.cleaned_data['father_dob']
            mother_dob = parentform.cleaned_data['mother_dob']
            phone_no = parentform.cleaned_data['phone_no']
            alternate_phone_no = parentform.cleaned_data['alternate_phone_no']
            email = parentform.cleaned_data['email']
            father_quali = parentform.cleaned_data['father_quali']
            mother_quali = parentform.cleaned_data['mother_quali']
            family_annual_income = parentform.cleaned_data['family_annual_income']
            parent = ParentDetails(
                user=request.user,
                father_name=father_name,
                mother_name=mother_name,
                father_dob=father_dob,
                mother_dob=mother_dob,
                phone_no=phone_no,
                alternate_phone_no=alternate_phone_no,
                email=email,
                father_quali=father_quali,
                mother_quali=mother_quali,
                family_annual_income=family_annual_income,
            )
            parent.save()
        if additionalform.is_valid():
            privious_school = additionalform.cleaned_data['privious_school']
            transfer_certificate_no = additionalform.cleaned_data['transfer_certificate_no']
            fee_waiver_category = additionalform.cleaned_data['fee_waiver_category']
            route_code = additionalform.cleaned_data['route_code']
            shift = additionalform.cleaned_data['shift']
            stoppage_name = additionalform.cleaned_data['stoppage_name']

            additional = AdditionalDetails(
                user=request.user,
                privious_school=privious_school,
                transfer_certificate_no=transfer_certificate_no,
                fee_waiver_category=fee_waiver_category,
                route_code=route_code,
                shift=shift,
                stoppage_name=stoppage_name,
            )
            additional.save()
        if documentsform.is_valid():
            photo = documentsform.cleaned_data['photo']
            id_proof = documentsform.cleaned_data['id_proof']
            caste_certificate = documentsform.cleaned_data['caste_certificate']
            domicile = documentsform.cleaned_data['domicile']
            transfer_certificate = documentsform.cleaned_data['transfer_certificate']
            character_certificate = documentsform.cleaned_data['character_certificate']

            document = Documents(
                user=request.user,
                photo=photo,
                id_proof=id_proof,
                caste_certificate=caste_certificate,
                domicile=domicile,
                transfer_certificate=transfer_certificate,
                character_certificate=character_certificate,
            )

            document.save()
        return redirect('home')

    print(error)

    context = {
        'studentform': studentform,
        'contactform': contactform,
        'parentform': parentform,
        'additionalform': additionalform,
        'documentsform': documentsform,
        'errors': error,
    }

    return render(request, 'student\studentdetail.html', context=context)


@login_required(login_url='login')
def UpdateRegisterStudent(request):
    error = []
    user = request.user
    student = get_object_or_404(Student, user=user)
    contact = get_object_or_404(ContactDetails, user=user)
    parent = get_object_or_404(ParentDetails, user=user)
    additional = get_object_or_404(AdditionalDetails, user=user)
    documents = get_object_or_404(Documents, user=user)

    studentform = StudentFrom(request.POST or None, instance=student)
    contactform = ContactDetailsFrom(request.POST or None, instance=contact)
    parentform = ParentDetailsFrom(request.POST or None, instance=parent)
    additionalform = AdditionalDetailsFrom(
        request.POST or None, instance=additional)
    documentsform = DocumentsFrom(
        request.POST, request.FILES, instance=documents)

    if studentform.is_valid():
        studentform.save()
    else:
        error.append("something wrong in Student detail")

    if contactform.is_valid():
        contactform.save()
    else:
        error.append("something wrong in Contact detail")

    if parentform.is_valid():
        parentform.save()
    else:
        error.append("something wrong in Parent detail")

    if additionalform.is_valid():
        additionalform.save()
    else:
        error.append("something wrong in Additional detail")

    if documentsform.is_valid():
        documentsform.save()
    else:
        error.append("something wrong in Documents")

    context = {
        'studentform': studentform,
        'contactform': contactform,
        'parentform': parentform,
        'additionalform': additionalform,
        'documentsform': documentsform,
        'errors': error,
    }

    return render(request, 'student/updateStudentDetail.html', context=context)
