from tokenizer_viz import TokenVisualization
import sentencepiece as spm

def save_html(html_content, file_path):
    with open(file_path, 'w') as file:
        file.write(html_content)

    
if __name__ == "__main__":    
    sample_text= """
    দেশের ৫ বিভাগে আগামী ৪৮ ঘণ্টার জন্য তাপপ্রবাহের সতর্কবার্তা দিয়েছে আবহাওয়া অধিদপ্তর। আজ বুধবার সন্ধ্যা ছয়টায় এ সতর্কবার্তা দেওয়া হয়েছে।
    যে পাঁচ বিভাগে তাপপ্রবাহের সতর্কবার্তা দেওয়া হয়েছে, সেগুলো হলো রাজশাহী, রংপুর, ঢাকা, খুলনা ও বরিশাল। আবহাওয়া অধিদপ্তর বলছে, জলীয় বাষ্প বেশি থাকার কারণে তাপপ্রবাহের এলাকাগুলোতে অস্বস্তিকর পরিস্থিতি থাকতে পারে।
    মুহাম্মদ আবুল কালাম মল্লিক বলেন, এখন দেশজুড়ে যে তাপমাত্রা, তা আগামী শনিবার পর্যন্ত অব্যাহত থাকতে পারে। এ সময় তাপমাত্রা ৩৬ থেকে ৪০ ডিগ্রি সেলসিয়াসের মধ্যে থাকতে পারে। তবে এর মধ্যে সিলেট ও ময়মনসিংহ বিভাগে বৃষ্টি হতে পারে। এরপর আগামী রোববার থেকে তাপমাত্রা কমতে পারে। রবি বা সোমবার থেকে ঢাকা বিভাগসহ বিভিন্ন বিভাগে বৃষ্টির সম্ভাবনা আছে।
    """
    
    tokenizer = spm.SentencePieceProcessor()
    tokenizer.load('bn_tokenizer/tokenizer.model.model')
    # Initialize the TokenVisualization class with the encoder and decoder functions
    token_viz = TokenVisualization(
        encoder=tokenizer.encode,
        decoder=tokenizer.decode
    )
    # Visualize the tokenization boundaries
    html = token_viz.visualize(sample_text)
    save_html(html, 'token_visualize.html')