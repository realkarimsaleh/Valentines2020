def valentine_tellings():
  import random
  import arabic_reshaper

  valentine = [
  "؟" "Desiginer" " هو أنت"
  "\nعشان كل ما بشوفك بحس أني بقلب"
  "\nFont Italic"
  "\nميال ميال",\
  "؟؟" "Pasta" "هو أنت بتحبي ال"
  "\nعشان كل ما بشوفك بحس أن أنا عايز"
  "\nPenne" "-أقرب المسافة ال-ما",\
  "بتحبي فيلم الناظر؟"
  "\nأوعدك لو أتجوزتيني"
  "\n!!هجبلك شقة وترابيزات بيلياردو وبينج",\
  "؟؟" "Pasta" "هو أنت بتحبي ال"
  "\nPenne" "-طب أنا عايز أقوي العلاقةال-ما",\
  "أنا سمعت انيك مابتحبش حد يكلمك في التليفون"
  "\nفهكلم بابا بقى",\
  "Command C"
  "\nCommand V"
  "\nمفهاش"
  "\nCommand Z",\
  "معلش يا جماعة هو جو هنا حر شوية؟؟"
  "\nأصل أنا حاسس إن بدوب"
  "\nفيكي",\
  "*Looks to you and passes a piece of paper*"
  "\nلأن الصمت في حَرَم الجمال جمال",\
  "؟؟" "Pizza" "هو أنت بتحبي ال"
  "\nطب ابعتلي عنوانك هبعتلك"
  "\nPizza"
  "\nسلامي وحبي وقبلاتي",\
  "slice Pizza" " عرفة لما بتبقى معاكي"
  "\nكده وجبنة تشد معاكي كده"
  "\nوتقعد تشد معاكي"
  "\nهو ده هيحصلي لما تسبني",\
  "؟؟" "Mulan" " ممكن نخرج ونتفرج على"
  "\nعشان"
  "\nif you say yes، you will make a man out of me",\
  "rating" " لو حد قلي أديلك"
  "\nمن" " 1-10"
  "\n"
  "هاديكي"
  "\n"
  " 11",\
  "إنت طالبة؟ أنا بردو طالب.... اديك",\
  "في عالم مظلم أبيض و أسود"
  "\nRGB" "أنت ال"
  "\nفي حياتي",\
  "إدا هو أنتي شايفة ال أنا شايفة؟ قمرين دول ولا عنين",\
  "؟؟" "Sheikh Zayed" " أنت سكنة في"
  "\nSheikh Zayed" " هو أنا بقول"
  "\nزايد حلاوة كدا ليه",\
  "أنا سمعت انتي بتحبي النوم أوي"
  "\nوانا بالنسبالي بعد ما سمعت الموضوع ده"
  "\nبقت مرتبتك عندي عالية أوي",\
  "I think I have a  " "قريش" " on you",\
  "؟؟" "YouTube" " أنت بتحبي"
  "\nLike" " أنت لو كنتي فيديو هعملك"
  "\nShare" " بس عمري هعمليك"
  "\nعشان لو شوفتك مع حد تاني هسبسكري",\
  "؟؟" "Breaking Bad" " بتحبي" 
  "\nmeth " " هنروح على" " first date " "بقة",\
  "؟؟" "Mahmoud El-Esseily" " بتحبي"
  "\nطب إيه ده أنا ممكن أخليكي تقابليه على فكرة"
  "\nفي فرحنا",\
  "؟؟" "Pizza" "بتحبي ال"
  "\nmmm Mozzarella",\
  "؟؟" "Sia" " بتحبي"
  "\nطب"
  "\n123 123"
  "\nحب",\
  "بوسي أنا بحب الطبخ"
  "\nFlambé" " وانتي بتخلي قلبي"
  "/nmy bae" " و عايزك تكوني",\
  "؟؟" "Maroon 5 " "بتحبي"
  "\nSongs About Jane " "هو في ألبوم اسمه"
  "\nبوسي أنا هحرقهولك يعني من الاخر كدا"
  "\n She Will Be Loved",\
  "؟؟" "Sheikh Zayed" " أنت سكنة في"
  "\n وانا وزني زايد من حبك",\
  "؟؟" "Lion King " "بتحبي"
  "\nRelationship" "أنا حاسس أن ال"
  "\nبتاعتنا بطيئة أنا شايف أنه لازم"
  "\n(Mufasa)" "ن",\
  "؟؟" "How I Met Your Mother " "بتحبي"
  "kids dats how I met your mother",\
  "صح؟" " Sharmoofers " "إنت بتحبي"
  "\nإنت حلوة أوي لدرجه"
  "\nأني لما بشوفك الكلام بيتلخبط"
  "\nمابقاش عارف أقول"
  "\nإيه أزيجي لاما بيبي زيجي لاما بيبي"
  "\n*in sharmoofers tone*",\
  "؟؟" "Cairokee " "بتحبي"
  "\nطب أثبت مكانك هنا عنوانك"
  "\n*Points to the heart*",\
  "marketing 4ps " "سمعت إن في"
  "\nPa7pik"
  "\nPa7pik"
  "\nPa7pik"
  "\nPa7pik"
  "\nPas Kda",\
  "؟؟" "Disney " "أنت بتحبي أفلام"
  "\nغامدي عنيك كدا ثانية"
  "\nSleeping Beauty " "إيه ده يا رب",\
  "؟؟" "Disney " "أنت بتحبي أفلام"
  "\nأنا حاسس إن احنا"
  "\nwe were mermaid for each other",\
  "حاولت أدورلك على عيبه" 
  "\nNot Found" " عيوب " "404 " "بس",\
  "أنا هكون صريح معاكي"
  "\nأنا نفسي أخش"
  "\n192.168.1.1"
  "\nمن بابه",\
  ]
  
  result = random.randint(0, len(valentine) )

  reshaped_text = arabic_reshaper.reshape(valentine[result])
    
  rev_text = reshaped_text[::-1]

    
  return rev_text
