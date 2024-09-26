import re

def password_strength(password):

    min_length = 8
    max_length = 15

    strength_criteria = {
        "length":len(password)>=8,
        "uppercase": re.search(r'[A-Z]',password) is not None,
        "lowercase": re.search(r'[a-z]',password) is not None,
        "digit": re.search(r'\d',password) is not None,
        "special_char": re.search(r'[@#$%*!]',password) is not None
    }
    #calculate score (each criteria gives 1 point)
    score = sum(strength_criteria.values())
    
    #provide feedback based on score
    if not strength_criteria["length"]:
        if len(password) < min_length:
            return 0, f"Password is too short! Minimum length should be {min_length} characters."
        else:
            return 0, f"Password is too long! Maximum length should be {max_length} characters."
        
    feedback = ""

    if score ==5:
        feedback = "Strong Password"
    elif score == 4:
        feedback = "Good Password. Consider adding more variety."
    elif score == 3:
        feedback = "Moderate Password. Try to add special characters or numbers."
    elif score == 2:
        feedback = "Weak Password. Try to include uppercase, lowercase, digits, and special characters."
    else:
        feedback = "Very weak Password.It must be atleast 8 characters long and include a variety of characters"
    return score,feedback

#Testing the function
password = input("Enter a password to check: ")
score,feedback = password_strength(password)
print(f"Password Score: {score} out of 5")
print(f"Feedback: {feedback}")