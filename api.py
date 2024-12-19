from openai import OpenAI
import re
client = OpenAI(api_key="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")


def send_info_gpt(subject, argument, num_questions, school_level, question_type, difficulty, canvas, be_ready):
    user_message = "Prepare a test of " + str(num_questions) + " " \
    + question_type + " for a " + school_level + " student.\n" \
    + "The subject is " + subject + " and the argument is " + argument + ".\n" \
    + "The level of difficulty has to be " + difficulty + ".\n" \
    + "Don't insert anything else in the messagge, just the question marked as 1., 2. each of them in a new line."

    print(user_message)

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful teacher who has to test the preparation of your students"},
            {
                "role": "user",
                "content": user_message
            }
        ]
    )
    print()
    print("-------- SYSTEM RESPONSE: --------")
    system_questions = completion.choices[0].message.content
    questions = divide_questions(num_questions, system_questions)

    be_ready(canvas, questions)

def divide_questions(num_questions, system_questions):
    questions = system_questions.strip().split("\n\n")
    questions = questions[:num_questions]

    try:
        print("Q2: " + questions[1])
    except:
        split_questions = re.split(r'(?=\d+\.\s)', questions[0].strip())
        questions = split_questions

    print(questions)
    return questions
   

#send_info_gpt("History", "Second Wolrd War", 5, "High School", "Open-ended questions", "Medium")