ExplainPrompt = """
As an AI language model, respond only to the sentence wrapped in double quotes from the given user input. Break down the sentence into parts, providing a clear Tamil explanation for each part. For each part, wrap key words, phrases, and meanings in double quotes.

For example, if the input is "Teacher, I need water. Can I drink water?", your response should look like this:

"Teacher, I need water. Can I drink water?" - "ஆசிரியர், எனக்கு தண்ணீர் வேண்டும். நான் தண்ணீர் குடிக்கலாமா?"

"Teacher" – "ஆசிரியரை" அழைக்கிறோம், "அவருடைய கவனத்தை பெற".

"I need water" - "எனக்கு தண்ணீர் வேண்டும்".

    - "I" – "நான்".\n

    - "need" – "வேண்டும்".\n

    - "water" – "தண்ணீர்".\n

"Can I drink water?" - "நான் தண்ணீர் குடிக்கலாமா?"

    - "Can I" – "நான் குடிக்கலாமா?" என்று அனுமதி கேட்கும் விதம்.

    - "drink" – "குடிக்க".\n

    - "water" – "தண்ணீர்".\n

Follow this format precisely for each sentence given, ensuring all key words, phrases, and meanings are wrapped in double quotes.
"""
