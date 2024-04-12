# Introduction to ConvLogRecaller dataset
## Structure

- Sampled Dialogues
  - AllDialogues.json
  - GPTDialogue.json

- Testing instances
  - MemConflict.json
  - MultipleConflict.json
  - MemRecall.json
  - MultipleRecall.json

## Files

- AllDialogues.json
    - This JSON file contains all the dialogues we sampled from the LED dataset, as well as additional dialogues we generated using LLM.
    
- GPTDialogue.json
    
    - This files contains only the dialogues we generated using LLM.
    
    - We generate dialogues based on five topics. The first step is to generate dialogues from GPT-3.5, and the second step is to rephrase the generated dialogues with Falcon-7B. Therefore, "topic_id" represents the topic number, "dialogue" represents the dialogues generated in the first step, "rephrased_dialogue" represents the dialogues that have been rephrased by Falcon-7B, and the “dialogue_id” follows the “dialogue_id” of dialogues from LED.
    
    - Example:
    
        ```json
        {
            "topic_id": 1,
            "dialogue": "S1: Do you want to play badminton tomorrow? I have a competition next Saturday. I need to practice for that.\nS2: Wow! That's nice. Tomorrow will be ok. How about at 5 p.m.\nS1: Ok! See you on the court!\nS2: Nice!",
            "rephrased_dialogue": "S1: Would you like to play badminton tomorrow? I have a competition next Saturday.\nS2: Wow! That's great. Tomorrow will be better. How about at 5 p.m.?\nS1: Certainly! I look forward to seeing you on the court.\nS2: Me too!",
            "dialogue_id": 1004
        }
        ```
    
        
- MemConflict.json

  - This file is intended for conducting the MemConflict experiment, where we focus on the question of which conflicts have occurred between the dialogues in "dialogues_with_clue" and the new dialogue.

  - “dialogues_with_clue” records the past dialogues between S1, S2.

  - “new_dialogue” is a sentence with some conflicts that manually designed

  - “Correct_Sentence” is the sentence from the original dialogue which contains no conflict 

  - “correctness” records whether there are conflicts between “dialogues_with_clue” and “new_dialogue”

  - Example:

    ```json
    {
      "dialogues_with_clue": [
        215
      ],
      "new_dialogue": "S1: Have you watched the TV series 'Click'?",
      "correct_sentence": "S1: Have you watched the movie 'Click'?",
      "correctness": 0
    }
    ```

- MultipleConflict.json

  - This file is similar to MemConflict.json, except that the dialogues in "dialogues_with_clue" are now multiple.

  - ```json
    {
      "dialogues_with_clue": [
        1006,
        1007
      ],
      "new_dialogue": "S1: I've never been in the semi-final or the final game of any badminton tournament before.",
      "correct_sentence": "S1: I've been in the semi-final and the final game of the badminton tournament last time, and finally I got the championship.",
      "correctness": 0
    }
    ```

- MemRecall.json

  - This file is intended for conducting the MemRecall experiment, where we focus on the question of what kind of response should be given after reading the dialogues in "dialogues_with_clue" and receiving the question in the "new_dialogue".

  - “dialogues_with_clue” records the past dialogues between S1, S2.

  - "new_dialogue" records the question asked by S3, who is distinct from S1 and S2.

  - “reply” is the ideal sentence should be replied by S1.

  - “crucial_reply” records the crucial words that should be included in S1’s response.

  - Example 

    ```json
    {
      "dialogues_with_clue": [
        215
      ],
      "new_dialogue": "S3: Have you heard of the movie 'click' before?\nS1:",
      "reply": "Yes, my friend told me it was a touching movie.",
      "crucial_reply": "Yes my friend touching movie"
    }
    ```

- MultipleRecall.json

  - This file is similar to MemRecall.json, except that the dialogues in "dialogues_with_clue" are now multiple.

  - Example 

    ```json
    {
      "dialogues_with_clue": [
        1003,
        1004,
        1005
      ],
      "new_dialogue": "S3: Did you practice for the badminton competition held last time on Saturday? Did you think you prepare for the competition well?\nS1:",
      "reply": "I practice for it but I don't think it's sufficient. So I got nervous before the competition.",
      "crucial_reply": "not sufficient nervous before competition"
    }
    ```
