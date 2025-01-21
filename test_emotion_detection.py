import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        result1 = emotion_detector("I am glad I did this project")
        self.assertEqual(result1['dominant_emotion'], 'joy')

        result2 = emotion_detector("I am really mad about someone stole my pen")
        self.assertEqual(result2['dominant_emotion'], 'anger')

        result3 = emotion_detector("I feel disgusted hearing about recent news")
        self.assertEqual(result3['dominant_emotion'], 'disgust')

        result4 = emotion_detector("I am so sad about my friend moving away")
        self.assertEqual(result4['dominant_emotion'], 'sadness')

        result5 = emotion_detector("I am really afraid of thunders")
        self.assertEqual(result5['dominant_emotion'], 'fear')

unittest.main()