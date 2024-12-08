from pymoood import analysis_emotion

function = analysis_emotion
emotions = ["I feel good",
            "I was fired yesterday",
            "Anger rises to the top of my head"]

for emotion in emotions:
    result = function(emotion)
    print(result)
