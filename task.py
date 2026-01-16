
total_classes = int(input("Enter total number of classes: "))
attended_classes = int(input("Enter number of classes attended: "))
medical = input("Do you have a medical certificate? (yes/no): ").lower()            #\press 1. For Yes \Press 2. For No


attendance = (attended_classes / total_classes) * 100
print(f"\n Attendance: ")


# if attendance >= 75:
#     print("Student is allowed to sit in the exam.")
# else:
#     if medical == "yes":
#         print("Attendance is less than 75%.")
#         print("Medical certificate provided.")
#         print("Special permission granted. Student is allowed to sit in the exam.")
#     else:
#         print("Attendance is less than 75% and no medical certificate.")
#         print("Student is NOT allowed to sit in the exam.")
