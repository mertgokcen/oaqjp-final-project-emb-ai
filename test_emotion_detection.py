from EmotionDetection.emotion_detection import emotion_detector 
import unittest

class TestSentimentAnalyzer(unittest.TestCase): 
    def test_sentiment_analyzer(self):
        result = sentiment_analyzer('I am glad this happened')
        self.assertEqual(result['dominant_emotion'], 'joy')
        
        result = sentiment_analyzer('I am really mad about this')
        self.assertEqual(result_1['dominant_emotion'], 'anger')
        
        result = sentiment_analyzer('I feel disgusted just hearing about this')
        self.assertEqual(result['dominant_emotion'], 'disgust')
        
        result = sentiment_analyzer('I am so sad about this')
        self.assertEqual(result_1['dominant_emotion'], 'sadness')
        
        result = sentiment_analyzer('I am really afraid that this will happen')
        self.assertEqual(result_1['dominant_emotion'], 'fear')

unittest.main()