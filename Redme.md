# הנחיות #

# דגשים: לא להשתמש בהשלמות אוטומטיות
# לעבוד עם הקובץ של המודל כדי לדעת מה השם המשתנה
# להוסיף נתונים לכל הטבלאות
# לשים לב לאותיות קטנות/גדולות
# להשלים את הקרוד, 

קישור: https://docs.djangoproject.com/en/4.0/


Create Read  Update Delete

#           READ |CREATE|UPDATE| DELETE
@api_view(['GET','POST','PUT','DELETE'])
def users(request,username):
    if request.method == 'PUT':
        user = username
        temp = Users.objects.filter(username=user)
        password = request.data('CurrentPassword')
        if password == temp.password:
            temp.password = request.data('newPassword') 
            temp.save()
            changed = True
        else:
            changed =False    
        return JsonResponse({'temp':temp, 'changed':changed}, safe=False)

#1)  USER = "Eli6969"

#    2) temp = {username= Eli, password = 4, email= Eli@@Gmail.com}
#       4) temp = {username= Eli, password = 555, email= Eli@@Gmail.com}
