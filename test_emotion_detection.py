import unittest
from EmotionDetection.emotion_detection import emotion_detector

# I defined a dict to loop over for testing
test_cases = {
    "I am glad this happened": "joy",
    "I am really mad about this": "anger",
    "I feel disgusted just hearing about this": "disgust",
    "I am so sad about this": "sadness",
    "I am really afraid that this will happen": "fear"
}

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        for statement, dominant_emotion in test_cases.items():
            self.assertEqual(emotion_detector(statement)["dominant_emotion"], dominant_emotion)

unittest.main()