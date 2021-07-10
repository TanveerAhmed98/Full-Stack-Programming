is_door_open = False
is_light_on = True
is_password_valid = False

if is_password_valid:
    print("The password is valid")
else:
    print("The password is not valid")

# if-else chaining

if is_light_on:
    print("The light is on")
elif is_door_open:
        print("The door is open but the light is off")
else:
    print("The light is not on also the door is also close")
    
