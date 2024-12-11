print("Mai Xuân Huy")
print("MSSV:235752021610062")
class ReverseWords:
    def __init__(self, text):
        self.text = text

    def reverse(self):
        
        words = self.text.split()
        
        
        words.reverse()
        
        
        reversed_text = ' '.join(words)
        
        return reversed_text

input_text = "hello .py"

reverse_words = ReverseWords(input_text)

print(f"Dữ liệu vào: {input_text}")
