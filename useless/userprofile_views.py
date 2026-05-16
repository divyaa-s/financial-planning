from django.shortcuts import render
import csv

def user_profile(request):
    user_id = request.user.id  # Assuming you're using Django's built-in authentication
    username = request.user.username  # Assuming you're using Django's built-in authentication
    email = request.user.email  # Assuming you're using Django's built-in authentication
    
    # Function to get join date from users.csv
    def get_join_date(user_id):
        with open('users.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == str(user_id):
                    return row[3]  # Assuming join date is at index 3 (adjust if necessary)

    join_date = get_join_date(user_id)

    context = {
        'user': {
            'id': user_id,
            'username': username,
            'email': email,
        },
        'join_date': join_date
    }
    return render(request, 'user_profile.html', context)
