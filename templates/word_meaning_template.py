word_meaning_template = '''
Translate and explain the following English word into Tamil.
Provide a detailed explanation that includes
the word’s meaning, usage in a sentence, and an easy-to-understand elaboration for Tamil-speaking users.
 If possible, provide synonyms in Tamil for a richer understanding.

 Input: Word: "Harmony"

Expected Output:

English Word: Harmony

1. Tamil Translation: ஒற்றுமை
2. Meaning: Harmony refers to a state of agreement or peaceful coexistence.
3. Usage in a Sentence: "The villagers lived in harmony with nature."
4. Tamil: "கிராமவாசிகள் இயற்கையுடன் ஒற்றுமையோடு வாழ்ந்தனர்."
4. Elaboration: "ஒற்றுமை என்பது மக்கள் அல்லது பொருட்கள் ஒருங்கிணைந்த ஒரு அமைதியான, சந்தோஷமான நிலையை குறிக்கிறது. இது உணர்வுகள், கருத்துகள், அல்லது செயல்களில் உள்ள ஒருமித்த தன்மை."
'''

thanglish_meaning_template = '''
You are an English tutor "Super Luna" translation assistant. A user inputs a sentence in "Thanglish" (a mix of Tamil and English). Your task is to:
1. Identify the English words from the sentence.
2. Provide the Tamil meaning for each identified English word.
3. Offer example sentences for that word, in both English and Tamil.

Example:
Input: அன் பிரிடிக்டபிள் meaning என்னன்னு தெரியுமா?
Output:
Meaning: ' unpredictable ' என்பதற்கு தமிழ் அர்த்தம்: ' முன்கூட்டிப் கணிக்க இயலாத.' \n
Example Sentences:\n
English: \nThe weather is unpredictable today.\n
Tamil: \nஇன்று வானிலை முன்கூட்டிப் கணிக்க இயலாததாக இருக்கிறது.

Now, please respond in the same format for the following user input: [insert Thanglish input here].


'''